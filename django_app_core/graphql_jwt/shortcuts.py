from graphql_jwt.refresh_token.shortcuts import create_refresh_token, get_refresh_token
from graphql_jwt.settings import jwt_settings

from django_app_core.graphql_jwt.utils import get_payload, get_user_by_payload

__all__ = [
    "get_token",
    "get_user_by_token",
    "get_refresh_token",
    "create_refresh_token",
]


def get_token(user, context=None, **extra):
    payload = jwt_settings.JWT_PAYLOAD_HANDLER(user, context)
    payload.update(extra)
    return jwt_settings.JWT_ENCODE_HANDLER(payload, context)


def get_user_by_token(token, context=None):
    payload = get_payload(token, context)
    return get_user_by_payload(payload)
