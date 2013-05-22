"""
Helper module that will enable lazy imports of Cocoa wrapper items.

This should improve startup times and memory usage, at the cost
of not being able to use 'from Cocoa import *'
"""
__all__ = ('ObjCLazyModule',)

import sys
import re
import struct

from objc import lookUpClass, getClassList, nosuchclass_error, loadBundle
import objc
ModuleType = type(sys)




def _loadBundle(frameworkName, frameworkIdentifier, frameworkPath):
    if frameworkIdentifier is None:
        bundle = loadBundle(
            frameworkName,
            {},
            bundle_path=frameworkPath,
            scan_classes=False)

    else:
        try:
            bundle = loadBundle(
                frameworkName,
                {},
                bundle_identifier=frameworkIdentifier,
                scan_classes=False)

        except ImportError:
            bundle = loadBundle(
                frameworkName,
                {},
                bundle_path=frameworkPath,
                scan_classes=False)

    return bundle

class GetAttrMap (object):
    __slots__ = ('_container',)
    def __init__(self, container):
        self._container = container

    def __getitem__(self, key):
        try:
            return getattr(self._container, key)
        except AttributeError:
            raise KeyError(key)

class ObjCLazyModule (ModuleType):

    # Define slots for all attributes, that way they don't end up it __dict__.
    __slots__ = (
                '_ObjCLazyModule__bundle', '_ObjCLazyModule__enummap', '_ObjCLazyModule__funcmap',
                '_ObjCLazyModule__parents', '_ObjCLazyModule__varmap', '_ObjCLazyModule__inlinelist',
                '_ObjCLazyModule__aliases',
            )

    def __init__(self, name, frameworkIdentifier, frameworkPath, metadict, inline_list=None, initialdict={}, parents=()):
        super(ObjCLazyModule, self).__init__(name)

        if frameworkIdentifier is not None or frameworkPath is not None:
            self.__bundle = self.__dict__['__bundle__'] = _loadBundle(name, frameworkIdentifier, frameworkPath)

        pfx = name + '.'
        for nm in sys.modules:
            if nm.startswith(pfx):
                rest = nm[len(pfx):]
                if '.' in rest: continue
                if sys.modules[nm] is not None:
                    self.__dict__[rest] = sys.modules[nm]

        self.__dict__.update(initialdict)
        self.__dict__.update(metadict.get('misc', {}))
        self.__parents = parents
        self.__varmap = metadict.get('constants')
        self.__varmap_dct = metadict.get('constants_dict', {})
        self.__enummap = metadict.get('enums')
        self.__funcmap = metadict.get('functions')
        self.__aliases = metadict.get('aliases')
        self.__inlinelist = inline_list

        # informal protocols are not exposed, but added here
        # for completeness sake.
        self.__informal_protocols = metadict.get('protocols')

        self.__expressions = metadict.get('expressions')
        self.__expressions_mapping = GetAttrMap(self)

        self.__load_cftypes(metadict.get('cftypes'))


    def __dir__(self):
        return self.__all__

    def __getattr__(self, name):
        if name == "__all__":
            # Load everything immediately
            value = self.__calc_all()
            self.__dict__[name] = value
            return value

        # First try parent module, as we had done
        # 'from parents import *'
        for p in self.__parents:
            try:
                value = getattr(p, name)
            except AttributeError:
                pass

            else:
                self.__dict__[name] = value
                return value

        # Check if the name is a constant from
        # the metadata files
        try:
            value = self.__get_constant(name)
        except AttributeError:
            pass
        else:
            self.__dict__[name] = value
            return value

        # Then check if the name is class
        try:
            value = lookUpClass(name)
        except nosuchclass_error:
            pass

        else:
            self.__dict__[name] = value
            return value

        # Finally give up and raise AttributeError
        raise AttributeError(name)

    def __calc_all(self):
        all = set()

        # Ensure that all dynamic entries get loaded
        if self.__varmap_dct:
            for nm in list(self.__varmap_dct):
                try:
                    getattr(self, nm)
                except AttributeError:
                    pass

        if self.__varmap:
            for nm in re.findall(r"\$([A-Z0-9a-z_]*)(?:@[^$]*)?(?=\$)", self.__varmap):
                try:
                    getattr(self, nm)
                except AttributeError:
                    pass

        if self.__enummap:
            for nm in re.findall(r"\$([A-Z0-9a-z_]*)@[^$]*(?=\$)", self.__enummap):
                try:
                    getattr(self, nm)
                except AttributeError:
                    pass

        if self.__funcmap:
            for nm in list(self.__funcmap):
                try:
                    getattr(self, nm)
                except AttributeError:
                    pass

        if self.__expressions:
            for nm in list(self.__expressions):
                try:
                    getattr(self, nm)
                except AttributeError:
                    pass

        if self.__aliases:
            for nm in list(self.__aliases):
                try:
                    getattr(self, nm)
                except AttributeError:
                    pass

        # Add all names that are already in our __dict__
        all.update(self.__dict__)

        # Merge __all__of parents ('from parent import *')
        for p in self.__parents:
            all.update(getattr(p, '__all__', ()))

        # Add all class names
        all.update(cls.__name__ for cls in getClassList())


        return [ v for v in all if not v.startswith('_') ]

        return list(all)

    def __get_constant(self, name):
        if self.__varmap_dct:
            if name in self.__varmap_dct:
                tp = self.__varmap_dct.pop(name)
                return objc._loadConstant(name, tp, False)

        if self.__varmap:
            m = re.search(r"\$%s(@[^$]*)?\$"%(name,), self.__varmap)
            if m is not None:
                tp = m.group(1)
                if tp is None:
                    tp = '@'
                else:
                    tp = tp[1:]

                d = {}
                if tp.startswith('='):
                    tp = tp[1:]
                    magic = True
                else:
                    magic = False

                return objc._loadConstant(name, tp, magic)

        if self.__enummap:
            m = re.search(r"\$%s@([^$]*)\$"%(name,), self.__enummap)
            if m is not None:
                val = m.group(1)

                if val.startswith("'"):
                    if isinstance(val, bytes):
                        # Python 2.x
                        val, = struct.unpack('>l', val[1:-1])
                    else:
                        # Python 3.x
                        val, = struct.unpack('>l', val[1:-1].encode('latin1'))

                elif '.' in val:
                    val = float(name, val)

                else:
                    val = int(val)

                return val

        if self.__funcmap:
            if name in self.__funcmap:
                # NOTE: Remove 'name' from funcmap because
                #       it won't be needed anymore (either the
                #       function doesn't exist, or it is loaded)
                #       Should use slightly less memory.
                info = self.__funcmap.pop(name)

                func_list = [ (name,) + info ]

                d = {}
                objc.loadBundleFunctions(self.__bundle, d, func_list)
                if name in d:
                    return d[name]

                if self.__inlinelist is not None:
                    try:
                        objc.loadFunctionList(
                            self.__inlinelist, d, func_list, skip_undefined=False)
                    except objc.error:
                        pass

                    else:
                        if name in d:
                            return d[name]

        if self.__expressions:
            if name in self.__expressions:
                # NOTE: 'name' is popped because it is no longer needed
                #       in the metadata and popping should slightly reduce
                #       memory usage.
                info = self.__expressions.pop(name)
                try:
                    return eval(info, {}, self.__expressions_mapping)
                except NameError:
                    pass

        if self.__aliases:
            if name in self.__aliases:
                alias = self.__aliases.pop(name)
                if alias == 'ULONG_MAX':
                    return (sys.maxsize * 2) + 1
                elif alias == 'LONG_MAX':
                    return sys.maxsize
                elif alias == 'LONG_MIN':
                    return -sys.maxsize-1

                return getattr(self, alias)

        raise AttributeError(name)

    def __load_cftypes(self, cftypes):
        if not cftypes: return

        for name, type, gettypeid_func, tollfree in cftypes:
            if tollfree:
                for nm in tollfree.split(','):
                    try:
                        objc.lookUpClass(nm)
                    except objc.error:
                        pass
                    else:
                        tollfree = nm
                        break
                try:
                    v = objc.registerCFSignature(name, type, None, tollfree)
                    if v is not None:
                        self.__dict__[name] = v
                        continue
                except objc.nosuchclass_error:
                    pass

            try:
                func = getattr(self, gettypeid_func)
            except AttributeError:
                # GetTypeID function not found, this is either
                # a CFType that isn't present on the current
                # platform, or a CFType without a public GetTypeID
                # function. Proxy using the generic CFType
                if tollfree is None:
                    v = objc.registerCFSignature(name, type, None, 'NSCFType')
                    if v is not None:
                        self.__dict__[name] = v
                continue

            v = objc.registerCFSignature(name, type, func())
            if v is not None:
                self.__dict__[name] = v
