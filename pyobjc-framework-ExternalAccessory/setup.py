'''
Wrappers for the "ExternalAccessory" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.3a0"

setup(
    name='pyobjc-framework-ExternalAccessory',
    description = "Wrappers for the framework ExternalAccessory on Mac OS X",
    min_os_level="10.13",
    packages = [ "ExternalAccessory" ],
    ext_modules = [
        Extension('ExternalAccessory._inlines',
            [ 'Modules/_ExternalAccessory_inlines.m' ],
            extra_link_args=['-framework', 'ExternalAccessory']),
        Extension("ExternalAccessory._ExternalAccessory",
            [ "Modules/_ExternalAccessory.m" ],
            extra_link_args=["-framework", "ExternalAccessory"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_ExternalAccessory')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
