"""
Foodie Explorer
================
A pure-Streamlit app (no HTML/CSS) that lets a signed-up user browse:
  Countries (10, near India)  ->  States / Regions  ->  Restaurants  ->  Menu + Ratings

Auth   : auth.py            (local signup/login, hashed passwords)
Data   : data.py            (curated static fallback content)
LLM    : llm_helper.py      (optional LangChain-powered live generation)

Run with:  streamlit run app.py
"""

import streamlit as st

import auth
import llm_helper
from data import COUNTRIES

st.set_page_config(
    page_title="Foodie Explorer",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# Session-state defaults
# --------------------------------------------------------------------------
defaults = {
    "logged_in": False,
    "username": None,
    "page": "countries",       # countries -> regions -> restaurants -> menu
    "selected_country": None,
    "selected_region": None,
    "selected_restaurant": None,
    "auth_mode": "Login",
    "llm_provider": "None (use built-in data)",
    "llm_api_key": "",
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def go_to(page: str):
    st.session_state.page = page


# --------------------------------------------------------------------------
# Hero header (native Streamlit only - no HTML/CSS)
# --------------------------------------------------------------------------
def hero_header(title: str, subtitle: str, icon: str = "🍽️"):
    with st.container(border=True):
        col_icon, col_text = st.columns([1, 8])
        with col_icon:
            st.markdown(f"# {icon}")
        with col_text:
            st.markdown(f"## :orange[{title}]")
            st.caption(subtitle)


def breadcrumb():
    parts = ["🌍 Countries"]
    if st.session_state.selected_country:
        parts.append(f"{st.session_state.selected_country}")
    if st.session_state.selected_region:
        parts.append(f"{st.session_state.selected_region}")
    if st.session_state.selected_restaurant:
        parts.append(f"{st.session_state.selected_restaurant}")
    st.markdown(" :gray[›] ".join(f":blue[{p}]" for p in parts))


def rating_stars(rating: float) -> str:
    full = int(rating)
    half = "✨" if (rating - full) >= 0.5 else ""
    return "⭐" * full + half + f"  `{rating}/5`"


# --------------------------------------------------------------------------
# Sidebar: account info + optional LangChain LLM settings
# --------------------------------------------------------------------------
def render_sidebar():
    with st.sidebar:
        st.markdown("### 👤 Account")
        st.success(f"Signed in as **{st.session_state.username}**")
        if st.button("🚪 Log out", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username = None
            go_to("countries")
            st.session_state.selected_country = None
            st.session_state.selected_region = None
            st.session_state.selected_restaurant = None
            st.rerun()

        st.divider()
        st.markdown("### 🧠 LangChain / LLM (optional)")
        st.caption(
            "Add an API key to generate live restaurant & menu data with "
            "an LLM via LangChain. Leave blank to use the built-in curated data."
        )
        st.session_state.llm_provider = st.selectbox(
            "Provider",
            ["None (use built-in data)", "Anthropic", "OpenAI"],
            index=["None (use built-in data)", "Anthropic", "OpenAI"].index(
                st.session_state.llm_provider
            ),
        )
        if st.session_state.llm_provider != "None (use built-in data)":
            st.session_state.llm_api_key = st.text_input(
                f"{st.session_state.llm_provider} API key",
                type="password",
                value=st.session_state.llm_api_key,
            )
            if llm_helper.is_configured(st.session_state.llm_api_key):
                st.info("LLM generation is active for new/unlisted regions.")
        st.divider()
        if st.button("⬅️ Back to Countries", use_container_width=True):
            st.session_state.selected_country = None
            st.session_state.selected_region = None
            st.session_state.selected_restaurant = None
            go_to("countries")
            st.rerun()


# --------------------------------------------------------------------------
# AUTH PAGE
# --------------------------------------------------------------------------
def render_auth():
    hero_header(
        "Foodie Explorer",
        "Discover famous restaurants and top-rated dishes across India and its neighbours.",
        icon="",
    )
    st.write("")

    col_l, col_mid, col_r = st.columns([1, 2, 1])
    with col_mid:
        with st.container(border=True):
            st.session_state.auth_mode = st.radio(
                "Choose an option",
                ["Login", "Sign up"],
                horizontal=True,
                index=["Login", "Sign up"].index(st.session_state.auth_mode),
            )

            if st.session_state.auth_mode == "Login":
                st.markdown("####  Log in")
                with st.form("login_form"):
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    submitted = st.form_submit_button("Log in", use_container_width=True)
                if submitted:
                    ok, message = auth.login(username, password)
                    if ok:
                        st.session_state.logged_in = True
                        st.session_state.username = username.strip()
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)

            else:
                st.markdown("#### Sign up")
                with st.form("signup_form"):
                    new_username = st.text_input("Choose a username")
                    new_password = st.text_input("Choose a password", type="password")
                    confirm_password = st.text_input("Confirm password", type="password")
                    submitted = st.form_submit_button("Create account", use_container_width=True)
                if submitted:
                    if new_password != confirm_password:
                        st.error("Passwords do not match.")
                    else:
                        ok, message = auth.signup(new_username, new_password)
                        if ok:
                            st.success(message + " Switch to the Login tab to continue.")
                        else:
                            st.error(message)


# --------------------------------------------------------------------------
# COUNTRIES PAGE
# --------------------------------------------------------------------------
def render_countries():
    hero_header(
        "Explore by Country",
        "India and 9 well-known neighbouring countries. Tap a country to see its states/regions.",
        icon="🌏",
    )
    st.write("")

    names = list(COUNTRIES.keys())
    cols_per_row = 5
    for row_start in range(0, len(names), cols_per_row):
        cols = st.columns(cols_per_row)
        for col, name in zip(cols, names[row_start:row_start + cols_per_row]):
            info = COUNTRIES[name]
            with col:
                with st.container(border=True):
                    st.markdown(f"### {info['flag']}")
                    st.markdown(f"**{name}**")
                    st.caption(info["blurb"])
                    if st.button("Explore ➜", key=f"country_{name}", use_container_width=True):
                        st.session_state.selected_country = name
                        st.session_state.selected_region = None
                        st.session_state.selected_restaurant = None
                        go_to("regions")
                        st.rerun()


# --------------------------------------------------------------------------
# REGIONS PAGE (states / cities within a country)
# --------------------------------------------------------------------------
def render_regions():
    country = st.session_state.selected_country
    info = COUNTRIES[country]
    breadcrumb()
    hero_header(
        f"{info['flag']} {country}",
        "Pick a state / region to see its most famous restaurants.",
        icon="🗺️",
    )
    st.write("")

    if st.button("⬅️ Back to countries"):
        go_to("countries")
        st.rerun()

    region_names = list(info["regions"].keys())
    cols_per_row = 5
    for row_start in range(0, len(region_names), cols_per_row):
        cols = st.columns(cols_per_row)
        for col, region in zip(cols, region_names[row_start:row_start + cols_per_row]):
            with col:
                with st.container(border=True):
                    st.markdown(f"**📍 {region}**")
                    n_places = len(info["regions"][region]["restaurants"])
                    st.caption(f"{n_places} featured restaurant(s)")
                    if st.button("View restaurants ➜", key=f"region_{region}", use_container_width=True):
                        st.session_state.selected_region = region
                        st.session_state.selected_restaurant = None
                        go_to("restaurants")
                        st.rerun()

    st.divider()
    with st.expander("🧠 Not listed? Ask the LLM for another region's restaurants"):
        custom_region = st.text_input("Type any city/state/region name", key="custom_region_input")
        if st.button("Generate with LangChain"):
            if not llm_helper.is_configured(st.session_state.llm_api_key):
                st.warning("Add an API key in the sidebar under 'LangChain / LLM' first.")
            elif not custom_region.strip():
                st.warning("Please type a region name.")
            else:
                with st.spinner("Asking the LLM for local favourites..."):
                    result = llm_helper.generate_region_restaurants(
                        country, custom_region.strip(),
                        st.session_state.llm_provider, st.session_state.llm_api_key,
                    )
                if result:
                    info["regions"][custom_region.strip()] = {"restaurants": result}
                    st.session_state.selected_region = custom_region.strip()
                    st.success(f"Generated restaurants for {custom_region.strip()}!")
                    go_to("restaurants")
                    st.rerun()
                else:
                    st.error("Could not generate data. Check your API key/provider and try again.")


# --------------------------------------------------------------------------
# RESTAURANTS PAGE
# --------------------------------------------------------------------------
def render_restaurants():
    country = st.session_state.selected_country
    region = st.session_state.selected_region
    restaurants = COUNTRIES[country]["regions"][region]["restaurants"]

    breadcrumb()
    hero_header(
        f" Famous Restaurants in {region}",
        f"Top picks in {region}, {country}. Tap a restaurant to see its menu & ratings.",
        icon="",
    )
    st.write("")

    if st.button("⬅️ Back to regions"):
        go_to("regions")
        st.rerun()

    cols = st.columns(2)
    for i, (name, details) in enumerate(restaurants.items()):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"###  {name}")
                st.write(details.get("desc", ""))
                avg_rating = round(
                    sum(d["rating"] for d in details["menu"]) / len(details["menu"]), 1
                ) if details.get("menu") else 0
                st.markdown(rating_stars(avg_rating) + "  _(avg. dish rating)_")
                if st.button("View menu ➜", key=f"resto_{name}", use_container_width=True):
                    st.session_state.selected_restaurant = name
                    go_to("menu")
                    st.rerun()


# --------------------------------------------------------------------------
# MENU PAGE
# --------------------------------------------------------------------------
def render_menu():
    country = st.session_state.selected_country
    region = st.session_state.selected_region
    restaurant = st.session_state.selected_restaurant
    details = COUNTRIES[country]["regions"][region]["restaurants"][restaurant]

    breadcrumb()
    hero_header(
        f" Menu — {restaurant}",
        details.get("desc", ""),
        icon="",
    )
    st.write("")

    if st.button("⬅️ Back to restaurants"):
        go_to("restaurants")
        st.rerun()

    st.write("")
    for item in details.get("menu", []):
        with st.container(border=True):
            c1, c2, c3 = st.columns([4, 2, 3])
            with c1:
                st.markdown(f"** {item['dish']}**")
            with c2:
                st.markdown(f"💰 {item['price']}")
            with c3:
                st.markdown(rating_stars(item["rating"]))
                st.progress(min(item["rating"] / 5, 1.0))


# --------------------------------------------------------------------------
# ROUTER
# --------------------------------------------------------------------------
def main():
    if not st.session_state.logged_in:
        render_auth()
        return

    render_sidebar()

    page = st.session_state.page
    if page == "countries" or not st.session_state.selected_country:
        render_countries()
    elif page == "regions":
        render_regions()
    elif page == "restaurants":
        render_restaurants()
    elif page == "menu":
        render_menu()
    else:
        render_countries()


if __name__ == "__main__":
    main()
