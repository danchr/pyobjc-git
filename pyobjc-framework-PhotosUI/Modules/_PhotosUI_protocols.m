/*
 * This file is generated by objective.metadata
 *
 * Last update: Tue May 26 22:53:41 2015
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(PHContentEditingController));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1011 */
#if PyObjC_BUILD_RELEASE >= 1012
    p = PyObjC_IdToPython(@protocol(PHLivePhotoViewDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1012 */
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(PHProjectExtensionController));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1013 */
#if PyObjC_BUILD_RELEASE >= 1014
    p = PyObjC_IdToPython(@protocol(PHProjectTypeDescriptionDataSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(PHProjectTypeDescriptionInvalidator));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1014 */
}
