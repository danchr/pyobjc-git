
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCARenderer (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessArgHasType(CARenderer.rendererWithCGLContext_options_, 0, '^{_CGLContextObject=}')
        self.failUnlessArgIsIn(CARenderer.beginFrameAtTime_timeStamp_, 1)


if __name__ == "__main__":
    main()
