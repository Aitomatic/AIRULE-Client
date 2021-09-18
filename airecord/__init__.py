import json
from pathlib import Path
from types import SimpleNamespace

from .data import DataSet
from .model import Model


__all__ = [
    '__version__',
    'DataSet',
    'Model'
]


metadata = SimpleNamespace(**json.load(open(Path(__file__).parent /
                                            'metadata.json')))

__version__ = metadata.VERSION
