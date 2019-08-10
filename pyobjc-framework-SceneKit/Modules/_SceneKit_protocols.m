/*
 * This file is generated by objective.metadata
 *
 * Last update: Tue May 26 22:53:41 2015
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(SCNActionable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNAnimatable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNBoundingVolume));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNNodeRendererDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNPhysicsContactDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNProgramDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNSceneExportDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNSceneRenderer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNSceneRendererDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNShadable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNTechniqueSupport));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1010 */
#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(SCNBufferStream));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1011 */
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(SCNAnimation));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNCameraControllerDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNAvoidOccluderConstraintDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SCNCameraControlConfiguration));
    Py_XDECREF(p);
#endif
}
