/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module framezoom

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.SGIX.framezoom Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_framezoom)
DECLARE_VOID_EXT(glFrameZoomSGIX, (GLint factor), (factor))
#endif
%}

/* FUNCTION DECLARATIONS */
void glFrameZoomSGIX(GLint factor);
DOC(glFrameZoomSGIX, "glFrameZoomSGIX(factor)")

/* CONSTANT DECLARATIONS */
#define              GL_FRAMEZOOM_SGIX 0x818B
#define       GL_FRAMEZOOM_FACTOR_SGIX 0x818C
#define   GL_MAX_FRAMEZOOM_FACTOR_SGIX 0x818D


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_framezoom)
"glFrameZoomSGIX",
#endif
	NULL
};

#define glInitFramezoomSGIX() InitExtension("GL_SGIX_framezoom", proc_names)
%}

int glInitFramezoomSGIX();
DOC(glInitFramezoomSGIX, "glInitFramezoomSGIX() -> bool")

%{
PyObject *__info()
{
	if (glInitFramezoomSGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

