"""
Helper module for KeyValue tests
"""
from objc.test.testbndl import PyObjCTest_KVBaseClass, PyObjCTest_KVPathClass

DirectString = u'Direct String'
IndirectString = u'Indirect String'
DirectNumber = 42
IndirectNumber = 84

class KVPyBase:
    def __init__(self):
        self.directString = DirectString
        self._indirectString = IndirectString
        self.directNumber = DirectNumber
        self._indirectNumber = IndirectNumber

    def get_indirectString(self):
        return self._indirectString

    def set_indirectString(self, aString):
        self._indirectString = aString

    def getIndirectNumber(self):
        return self._indirectNumber

    def setIndirectNumber(self, aNumber):
        self._indirectNumber = aNumber

class KVPyPath:
    def __init__(self):
        self.directHead = KVPyBase()
        self._indirectHead = KVPyBase()

    def indirectHead(self):
        return self._indirectHead

    def setIndirectHead(self, aHead):
        self._indirectHead = aHead

class KVPySubObjCBase (PyObjCTest_KVBaseClass):
    pass

class KVPySubObjCPath (PyObjCTest_KVPathClass):
    pass

class KVPySubOverObjCBase (PyObjCTest_KVBaseClass):
    def init(self):
        self = super(KVPySubOverObjCBase, self).init()
        if not self:
            return self

        self.overDirectString = DirectString
        self._overIndirectString = IndirectString
        return self

    def getOverIndirectString(self):
        return self._overIndirectString

    def setOverIndirectString(self, aString):
        self._overIndirectString = aString

class KVPySubOverObjCPath(PyObjCTest_KVPathClass):
    def init(self):
        self = super(KVPySubOverObjCPath, self).init()
        self.overDirectHead = KVPySubOverObjCBase.new()
        self._overIndirectHead = KVPySubOverObjCBase.new()
        return self

    def overIndirectHead(self):
        return self._overIndirectHead

    def setOverIndirectHead(self, aHead):
        self._overIndirectHead = aHead
