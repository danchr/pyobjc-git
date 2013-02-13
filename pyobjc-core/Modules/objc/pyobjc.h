#ifndef PyObjC_H
#define PyObjC_H

/*
 * Central include file for PyObjC.
 */

#define OBJC_VERSION "3.0a1"

/*
 * Loading Quartz results close to 5K classes
 * on OSX 10.8
 */
#define PYOBJC_EXPECTED_CLASS_COUNT 10000
#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include "structmember.h"
#include "pyobjc-compat.h"

#import <Foundation/Foundation.h>

/*
 * SET_FIELD(op, value):
 *    macro for updating the value of 'op' to 'value',
 *    steals a reference to 'value'.
 *
 *    use this instead of 'Py_XDECREF(op); op = value'
 */
#define SET_FIELD(op, value)                    \
    do {                                        \
        PyObject* _py_tmp = (PyObject*)(op);    \
        (op) = value;                           \
        Py_XDECREF(_py_tmp);                    \
    } while(0)

/*
 * SET_FIELD_INCREF(op, value):
 *    macro for updating the value of 'op' to 'value'.
 *
 *    use this instead of 'Py_XDECREF(op); Py_INCREF(value); op = value'
 */
#define SET_FIELD_INCREF(op, value)             \
    do {                                        \
        PyObject* _py_tmp = (PyObject*)(op);    \
        Py_XINCREF(value);                       \
        (op) = value;                           \
        Py_XDECREF(_py_tmp);                    \
    } while(0)

#ifdef __clang__

/* This is a crude hack to disable a otherwise useful warning in the context of
 * PyTuple_SET_ITEM, without disabling it everywhere
 */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Warray-bounds"
static inline void _PyObjCTuple_SetItem(PyObject* tuple, Py_ssize_t idx, PyObject* value)
{
    PyTuple_SET_ITEM(tuple, idx, value);
}
#undef PyTuple_SET_ITEM
#define PyTuple_SET_ITEM(a, b, c) _PyObjCTuple_SetItem(a, b, c)

static inline PyObject* _PyObjCTuple_GetItem(PyObject* tuple, Py_ssize_t idx)
{
    return PyTuple_GET_ITEM(tuple, idx);
}
#undef PyTuple_GET_ITEM
#define PyTuple_GET_ITEM(a, b) _PyObjCTuple_GetItem(a, b)

#pragma clang diagnostic pop

#endif /* __clang__ */


/* PyObjC_DEBUG: If defined the bridge will perform more internal checks */
#ifdef Py_DEBUG
   /* Enable when Python is compiled with internal checks enabled */
#  define PyObjC_DEBUG
#endif

/* PyObjC_ERROR_ABORT: If defined an internal error will result in an abort() */
#define    PyObjC_ERROR_ABORT 1

/* PyObjC_FAST_BUT_INEXACT: If defined the method lookup will add a selector
 * to the __dict__ of the class of the object that you looked up the selector,
 * when it it is not defined the selector is added to the dict of the class that
 * actually defines the method.
 *
 * The latter is slightly more correct when using objc.super on arbitrary classes,
 * but does result in more calls to the objc runtime and appears to be slower.
 *
 * NOTE: Option is present for performance testing.
 */
/*#define PyObjC_FAST_BUT_INEXACT 1*/


#include <objc/objc-runtime.h>
#include <objc/objc.h>

/* Define PyObjC_UNICODE_FAST_PATH when
 * 1) We're before Python 3.3, and
 * 2) Py_UNICODE has the same size as unichar
 *
 * Python 3.3 has an optimized representation that
 * makes it impossible to use the "fast path"
 */
#if PY_VERSION_HEX >= 0x03030000
#undef PyObjC_UNICODE_FAST_PATH
#elif Py_UNICODE_SIZE == 2
#define PyObjC_UNICODE_FAST_PATH
#endif

/*
 * XXX: disable the fast path for
 * unicode strings due to unexplained
 * test failures.
 */
#if 0
#ifdef PyObjC_UNICODE_FAST_PATH
#undef PyObjC_UNICODE_FAST_PATH
#endif
#endif

#include "arc-runtime.h"
#include "objc-runtime-compat.h"
#include "proxy-registry.h"
#include "objc_support.h"
#include "pointer-support.h"
#include "OC_PythonObject.h"
#include "OC_PythonArray.h"
#include "OC_PythonData.h"
#include "OC_PythonDictionary.h"
#include "OC_PythonUnicode.h"

#if PY_MAJOR_VERSION == 2
#include "OC_PythonString.h"
#endif

