"""
Tests for the new-style metadata format interface.

Note: Tests for calling from ObjC into python are in test_metadata_py.py

TODO:
- Add tests for calling functions instead of methods
- The python->C interface (that is the contents of the metadata object) is
  likely to change when the bridge is feature-complete.
- Probably need special-casing for arrays (numarray and array.array)!
"""
import objc
from PyObjCTools.TestSupport import *
import warnings
import array
import sys

from PyObjCTest.metadata import *

def setupMetaData():
    # Note to self: what we think of as the first argument of a method is 
    # actually the third one, the objc runtime implicitly passed 'self' and
    # the selector as well. Therefore we need to start counting at 2 instead
    # of 0.
    #
    # Note2: the code below would normally be done using a metadata file 
    # instead of hardcoding.
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"boolClassMethod",
            dict(
                retval=dict(type=objc._C_NSBOOL)
            ))

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"unknownLengthArray",
            dict(
                retval=dict(c_array_of_variable_length=True),
        ))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"unknownLengthMutable",
            dict(
                retval=dict(c_array_of_variable_length=True),
        ))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeVariableLengthArray:halfCount:",
            dict(
                arguments={
                    2+0: dict(c_array_of_variable_length=True, type_modifier=objc._C_IN),
                }
        ))

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"varargsMethodWithObjects:",
            dict(
                variadic=True,
            ))

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"ignoreMethod",
            dict(
                suggestion='please ignore me',
            ))

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeArrayWithFormat:",
            dict(
                variadic=True,
                arguments={
                    2+0: dict(printf_format=True),
                }
            ))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeArrayWithCFormat:",
            dict(
                variadic=True,
                arguments={
                    2+0: dict(printf_format=True),
                }
            ))

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeArrayWithArguments:",
            dict(
                variadic=True,
                c_array_delimited_by_null=True
            ))

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"make4Tuple:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"null4Tuple:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeObjectArray:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeStringArray:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullStringArray:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArray:count:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArray:halfCount:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_of_variable_length=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArray:countPtr:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
                  2+1:  dict(type_modifier=objc._C_IN, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullIntArray:count:",
            dict(
                arguments={
                  2+0:  dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillArray:uptoCount:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillArray:count:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullfillArray:count:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"maybeFillArray:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fill4Tuple:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullfill4Tuple:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillStringArray:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullfillStringArray:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_OUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverseArray:uptoCount:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverseArray:count:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullreverseArray:count:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverseStrings:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullreverseStrings:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_delimited_by_null=True, null_accepted=True),
                }
            )
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"maybeReverseArray:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, c_array_length_in_result=True, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"reverse4Tuple:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=False),
                }
            )
        )
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullreverse4Tuple:",
            dict(
                arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, c_array_of_fixed_length=4, null_accepted=True),
                }
            )
        )




    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArrayOf5",
            dict(
                retval=dict(c_array_of_fixed_length=5)
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeStringArray",
            dict(
                retval=dict(c_array_delimited_by_null=True),
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeIntArrayOf:",
            dict(
                retval=dict(c_array_length_in_arg=2+0)
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullIntArrayOf5",
            dict(
                retval=dict(c_array_of_fixed_length=5)
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullStringArray",
            dict(
                retval=dict(c_array_delimited_by_null=True),
            ),
        )

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"nullIntArrayOf:",
            dict(
                retval=dict(c_array_length_in_arg=2+0)
            ),
        )


    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"sumX:andY:", 
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_IN, null_accepted=False),
                    2+1: dict(type_modifier=objc._C_IN, null_accepted=False),
                }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"divBy5:remainder:", 
            dict(arguments={
                    2+1: dict(type_modifier=objc._C_OUT, null_accepted=False),
                }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"swapX:andY:", 
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                    2+1: dict(type_modifier=objc._C_INOUT, null_accepted=False),
                }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"input:output:inputAndOutput:",
            dict(arguments={
                    2+0: dict(type_modifier=objc._C_IN, null_accepted=True),
                    2+1: dict(type_modifier=objc._C_OUT, null_accepted=True),
                    2+2: dict(type_modifier=objc._C_INOUT, null_accepted=True),
            }))

    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeDataForBytes:count:",
            dict(arguments={
                2+0: dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
            }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"makeDataForVoids:count:",
            dict(arguments={
                2+0: dict(type_modifier=objc._C_IN, c_array_length_in_arg=2+1, null_accepted=False),
            }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"addOneToBytes:count:",
            dict(arguments={
                2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=False),
            }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"addOneToVoids:count:",
            dict(arguments={
                2+0: dict(type_modifier=objc._C_INOUT, c_array_length_in_arg=2+1, null_accepted=False),
            }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillBuffer:count:",
            dict(arguments={
                2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=False),
            }))
    objc.registerMetaDataForSelector(b"OC_MetaDataTest", b"fillVoids:count:",
            dict(arguments={
                2+0: dict(type_modifier=objc._C_OUT, c_array_length_in_arg=2+1, null_accepted=False),
            }))


setupMetaData()

class TestArrayDefault (TestCase):
    # TODO: what is the default anyway?
    pass

class TestArraysOut (TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        v = o.fill4Tuple_(None)
        self.assertEquals(list(v), [0, -1, -8, -27])

        self.assertRaises(ValueError, o.fill4Tuple_, objc.NULL)

        n, v = o.nullfill4Tuple_(None)
        self.assertEquals(n, 1)
        self.assertEquals(list(v), [0, -1, -8, -27])

        n, v = o.nullfill4Tuple_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIsObject(v, objc.NULL)

        a = array.array('i', [0]* 4)
        v = o.fill4Tuple_(a);
        self.assertIsObject(a, v)
        self.assertEquals(list(a), [0, -1, -8, -27])

        a = array.array('i', [0]* 5)
        self.assertRaises(ValueError, o.fill4Tuple_, a)
        a = array.array('i', [0]* 3)
        self.assertRaises(ValueError, o.fill4Tuple_, a)
        
    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        # Output only arrays of null-terminated arrays cannot be
        # wrapped automaticly. How is the bridge supposed to know
        # how much memory it should allocate for the C-array?
        self.assertRaises(TypeError, o.fillStringArray_, None)
        self.assertRaises(ValueError, o.fillStringArray_, objc.NULL)

        self.assertRaises(TypeError, o.nullfillStringArray_)
        self.assertRaises(TypeError, o.nullfillStringArray_, None)
        n, v = o.nullfillStringArray_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIsObject(v, objc.NULL)

    def testWithCount(self):
        o = OC_MetaDataTest.new()

        v = o.fillArray_count_(None, 3)
        self.assertEquals(list(v),  [0,1,4])

        v = o.fillArray_count_(None, 3)
        self.assertEquals(list(v),  [0,1,4])

        v = o.fillArray_count_(None, 5)
        self.assertEquals(list(v),  [0,1,4,9,16])

        v = o.fillArray_count_(None, 0)
        self.assertEquals(list(v),  [])

        self.assertRaises(ValueError, o.fillArray_count_, objc.NULL, 0)

        n, v = o.nullfillArray_count_(None, 4)
        self.assertEquals(n, 1)
        self.assertEquals(list(v),  [0,1,4,9])
        n, v = o.nullfillArray_count_(None, 3)
        self.assertEquals(n, 1)
        self.assertEquals(list(v),  [0,1,4])

        n, v = o.nullfillArray_count_(objc.NULL, 3)
        self.assertEquals(n, 0)
        self.assertIsObject(v, objc.NULL)

        a = array.array('i', [0]* 10)
        v = o.fillArray_count_(a, 10);
        self.assertIsObject(a, v)
        self.assertEquals(list(a), [0, 1, 4, 9, 16, 25, 36, 49, 64, 81 ])

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()

        c, v = o.fillArray_uptoCount_(None, 20)
        self.assertEquals(c, 10)
        self.assertEquals(list(v),  [i+2 for i in range(10)])

        c, v = o.maybeFillArray_(None)
        self.assertEquals(c, 2)
        self.assertEquals(list(v),  [10, 11])


class TestArraysInOut (TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        a = (1,2,3,4)
        v = o.reverse4Tuple_(a)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (4,3,2,1))

        self.assertRaises(ValueError, o.reverse4Tuple_, (1,2,3))
        self.assertRaises(ValueError, o.reverse4Tuple_, (1,2,3,4,5))
        self.assertRaises(ValueError, o.reverse4Tuple_, objc.NULL)

        a = (1,2,3,4)
        n, v = o.nullreverse4Tuple_(a)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1,2,3,4))
        self.assertEquals(v, (4,3,2,1))

        n, v = o.nullreverse4Tuple_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIsObject(v, objc.NULL)

        a = array.array('h', [1, 2, 3, 4])
        v = o.reverse4Tuple_(a)
        self.assertIsObject(v, a)
        self.assertEquals(list(a), [4,3,2,1])

        a = array.array('h', [1, 2, 3, 4, 5])
        self.assertRaises(ValueError, o.reverse4Tuple_, a)
        a = array.array('h', [1, 2, 3])
        self.assertRaises(ValueError, o.reverse4Tuple_, a)

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        a = (b'a', b'b', b'c')
        v = o.reverseStrings_(a)
        self.assertEquals(a, (b'a', b'b', b'c'))
        self.assertEquals(v, (b'c', b'b', b'a'))

        self.assertRaises(ValueError, o.reverseStrings_, (1,2))
        self.assertRaises(ValueError, o.reverseStrings_, objc.NULL)

        a = (b'a', b'b', b'c')
        n, v = o.nullreverseStrings_(a)
        self.assertEquals(n, 1)
        self.assertEquals(a, (b'a', b'b', b'c'))
        self.assertEquals(v, (b'c', b'b', b'a'))

        n, v = o.nullreverseStrings_(objc.NULL)
        self.assertEquals(n, 0)
        self.assertIsObject(v, objc.NULL)

    def testWithCount(self):
        o = OC_MetaDataTest.new()

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 4)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        v = o.reverseArray_count_(a, 5)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        # Nice to have, but doesn't work without major
        # surgery:
        #a = (1.0, 2.0, 3.0, 4.0, 5.0)
        #v = o.reverseArray_count_(a, None)
        #self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        #self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        self.assertRaises(ValueError, o.reverseArray_count_, (1.0, 2.0), 5)
        self.assertRaises(ValueError, o.reverseArray_count_, objc.NULL, 0)

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = o.nullreverseArray_count_(a, 4)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (4.0, 3.0, 2.0, 1.0))

        a = (1.0, 2.0, 3.0, 4.0, 5.0)
        n, v = o.nullreverseArray_count_(a, 5)
        self.assertEquals(n, 1)
        self.assertEquals(a, (1.0, 2.0, 3.0, 4.0, 5.0))
        self.assertEquals(v, (5.0, 4.0, 3.0, 2.0, 1.0))

        n, v = o.nullreverseArray_count_(objc.NULL, 0)
        self.assertEquals(n, 0)
        self.assertIsObject(v, objc.NULL)

        a = array.array('f', [5.0, 7.0, 9.0, 11.0, 13.0])
        v = o.reverseArray_count_(a, 5)
        self.assertIsObject(a, v)
        self.assertEquals(list(a), [13.0, 11.0, 9.0, 7.0, 5.0])

    def testWithCountInResult(self):
        o = OC_MetaDataTest.new()

        c, v = o.reverseArray_uptoCount_(range(10), 10)
        self.assertEquals(c, 5)
        self.assertEquals(len(v), 5)
        self.assertEquals(list(v),  [9, 8, 7, 6, 5])
        
        c, v = o.maybeReverseArray_([1,2,3,4])
        self.assertEquals(c, 2)
        self.assertEquals(len(v), 2)
        self.assertEquals(list(v),  [4, 3])

