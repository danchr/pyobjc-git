from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSTabViewHelper(NSObject):
    def tabView_shouldSelectTabViewItem_(self, tv, it):
        return 1


class TestNSTabView(TestCase):
    def testConstants(self):
        self.assertEqual(NSTopTabsBezelBorder, 0)
        self.assertEqual(NSLeftTabsBezelBorder, 1)
        self.assertEqual(NSBottomTabsBezelBorder, 2)
        self.assertEqual(NSRightTabsBezelBorder, 3)
        self.assertEqual(NSNoTabsBezelBorder, 4)
        self.assertEqual(NSNoTabsLineBorder, 5)
        self.assertEqual(NSNoTabsNoBorder, 6)

        self.assertEqual(NSTabPositionNone, 0)
        self.assertEqual(NSTabPositionTop, 1)
        self.assertEqual(NSTabPositionLeft, 2)
        self.assertEqual(NSTabPositionBottom, 3)
        self.assertEqual(NSTabPositionRight, 4)

        self.assertEqual(NSTabViewBorderTypeNone, 0)
        self.assertEqual(NSTabViewBorderTypeLine, 1)
        self.assertEqual(NSTabViewBorderTypeBezel, 2)

    def testMethods(self):
        self.assertResultIsBOOL(NSTabView.allowsTruncatedLabels)
        self.assertResultIsBOOL(NSTabView.drawsBackground)
        self.assertArgIsBOOL(NSTabView.setAllowsTruncatedLabels_, 0)
        self.assertArgIsBOOL(NSTabView.setDrawsBackground_, 0)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSTabViewHelper.tabView_shouldSelectTabViewItem_)


if __name__ == "__main__":
    main()
