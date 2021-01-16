from functools import wraps
from typing import Callable

import keyring

credentials_key = "tcli"


def set_password(user_name: str, password: str):
    keyring.set_password(credentials_key, user_name, password)


def get_password(user_name: str) -> str:
    return keyring.get_password(credentials_key, user_name)


def ensure_password_is_set(user_name: str) -> Callable:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not get_password(user_name):
                raise RuntimeError(
                    "Username and/or password not found in CLI configuration. "
                    "Run tcli configure credentials to set a username and password."
                )

            return f(*args, **kwargs)

        return wrapper

    return decorator


def delete_password(user_name: str):
    keyring.delete_password(credentials_key, user_name)
