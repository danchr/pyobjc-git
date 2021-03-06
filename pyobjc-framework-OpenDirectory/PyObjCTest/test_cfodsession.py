from PyObjCTools.TestSupport import *
import CFOpenDirectory


class TestCFODSession(TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODSessionGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CFOpenDirectory.ODSessionCreate)
        self.assertArgIsOut(CFOpenDirectory.ODSessionCreate, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODSessionCopyNodeNames)
        self.assertArgIsOut(CFOpenDirectory.ODSessionCopyNodeNames, 2)

    def testConstants(self):
        self.assertIsInstance(
            CFOpenDirectory.kODSessionDefault,
            (CFOpenDirectory.ODSessionRef, type(None)),
        )


if __name__ == "__main__":
    main()
