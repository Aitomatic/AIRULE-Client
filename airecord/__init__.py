import json
from pathlib import Path
from types import SimpleNamespace

from django.conf import settings as django_settings
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

from .h1st_ai_app import settings as airecord_django_settings

from .util import _AIRECORD_DIR_PATH


__all__ = [
    '__version__',
    '_AIRECORD_DIR_PATH',
]


metadata = SimpleNamespace(**json.load(open(Path(__file__).parent /
                                            'metadata.json')))
__version__ = metadata.VERSION


django_settings.configure(**{
    SETTING_KEY: setting_value
    for SETTING_KEY, setting_value in airecord_django_settings.__dict__.items()
    if SETTING_KEY.isupper()
})
get_wsgi_application()
print('Migrating Local aiRecord Database...')
call_command('migrate')
