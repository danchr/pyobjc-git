"""
This module can be used to generate wrappers for existing Cocoa frameworks

NOTE:
- The "parser" is very dumb, and I still don't like it. I wonder if turning
  it upside down would help.

TODO
- Finish the implementation
  * Functions
    | Need to specify input/output arguments (no usecase yet)
    | Need to specify that some pointers are not "bad" (e.g. NSZone*)
  * Method definitions
  * Emit a protocols "module" (instead of Scripts/gen_protocols.py)
  * Properly encode C types
  * What can we do about enums are defined using other constants that we
    don't wrap? 
- Test the output on MacOS X
  * ... for the frameworks we support in PyObjC
  * ... for Colloqui SDK
  * ... for QuickSilver SDK
  * ... for ???
- Add documentation that explains how to wrap an existing framework,
  preferably with some examples.
- Use this generator instead of our current CodeGenerator scripts
- What can we do on GNUstep?
"""

__all__=(
    'generateWrappersForFramework',
)


import os
import objc
import re
import sys

HEADER="""\
#              THIS FILE IS GENERATED DO NOT MODIFY
#
# This file was generated by PyObjCTools.WrapperGenerator based on the
# headers in %(frameworkPath)s

import objc as _objc

"""

WITH_IDENTIFIER="""\
if _objc.platform == 'MACOSX':
    _bundle = _objc.loadBundle(
        '%(frameworkName)s',
        globals(),
        bundle_identifier='%(frameworkIdentifier)s',
    )
else:
    _bundle = _objc.loadBundle(
        '%(frameworkName)s',
        globals(),
        bundle_path='%(frameworkPath)s',
    )

"""

WITHOUT_IDENTIFIER="""\
_bundle = _objc.loadBundle(
    '%(frameworkName)s',
    globals(),
    bundle_path='%(frameworkPath)s',
)

"""

FOOTER="""\

# Load global variables
_objc.loadBundleVariables(_bundle, globals(), _VARIABLES)

# Load global functions
_objc.loadBundleFunctions(_bundle, globals(), _FUNCTIONS)

# Clean up after ourselfs
del _objc, _bundle, _VARIABLES, _FUNCTIONS
"""

def generateWrappersForFramework(outfp, frameworkPath, frameworkIdentifier=None, frameworkName=None, globalVariablePrefix=None, functionPrefix=None, ignoreHeaders=(), ignoreFunctions=(), frameworkInclude=None, frameworkLink=None, opaquePointers=()):

    # Try to load the framework, this helps the parser to find classes
    # in method/variable signatures
    objc.runtime.NSBundle.bundleWithPath_(frameworkPath).load()

    p = DumbHeaderParser(
            global_variable_prefix=globalVariablePrefix,
            function_prefix=functionPrefix,
            ignore_functions=ignoreFunctions,
            framework_include=frameworkInclude,
            framework_link=frameworkLink,
            opaque_pointers=opaquePointers,
    )
    for fn in os.listdir(os.path.join(frameworkPath, 'Headers')):
        if not fn.endswith('.h'):
            continue

        if fn in ignoreHeaders:
            continue

        fn = os.path.join(frameworkPath, 'Headers', fn)

        fp = open(fn, 'r')
        p.parse(fp)
        fp.close()

    if frameworkName is None:
        frameworkName = os.path.splitext(os.path.basename(frameworkPath))[0]


    vars = {
        'frameworkPath': frameworkPath,
        'frameworkIdentifier': frameworkIdentifier,
        'frameworkName': frameworkName
    }
    outfp.write(HEADER%vars)
    if frameworkIdentifier is None:
        outfp.write(WITHOUT_IDENTIFIER%vars)
    else:
        outfp.write(WITH_IDENTIFIER%vars)

    outfp.write('# Definitions for global variables\n')
    outfp.write('_VARIABLES=(\n')
    for item in p.global_variables:
        outfp.write('    (%s),\n'%(', '.join(map(repr, item))))
    outfp.write(')\n\n')

    outfp.write('# Definitions for simple global functions\n')
    outfp.write('_FUNCTIONS=(\n')
    for item in p.simple_functions:
        outfp.write('    (%s),\n'%(', '.join(map(repr, item))))
    outfp.write(')\n\n')

    outfp.write("# Special type signatures\n")
    outfp.write('TYPE_SIGNATURES={\n')
    for k,v in p.type_signatures.iteritems():
        if v.endswith('*'): continue
        if v == 'va_list': continue
        outfp.write('    %s: %s,\n'%(repr(k), repr(v)))
    outfp.write('}\n\n')

    outfp.write('# Global constants/enums\n')
    names = p.enums.keys()
    names.sort()

    for nm in names:
        entries = p.enums[nm]

        if nm is None:
            outfp.write("# Values from #define's\n")
        else:
            outfp.write("# Values from enumation %s\n"%(nm,))

        for k, v in entries:
            if isinstance(v, tuple):
                outfp.write('%s=%s+%s\n'%(k, v[0], v[1]))
            else:
                outfp.write('%s=%s\n'%(k, v))

        outfp.write('\n\n')

    outfp.write(FOOTER%vars)


