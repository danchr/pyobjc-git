'''
Python mapping for the ExecutionPolicy framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''

import objc
import sys
import Foundation

from ExecutionPolicy import _metadata

sys.modules['ExecutionPolicy'] = mod = objc.ObjCLazyModule(
    "ExecutionPolicy",
    "com.apple.executionpolicy",
    objc.pathForFramework("/System/Library/Frameworks/ExecutionPolicy.framework"),
    _metadata.__dict__, _inline_list_, {
        '__doc__': __doc__,
        'objc': objc,
        '__path__': __path__,
        '__loader__': globals().get('__loader__', None),
    }, (Foundation,))

import sys
del sys.modules['ExecutionPolicy._metadata']
