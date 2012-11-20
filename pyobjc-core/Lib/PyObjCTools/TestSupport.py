"""
Helper code for implementing unittests.

This module is unsupported and is primairily used in the PyObjC
testsuite.
"""
from __future__ import print_function
import plistlib as _pl
import unittest as _unittest
import objc
import os as _os
import gc as _gc
import subprocess as _subprocess
import sys as _sys
import struct as _struct
from distutils.sysconfig import get_config_var as _get_config_var
import re as _re
import warnings

# Ensure that methods in this module get filtered in the tracebacks
# from unittest
__unittest = False

# Have a way to disable the autorelease pool behaviour
_usepool = not _os.environ.get('PYOBJC_NO_AUTORELEASE')
_useleaks = bool(_os.environ.get('PyOBJC_USE_LEAKS'))
_leaksVerbose = True

def _typemap(tp):
    if tp is None: return None
    return tp.replace(b'_NSRect', b'CGRect').replace(b'_NSPoint', b'CGPoint').replace(b'_NSSize', b'CGSize')

def sdkForPython(_cache=[]):
    """
    Return the SDK version used to compile Python itself,
    or None if no framework was used
    """
    if not _cache:

        cflags = _get_config_var('CFLAGS')
        m = _re.search('-isysroot\s+([^ ]*)(\s|$)', cflags)
        if m is None:
            _cache.append(None)
            return None


        path = m.group(1)
        if path == '/':
            result = tuple(map(int, os_release().split('.')))
            _cache.append(result)
            return result

        bn = _os.path.basename(path)
        version = bn[6:-4]
        if version.endswith('u'):
            version = version[:-1]


        result =  tuple(map(int, version.split('.')))
        _cache.append(result)
        return result

    return _cache[0]

def fourcc(v):
    """
    Decode four-character-code integer definition

    (e.g. 'abcd')
    """
    return _struct.unpack('>i', v)[0]

def cast_int(value):
    """
    Cast value to 32bit integer

    Usage:
        cast_int(1 << 31) == -1

    (where as: 1 << 31 == 2147483648)
    """
    value = value & 0xffffffff
    if value & 0x80000000:
        value =   ~value + 1 & 0xffffffff
        return -value
    else:
        return value

def cast_longlong(value):
    """
    Cast value to 64bit integer

    Usage:
        cast_longlong(1 << 63) == -1
    """
    value = value & 0xffffffffffffffff
    if value & 0x8000000000000000:
        value =   ~value + 1 & 0xffffffffffffffff
        return -value
    else:
        return value

def cast_uint(value):
    """
    Cast value to 32bit integer

    Usage:
        cast_int(1 << 31) == 2147483648

    """
    value = value & 0xffffffff
    return value

def cast_ulonglong(value):
    """
    Cast value to 64bit integer
    """
    value = value & 0xffffffffffffffff
    return value

_os_release = None
def os_release():
    """
    Returns '10.5' on all releases of Leopard, simularly for other
    major releases.
    """
    global _os_release
    if _os_release is not None:
        return _os_release

    pl = _pl.readPlist('/System/Library/CoreServices/SystemVersion.plist')
    v = pl['ProductVersion']
    return '.'.join(v.split('.')[:2])


def is32Bit():
    """
    Return True if we're running in 32-bit mode
    """
    if _sys.maxsize > 2 ** 32:
        return False
    return True

def onlyIf(expr, message=None):
    """
    Usage::

        class Tests (unittest.TestCase):

            @onlyIf(1 == 2)
            def testUnlikely(self):
                pass

    The test only runs when the argument expression is true
    """
    def callback(function):
        if not expr:
            if hasattr(_unittest, 'skip'):
                return _unittest.skip(message)(function)
            return lambda self: None
        else:
            return function
    return callback

def onlyPython2(function):
    """
    Usage:
        class Tests (unittest.TestCase):

            @onlyPython2
            def testPython2(self):
                pass

    The test is only executed for Python 2.x
    """
    return onlyIf(_sys.version_info[0] == 2, "python2.x only")(function)

