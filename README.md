#  Foodie Explorer

A pure-Streamlit app (no HTML/CSS, no custom JS) for exploring famous
restaurants and top-rated dishes across **India and 9 well-known
neighbouring countries**.

## Flow

1. **Sign up / Log in** — accounts are stored locally in `users.json`
   with salted, hashed passwords (`auth.py`).
2. **Countries** — 10 countries are shown as cards: India, Nepal, Bhutan,
   Sri Lanka, Bangladesh, Pakistan, China, Myanmar, Maldives, Thailand.
3. **States / Regions** — tap a country (e.g. *India*) to see its 10
   states (Andhra Pradesh, Telangana, Tamil Nadu, Karnataka, Kerala,
   Maharashtra, Gujarat, Punjab, West Bengal, Rajasthan). Other countries
   show their top regions/cities.
4. **Restaurants** — tap a state/region (e.g. *Andhra Pradesh*) to see
   its famous restaurants.
5. **Menu** — tap a restaurant to see its menu, prices, and star ratings
   out of 5 for each dish.

## LangChain + LLM (optional)

`llm_helper.py` wires up **LangChain** with either **Anthropic Claude**
or **OpenAI GPT** models. In the sidebar you can paste an API key; from
then on, the "Not listed? Ask the LLM" box on the Regions page will use
LangChain to generate realistic restaurants + menus for any region you
type in, in the same JSON shape as the built-in data.

If you don't add a key, the app works fully offline using the curated
data in `data.py` — nothing is required to run it.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`).

## Project structure

```
foodie_explorer/
├── app.py              # Main Streamlit app (UI + navigation/routing)
├── auth.py             # Local signup/login (hashed passwords, users.json)
├── data.py             # Curated static data: countries -> regions -> restaurants -> menu
├── llm_helper.py        # Optional LangChain + LLM live-generation helper
├── requirements.txt
├── .streamlit/
│   └── config.toml     # Hero colour theme (native Streamlit theming, no CSS)
└── README.md
```

## Notes

- Styling uses **only** native Streamlit primitives: `st.container(border=True)`,
  `st.columns`, `st.markdown` colour spans (e.g. `:orange[...]`), emojis, and
  `.streamlit/config.toml` theming — no raw HTML or CSS anywhere.
- `users.json` is created automatically on first signup; delete it to reset accounts.
- To add real API keys permanently instead of typing them each run, set the
  `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` environment variable before launch,
  or edit `llm_helper.py`.
