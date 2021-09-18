import json
from pathlib import Path
from types import SimpleNamespace

from .data import DataSet
from .model import Model


__all__ = [
    '__version__',
    '_AIRECORD_DIR_PATH',
    'DataSet',
    'Model',
]


metadata = SimpleNamespace(**json.load(open(Path(__file__).parent /
                                            'metadata.json')))

__version__ = metadata.VERSION


_AIRECORD_DIR_PATH = Path.home() / '.airecord'
_AIRECORD_DIR_PATH.mkdir(exist_ok=True)