#include "OC_PythonEnumerator.h"
#include "OC_PythonDate.h"
#include "OC_PythonNumber.h"
#include "OC_PythonSet.h"
#include "method-signature.h"
#include "objc_util.h"
#include "objc-class.h"
#include "objc-object.h"
#include "selector.h"
#include "libffi_support.h"
#include "super-call.h"
#include "instance-var.h"
#include "class-builder.h"
#include "ObjCPointer.h"
#include "informal-protocol.h"
#include "formal-protocol.h"
#include "alloc_hack.h"
#include "pyobjc_unicode.h"
#include "class-descriptor.h"
#include "class-list.h"
#include "struct-wrapper.h"
#include "method-imp.h"
#include "bundle-variables.h"
#include "function.h"
#include "varlist.h"
#include "objc_super.h"
#include "fsref.h"
#include "fsspec.h"


/*
 * XXX: All definitions below here should be moved to different/new
 * headers
 */

/* On MacOS X, +signatureWithObjCTypes: is a method of NSMethodSignature,
 * but that method is not present in the header files. We add the definition
 * here to avoid warnings.
 *
 * XXX: We use an undocumented API, but we also don't have much choice: we
 * must create the things and this is the only way to do it...
 */
@interface NSMethodSignature (WarningKiller)
    +(instancetype)signatureWithObjCTypes:(const char*)types;
@end /* interface NSMethodSignature */


extern BOOL PyObjC_useKVO;
extern BOOL PyObjC_nativeProperties;
extern int PyObjC_VerboseLevel;
#if PY_MAJOR_VERSION == 2
extern int PyObjC_StrBridgeEnabled;
#endif
extern PyObject *PyObjCStrBridgeWarning;
extern PyObject *PyObjC_NSNumberWrapper;


int PyObjCAPI_Register(PyObject* module);
#define PYOBJC_BUILD
#include "pyobjc-api.h"
#include "registry.h"
#include "corefoundation.h"
#include "closure_pool.h"
#include "block_support.h"
#include "helpers.h"

extern PyObject* PyObjCMethodAccessor_New(PyObject* base, int class_method);

/* Needed by method-accessor, name will be changed soon */
extern PyTypeObject PyObjCMethodAccessor_Type;
char* PyObjC_SELToPythonName(SEL, char*, size_t);


/* opaque-pointer.m */
PyObject* PyObjCCreateOpaquePointerType(const char* name,
        const char* typestr, const char* docstr);

/* objc-NULL.m */
extern PyObject* PyObjC_NULL;
extern PyObject* PyObjCInitNULL(void);

/* socketsupport.m */
int PyObjC_SockAddrFromPython(PyObject*, void*);
PyObject* PyObjC_SockAddrToPython(void*);

/* module.m */
extern PyObject* PyObjC_TypeStr2CFTypeID;
extern PyObject* PyObjC_AdjustSelf(PyObject* self);
extern PyObject* PyObjC_callable_docstr_get(PyObject* callable, void* closure);
#if PY_VERSION_HEX >= 0x03030000
extern PyObject* PyObjC_callable_signature_get(PyObject* callable, void* closure);
#endif




#ifdef PyObjC_DEBUG

#ifdef PyObjCErr_InternalError
#define _PyObjC_InternalError_Bailout()    abort()
#else
#define _PyObjC_InternalError_Bailout()    ((void)0)
#endif

#define PyObjCErr_InternalError() \
    do { \
    PyErr_Format(PyObjCExc_InternalError, \
       "PyObjC: internal error in %s at %s:%d", \
       __FUNCTION__, __FILE__, __LINE__); \
       _PyObjC_InternalError_Bailout(); \
    } while (0)

#define PyObjCErr_InternalErrorMesg(msg) \
    do { \
    PyErr_Format(PyObjCExc_InternalError, \
      "PyObjC: internal error in %s at %s:%d: %s", \
       __FUNCTION__, __FILE__, __LINE__, msg); \
       _PyObjC_InternalError_Bailout(); \
    } while (0)

#define PyObjC_Assert(expr, retval) \
    do { \
    if (!(expr)) { PyObjCErr_InternalErrorMesg(\
            "assertion failed: " #expr); return (retval); } \
    } while (0)
#else

#define PyObjCErr_InternalError()    ((void)0)
#define PyObjCErr_InternalErrorMesg(mesg)    ((void)0)

#define PyObjC_Assert(expr, retval)    ((void)0)

#endif

#endif /* PyObjC_H */
