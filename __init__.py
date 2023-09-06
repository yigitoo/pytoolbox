# imports
from . import economics
from . import nn
from . import ml
from . import mathtools

__all__ = [
    'economics'
    'nn',
    'ml'
]

__version__ = "v0.0.2"
__name__ = 'pytoolbox'

__spec__ = {
    'Author': 'Yigit GUMUS',
    'Category': 'Personal Toolbox for multiple purposes',
    'Description': 'Toolbox for multiple purposes like ML, NN and Economics and Statistics.',
    'License': 'Apache License, Version 2.0',
    'LicenseUrl': 'http://github.com/yigitoo/toolbox/tree/master/LICENSE.md',
    'GithubUrl': 'http://github.com/yigitoo/pytoolbox',
    'GithubUsername': 'yigitoo',
    'Mail': 'rawns0909@gmail.com',
    'Instagram': 'instagram.com/yigiittgumus',
    'XAccount': 'x.com/yigitgumus09',
}

if __name__ == "__main__" and __package__ is None:
    __package__ = 'pytoolbox'
