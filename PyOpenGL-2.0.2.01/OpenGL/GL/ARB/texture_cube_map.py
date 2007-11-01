import string
__version__ = string.split('$Revision: 1.10 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_cube_map.txt'
__api_version__ = 0x100

GL_NORMAL_MAP_ARB = 0x8511
GL_REFLECTION_MAP_ARB = 0x8512

GL_TEXTURE_CUBE_MAP_ARB = 0x8513

GL_TEXTURE_BINDING_CUBE_MAP_ARB = 0x8514

GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = 0x851A

GL_PROXY_TEXTURE_CUBE_MAP_ARB = 0x851B

GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB = 0x851C

def glInitTextureCubeMapARB():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_ARB_texture_cube_map")

glInitTexCubeMapARB = glInitTextureCubeMapARB

def __info():
	if glInitTextureCubeMapARB():
		return [('GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB', GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB, 'i')]

