"""
Python mapping for the OSLog framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc
import sys
import Foundation

from OSLog import _metadata
import OSLog._OSLog


sys.modules["OSLog"] = mod = objc.ObjCLazyModule(
    "OSLog",
    "com.apple.OSLog",
    objc.pathForFramework("/System/Library/Frameworks/OSLog.framework"),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation,),
)

import sys

del sys.modules["OSLog._metadata"]
