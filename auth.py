"""
Lightweight signup/login system for Foodie Explorer.
Users are stored in a local JSON file with salted-hash passwords.
No external auth service is used, so the app works fully offline.
"""

import json
import os
import hashlib
import hmac
import secrets

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")


def _load_users() -> dict:
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def _save_users(users: dict) -> None:
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)


def _hash_password(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()


def signup(username: str, password: str) -> tuple[bool, str]:
    """Create a new user. Returns (success, message)."""
    username = username.strip()
    if not username or not password:
        return False, "Username and password cannot be empty."
    if len(password) < 4:
        return False, "Password should be at least 4 characters."

    users = _load_users()
    if username in users:
        return False, "That username is already taken."

    salt = secrets.token_hex(8)
    users[username] = {
        "salt": salt,
        "hash": _hash_password(password, salt),
    }
    _save_users(users)
    return True, "Account created! You can now log in."


def login(username: str, password: str) -> tuple[bool, str]:
    """Validate credentials. Returns (success, message)."""
    username = username.strip()
    users = _load_users()
    record = users.get(username)
    if not record:
        return False, "No account found with that username."

    expected = _hash_password(password, record["salt"])
    if hmac.compare_digest(expected, record["hash"]):
        return True, "Login successful."
    return False, "Incorrect password."