class TestArraysIn (TestCase):
    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        v = o.make4Tuple_((1.0, 4.0, 8.0, 12.5))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 4.0, 8.0, 12.5])

        v = o.make4Tuple_((1, 2, 3, 4))
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1.0, 2.0, 3.0, 4.0])

        self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3))
        self.assertRaises(ValueError, o.make4Tuple_, (1, 2, 3, 4, 5))
        self.assertRaises(ValueError, o.make4Tuple_, objc.NULL)

        v = o.null4Tuple_(objc.NULL)
        self.assertIsNone(v)

        a = array.array('d', [2.5, 3.5, 4.5, 5.5])
        v = o.make4Tuple_(a)
        self.assertEquals(list(v), [2.5, 3.5, 4.5, 5.5])

    def testNullTerminated(self):
        o = OC_MetaDataTest.new()

        v = o.makeStringArray_((b"hello", b"world", b"there"))
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [u"hello", u"world", u"there"])
        self.assertIsInstance(v, objc.lookUpClass("NSArray"))
        self.assertIsInstance(v[0], unicode)

        NSObject = objc.lookUpClass('NSObject')
        p, q, r = NSObject.new(), NSObject.new(), NSObject.new()
        v = o.makeObjectArray_((p, q, r))
        self.assertEquals(len(v), 3)
        self.assertIsObject(v[0], p)
        self.assertIsObject(v[1], q)
        self.assertIsObject(v[2], r)


        v = o.makeStringArray_(())
        self.assertEquals(len(v), 0)

        self.assertRaises(ValueError, o.makeStringArray_, [1,2])
        self.assertRaises(ValueError, o.makeStringArray_, objc.NULL)

        v = o.nullStringArray_(objc.NULL)
        self.assertEquals(v, None)

    def testWithCount(self):
        o = OC_MetaDataTest.new()

        v = o.makeIntArray_count_((1,2,3,4), 3)
        self.assertEquals(len(v), 3)
        self.assertEquals(list(v), [1,2,3])
        
        # XXX: This one would be nice to have, but not entirely trivial
        #v = o.makeIntArray_count_((1,2,3,4), None)
        #self.assertEquals(len(v), 3)
        #self.assertEquals(list(v), [1,2,3,4])

        self.assertRaises(ValueError, o.makeIntArray_count_, [1,2,3], 4)
        self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 0)
        self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        v = o.nullIntArray_count_(objc.NULL, 0)
        self.assertEquals(v, None)

        self.assertRaises(ValueError, o.makeIntArray_count_, objc.NULL, 1)

        # Make sure this also works when the length is in a pass-by-reference argument
        v = o.makeIntArray_countPtr_((1,2,3,4), 4)
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [1,2,3,4])

        a = array.array('i', range(20))
        v = o.makeIntArray_count_(a, 7)
        self.assertEquals(list(v), list(range(7)))

        self.assertRaises(ValueError, o.makeIntArray_count_, a, 21)


