/*
 * This file is generated by objective.metadata
 *
 * Last update: Tue Aug 19 22:15:50 2014
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(CBCentralManagerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CBPeripheralDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CBPeripheralManagerDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1010 */
}
