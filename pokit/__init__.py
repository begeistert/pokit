"""The module helps using Pokit devices into a PC.
for example:
the expression E**(pi*I) will be converted into -1
the expression (x+x)**2 will be converted into 4*x**2
"""

from .Meter import *
from .connect import *

__all__ = [
    'connect', 'Meter.py']