class TestArrayReturns (TestCase):
    # TODO:
    # - Add null-terminated arrays of various supported types:
    #   -> integers
    #   -> CF-types

    def testFixedSize(self):
        o = OC_MetaDataTest.new()

        v = o.makeIntArrayOf5()
        self.assertEquals( len(v), 5 )
        self.assertEquals( v[0], 0 )
        self.assertEquals( v[1], 1 )
        self.assertEquals( v[2], 4 )
        self.assertEquals( v[3], 9 )
        self.assertEquals( v[4], 16 )

        v = o.nullIntArrayOf5()
        self.assertEquals(v, objc.NULL)

    def testSizeInArgument(self):
        o = OC_MetaDataTest.new()
        v = o.makeIntArrayOf_(3)
        self.assertEquals(len(v), 3)
        self.assertEquals(v[0], 0)
        self.assertEquals(v[1], 1)
        self.assertEquals(v[2], 8)

        v = o.makeIntArrayOf_(10)
        self.assertEquals(len(v), 10)
        for i in range(10):
            self.assertEquals(v[i], i**3)

        v = o.nullIntArrayOf_(100)
        self.assertEquals(v, objc.NULL)

    def testNULLterminated(self):
        o  = OC_MetaDataTest.new()

        v = o.makeStringArray()
        self.assertEquals(len(v), 4)
        self.assertEquals(list(v), [b"hello", b"world", b"out", b"there"])

        v = o.nullStringArray()
        self.assertEquals(v, objc.NULL)