#
# Start of a braindead parser for header-files
#

SIMPLE_TYPES={
    'id':               objc._C_ID,
    'Class':            objc._C_CLASS,
    'SEL':              objc._C_SEL,
    'char':             objc._C_CHR,
    'unsigned char':    objc._C_UCHR,
    'short':            objc._C_SHT,
    'unsigned short':   objc._C_USHT,
    'int':              objc._C_INT,
    'signed int':       objc._C_INT,
    'signed':           objc._C_INT,
    'unsigned int':     objc._C_UINT,
    'unsigned':         objc._C_UINT,
    'long':             objc._C_LNG,
    'unsigned long':    objc._C_ULNG,
    'float':            objc._C_FLT,
    'double':           objc._C_DBL,
    'void':             objc._C_VOID,
    'long long':        objc._C_LNGLNG,
    'unsigned long long': objc._C_ULNGLNG,
    'bool':             objc._C_BOOL,
    'BOOL':             objc._C_NSBOOL,
}

LINE_COMMENT_RE=re.compile('//.*')
BLOCK_1_RE=re.compile('/\*([^*]|(\*[^/]))*\*/')
BLOCK_S_RE=re.compile('/\*')
BLOCK_E_RE=re.compile('\*/')

IDENTIFIER='[A-Za-z_][A-Za-z0-9_]*'
IDENTIFIER_RE=re.compile('(' + IDENTIFIER + ')')
INTERFACE_START_RE=re.compile(
        r'@interface\s+(?P<name>' + IDENTIFIER + ')' +
        r'(\s*\((?P<category>' + IDENTIFIER + ')\))?' +
        r'(\s*:\s*(?P<super>' + IDENTIFIER + r'))?(\s*<(?P<protocols>[^>]*)>)?')

PROTOCOL_START_RE=re.compile(
        r'@protocol\s+(?P<name>' + IDENTIFIER + ')' +
        r'(\s*<(?P<super>' + IDENTIFIER + '))?')

GLOBAL_STRING_RE=re.compile(r'NSString\s*\*\s*(const\s+)?(' + 
    IDENTIFIER + '(\s*,\s*\*\s*' + IDENTIFIER + ')*)(\s+AVAILABLE_\w+)?;')

GLOBAL_VARIABLE_RE=r'%(PFX)s\s+(const\s+)?(' + IDENTIFIER + r')\s+(' + IDENTIFIER + r'\s*(,\s*' + IDENTIFIER + r')*)\s*;'

DEFINE_RE=re.compile('^#\s*define\s+(?P<name>' + IDENTIFIER + ')\s+(?P<value>\d+)$')

SINGLE_LINE_ENUM_RE=re.compile('(?P<typedef>typedef\s+)?enum\s*(?P<enum_name>' + IDENTIFIER +')\s+{(?P<values>[^}]*)}\s*(?P<typedef_name>' + IDENTIFIER + ')')
ENUM_VALUE=re.compile(r'^(?P<name>' + IDENTIFIER + r')\s*(=\s*(?P<value>.*))?$')

