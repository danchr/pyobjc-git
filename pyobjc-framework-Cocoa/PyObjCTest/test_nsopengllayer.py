from PyObjCTools.TestSupport import *

from AppKit import *


class TestNSOpenGLLayer(TestCase):
    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(
            NSOpenGLLayer.canDrawInOpenGLContext_pixelFormat_forLayerTime_displayTime_
        )
        self.assertArgIsIn(
            NSOpenGLLayer.canDrawInOpenGLContext_pixelFormat_forLayerTime_displayTime_,
            3,
        )

        self.assertArgIsIn(
            NSOpenGLLayer.drawInOpenGLContext_pixelFormat_forLayerTime_displayTime_, 3
        )


if __name__ == "__main__":
    main()