class TestByReference (TestCase):
    # Pass by reference arguments. 
    # Note that these tests aren't exhaustive, we have test_methods and
    # test_methods2 for that :-)

    def testInput(self):
        o = OC_MetaDataTest.new()
        
        r = o.sumX_andY_(1, 2)
        self.assertEquals(r, 1+2)

        r = o.sumX_andY_(2535, 5325)
        self.assertEquals(r, 2535 + 5325)

        self.assertRaises(ValueError, o.sumX_andY_, 42, objc.NULL)

    def testOutput(self):
        o = OC_MetaDataTest.new()

        div, rem = o.divBy5_remainder_(55, None)
        self.assertEquals(div, 11)
        self.assertEquals(rem, 0)

        div, rem = o.divBy5_remainder_(13, None)
        self.assertEquals(div, 2)
        self.assertEquals(rem, 3)

        self.assertRaises(ValueError, o.divBy5_remainder_, 42, objc.NULL)

    def testInputOutput(self):
        o = OC_MetaDataTest.new()
        x, y = o.swapX_andY_(42, 284)
        self.assertEquals(x, 284)
        self.assertEquals(y, 42)

        self.assertRaises(ValueError, o.swapX_andY_, 42, objc.NULL)

    def testNullAccepted(self):
        o = OC_MetaDataTest.new();

        def makeNum(value):
            return int(value, 0)

        # All arguments present
        r, y, z = o.input_output_inputAndOutput_(1, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 3)
        self.assertEquals(y, 3)
        self.assertEquals(z, -1)

        r, y, z = o.input_output_inputAndOutput_(1, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 3)
        self.assertEquals(y, 3)
        self.assertEquals(z, -1)

        # Argument 1 is NULL
        r, y, z = o.input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 40)
        self.assertEquals(z, -2)

        r, y, z = o.input_output_inputAndOutput_(objc.NULL, None, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 40)
        self.assertEquals(z, -2)

        # Argument 2 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, objc.NULL, 2)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, objc.NULL)
        self.assertEquals(z, -1)

        # Argument 3 is NULL
        r, y, z = o.input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 43)
        self.assertEquals(z, objc.NULL)

        r, y, z = o.input_output_inputAndOutput_(1, None, objc.NULL)
        self.assertEquals(len(r), 3)
        self.assertEquals(len(filter(None, map(makeNum, r))), 2)
        self.assertEquals(y, 43)
        self.assertEquals(z, objc.NULL)

