from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-f1_#v+cjsg+&(473n48fiofkgyg*372etoh8q!m@5n&jk4b#jx"
ALLOWED_HOSTS = ["*"]

try:
    from .local import *
except ImportError:
    pass
