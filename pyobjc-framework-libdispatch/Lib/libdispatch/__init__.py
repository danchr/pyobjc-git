'''
Python mapping for the dispatch library on macOS

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions.
'''

import objc
import sys

from libdispatch import _metadata


sys.modules['libdispatch'] = mod = objc.ObjCLazyModule(
    "libdispatch",
    None,
    None,
    _metadata.__dict__, None, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    })

import sys
del sys.modules['libdispatch._metadata']