class TestPrintfFormat (TestCase):
    def test_nsformat(self):
        o = OC_MetaDataTest.new()

        v = o.makeArrayWithFormat_("%3d", 10)
        self.assertEquals(list(v), [ "%3d", " 10"])

        v = o.makeArrayWithFormat_("%s", b"foo")
        self.assertEquals(list(v), [ "%s", "foo"])

        v = o.makeArrayWithFormat_("hello %s", b"world")
        self.assertEquals(list(v), [ "hello %s", "hello world"])

        v = o.makeArrayWithFormat_(u"hello %s", b"world")
        self.assertEquals(list(v), [ "hello %s", u"hello world"])

        self.assertRaises(ValueError, o.makeArrayWithFormat_, "%s")

    def test_cformat(self):
        o = OC_MetaDataTest.new()

        v = o.makeArrayWithCFormat_(b"%3d", 10)
        self.assertEquals(list(v), [ "%3d", " 10"])

        v = o.makeArrayWithCFormat_(b"hello %s", b"world")
        self.assertEquals(list(v), [ "hello %s", "hello world"])

        v = o.makeArrayWithCFormat_(b"hello %s x %d", b"world", 42)
        self.assertEquals(list(v), [ "hello %s x %d", "hello world x 42"])

        # As we implement a format string parser we'd better make sure that
        # that code is correct...

        # Generic table below doesn't work for these
        for fmt, args in [
            ( b'%#+x', (99,)),
            ( b'%+#x', (99,)),
            ( b'% #x', (99,)),
            ]:

                v = o.makeArrayWithCFormat_(fmt, *args)
                self.assertEquals(map(unicode, list(v)), [fmt.decode('latin'), (fmt.decode('latin')%args)[1:]] )

        # Insert thousands seperator, the one in the C locale is ''
        v = o.makeArrayWithCFormat_(b"%'d", 20000)
        self.assertEquals(list(v), [ "%'d", '20000'])
        v = o.makeArrayWithCFormat_(b"%hhd", 20)
        self.assertEquals(list(v), [ "%hhd", '20'])
        v = o.makeArrayWithCFormat_(b"%lld", 20)
        self.assertEquals(list(v), [ "%lld", '20'])
        v = o.makeArrayWithCFormat_(b"%lld", -20)
        self.assertEquals(list(v), [ "%lld", '-20'])
        v = o.makeArrayWithCFormat_(b"%zd", 20)
        self.assertEquals(list(v), [ "%zd", '20'])
        v = o.makeArrayWithCFormat_(b"%td", 20)
        self.assertEquals(list(v), [ "%td", '20'])
        v = o.makeArrayWithCFormat_(b"%qd", 20)
        self.assertEquals(list(v), [ "%qd", '20'])
        v = o.makeArrayWithCFormat_(b"%qd", -20)
        self.assertEquals(list(v), [ "%qd", '-20'])
        v = o.makeArrayWithCFormat_(b"%D", -20)
        self.assertEquals(list(v), [ "%D", '-20'])
        v = o.makeArrayWithCFormat_(b"%O", 8)
        self.assertEquals(list(v), [ "%O", '10'])
        v = o.makeArrayWithCFormat_(b"%U", 8)
        self.assertEquals(list(v), [ "%U", '8'])

        obj = object()
        v = o.makeArrayWithCFormat_(b"%p", obj)
        self.assertEquals(list(v), [ "%p", '%#x'%(id(obj),)])

        v = o.makeArrayWithCFormat_(b"%lc%lc", 'd', 'e')
        self.assertEquals(list(v), [ "%lc%lc", 'de'])

        v = o.makeArrayWithCFormat_(b"%C", 'A')
        self.assertEquals(list(v), [ "%C", 'A'])

        v = o.makeArrayWithCFormat_(b"%C%C%c", 'A', 90, 'b')
        self.assertEquals(list(v), [ "%C%C%c", 'A%cb'%(90,)])

        v = o.makeArrayWithCFormat_(b"%S", 'hello world')
        self.assertEquals(list(v), [ "%S", 'hello world'])
        v = o.makeArrayWithCFormat_(b"%S", u'hello world')
        self.assertEquals(list(v), [ "%S", 'hello world'])

        v = o.makeArrayWithCFormat_(b"%ls", 'hello world')
        self.assertEquals(list(v), [ "%ls", 'hello world'])
        v = o.makeArrayWithCFormat_(b"%ls", u'hello world')
        self.assertEquals(list(v), [ "%ls", 'hello world'])

        TEST_TAB = [
            ( b'% #d', (99,)),
            ( b'%0#4x', (99,)),
            ( b'%#+d', (99,)),
            ( b'%+#d', (99,)),
            ( b'%o', (20,) ),
            ( b'%10o', (9,) ),
            ( b'%d %.*o', (2, 5, 7,) ),
            ( b'%*o', (5, 7,) ),
            ( b'%.*o', (5, 7,) ),
            ( b'%.*f', (3, 0.23424)),
            ( b'%*.*f', (12, 3, 0.23424)),
            ( b'%F', (-4.6,)),
            ( b'%f', (2.7,)),
            ( b'%e', (2.7,)),
            ( b'%E', (-4.6,)),
            ( b'%g', (2.7,)),
            ( b'%G', (-4.6,)),
            ( b'%.9f', (0.249,)),
            ( b'%ld', (42,)),
            ( b'%c', (42,)),
            ( b'%hd', (42,)),
            ( b'%lx', (42,)),
            ( b'%%%d%%', (99,)),
            ( b'%c', ('a',) ),
            ( b'%c%c', ('c', 'd')),
            ( b'%c%c', (90, 'd')),
            ( b'%f %f %f %f %f %f %f %f', (1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5))

            # We don't have long double support at all
            #( '%Lg', (42.0,)),
        ]

        for fmt, args in TEST_TAB:
            v = o.makeArrayWithCFormat_(fmt, *args)
            self.assertEquals(list(v), [ fmt.decode('latin1'), fmt.decode('latin1')%args ])


