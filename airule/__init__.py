import json
from typing import SimpleNamespace


metadata = SimpleNamespace(**json.load('metadata.json'))


__version__ = metadata.VERSION
