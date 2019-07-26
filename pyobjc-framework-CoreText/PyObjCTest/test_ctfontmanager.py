from PyObjCTools.TestSupport import *
from CoreText import *


class TestCTFontManager (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCTFontManagerScopeNone, 0)
        self.assertEqual(kCTFontManagerScopeProcess, 1)
        self.assertEqual(kCTFontManagerScopePersistent, 2)
        self.assertEqual(kCTFontManagerScopeSession, 2)
        self.assertEqual(kCTFontManagerScopeUser, kCTFontManagerScopePersistent)


        self.assertIsInstance(kCTFontManagerBundleIdentifier, unicode)

        self.assertEqual(kCTFontManagerAutoActivationDefault, 0)
        self.assertEqual(kCTFontManagerAutoActivationDisabled, 1)
        self.assertEqual(kCTFontManagerAutoActivationEnabled, 2)
        self.assertEqual(kCTFontManagerAutoActivationPromptUser, 3)

        self.assertIsInstance(kCTFontManagerRegisteredFontsChangedNotification, unicode)


    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertResultIsCFRetained(CTFontManagerCopyAvailablePostScriptNames)
        self.assertResultIsCFRetained(CTFontManagerCopyAvailableFontFamilyNames)
        self.assertResultIsCFRetained(CTFontManagerCopyAvailableFontURLs)
        self.assertResultIsCFRetained(CTFontManagerCreateFontDescriptorsFromURL)

        self.assertArgHasType(CTFontManagerCompareFontFamilyNames, 0, b"^{__CFString=}")
        self.assertArgHasType(CTFontManagerCompareFontFamilyNames, 1, b"^{__CFString=}")
        self.assertArgHasType(CTFontManagerCompareFontFamilyNames, 2, b"^v")
        self.assertArgIsOut(CTFontManagerRegisterFontsForURL, 2)
        self.assertArgIsOut(CTFontManagerUnregisterFontsForURL, 2)
        self.assertArgIsOut(CTFontManagerRegisterFontsForURLs, 2)
        self.assertArgIsOut(CTFontManagerUnregisterFontsForURLs, 2)
        self.assertArgHasType(CTFontManagerEnableFontDescriptors, 1, objc._C_BOOL)
        CTFontManagerGetScopeForURL # Test that function exists
        self.assertResultHasType(CTFontManagerIsSupportedFont, objc._C_BOOL)
        self.assertResultIsCFRetained(CTFontManagerCreateFontRequestRunLoopSource)
        self.assertArgIsBlock(CTFontManagerCreateFontRequestRunLoopSource, 1, b"@@i")

        CTFontManagerGetAutoActivationSetting
        CTFontManagerSetAutoActivationSetting

    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertResultIsCFRetained(CTFontManagerCreateFontDescriptorFromData)


    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(CTFontManagerCreateFontDescriptorFromData)
        self.assertArgIsOut(CTFontManagerRegisterGraphicsFont, 1)
        self.assertArgIsOut(CTFontManagerUnregisterGraphicsFont, 1)

    @min_os_level('10.13')
    def testFunctions10_13(self):
        self.assertResultIsCFRetained(CTFontManagerCreateFontDescriptorsFromData)

    @min_os_level('10.15')
    def testFunctions10_15(self):
        self.assertArgIsBlock(CTFontManagerRegisterFontURLs, 2, objc._C_BOOL + objc._C_ID + objc._C_BOOL)
        self.assertArgIsBlock(CTFontManagerUnregisterFontURLs, 2, objc._C_BOOL + objc._C_ID + objc._C_BOOL)
        self.assertArgIsBlock(CTFontManagerRegisterFontDescriptors, 3, objc._C_BOOL + objc._C_ID + objc._C_BOOL)
        self.assertArgIsBlock(CTFontManagerUnregisterFontDescriptors, 2, objc._C_BOOL + objc._C_ID + objc._C_BOOL)

        self.assertResultIsCFRetained(CTFontManagerCopyRegisteredFontDescriptors)

if __name__ == "__main__":
    main()