START_ENUM_RE=re.compile(r'(?P<typedef>typedef\s+)?enum(\s+(?P<name>' + IDENTIFIER + r'))?\s*{')
START_ENUM_RE2=re.compile(r'(?P<typedef>typedef\s+)?enum(\s+(?P<name>' + IDENTIFIER + r'))?\s*$')

FUNCTION_PROTOTYPE=(
    r'%(PFX)s(.+\s+.+\([^);{]+\)\s*(?:[;{]|$))'
)


CALCULATE_SIGNATURE_SOURCE="""
#import %(framework)s
#include <stdio.h>

int main(void)
{
    printf("%%s\\n", @encode(%(typename)s));
    return 0;
}
"""

def stripcomment(fp):
    """
    Remove C-style comments from the input, yield stripped lines
    """

    in_comment = False

    for ln in fp:
        if in_comment:
            m = BLOCK_E_RE.search(ln)
            if not m:
                continue
            ln = ln[m.end():]
            in_comment = False

        else:
            ln = LINE_COMMENT_RE.sub('', ln)
            ln = BLOCK_1_RE.sub('', ln)

            m = BLOCK_S_RE.search(ln)
            if m:
                in_comment = 1
                ln = ln[:m.start()]

            yield ln.strip()

class DumbHeaderParser (object):
    def __init__(self, global_variable_prefix=None, function_prefix=None, ignore_functions = (), framework_include=None, framework_link=None, opaque_pointers=()):
        self.in_interface = False
        self.in_protocol = False
        self.in_enum = False

        self.ignore_functions = ignore_functions
        self.framework_include = framework_include
        self.framework_link = framework_link
        self.opaque_pointers = opaque_pointers

        self.global_variables = []
        self.protocols = []
        self.interfaces = {}
        self.simple_functions = []
        self.enums = {}
        self.type_signatures = {}

        if global_variable_prefix is not None:
            self.global_variable_re = re.compile(
                GLOBAL_VARIABLE_RE%{'PFX': global_variable_prefix})
        else:
            self.global_variable_re = None

        if function_prefix is None:
            self.function_prefix_re = None
        elif isinstance(function_prefix, str):
            self.function_prefix_re = re.compile(FUNCTION_PROTOTYPE%{'PFX':function_prefix})
        else:
            self.function_prefix_re = re.compile(FUNCTION_PROTOTYPE%{'PFX':'(?:' + '|'.join(function_prefix) +  ')'})

    def parse(self, fp):
        self.in_interface = False
        self.in_prococol = False
        self.in_enum = False

        for ln in stripcomment(fp):
            self.process_line(ln.strip())

    def finish_enum(self, enum_name, enum_values):
        """
        Process the contents of an enum definition
        """
        cur_value = -1
        enum = []
        self.enums[enum_name] = enum

        for v in enum_values:
            v = v.strip()
            if not v:
                continue
            m = ENUM_VALUE.match(v)
            name = m.group('name')
            value = m.group('value')

            if value is None:
                if isinstance(cur_value, int):
                    cur_value = cur_value + 1
                else:
                    cur_value = (cur_value[0], cur_value[1]+1)
                value = cur_value
            else:
                try:
                    value = int(value)
                    cur_value = value
                except ValueError:
                    cur_value = (value, 0)
            enum.append((name, value))


    def process_line(self, ln):
        if self.in_enum:
            if ln.startswith('}'):
                self.in_enum = False
                if self.enum_typedef:
                    m = IDENTIFIER_RE.search(ln)
                    if m:
                        self.enum_name = m.group(1)
                    self.finish_enum(self.enum_name, self.enum_value)
                    self.enum_name = self.enum_value = None

            else:
                if self.need_brace:
                    if not ln.startswith('{'):
                        self.in_enum = False
                    self.need_brace = False
                    return

                if ln.startswith('#'):
                    # Skip preprocessor stuff.
                    return

                self.enum_value.extend(list(ln.split(',')))


        if self.in_interface or self.in_protocol:
            # XXX: Parse method declarations, needed to replace
            # gen_protocols
            if ln.startswith('@end'):
                if self.in_protocol:
                    self.current_protocol['methods'] = self.current_methods
                    self.protocols.append(self.current_protocol)
                elif self.in_interface:
                    v = self.interfaces.setdefault(self.current_interface['name'], {})

                    v['name'] = self.current_interface['name']
                    if self.current_interface['super'] is not None:
                        v['super'] = self.current_interface['super']

                    if self.current_interface['protocols'] is not None:
                        v['protocols'] = self.current_interface['protocols']
            
                    if 'methods' in v:
                        v.setdefault('methods', []).extend(self.current_methods)

                    if self.current_interface['category'] is not None:
                        v.setdefault('categories', []).append(
                                self.current_interface)
                    
                self.current_protocol = None
                self.current_interface = None
                self.current_methods = None
                self.in_interface = False
                self.in_protocol = False
            return

        m = INTERFACE_START_RE.match(ln)
        if m:
            self.in_interface = True
            name = m.group('name')
            category = m.group('category')
            supername = m.group('super')
            protocols = m.group('protocols')
            if protocols is None:
                protocols = ()
            else:
                protocols = [
                    p.strip() for p in protocols.split(',')
                ]

            self.current_interface = {
                'name': name,
                'super': supername,
                'protocols': protocols,
                'category': category,
            }
            self.current_methods = []

            return

        m = PROTOCOL_START_RE.match(ln)
        if m:
            self.in_protocol = True
            name = m.group('name')
            supers = m.group('super')
            if supers is None:
                supers = ()
            else:
                supers = [ p.strip() for p in supers.split(',') ]

            self.current_protocol = {'name':name, 'supers':supers }
            self.current_methods = []
            return

        m = GLOBAL_STRING_RE.search(ln)
        if m:
            identifiers = m.group(2)
            identifiers = [ n.strip() for n in identifiers.split(',')]
            for n in identifiers:
                self.global_variables.append((n, '@'))

            return

        if self.global_variable_re is not None:
            m = self.global_variable_re.match(ln)
            if m:
                tp = m.group(2)
                identifiers = m.group(3)
                identifiers = [ n.strip() for n in identifiers.split(',')]
                for n in identifiers:
                    self.global_variables.append((n, self.encode(tp.strip())))
                return

        m = DEFINE_RE.match(ln)
        if m:
            name = m.group('name')
            value = m.group('value')

            if name == 'nil':
                # Grr, the compiler on GNUstep complains about this one
                return

            l = self.enums.setdefault(None, [])
            l.append((name, int(value)))
            return

        m = SINGLE_LINE_ENUM_RE.search(ln)
        if m:
            values = m.group('values')
            values = values.split(',')

            if m.group('typedef'):
                name = m.group('typedef_name')
            else:
                name = m.group('enum_name')

            self.finish_enum(name, values)

        m = START_ENUM_RE.search(ln)
        if m:
            self.in_enum = True
            self.enum_typedef = m.group('typedef') is not None
            self.enum_name = m.group('name')
            self.enum_value = []
            self.need_brace = False
            return

        m = START_ENUM_RE2.search(ln)
        if m:
            self.in_enum = True
            self.enum_typedef = m.group('typedef') is not None
            self.enum_name = m.group('name')
            self.enum_value = []
            self.need_brace = True
            return

        if self.function_prefix_re is not None:
            m = self.function_prefix_re.match(ln)
            if m:
                prototype = m.group(1).strip()
                if prototype[-1] != ')':
                    prototype = prototype[:-1].strip() + ';'
                rettype, funcname, arguments = self.parse_prototype(prototype)
                if funcname is None:
                    return

                if funcname in self.ignore_functions:
                    return
                signature = self.make_func_signature(rettype, arguments)
                if signature is None:
                    print >>sys.stderr, "WARN: Ignore function:\n%s"%(prototype,)
                    return
                self.simple_functions.append(
                        (funcname, signature, prototype)
                )

    def encode(self, tp):
        # This needs to be fixed, see the gen_protocols script for details
        tp = tp.replace('\t', ' ')
        tp = tp.replace(' *', '*')

        idx = tp.find('<') 
        if idx != -1:
            tp = tp[:idx].strip()

        if tp in SIMPLE_TYPES:
            return SIMPLE_TYPES[tp]

        if tp in self.type_signatures:
            return self.type_signatures[tp]

        if tp.endswith('*'):
            try:
                getattr(objc.runtime, tp[:-1])
                return objc._C_ID
            except AttributeError:
                pass

        # XXX: it might be useful to insert a parser for C-types here

        # Use a little C program to calculate the signature
        src = CALCULATE_SIGNATURE_SOURCE % {
                'framework': self.framework_include,
                'typename': tp,
            }

        prgname = "/tmp/wg.%s"%(os.getpid(),)
        srcname = prgname + ".m"

        fd = open(srcname, 'w')
        fd.write(src)
        fd.close()

        fd = os.popen("cc -o %s %s %s"%(prgname, srcname, self.framework_link))
        lines = fd.read()
        sys.stdout.write(lines)
        xit = fd.close()
        os.unlink(srcname)
        if xit is not None:
            raise ValueError, "1Cannot encode %s"%(tp,)

        fd = os.popen(prgname)
        lines = fd.read()
        xit = fd.close()
        os.unlink(prgname)
        if xit is not None:
            raise ValueError, "2Cannot encode %s"%(tp,)

        typestr = lines.strip()
        self.type_signatures[tp] = typestr
        return typestr

    def isOpaquePointer(self, value):
        return value.replace('const', '').replace(' ', '') in self.opaque_pointers

    def make_func_signature(self, rettype, arguments):
        result = []

        rettype = self.encode(rettype)
        if not rettype:
            return None

        if rettype[0] == objc._C_PTR:
            if not self.isOpaquePointer(rettype):
                return None

        result.append(rettype)

        for a, t in arguments:
            a = self.encode(a)
            if not a:
                return None

            if a[0] == objc._C_PTR:
                if not self.isOpaquePointer(a):
                    return None

            result.append(a)

        return ''.join(result)

    def parse_prototype(self, protostr):
        """
        Parse a C prototype. It is unlikely that this function will correctly 
        parse all valid prototypes.
        """
        protostr = protostr.strip()
        if protostr[-1] != ')':
            protostr = protostr.strip()[:-1].strip()
        idx = protostr.index('(')

        arguments = [ x.strip() for x in protostr[idx+1:-1].split(',') ]
        before = protostr[:idx].strip()
        idx=len(before)-1
        while before[idx].isalnum() or before[idx] == '_':
            idx -= 1

        funcname = before[idx+1:].strip()
        retval = before[:idx+1].strip()

        new_arguments = []
        if len(arguments)  != 1 or arguments[0] != 'void' and arguments[0] != '':
            for a in arguments:
                if a == '...':
                    return None, None, None

                idx = len(a)-1
                while idx > 0 and (a[idx].isalnum() or a[idx] == '_'):
                    idx -= 1
                new_arguments.append((a[:idx+1].strip(), a[idx+1:].strip()))
        arguments = tuple(new_arguments)

        return retval, funcname, arguments

if __name__ == "__main__":
    import sys

    generateWrappersForFramework(sys.stdout,
            '/System/Library/Frameworks/Foundation.framework',
            'com.apple.Foundation',
            globalVariablePrefix='FOUNDATION_EXPORT',
            functionPrefix=['FOUNDATION_STATIC_INLINE', 'FOUNDATION_EXPORT'],
            frameworkInclude="<Foundation/Foundation.h>",
            frameworkLink="-framework Foundation",
            opaquePointers=('NSZone*', 'NSDecimal*'),
    )
