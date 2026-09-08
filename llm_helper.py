"""
Optional LangChain + LLM integration for Foodie Explorer.

If an API key is supplied (Anthropic or OpenAI, via environment variable
or the sidebar in the app), this module uses LangChain to ask an LLM to
invent realistic, well-formatted restaurant and menu data for a
country/region that is not already covered by data.py.

If no API key is configured, every function simply returns None and the
app falls back to the static data in data.py. This keeps the app fully
usable with zero setup, while still demonstrating a real LangChain + LLM
project as requested.
"""

import json
import os
import re

SYSTEM_PROMPT = (
    "You are a concise, accurate local food guide. When asked about a "
    "region, you invent a short, plausible list of famous restaurants "
    "and their signature menu items with ratings out of 5. "
    "Always reply with ONLY valid JSON, no prose, no markdown fences, "
    "matching exactly this schema:\n"
    '{"restaurants": {"Restaurant Name": {"desc": "one sentence", '
    '"menu": [{"dish": "Dish name", "price": "local currency + amount", '
    '"rating": 4.5}]}}}\n'
    "Include 2 restaurants, each with 3 menu items."
)


def _get_llm(provider: str, api_key: str):
    """Build and return a LangChain chat model, or None if unavailable."""
    if not api_key:
        return None
    try:
        if provider == "Anthropic":
            from langchain_anthropic import ChatAnthropic

            return ChatAnthropic(
                model="claude-3-5-haiku-20241022",
                anthropic_api_key=api_key,
                temperature=0.7,
            )
        elif provider == "OpenAI":
            from langchain_openai import ChatOpenAI

            return ChatOpenAI(
                model="gpt-4o-mini",
                openai_api_key=api_key,
                temperature=0.7,
            )
    except ImportError:
        return None
    return None


def _extract_json(text: str) -> dict | None:
    """Pull a JSON object out of an LLM reply, tolerating stray text/fences."""
    text = text.strip()
    text = re.sub(r"^```(json)?", "", text).strip()
    text = re.sub(r"```$", "", text).strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


def generate_region_restaurants(country: str, region: str, provider: str, api_key: str) -> dict | None:
    """
    Ask the LLM to invent restaurants + menu for a country/region that
    isn't in the static dataset. Returns a dict shaped like
    data.py's "restaurants" value, or None if generation isn't possible.
    """
    llm = _get_llm(provider, api_key)
    if llm is None:
        return None

    from langchain_core.messages import HumanMessage, SystemMessage

    user_prompt = (
        f"Country: {country}\n"
        f"Region/City: {region}\n"
        "Give famous local restaurants and their signature dishes."
    )

    try:
        response = llm.invoke(
            [SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=user_prompt)]
        )
        data = _extract_json(response.content)
        if data and "restaurants" in data:
            return data["restaurants"]
    except Exception:
        return None
    return None


def is_configured(api_key: str) -> bool:
    return bool(api_key and api_key.strip())
