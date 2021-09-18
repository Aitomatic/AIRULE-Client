import json
import os
from pathlib import Path
from types import SimpleNamespace

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

from .model import AuditTrailedModel
from .util import _AIRECORD_DIR_PATH

from .h1st_ai_app import settings


__all__ = (
    '__metadata__', '__version__',
    'AuditTrailedModel',
    '_AIRECORD_DIR_PATH',
)


# extract package metadata
__metadata__ = SimpleNamespace(**json.load(open(Path(__file__).parent /
                                                'metadata.json')))
__version__ = __metadata__.VERSION


# connect to local aiRecord Django app
os.environ['DJANGO_SETTINGS_MODULE'] = settings.__name__
get_wsgi_application()

# migrate local aiRecord database
print('Migrating Local aiRecord Database...')
call_command('migrate')
