
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrintPanel (TestCase):

    def testConstants(self):
        self.failUnlessEqual(NSPrintPanelShowsCopies, 0x01)
        self.failUnlessEqual(NSPrintPanelShowsPageRange, 0x02)
        self.failUnlessEqual(NSPrintPanelShowsPaperSize, 0x04)
        self.failUnlessEqual(NSPrintPanelShowsOrientation, 0x08)
        self.failUnlessEqual(NSPrintPanelShowsScaling, 0x10)
        self.failUnlessEqual(NSPrintPanelShowsPageSetupAccessory, 0x100)
        self.failUnlessEqual(NSPrintPanelShowsPreview, 0x20000)

        self.failUnlessIsInstance(NSPrintPhotoJobStyleHint, unicode)
        self.failUnlessIsInstance(NSPrintPanelAccessorySummaryItemNameKey, unicode)
        self.failUnlessIsInstance(NSPrintPanelAccessorySummaryItemDescriptionKey, unicode)

    def testMethods(self):
        self.fail("- (void)beginSheetWithPrintInfo:(NSPrintInfo *)printInfo modalForWindow:(NSWindow *)docWindow delegate:(id)delegate didEndSelector:(SEL)didEndSelector contextInfo:(void *)contextInfo;")



if __name__ == "__main__":
    main()
