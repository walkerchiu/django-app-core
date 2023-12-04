from typing import Tuple

from django.conf import settings
from django.db import connection

DJANGO_APP_ORGANIZATION_INSTALLED = (
    importlib.util.find_spec("django_app_organization") is not None
)
if DJANGO_APP_ORGANIZATION_INSTALLED:
    from django_app_organization.models import Organization


class TranslationHelper:
    def __init__(self):
        if DJANGO_APP_ORGANIZATION_INSTALLED:
            self.organization = Organization.objects.only("id").get(
                schema_name=connection.schema_name
            )
            self.language_code = self.organization.language_code
            self.language_support = self.organization.language_support
        else:
            self.organization = None
            self.language_code = settings.LANGUAGE_CODE
            self.language_support = settings.LANGUAGE_SUPPORT

    def validate_translations_from_input(
        self,
        label: str,
        translations: list,
        required: bool = True,
        default_language_required: bool = False,
    ) -> Tuple[bool, str]:
        missing_data_in_default_language = True

        if required and (translations is None or len(translations) == 0):
            return False, str(label) + ": The translations is required!"

        for index, translation in enumerate(translations):
            if translation["language_code"] not in self.language_support:
                return (
                    False,
                    str(label)
                    + f": The languageCode of the translation at index {index} is invalid!",
                )
            if translation["language_code"] == self.language_code:
                missing_data_in_default_language = False

        if default_language_required and missing_data_in_default_language:
            return (
                False,
                str(label)
                + f": Missing data in default language! ({self.language_code})",
            )

        return True, None
