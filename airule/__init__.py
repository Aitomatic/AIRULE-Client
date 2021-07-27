import json
from types import SimpleNamespace


metadata = SimpleNamespace(**json.load('metadata.json'))


__version__ = metadata.VERSION