class TestVariadic (TestCase):
    def testRaises(self):
        o = OC_MetaDataTest.new()

        self.assertRaises(TypeError, o.varargsMethodWithObjects_, 1)
        self.assertRaises(TypeError, o.varargsMethodWithObjects_, 1, 2, 3)

class TestIgnore (TestCase):
    def testRaises(self):
        o = OC_MetaDataTest.new()

        self.assertRaises(TypeError, o.ignoreMethod)

    def testClassmethods(self):
        self.assertResultIsBOOL(OC_MetaDataTest.boolClassMethod)

class TestMetaDataAccess (TestCase):
    def testNew(self):
        self.assertResultIsRetained(OC_MetaDataTest.new)

    def testSuggestions(self):
        meta = OC_MetaDataTest.varargsMethodWithObjects_.__metadata__()
        self.assertIsInstance(meta, dict)
        self.assertIsIn('suggestion', meta)
        self.assertEquals(meta['suggestion'], "Variadic functions/methods are not supported")

        meta = OC_MetaDataTest.ignoreMethod.__metadata__()
        self.assertIsInstance(meta, dict)
        self.assertIsIn('suggestion', meta)
        self.assertEquals(meta['suggestion'], "please ignore me")

    def testPrintfFormat(self): 
        meta = OC_MetaDataTest.makeArrayWithFormat_.__metadata__()
        self.assertEquals(meta['variadic'], True)
        self.assertIsNotIn('printf_format', meta['arguments'][0])
        self.assertEquals(meta['arguments'][2]['printf_format'], True)

    def testVariadic(self):
        meta = OC_MetaDataTest.makeArrayWithFormat_.__metadata__()
        self.assertEquals(meta['variadic'], True)

        meta = OC_MetaDataTest.ignoreMethod.__metadata__()
        self.assertEquals(meta['variadic'], False)
       
    def testTypes(self):
        meta = OC_MetaDataTest.ignoreMethod.__metadata__()
        self.assertEquals(meta['retval']['type'], objc._C_INT)
        self.assertEquals(meta['arguments'][0]['type'], objc._C_ID)
        self.assertEquals(meta['arguments'][1]['type'], objc._C_SEL)


        meta = OC_MetaDataTest.make4Tuple_.__metadata__()
        self.assertEquals(meta['retval']['type'], objc._C_ID)
        self.assertEquals(meta['arguments'][0]['type'], objc._C_ID)
        self.assertEquals(meta['arguments'][1]['type'], objc._C_SEL)
        self.assertEquals(meta['arguments'][2]['type'], objc._C_IN + objc._C_PTR + objc._C_DBL)

    def testAllowNull(self):
        meta = OC_MetaDataTest.make4Tuple_.__metadata__()
        self.assertIsNotIn('null_accepted', meta['retval'])
        self.assertIsNotIn( 'null_accepted', meta['arguments'][0])

        meta = OC_MetaDataTest.make4Tuple_.__metadata__()
        self.assertEquals(meta['arguments'][2]['null_accepted'], False)

        meta = OC_MetaDataTest.null4Tuple_.__metadata__()
        self.assertEquals(meta['arguments'][2]['null_accepted'], True)

    def alreadyRetained(self):
        meta = OC_MetaDataTest.null4Tuple_.__metadata__()
        self.assertEquals(meta['already_retained'], False)

        meta = OC_MetaDataTest.alloc.__metadata__()
        self.assertEquals(meta['already_retained'], True)

    def testClassMethod(self):
        meta = OC_MetaDataTest.alloc.__metadata__()
        self.assertEquals(meta['classmethod'], True)

        meta = OC_MetaDataTest.pyobjc_instanceMethods.init.__metadata__()
        self.assertEquals(meta['classmethod'], False)