def onlyPython3(function):
    """
    Usage:
        class Tests (unittest.TestCase):

            @onlyPython3
            def testPython3(self):
                pass

    The test is only executed for Python 3.x
    """
    return onlyIf(_sys.version_info[0] == 3, "python3.x only")(function)

def onlyOn32Bit(function):
    """
    Usage::

        class Tests (unittest.TestCase):

            @onlyOn32Bit
            def test32BitOnly(self):
                pass

    The test runs only on 32-bit systems
    """
    return onlyIf(is32Bit(), "32-bit only")(function)

def onlyOn64Bit(function):
    """
    Usage::

        class Tests (unittest.TestCase):

            @onlyOn64Bit
            def test64BitOnly(self):
                pass

    The test runs only on 64-bit systems
    """
    return onlyIf(not is32Bit(), "64-bit only")(function)


def min_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @min_os_level('10.6')
            def testSnowLeopardCode(self):
                pass
    """
    if os_release() >= release:
        def decorator(function):
            return function

    else:
        if _sys.version_info[:2] >= (2, 7):
            return _unittest.skip("min_os_level(%s)"%(release,))
        else:
            return lambda self: None

    return decorator

def max_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @max_os_level('10.5')
            def testUntilLeopard(self):
                pass
    """
    if os_release() <= release:
        def decorator(function):
            return function

    else:
        if _sys.version_info[:2] >= (2, 7):
            return _unittest.skip("max_os_level(%s)"%(release,))
        else:
            return lambda self: None

    return decorator



def _leaks():
    data = _subprocess.Popen(
            ['/usr/bin/leaks', str(_os.getpid())], stdout=_subprocess.PIPE
        ).communicate()[0]
    return data.splitlines()


_poolclass = objc.lookUpClass('NSAutoreleasePool')
_nscftype = objc.lookUpClass('NSCFType')

_typealias = {}
if not is32Bit():
    _typealias[objc._C_LNG_LNG] = objc._C_LNG
    _typealias[objc._C_ULNG_LNG] = objc._C_ULNG

else:
    _typealias[objc._C_LNG] = objc._C_INT
    _typealias[objc._C_ULNG] = objc._C_UINT

