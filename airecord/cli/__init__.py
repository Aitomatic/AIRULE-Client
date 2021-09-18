import sys

import click

from django.core.management import call_command

from ..h1st_ai_app import __path__


@click.command()
def airecord():
    # make sure Django picks up the settings.py in airecord/h1st_ai_app
    sys.path.insert(0, __path__[0])

    # run Django server locally
    call_command('runserver')