if sys.version_info[0] == 3:
    def buffer_as_bytes(v):
        if isinstance(v, bytes):
            return v
        return bytes(v)
else:
    def buffer_as_bytes(v):
        return str(buffer(v))

class TestBuffers (TestCase):
    # Some tests that check if buffer APIs get sane treatment

    def testInChars(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeDataForBytes_count_(b"hello world", len(b"hello world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEquals(v.length(), len(b"hello world"))
        self.assertEquals(buffer_as_bytes(v), b"hello world")

        v = o.makeDataForBytes_count_(b"hello\0world", len(b"hello\0world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEquals(v.length(), len(b"hello\0world"))
        self.assertEquals(buffer_as_bytes(v), b"hello\0world")

        a = array.array('b', b'foobar monday')
        v = o.makeDataForBytes_count_(a, len(a))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEquals(v.length(), len(a))
        self.assertEquals(buffer_as_bytes(v), buffer_as_bytes(a))

    def testInVoids(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeDataForBytes_count_(b"hello world", len(b"hello world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEquals(v.length(), len(b"hello world"))
        self.assertEquals(buffer_as_bytes(v), b"hello world")

        v = o.makeDataForBytes_count_(b"hello\0world", len(b"hello\0world"))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEquals(v.length(), len(b"hello\0world"))
        self.assertEquals(buffer_as_bytes(v), b"hello\0world")

        a = array.array('b', b'foobar monday')
        v = o.makeDataForBytes_count_(a, len(a))
        self.assertIsInstance(v, objc.lookUpClass("NSData"))

        self.assertEquals(v.length(), len(a))
        self.assertEquals(buffer_as_bytes(v), buffer_as_bytes(a))

    def testInOutChars(self):
        o = OC_MetaDataTest.alloc().init()
        
        input = b"hello " + b"world"
        v = o.addOneToBytes_count_(input, len(input))
        self.assertIsInstance(v, bytes)

        self.assertEquals(input, b"hello world")
        self.assertEquals(input[0:5], b"hello")
        if sys.version_info[0] == 2:
            self.assertEquals(
                [ ord(x)+1 for x in input ],
                [ ord(x) for x in v ])
        else:
            self.assertEquals(
                [ x+1 for x in input ],
                [ x for x in v ])

        input = array.array('b', b"hello\0world")
        v = o.addOneToBytes_count_(input, len(input))
        self.assertIsObject(v, input)
        self.assertNotEquals(input[0:5], b"hello")
        if sys.version_info[0] == 2:
            self.assertEquals(
                [ ord(x)+1 for x in "hello\0world" ],
                [ ord(x) for x in v ])
        else:
            self.assertEquals(
                [ x+1 for x in b"hello\0world" ],
                [ x for x in v ])


    def testInOutVoids(self):
        o = OC_MetaDataTest.alloc().init()
        
        input = b"hello " + b"world"
        v = o.addOneToVoids_count_(input, len(input))
        self.assertIsInstance(v, type(b""))

        self.assertEquals(input, b"hello world")
        self.assertEquals(input[0:5], b"hello")

        if sys.version_info[0] == 2:
            self.assertEquals(
                [ ord(x)+2 for x in input ],
                [ ord(x) for x in v ])
        else:
            self.assertEquals(
                [ x+2 for x in input ],
                [ x for x in v ])

        input = array.array('b', b"hello\0world")
        v = o.addOneToVoids_count_(input, len(input))
        self.assertIsObject(v, input)
        self.assertNotEquals(input[0:5], b"hello")
        if sys.version_info[0] == 2:
            self.assertEquals(
                [ ord(x)+2 for x in b"hello\0world" ],
                [ ord(x) for x in v ])
        else:
            self.assertEquals(
                [ x+2 for x in b"hello\0world" ],
                [ x for x in v ])

    def testOutChars(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.fillBuffer_count_(None, 44);
        self.assertEquals(v, b'\xfe'*44);

        a = array.array('b', b'0' * 44)
        v = o.fillBuffer_count_(a, 44);
        self.assertEquals(buffer_as_bytes(v), b'\xfe'*44);
        self.assertIsObject(v, a)

    def testOutVoids(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.fillVoids_count_(None, 44);
        self.assertEquals(v, b'\xab'*44);

        if sys.version_info[0] == 2:
            a = array.array('c', '0' * 44)
        else:
            a = array.array('b', (0,) * 44)
        v = o.fillVoids_count_(a, 44);
        self.assertEquals(buffer_as_bytes(v), b'\xab'*44);
        self.assertIsObject(v, a)

class TestVariableLengthValue (TestCase):

    def testResult(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.unknownLengthArray()
        self.assertIsInstance(v, objc.varlist)

        self.assertEquals(v[0], 1)
        self.assertEquals(v[1], 3)
        self.assertEquals(v[5], 13)

        #self.fail((type(v), v))
        #self.fail((v[0:2], type(v[0:2])))
        self.assertEquals(v[0:2], (1,3))

        self.assertEquals(v.as_tuple(5), (1, 3, 5, 7, 11))
        self.assertEquals(v.as_tuple(0), ())
        self.assertEquals(v.as_tuple(8), (1, 3, 5, 7, 11, 13, 17, 19))

        v = o.unknownLengthMutable()
        self.assertIsInstance(v, objc.varlist)

        v[1] = 42
        self.assertEquals(v[1], 42)
        v[0:10] = range(10)
        self.assertEquals(v[0], 0)
        self.assertEquals(v[5], 5)
        self.assertEquals(v[8], 8)

    def testInput(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeIntArray_halfCount_((1,2,3,4,5,6), 2)
        self.assertEquals(list(v), [1,2,3,4])

        # XXX: Hard crash when using o.makeVariableLengthArray_halfCount_???

class TestVariadicArray (TestCase):
    def testObjects(self):
        o = OC_MetaDataTest.alloc().init()

        v = o.makeArrayWithArguments_()
        self.assertEquals(v, [])

        v = o.makeArrayWithArguments_(1, 2, 3)
        self.assertEquals(v, [1, 2, 3])

        v = o.makeArrayWithArguments_(4, None, 5)
        self.assertEquals(v, [4])

        v = o.makeArrayWithArguments_(*range(40))
        self.assertEquals(v, list(range(40)))

if __name__ == "__main__":
    main()
