/*
 * This file is generated by objective.metadata
 *
 * Last update: Sun Dec 28 14:22:11 2014
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(DOMEventListener)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(DOMEventTarget)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(DOMNodeFilter)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(DOMXPathNSResolver)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WebDocumentRepresentation)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WebDocumentSearching)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WebDocumentText)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WebDocumentView)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WebOpenPanelResultListener)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WebPlugInViewFactory)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WebPolicyDecisionListener)); Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1010 */
#if defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(WKNavigationDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WKScriptMessageHandler)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(WKUIDelegate)); Py_XDECREF(p);
#endif /* defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1010 */
}
