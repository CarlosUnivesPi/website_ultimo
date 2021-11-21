import environ

from plataforma_cursos.settings.settings import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOTSTS")

DATABASES = {
    "default": env.db(),
}