class TestCase (_unittest.TestCase):
    """
    A version of TestCase that wraps every test into its own
    autorelease pool.

    This also adds a number of useful assertion methods
    """


    def assertIsCFType(self, tp, message = None):
        if not isinstance(tp, objc.objc_class):
            self.fail(message or "%r is not a CFTypeRef type"%(tp,))

        if tp is _nscftype:
            self.fail(message or "%r is not a unique CFTypeRef type"%(tp,))


    def assertIsOpaquePointer(self, tp, message = None):
        if not hasattr(tp, "__pointer__"):
            self.fail(message or "%r is not an opaque-pointer"%(tp,))

        if not hasattr(tp, "__typestr__"):
            self.fail(message or "%r is not an opaque-pointer"%(tp,))


    def assertResultIsNullTerminated(self, method, message = None):
        info = method.__metadata__()
        if not info['retval'].get('c_array_delimited_by_null'):
            self.fail(message or "result of %r is not a null-terminated array"%(method,))

    def assertIsNullTerminated(self, method, message = None):
        info = method.__metadata__()
        if not info.get('c_array_delimited_by_null') or not info.get('variadic'):
            self.fail(message or "%s is not a variadic function with a null-terminated list of arguments"%(method,))

    def assertArgIsNullTerminated(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset].get('c_array_delimited_by_null'):
            self.fail(message or "argument %d of %r is not a null-terminated array"%(argno, method))

    def assertArgIsVariableSize(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset].get('c_array_of_variable_length'):
            self.fail(message or "argument %d of %r is not a variable sized array"%(method,))

    def assertResultIsVariableSize(self, method, message = None):
        info = method.__metadata__()
        if not info['retval'].get('c_array_of_variable_length'):
            self.fail(message or "result of %r is not a variable sized array"%(argno, method))

    def assertArgSizeInResult(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset].get('c_array_length_in_result'):
            self.fail(message or "argument %d of %r does not have size in result"%(argno, method))

    def assertArgIsPrintf(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info.get('variadic'):
            self.fail(message or "%r is not a variadic function"%(method,))

        if not info['arguments'][argno+offset].get('printf_format'):
            self.fail(message or "%r argument %d is not a printf format string"%(method, argno))

    def assertArgIsCFRetained(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset]['already_cfretained']:
            self.fail(message or "%r is not cfretained"%(method,))

    def assertArgIsNotCFRetained(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if info['arguments'][argno+offset]['already_cfretained']:
            self.fail(message or "%r is cfretained"%(method,))

    def assertResultIsCFRetained(self, method, message = None):
        info = method.__metadata__()
        if not info['retval']['already_cfretained']:
            self.fail(message or "%r is not cfretained"%(method,))

    def assertResultIsNotCFRetained(self, method, message = None):
        info = method.__metadata__()
        if info['retval']['already_cfretained']:
            self.fail(message or "%r is cfretained"%(method,))

    def assertResultIsRetained(self, method, message = None):
        info = method.__metadata__()
        if not info['retval']['already_retained']:
            self.fail(message or "%r is not retained"%(method,))

    def assertResultIsNotRetained(self, method, message = None):
        info = method.__metadata__()
        if info['retval']['already_retained']:
            self.fail(message or "%r is retained"%(method,))

    def assertResultHasType(self, method, tp, message=None):
        info = method.__metadata__()
        type = info['retval']['type']
        if type != tp and _typemap(type) != _typemap(tp) \
                and _typealias.get(type, type) != _typealias.get(tp, tp):
            self.fail(message or "result of %r is not of type %r, but %r"%(
                method, tp, type))
        
    def assertArgHasType(self, method, argno, tp, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != tp and _typemap(type) != _typemap(tp) \
                and _typealias.get(type, type) != _typealias.get(tp, tp):
            self.fail(message or "arg %d of %s is not of type %r, but %r"%(
                argno, method, tp, type))

    def assertArgIsFunction(self, method, argno, sel_type, retained, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != b'^?':
            self.fail(message or "arg %d of %s is not of type function_pointer"%(
                argno, method))

        st = info['arguments'][argno+offset].get('callable')
        if st is None:
            self.fail(message or "arg %d of %s is not of type function_pointer"%(
                argno, method))

        iface = st['retval']['type']
        for a in st['arguments']:
            iface += a['type']

        if iface != sel_type:
            self.fail(message or "arg %d of %s is not a function_pointer with type %r, but %r"%(argno, method, sel_type, iface))


        st = info['arguments'][argno+offset]['callable_retained']
        if bool(st) != bool(retained):
            self.fail(message or "arg %d of %s; retained: %r, expected: %r"%(
                argno, method, st, retained))

    def assertArgIsBlock(self, method, argno, sel_type, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            type = info['arguments'][argno+offset]['type']
        except IndexError:
            self.fail("arg %d of %s does not exist"%(argno, method))

        if type != b'@?':
            self.fail(message or "arg %d of %s is not of type block: %s"%(
                argno, method, type))

        st = info['arguments'][argno+offset].get('callable')
        if st is None:
            self.fail(message or "arg %d of %s is not of type block: no callable"%(
                argno, method))

        iface = st['retval']['type']
        if st['arguments'][0]['type'] != b'^v':
            self.fail(message or "arg %d of %s has an invalid block signature"%(argno, method))
        for a in st['arguments'][1:]:
            iface += a['type']

        if iface != sel_type:
            self.fail(message or "arg %d of %s is not a block with type %r, but %r"%(argno, method, sel_type, iface))

    def assertResultIsBlock(self, method, sel_type, message=None):
        info = method.__metadata__()
        type = info['retval']['type']
        if type != b'@?':
            self.fail(message or "result of %s is not of type block: %s"%(
                method, type))

        st = info['retval'].get('callable')
        if st is None:
            self.fail(message or "result of %s is not of type block: no callable specified"%(
                method))

        iface = st['retval']['type']
        if st['arguments'][0]['type'] != b'^v':
            self.fail(message or "result %s has an invalid block signature"%(method))
        for a in st['arguments'][1:]:
            iface += a['type']

        if iface != sel_type:
            self.fail(message or "result of %s is not a block with type %r, but %r"%(method, sel_type, iface))

    def assertArgIsSEL(self, method, argno, sel_type, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != objc._C_SEL:
            self.fail(message or "arg %d of %s is not of type SEL"%(
                argno, method))

        st = info['arguments'][argno+offset].get('sel_of_type')
        if st != sel_type and _typemap(st) != _typemap(sel_type):
            self.fail(message or "arg %d of %s doesn't have sel_type %r but %r"%(
                argno, method, sel_type, st))

    def assertResultIsBOOL(self, method, message=None):
        info = method.__metadata__()
        type = info['retval']['type']
        if type != objc._C_NSBOOL:
            self.fail(message or "result of %s is not of type BOOL, but %r"%(
                method, type))

    def assertArgIsBOOL(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != objc._C_NSBOOL:
            self.fail(message or "arg %d of %s is not of type BOOL, but %r"%(
                argno, method, type))

    def assertArgIsFixedSize(self, method, argno, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        cnt = info['arguments'][argno+offset]['c_array_of_fixed_length']
        if cnt != count:
            self.fail(message or "arg %d of %s is not a C-array of length %d"%(
                argno, method, count))

    def assertArgSizeInArg(self, method, argno, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        cnt = info['arguments'][argno+offset]['c_array_length_in_arg']
        if isinstance(count, (list, tuple)):
            count2 = tuple(x + offset for x in count)
        else:
            count2 = count + offset
        if cnt != count2:
            self.fail(message or "arg %d of %s is not a C-array of with length in arg %d"%(
                argno, method, count))

    def assertResultSizeInArg(self, method, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        cnt = info['retval']['c_array_length_in_arg']
        if cnt != count + offset:
            self.fail(message or "result %s is not a C-array of with length in arg %d"%(
                argno, method, count))


    def assertArgIsOut(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if not type.startswith(b'o^'):
            self.fail(message or "arg %d of %s is not an 'out' argument"%(
                argno, method))

    def assertArgIsInOut(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if not type.startswith(b'N^'):
            self.fail(message or "arg %d of %s is not an 'inout' argument"%(
                argno, method))

    def assertArgIsIn(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if not type.startswith(b'n^'):
            self.fail(message or "arg %d of %s is not an 'in' argument"%(
                argno, method))

    
    #
    # Addition assert methods, all of them should only be necessary for
    # python 2.7 or later
    #

    if not hasattr(_unittest.TestCase, 'assertItemsEqual'): # pragma: no cover
        def assertItemsEqual(self, seq1, seq2, message=None):
            self.assertEqual(set(seq1), set(seq2), message)

    if not hasattr(_unittest.TestCase, 'assertIs'): # pragma: no cover
        def assertIs(self, value, test, message = None):
            if value is not test:
                self.fail(message or  "%r (id=%r) is not %r (id=%r) "%(value, id(value), test, id(test)))

    if not hasattr(_unittest.TestCase, 'assertIsNot'): # pragma: no cover
        def assertIsNot(self, value, test, message = None):
            if value is test:
                self.fail(message or  "%r is %r"%(value, test))

    if not hasattr(_unittest.TestCase, 'assertIsNone'): # pragma: no cover
        def assertIsNone(self, value, message = None):
            self.assertIs(value, None)

    if not hasattr(_unittest.TestCase, 'assertIsNotNone'): # pragma: no cover
        def assertIsNotNone(self, value, message = None):
            if value is None:
                sel.fail(message, "%r is not %r"%(value, test))

    if not hasattr(_unittest.TestCase, 'assertStartsWith'): # pragma: no cover
        def assertStartswith(self, value, check, message=None):
            if not value.startswith(check):
                self.fail(message or "not %r.startswith(%r)"%(value, check))

    if not hasattr(_unittest.TestCase, 'assertHasAttr'): # pragma: no cover
        def assertHasAttr(self, value, key, message=None):
            if not hasattr(value, key):
                self.fail(message or "%s is not an attribute of %r"%(key, value))

    if not hasattr(_unittest.TestCase, 'assertNotHasAttr'): # pragma: no cover
        def assertNotHasAttr(self, value, key, message=None):
            if hasattr(value, key):
                self.fail(message or "%s is an attribute of %r"%(key, value))

    if not hasattr(_unittest.TestCase, 'assertIsInstance'): # pragma: no cover
        def assertIsInstance(self, value, types, message=None):
            if not isinstance(value, types):
                self.fail(message or "%s is not an instance of %r but %s"%(value, types, type(value)))

    if not hasattr(_unittest.TestCase, 'assertIsNotInstance'): # pragma: no cover
        def assertIsNotInstance(self, value, types, message=None):
            if isinstance(value, types):
                self.fail(message or "%s is an instance of %r"%(value, types))

    if not hasattr(_unittest.TestCase, 'assertIn'): # pragma: no cover
        def assertIn(self, value, seq, message=None):
            if value not in seq:
                self.fail(message or "%r is not in %r"%(value, seq))

    if not hasattr(_unittest.TestCase, 'assertNotIn'): # pragma: no cover
        def assertNotIn(self, value, seq, message=None):
            if value in seq:
                self.fail(message or "%r is in %r"%(value, seq))


    if not hasattr(_unittest.TestCase, 'assertGreaterThan'): # pragma: no cover
        def assertGreaterThan(self, val, test, message=None):
            if not (val > test):
                self.fail(message or '%r <= %r'%(val, test))

    if not hasattr(_unittest.TestCase, 'assertGreaterEqual'): # pragma: no cover
        def assertGreaterEqual(self, val, test, message=None):
            if not (val >= test):
                self.fail(message or '%r < %r'%(val, test))

    if not hasattr(_unittest.TestCase, 'assertLessThan'): # pragma: no cover
        def assertLessThan(self, val, test, message=None):
            if not (val < test):
                self.fail(message or '%r >= %r'%(val, test))

    if not hasattr(_unittest.TestCase, 'assertLessEqual'): # pragma: no cover
        def assertLessEqual(self, val, test, message=None):
            if not (val <= test):
                self.fail(message or '%r > %r'%(val, test))

    if not hasattr(_unittest.TestCase, "assertAlmostEquals"): # pragma: no cover
        def assertAlmostEquals(self, val1, val2, message=None):
            self.failUnless(abs (val1 - val2) < 0.00001, 
                    message or 'abs(%r - %r) >= 0.00001'%(val1, val2))


    def run(self, *args):
        """
        Run the test, same as unittest.TestCase.run, but every test is
        run with a fresh autorelease pool.
        """
        if _useleaks:
            leaksBefore = _leaks()
        if _usepool:
            p = _poolclass.alloc().init()
        else:
            p = 1

        try:
            _unittest.TestCase.run(self, *args)
        finally:
            _gc.collect()
            del p
            _gc.collect()
            
            if _useleaks:
                leaksAfter = _leaks()
                if len(leaksBefore) != len(leaksAfter):
                    print("\ntest %s is leaking [%d lines]"%(self, len(leaksAfter) - len(leaksBefore)))
                    if _leaksVerbose:
                        # XXX: add a smartish filter the surpresses the leaks
                        # in leaksBefore.
                        for ln in leaksAfter:
                            print(ln)


main = _unittest.main

if hasattr(_unittest, 'expectedFailure'):
    expectedFailure = _unittest.expectedFailure

else: # pragma: no cover (py2.6)

    def expectedFailure(func):
        def test(self):
            try:
                func(self)
            
            except AssertionError:
                return

            self.fail("test unexpectedly passed")
        test.__name__ == func.__name__

        return test

# XXX: filterwarnings relies on implementation details of
#      the warnings module
class filterWarnings (object):
    def __init__(self, kind, category):
        self._kind = kind
        self._category = category

    def __enter__(self):
        warnings.filterwarnings(self._kind, category=self._category)

    def __exit__(self, type, value, tp):
        del warnings.filters[0]
