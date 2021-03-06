from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSTextHelper(NSObject):
    def textShouldBeginEditing_(self, t):
        return 1

    def textShouldEndEditing_(self, t):
        return 1


class TestNSText(TestCase):
    def testConstants(self):
        self.assertEqual(NSEnterCharacter, unichr(0x0003))
        self.assertEqual(NSBackspaceCharacter, unichr(0x0008))
        self.assertEqual(NSTabCharacter, unichr(0x0009))
        self.assertEqual(NSNewlineCharacter, unichr(0x000A))
        self.assertEqual(NSFormFeedCharacter, unichr(0x000C))
        self.assertEqual(NSCarriageReturnCharacter, unichr(0x000D))
        self.assertEqual(NSBackTabCharacter, unichr(0x0019))
        self.assertEqual(NSDeleteCharacter, unichr(0x007F))
        self.assertEqual(NSLineSeparatorCharacter, unichr(0x2028))
        self.assertEqual(NSParagraphSeparatorCharacter, unichr(0x2029))

        self.assertEqual(NSLeftTextAlignment, 0)
        self.assertEqual(NSRightTextAlignment, 1)
        self.assertEqual(NSCenterTextAlignment, 2)
        self.assertEqual(NSJustifiedTextAlignment, 3)
        self.assertEqual(NSNaturalTextAlignment, 4)

        self.assertEqual(NSTextAlignmentLeft, 0)
        self.assertEqual(NSTextAlignmentRight, 1)
        self.assertEqual(NSTextAlignmentCenter, 2)
        self.assertEqual(NSTextAlignmentJustified, 3)
        self.assertEqual(NSTextAlignmentNatural, 4)

        self.assertEqual(NSWritingDirectionNatural, -1)
        self.assertEqual(NSWritingDirectionLeftToRight, 0)
        self.assertEqual(NSWritingDirectionRightToLeft, 1)

        self.assertEqual(NSIllegalTextMovement, 0)
        self.assertEqual(NSReturnTextMovement, 0x10)
        self.assertEqual(NSTabTextMovement, 0x11)
        self.assertEqual(NSBacktabTextMovement, 0x12)
        self.assertEqual(NSLeftTextMovement, 0x13)
        self.assertEqual(NSRightTextMovement, 0x14)
        self.assertEqual(NSUpTextMovement, 0x15)
        self.assertEqual(NSDownTextMovement, 0x16)
        self.assertEqual(NSCancelTextMovement, 0x17)
        self.assertEqual(NSOtherTextMovement, 0)

        self.assertIsInstance(NSTextDidBeginEditingNotification, unicode)
        self.assertIsInstance(NSTextDidEndEditingNotification, unicode)
        self.assertIsInstance(NSTextDidChangeNotification, unicode)

        self.assertEqual(NSTextMovementReturn, 0x10)
        self.assertEqual(NSTextMovementTab, 0x11)
        self.assertEqual(NSTextMovementBacktab, 0x12)
        self.assertEqual(NSTextMovementLeft, 0x13)
        self.assertEqual(NSTextMovementRight, 0x14)
        self.assertEqual(NSTextMovementUp, 0x15)
        self.assertEqual(NSTextMovementDown, 0x16)
        self.assertEqual(NSTextMovementCancel, 0x17)
        self.assertEqual(NSTextMovementOther, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(NSTextWritingDirectionEmbedding, 0 << 1)
        self.assertEqual(NSTextWritingDirectionOverride, 1 << 1)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(NSTextMovementUserInfoKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSText.writeRTFDToFile_atomically_)
        self.assertArgIsBOOL(NSText.writeRTFDToFile_atomically_, 1)
        self.assertResultIsBOOL(NSText.readRTFDFromFile_)
        self.assertResultIsBOOL(NSText.isEditable)
        self.assertArgIsBOOL(NSText.setEditable_, 0)
        self.assertResultIsBOOL(NSText.isSelectable)
        self.assertArgIsBOOL(NSText.setSelectable_, 0)
        self.assertResultIsBOOL(NSText.isRichText)
        self.assertArgIsBOOL(NSText.setRichText_, 0)
        self.assertResultIsBOOL(NSText.importsGraphics)
        self.assertArgIsBOOL(NSText.setImportsGraphics_, 0)
        self.assertResultIsBOOL(NSText.isFieldEditor)
        self.assertArgIsBOOL(NSText.setFieldEditor_, 0)
        self.assertResultIsBOOL(NSText.usesFontPanel)
        self.assertArgIsBOOL(NSText.setUsesFontPanel_, 0)
        self.assertResultIsBOOL(NSText.drawsBackground)
        self.assertArgIsBOOL(NSText.setDrawsBackground_, 0)
        self.assertResultIsBOOL(NSText.isRulerVisible)
        self.assertResultIsBOOL(NSText.isHorizontallyResizable)
        self.assertArgIsBOOL(NSText.setHorizontallyResizable_, 0)
        self.assertResultIsBOOL(NSText.isVerticallyResizable)
        self.assertArgIsBOOL(NSText.setVerticallyResizable_, 0)

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        objc.protocolNamed("NSTextDelegate")

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSTextHelper.textShouldBeginEditing_)
        self.assertResultIsBOOL(TestNSTextHelper.textShouldEndEditing_)


if __name__ == "__main__":
    main()
