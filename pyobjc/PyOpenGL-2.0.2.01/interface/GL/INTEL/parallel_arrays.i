/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module parallel_arrays

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.INTEL.parallel_arrays Module for PyOpenGL
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

#if !EXT_DEFINES_PROTO || !defined(GL_INTEL_parallel_arrays)
DECLARE_VOID_EXT(glVertexPointervINTEL, (GLint size, GLenum type, const GLvoid* *pointer), (size, type, pointer))
DECLARE_VOID_EXT(glNormalPointervINTEL, (GLenum type, const GLvoid* *pointer), (type, pointer))
DECLARE_VOID_EXT(glColorPointervINTEL, (GLint size, GLenum type, const GLvoid* *pointer), (size, type, pointer))
DECLARE_VOID_EXT(glTexCoordPointervINTEL, (GLint size, GLenum type, const GLvoid* *pointer), (size, type, pointer))
#endif
%}

/* FUNCTION DECLARATIONS */
void glVertexPointervINTEL(GLint size, GLenum type, const GLvoid* *pointer);
DOC(glVertexPointervINTEL, "glVertexPointervINTEL(size, type, pointer)")
void glNormalPointervINTEL(GLenum type, const GLvoid* *pointer);
DOC(glNormalPointervINTEL, "glNormalPointervINTEL(type, pointer)")
void glColorPointervINTEL(GLint size, GLenum type, const GLvoid* *pointer);
DOC(glColorPointervINTEL, "glColorPointervINTEL(size, type, pointer)")
void glTexCoordPointervINTEL(GLint size, GLenum type, const GLvoid* *pointer);
DOC(glTexCoordPointervINTEL, "glTexCoordPointervINTEL(size, type, pointer)")

/* CONSTANT DECLARATIONS */
#define       GL_PARALLEL_ARRAYS_INTEL 0x83F4
#define GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL 0x83F5
#define GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL 0x83F6
#define GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL 0x83F7
#define GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL 0x83F8


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_INTEL_parallel_arrays)
"glVertexPointervINTEL",
"glNormalPointervINTEL",
"glColorPointervINTEL",
"glTexCoordPointervINTEL",
#endif
	NULL
};

#define glInitParallelArraysINTEL() InitExtension("GL_INTEL_parallel_arrays", proc_names)
%}

int glInitParallelArraysINTEL();
DOC(glInitParallelArraysINTEL, "glInitParallelArraysINTEL() -> bool")

%{
PyObject *__info()
{
	if (glInitParallelArraysINTEL())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

