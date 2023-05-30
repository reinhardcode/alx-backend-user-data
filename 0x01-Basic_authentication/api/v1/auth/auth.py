#!/usr/bin/env python3
"""
module that contains the authentication class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """authentication class to manage
    the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authorized path"""
        if path:
            path = path.strip('/')
            path = '/' + path + '/'
        try:
            if path in excluded_paths:
                return False
            return True
        except (Exception):
            return True

    def authorization_header(self, request=None) -> str:
        """authorize headers"""
        if not request or 'Authorization' not in request.headers.keys():
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
