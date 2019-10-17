"""
Wrappers for the "PushKit" framework on macOS 10.15 and later.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup, Extension
import os

VERSION = '6.0'

setup(
    name="pyobjc-framework-PushKit",
    description="Wrappers for the framework PushKit on macOS",
    min_os_level="10.15",
    packages=["PushKit"],
    ext_modules=[
        Extension(
            "PushKit._PushKit",
            ["Modules/_PushKit.m"],
            extra_link_args=["-framework", "PushKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_PushKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
