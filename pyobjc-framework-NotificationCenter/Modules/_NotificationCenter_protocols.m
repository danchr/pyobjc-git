/*
 * This file is generated by objective.metadata
 *
 * Last update: Sun Aug 10 14:29:53 2014
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(NCWidgetListViewDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NCWidgetProviding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NCWidgetSearchViewDelegate));
    Py_XDECREF(p);
#endif /* defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1009 */
}
