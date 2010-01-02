import objc
import PyObjCTest.fnd as Foundation
from PyObjCTools.TestSupport import *

class TestBundleVariables (TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testStrings(self):
        d = {}
        objc.loadBundleVariables(self.bundle, d, [
                ('NSAppleScriptErrorMessage', b'@'),
                ('NSBundleDidLoadNotification', b'@'),
            ])

        self.assertIsIn(u'NSBundleDidLoadNotification', d)
        self.assertIsIn(u'NSAppleScriptErrorMessage', d)

        self.assertIsInstance(d[u'NSAppleScriptErrorMessage'], objc.pyobjc_unicode)
        self.assertIsInstance(d[u'NSBundleDidLoadNotification'], objc.pyobjc_unicode)

    def testSimple(self):
        d = {}
        objc.loadBundleVariables(self.bundle, d, [
                ('NSDebugEnabled', objc._C_NSBOOL),
                ('NSFoundationVersionNumber', objc._C_DBL),
            ])

        self.assertIsIn('NSDebugEnabled', d)
        self.assertIsIn('NSFoundationVersionNumber', d)

        self.assertIsInstance(d['NSFoundationVersionNumber'], float)
        self.assertIsInstance(d['NSDebugEnabled'], int)


if __name__ == "__main__":
    main()


