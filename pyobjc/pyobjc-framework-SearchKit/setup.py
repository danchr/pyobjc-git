''' 
Wrappers for framework 'SearchKit'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-SearchKit',
    version='2.2b1',
    description = "Wrappers for the framework SearchKit on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "SearchKit" ],
    package_dir = { '': 'Lib' },
    setup_requires = [ 
        'bdist_mpkg>=0.4.2',
    ],
    install_requires = [ 
        'pyobjc-core>=2.0',
        'pyobjc-framework-Cocoa>=2.0',
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.xml'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('SearchKit'),

    # The package is actually zip-safe, but py2app isn't zip-aware yet.
    zip_safe = False,
)
