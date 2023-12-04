# django_app_core/apps.py

from django.apps import AppConfig


class DjangoAppCoreConfig(AppConfig):
    name = "django_app_core"

    def ready(self):
        pass
