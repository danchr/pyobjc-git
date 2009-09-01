from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSFileHandle (TestCase):
    def testConstants(self):
        self.failUnless( isinstance(NSFileHandleOperationException, unicode) )
        self.failUnless( isinstance(NSFileHandleReadCompletionNotification, unicode) )
        self.failUnless( isinstance(NSFileHandleReadToEndOfFileCompletionNotification, unicode) )
        self.failUnless( isinstance(NSFileHandleConnectionAcceptedNotification, unicode) )
        self.failUnless( isinstance(NSFileHandleDataAvailableNotification, unicode) )
        self.failUnless( isinstance(NSFileHandleNotificationDataItem, unicode) )
        self.failUnless( isinstance(NSFileHandleNotificationFileHandleItem, unicode) )
        self.failUnless( isinstance(NSFileHandleNotificationMonitorModes, unicode) )

    def testMethods(self):
        f = NSFileHandle.alloc().initWithFileDescriptor_closeOnDealloc_(0, False)
        self.failUnlessArgIsBOOL(f.initWithFileDescriptor_closeOnDealloc_, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsOut(NSFileHandle.fileHandleForReadingFromURL_error_, 1)
        self.failUnlessArgIsOut(NSFileHandle.fileHandleForWritingToURL_error_, 1)
        self.failUnlessArgIsOut(NSFileHandle.fileHandleForUpdatingURL_error_, 1)


if __name__ == "__main__":
    main()
