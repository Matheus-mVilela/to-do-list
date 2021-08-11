from django.contrib import auth
from . import models

def user_login(request, username: str, password: str) -> models.User:

    user = auth.authenticate(request, username=username, password=password)
    if not user:
        return None

    auth.login(request, user)
    return user


def user_logout(request):
    return auth.logout(request)
