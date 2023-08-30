# imports
from . import economics
from . import nn
from . import ml

__all__ = [
    'economics'
    'nn',
    'ml'
]

__version__ = "0.0.1"
__name__ = 'toolbox'

__spec__ = {
    'Author': 'Yigit GUMUS',
    'Category': 'Personal Toolbox for multiple purposes',
    'Description': 'Toolbox for multiple purposes like ML, NN and Economics and Statistics.',
    'License': 'Apache License, Version 2.0',
    'LicenseUrl': 'http://github.com/yigitoo/toolbox/tree/master/LICENSE.md'
}

if __name__ == "__main__" and __package__ is None:
    __package__ = 'toolbox'
