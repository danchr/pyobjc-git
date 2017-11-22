'''
Wrappers for the "AVFoundation" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup
import os

VERSION="4.0.2b1"

setup(
    name='pyobjc-framework-libdispatch',
    description = "Wrappers for libdispatch on macOS",
    min_os_level="10.10",
    packages = [ "libdispatch" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
    ],
    long_description=__doc__,
)
