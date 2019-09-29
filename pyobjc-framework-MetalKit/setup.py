"""
Wrappers for the "MetalKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup, Extension
import os

VERSION = "6.0a0"

setup(
    name="pyobjc-framework-MetalKit",
    description="Wrappers for the framework MetalKit on macOS",
    min_os_level="10.11",
    packages=["MetalKit"],
    ext_modules=[
        Extension(
            "MetalKit._MetalKit",
            ["Modules/_MetalKit.m"],
            extra_link_args=["-framework", "MetalKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_MetalKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
#        "pyobjc-framework-Metal>=" + VERSION
        ],
    long_description=__doc__,
)
