from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Photos

    class TestPHContentEditingOutput(TestCase):
        @min_os_level("10.11")
        def testClasses(self):
            self.assertIsInstance(Photos.PHContentEditingOutput, objc.objc_class)


if __name__ == "__main__":
    main()
