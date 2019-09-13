# This file is generated by objective.metadata
#
# Last update: Fri Sep 13 15:53:05 2019

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a

misc = {
}
misc.update({'sfntInstance': objc.createStructType('sfntInstance', sel32or64(b'{sfntInstance=ss[1l]}', b'{sfntInstance=ss[1i]}'), ['nameID', 'flags', 'coord']), 'sfntFontDescriptor': objc.createStructType('sfntFontDescriptor', sel32or64(b'{sfntFontDescriptor=Ll}', b'{sfntFontDescriptor=Ii}'), ['name', 'value']), 'sfntCMapExtendedSubHeader': objc.createStructType('sfntCMapExtendedSubHeader', sel32or64(b'{sfntCMapExtendedSubHeader=SSLL}', b'{sfntCMapExtendedSubHeader=SSII}'), ['format', 'reserved', 'length', 'language']), 'sfntVariationAxis': objc.createStructType('sfntVariationAxis', sel32or64(b'{sfntVariationAxis=Llllss}', b'{sfntVariationAxis=Iiiiss}'), ['axisTag', 'minValue', 'defaultValue', 'maxValue', 'flags', 'nameID']), 'CTParagraphStyleSetting': objc.createStructType('CTParagraphStyleSetting', sel32or64(b'{CTParagraphStyleSetting=IL^v}', b'{CTParagraphStyleSetting=IQ^v}'), ['spec', 'valueSize', 'value']), 'sfntVariationHeader': objc.createStructType('sfntVariationHeader', sel32or64(b'{sfntVariationHeader=lSSSSSS[1{sfntVariationAxis=Llllss}][1{sfntInstance=ss[1l]}]}', b'{sfntVariationHeader=iSSSSSS[1{sfntVariationAxis=Iiiiss}][1{sfntInstance=ss[1i]}]}'), ['version', 'offsetToData', 'countSizePairs', 'axisCount', 'axisSize', 'instanceCount', 'instanceSize', 'axis', 'instance']), 'sfntDescriptorHeader': objc.createStructType('sfntDescriptorHeader', sel32or64(b'{sfntDescriptorHeader=ll[1{sfntFontDescriptor=Ll}]}', b'{sfntDescriptorHeader=ii[1{sfntFontDescriptor=Ii}]}'), ['version', 'descriptorCount', 'descriptor']), 'sfntDirectory': objc.createStructType('sfntDirectory', sel32or64(b'{sfntDirectory=LSSSS[1{sfntDirectoryEntry=LLLL}]}', b'{sfntDirectory=ISSSS[1{sfntDirectoryEntry=IIII}]}'), ['format', 'numOffsets', 'searchRange', 'entrySelector', 'rangeShift', 'table']), 'sfntFeatureName': objc.createStructType('sfntFeatureName', sel32or64(b'{sfntFeatureName=SSlSs}', b'{sfntFeatureName=SSiSs}'), ['featureType', 'settingCount', 'offsetToSettings', 'featureFlags', 'nameID']), 'sfntDirectoryEntry': objc.createStructType('sfntDirectoryEntry', sel32or64(b'{sfntDirectoryEntry=LLLL}', b'{sfntDirectoryEntry=IIII}'), ['tableTag', 'checkSum', 'offset', 'length']), 'sfntCMapEncoding': objc.createStructType('sfntCMapEncoding', sel32or64(b'{sfntCMapEncoding=SSL}', b'{sfntCMapEncoding=SSI}'), ['platformID', 'scriptID', 'offset']), 'sfntFontFeatureSetting': objc.createStructType('sfntFontFeatureSetting', b'{sfntFontFeatureSetting=Ss}', ['setting', 'nameID']), 'sfntFontRunFeature': objc.createStructType('sfntFontRunFeature', b'{sfntFontRunFeature=SS}', ['featureType', 'setting']), 'sfntCMapSubHeader': objc.createStructType('sfntCMapSubHeader', b'{sfntCMapSubHeader=SSS}', ['format', 'length', 'languageID']), 'sfntNameHeader': objc.createStructType('sfntNameHeader', b'{sfntNameHeader=SSS[1{sfntNameRecord=SSSSSS}]}', ['format', 'count', 'stringOffset', 'rec']), 'sfntCMapHeader': objc.createStructType('sfntCMapHeader', sel32or64(b'{sfntCMapHeader=SS[1{sfntCMapEncoding=SSL}]}', b'{sfntCMapHeader=SS[1{sfntCMapEncoding=SSI}]}'), ['version', 'numTables', 'encoding']), 'FontVariation': objc.createStructType('FontVariation', sel32or64(b'{FontVariation=Ll}', b'{FontVariation=Ii}'), ['name', 'value']), 'sfntFeatureHeader': objc.createStructType('sfntFeatureHeader', sel32or64(b'{sfntFeatureHeader=lSSl[1{sfntFeatureName=SSlSs}][1{sfntFontFeatureSetting=Ss}][1{sfntFontRunFeature=SS}]}', b'{sfntFeatureHeader=iSSi[1{sfntFeatureName=SSiSs}][1{sfntFontFeatureSetting=Ss}][1{sfntFontRunFeature=SS}]}'), ['version', 'featureNameCount', 'featureSetCount', 'reserved', 'names', 'settings', 'runs']), 'sfntNameRecord': objc.createStructType('sfntNameRecord', b'{sfntNameRecord=SSSSSS}', ['platformID', 'scriptID', 'languageID', 'nameID', 'length', 'offset'])})
constants = '''$kCTBackgroundColorAttributeName@^{__CFString=}$kCTBaselineClassAttributeName@^{__CFString=}$kCTBaselineClassHanging@^{__CFString=}$kCTBaselineClassIdeographicCentered@^{__CFString=}$kCTBaselineClassIdeographicHigh@^{__CFString=}$kCTBaselineClassIdeographicLow@^{__CFString=}$kCTBaselineClassMath@^{__CFString=}$kCTBaselineClassRoman@^{__CFString=}$kCTBaselineInfoAttributeName@^{__CFString=}$kCTBaselineOffsetAttributeName@^{__CFString=}$kCTBaselineOriginalFont@^{__CFString=}$kCTBaselineReferenceFont@^{__CFString=}$kCTBaselineReferenceInfoAttributeName@^{__CFString=}$kCTCharacterShapeAttributeName@^{__CFString=}$kCTFontAttributeName@^{__CFString=}$kCTFontBaselineAdjustAttribute@^{__CFString=}$kCTFontCascadeListAttribute@^{__CFString=}$kCTFontCharacterSetAttribute@^{__CFString=}$kCTFontCollectionDisallowAutoActivationOption@^{__CFString=}$kCTFontCollectionIncludeDisabledFontsOption@^{__CFString=}$kCTFontCollectionRemoveDuplicatesOption@^{__CFString=}$kCTFontCopyrightNameKey@^{__CFString=}$kCTFontDescriptionNameKey@^{__CFString=}$kCTFontDescriptorMatchingCurrentAssetSize@^{__CFString=}$kCTFontDescriptorMatchingDescriptors@^{__CFString=}$kCTFontDescriptorMatchingError@^{__CFString=}$kCTFontDescriptorMatchingPercentage@^{__CFString=}$kCTFontDescriptorMatchingResult@^{__CFString=}$kCTFontDescriptorMatchingSourceDescriptor@^{__CFString=}$kCTFontDescriptorMatchingTotalAssetSize@^{__CFString=}$kCTFontDescriptorMatchingTotalDownloadedSize@^{__CFString=}$kCTFontDesignerNameKey@^{__CFString=}$kCTFontDesignerURLNameKey@^{__CFString=}$kCTFontDisplayNameAttribute@^{__CFString=}$kCTFontDownloadableAttribute@^{__CFString=}$kCTFontDownloadedAttribute@^{__CFString=}$kCTFontEnabledAttribute@^{__CFString=}$kCTFontFamilyNameAttribute@^{__CFString=}$kCTFontFamilyNameKey@^{__CFString=}$kCTFontFeatureSampleTextKey@^{__CFString=}$kCTFontFeatureSelectorDefaultKey@^{__CFString=}$kCTFontFeatureSelectorIdentifierKey@^{__CFString=}$kCTFontFeatureSelectorNameKey@^{__CFString=}$kCTFontFeatureSelectorSettingKey@^{__CFString=}$kCTFontFeatureSettingsAttribute@^{__CFString=}$kCTFontFeatureTooltipTextKey@^{__CFString=}$kCTFontFeatureTypeExclusiveKey@^{__CFString=}$kCTFontFeatureTypeIdentifierKey@^{__CFString=}$kCTFontFeatureTypeNameKey@^{__CFString=}$kCTFontFeatureTypeSelectorsKey@^{__CFString=}$kCTFontFeaturesAttribute@^{__CFString=}$kCTFontFixedAdvanceAttribute@^{__CFString=}$kCTFontFormatAttribute@^{__CFString=}$kCTFontFullNameKey@^{__CFString=}$kCTFontLanguagesAttribute@^{__CFString=}$kCTFontLicenseNameKey@^{__CFString=}$kCTFontLicenseURLNameKey@^{__CFString=}$kCTFontMacintoshEncodingsAttribute@^{__CFString=}$kCTFontManagerBundleIdentifier@^{__CFString=}$kCTFontManagerErrorDomain@^{__CFString=}$kCTFontManagerErrorFontAssetNameKey@^{__CFString=}$kCTFontManagerErrorFontDescriptorsKey@^{__CFString=}$kCTFontManagerErrorFontURLsKey@^{__CFString=}$kCTFontManagerRegisteredFontsChangedNotification@^{__CFString=}$kCTFontManufacturerNameKey@^{__CFString=}$kCTFontMatrixAttribute@^{__CFString=}$kCTFontNameAttribute@^{__CFString=}$kCTFontOpenTypeFeatureTag@^{__CFString=}$kCTFontOpenTypeFeatureValue@^{__CFString=}$kCTFontOrientationAttribute@^{__CFString=}$kCTFontPostScriptCIDNameKey@^{__CFString=}$kCTFontPostScriptNameKey@^{__CFString=}$kCTFontPriorityAttribute@^{__CFString=}$kCTFontRegistrationScopeAttribute@^{__CFString=}$kCTFontRegistrationUserInfoAttribute@^{__CFString=}$kCTFontSampleTextNameKey@^{__CFString=}$kCTFontSizeAttribute@^{__CFString=}$kCTFontSlantTrait@^{__CFString=}$kCTFontStyleNameAttribute@^{__CFString=}$kCTFontStyleNameKey@^{__CFString=}$kCTFontSubFamilyNameKey@^{__CFString=}$kCTFontSymbolicTrait@^{__CFString=}$kCTFontTrademarkNameKey@^{__CFString=}$kCTFontTraitsAttribute@^{__CFString=}$kCTFontURLAttribute@^{__CFString=}$kCTFontUniqueNameKey@^{__CFString=}$kCTFontVariationAttribute@^{__CFString=}$kCTFontVariationAxisDefaultValueKey@^{__CFString=}$kCTFontVariationAxisHiddenKey@^{__CFString=}$kCTFontVariationAxisIdentifierKey@^{__CFString=}$kCTFontVariationAxisMaximumValueKey@^{__CFString=}$kCTFontVariationAxisMinimumValueKey@^{__CFString=}$kCTFontVariationAxisNameKey@^{__CFString=}$kCTFontVendorURLNameKey@^{__CFString=}$kCTFontVersionNameKey@^{__CFString=}$kCTFontWeightTrait@^{__CFString=}$kCTFontWidthTrait@^{__CFString=}$kCTForegroundColorAttributeName@^{__CFString=}$kCTForegroundColorFromContextAttributeName@^{__CFString=}$kCTFrameClippingPathsAttributeName@^{__CFString=}$kCTFramePathClippingPathAttributeName@^{__CFString=}$kCTFramePathFillRuleAttributeName@^{__CFString=}$kCTFramePathWidthAttributeName@^{__CFString=}$kCTFrameProgressionAttributeName@^{__CFString=}$kCTGlyphInfoAttributeName@^{__CFString=}$kCTHorizontalInVerticalFormsAttributeName@^{__CFString=}$kCTKernAttributeName@^{__CFString=}$kCTLanguageAttributeName@^{__CFString=}$kCTLigatureAttributeName@^{__CFString=}$kCTParagraphStyleAttributeName@^{__CFString=}$kCTRubyAnnotationAttributeName@^{__CFString=}$kCTRubyAnnotationScaleToFitAttributeName@^{__CFString=}$kCTRubyAnnotationSizeFactorAttributeName@^{__CFString=}$kCTRunDelegateAttributeName@^{__CFString=}$kCTStrokeColorAttributeName@^{__CFString=}$kCTStrokeWidthAttributeName@^{__CFString=}$kCTSuperscriptAttributeName@^{__CFString=}$kCTTabColumnTerminatorsAttributeName@^{__CFString=}$kCTTrackingAttributeName@^{__CFString=}$kCTTypesetterOptionAllowUnboundedLayout@^{__CFString=}$kCTTypesetterOptionDisableBidiProcessing@^{__CFString=}$kCTTypesetterOptionForcedEmbeddingLevel@^{__CFString=}$kCTUnderlineColorAttributeName@^{__CFString=}$kCTUnderlineStyleAttributeName@^{__CFString=}$kCTVerticalFormsAttributeName@^{__CFString=}$kCTWritingDirectionAttributeName@^{__CFString=}$'''
enums = '''$cmapFontTableTag@1668112752$descriptorFontTableTag@1717859171$featureFontTableTag@1717920116$kANKRCurrentVersion@0$kAbbrevSquaredLigaturesOffSelector@15$kAbbrevSquaredLigaturesOnSelector@14$kAllCapsSelector@1$kAllLowerCaseSelector@2$kAllTypeFeaturesOffSelector@1$kAllTypeFeaturesOnSelector@0$kAllTypographicFeaturesType@0$kAltHalfWidthTextSelector@6$kAltProportionalTextSelector@5$kAlternateHorizKanaOffSelector@1$kAlternateHorizKanaOnSelector@0$kAlternateKanaType@34$kAlternateVertKanaOffSelector@3$kAlternateVertKanaOnSelector@2$kAnnotationType@24$kAsteriskToMultiplyOffSelector@3$kAsteriskToMultiplyOnSelector@2$kBSLNControlPointFormatNoMap@2$kBSLNControlPointFormatWithMap@3$kBSLNCurrentVersion@65536$kBSLNDistanceFormatNoMap@0$kBSLNDistanceFormatWithMap@1$kBSLNHangingBaseline@3$kBSLNIdeographicCenterBaseline@1$kBSLNIdeographicHighBaseline@5$kBSLNIdeographicLowBaseline@2$kBSLNLastBaseline@31$kBSLNMathBaseline@4$kBSLNNoBaseline@255$kBSLNNoBaselineOverride@255$kBSLNNumBaselineClasses@32$kBSLNRomanBaseline@0$kBSLNTag@1651731566$kBoxAnnotationSelector@1$kCJKItalicRomanOffSelector@3$kCJKItalicRomanOnSelector@2$kCJKItalicRomanSelector@1$kCJKRomanSpacingType@103$kCJKSymbolAltFiveSelector@5$kCJKSymbolAltFourSelector@4$kCJKSymbolAltOneSelector@1$kCJKSymbolAltThreeSelector@3$kCJKSymbolAltTwoSelector@2$kCJKSymbolAlternativesType@29$kCJKVerticalRomanCenteredSelector@0$kCJKVerticalRomanHBaselineSelector@1$kCJKVerticalRomanPlacementType@31$kCTAdobeCNS1CharacterCollection@1$kCTAdobeGB1CharacterCollection@2$kCTAdobeJapan1CharacterCollection@3$kCTAdobeJapan2CharacterCollection@4$kCTAdobeKorea1CharacterCollection@5$kCTCenterTextAlignment@2$kCTCharacterCollectionAdobeCNS1@1$kCTCharacterCollectionAdobeGB1@2$kCTCharacterCollectionAdobeJapan1@3$kCTCharacterCollectionAdobeJapan2@4$kCTCharacterCollectionAdobeKorea1@5$kCTCharacterCollectionIdentityMapping@0$kCTFontAlertHeaderFontType@18$kCTFontApplicationFontType@9$kCTFontBoldTrait@2$kCTFontClarendonSerifsClass@1073741824$kCTFontClassClarendonSerifs@1073741824$kCTFontClassFreeformSerifs@1879048192$kCTFontClassMaskShift@28$kCTFontClassMaskTrait@4026531840$kCTFontClassModernSerifs@805306368$kCTFontClassOldStyleSerifs@268435456$kCTFontClassOrnamentals@2415919104$kCTFontClassSansSerif@2147483648$kCTFontClassScripts@2684354560$kCTFontClassSlabSerifs@1342177280$kCTFontClassSymbolic@3221225472$kCTFontClassTransitionalSerifs@536870912$kCTFontClassUnknown@0$kCTFontCollectionCopyDefaultOptions@0$kCTFontCollectionCopyStandardSort@2$kCTFontCollectionCopyUnique@1$kCTFontColorGlyphsTrait@8192$kCTFontCompositeTrait@16384$kCTFontCondensedTrait@64$kCTFontControlContentFontType@26$kCTFontDefaultOrientation@0$kCTFontDescriptorMatchingDidBegin@0$kCTFontDescriptorMatchingDidFailWithError@8$kCTFontDescriptorMatchingDidFinish@1$kCTFontDescriptorMatchingDidFinishDownloading@6$kCTFontDescriptorMatchingDidMatch@7$kCTFontDescriptorMatchingDownloading@5$kCTFontDescriptorMatchingStalled@3$kCTFontDescriptorMatchingWillBeginDownloading@4$kCTFontDescriptorMatchingWillBeginQuerying@2$kCTFontEmphasizedSystemDetailFontType@20$kCTFontEmphasizedSystemFontType@3$kCTFontExpandedTrait@32$kCTFontFormatBitmap@5$kCTFontFormatOpenTypePostScript@1$kCTFontFormatOpenTypeTrueType@2$kCTFontFormatPostScript@4$kCTFontFormatTrueType@3$kCTFontFormatUnrecognized@0$kCTFontFreeformSerifsClass@1879048192$kCTFontHorizontalOrientation@1$kCTFontItalicTrait@1$kCTFontLabelFontType@10$kCTFontManagerAutoActivationDefault@0$kCTFontManagerAutoActivationDisabled@1$kCTFontManagerAutoActivationEnabled@2$kCTFontManagerAutoActivationPromptUser@3$kCTFontManagerErrorAlreadyRegistered@105$kCTFontManagerErrorCancelledByUser@304$kCTFontManagerErrorDuplicatedName@305$kCTFontManagerErrorExceededResourceLimit@106$kCTFontManagerErrorFileNotFound@101$kCTFontManagerErrorInUse@202$kCTFontManagerErrorInsufficientInfo@303$kCTFontManagerErrorInsufficientPermissions@102$kCTFontManagerErrorInvalidFilePath@306$kCTFontManagerErrorInvalidFontData@104$kCTFontManagerErrorMissingEntitlement@302$kCTFontManagerErrorNotRegistered@201$kCTFontManagerErrorRegistrationFailed@301$kCTFontManagerErrorSystemRequired@203$kCTFontManagerErrorUnrecognizedFormat@103$kCTFontManagerScopeNone@0$kCTFontManagerScopePersistent@2$kCTFontManagerScopeProcess@1$kCTFontManagerScopeSession@3$kCTFontManagerScopeUser@2$kCTFontMenuItemCmdKeyFontType@14$kCTFontMenuItemFontType@12$kCTFontMenuItemMarkFontType@13$kCTFontMenuTitleFontType@11$kCTFontMessageFontType@23$kCTFontMiniEmphasizedSystemFontType@7$kCTFontMiniSystemFontType@6$kCTFontModernSerifsClass@805306368$kCTFontMonoSpaceTrait@1024$kCTFontNoFontType@4294967295$kCTFontOldStyleSerifsClass@268435456$kCTFontOptionsDefault@0$kCTFontOptionsPreferSystemFont@4$kCTFontOptionsPreventAutoActivation@1$kCTFontOrientationDefault@0$kCTFontOrientationHorizontal@1$kCTFontOrientationVertical@2$kCTFontOrnamentalsClass@2415919104$kCTFontPaletteFontType@24$kCTFontPriorityComputer@30000$kCTFontPriorityDynamic@50000$kCTFontPriorityNetwork@20000$kCTFontPriorityProcess@60000$kCTFontPrioritySystem@10000$kCTFontPriorityUser@40000$kCTFontPushButtonFontType@16$kCTFontSansSerifClass@2147483648$kCTFontScriptsClass@2684354560$kCTFontSlabSerifsClass@1342177280$kCTFontSmallEmphasizedSystemFontType@5$kCTFontSmallSystemFontType@4$kCTFontSmallToolbarFontType@22$kCTFontSymbolicClass@3221225472$kCTFontSystemDetailFontType@19$kCTFontSystemFontType@2$kCTFontTableAcnt@1633906292$kCTFontTableAnkr@1634626418$kCTFontTableAvar@1635148146$kCTFontTableBASE@1111577413$kCTFontTableBdat@1650745716$kCTFontTableBhed@1651008868$kCTFontTableBloc@1651273571$kCTFontTableBsln@1651731566$kCTFontTableCBDT@1128416340$kCTFontTableCBLC@1128418371$kCTFontTableCFF@1128678944$kCTFontTableCFF2@1128678962$kCTFontTableCOLR@1129270354$kCTFontTableCPAL@1129333068$kCTFontTableCidg@1667851367$kCTFontTableCmap@1668112752$kCTFontTableCvar@1668702578$kCTFontTableCvt@1668707360$kCTFontTableDSIG@1146308935$kCTFontTableEBDT@1161970772$kCTFontTableEBLC@1161972803$kCTFontTableEBSC@1161974595$kCTFontTableFdsc@1717859171$kCTFontTableFeat@1717920116$kCTFontTableFmtx@1718449272$kCTFontTableFond@1718578788$kCTFontTableFpgm@1718642541$kCTFontTableFvar@1719034226$kCTFontTableGDEF@1195656518$kCTFontTableGPOS@1196445523$kCTFontTableGSUB@1196643650$kCTFontTableGasp@1734439792$kCTFontTableGlyf@1735162214$kCTFontTableGvar@1735811442$kCTFontTableHVAR@1213612370$kCTFontTableHdmx@1751412088$kCTFontTableHead@1751474532$kCTFontTableHhea@1751672161$kCTFontTableHmtx@1752003704$kCTFontTableHsty@1752396921$kCTFontTableJSTF@1246975046$kCTFontTableJust@1786082164$kCTFontTableKern@1801810542$kCTFontTableKerx@1801810552$kCTFontTableLTSH@1280594760$kCTFontTableLcar@1818452338$kCTFontTableLoca@1819239265$kCTFontTableLtag@1819566439$kCTFontTableMATH@1296127048$kCTFontTableMERG@1296388679$kCTFontTableMVAR@1297498450$kCTFontTableMaxp@1835104368$kCTFontTableMeta@1835365473$kCTFontTableMort@1836020340$kCTFontTableMorx@1836020344$kCTFontTableName@1851878757$kCTFontTableOS2@1330851634$kCTFontTableOpbd@1869636196$kCTFontTableOptionExcludeSynthetic@1$kCTFontTableOptionNoOptions@0$kCTFontTablePCLT@1346587732$kCTFontTablePost@1886352244$kCTFontTablePrep@1886545264$kCTFontTableProp@1886547824$kCTFontTableSTAT@1398030676$kCTFontTableSVG@1398163232$kCTFontTableSbit@1935829364$kCTFontTableSbix@1935829368$kCTFontTableTrak@1953653099$kCTFontTableVDMX@1447316824$kCTFontTableVORG@1448038983$kCTFontTableVVAR@1448493394$kCTFontTableVhea@1986553185$kCTFontTableVmtx@1986884728$kCTFontTableXref@2020762982$kCTFontTableZapf@1516335206$kCTFontToolTipFontType@25$kCTFontToolbarFontType@21$kCTFontTraitBold@2$kCTFontTraitClassMask@4026531840$kCTFontTraitColorGlyphs@8192$kCTFontTraitComposite@16384$kCTFontTraitCondensed@64$kCTFontTraitExpanded@32$kCTFontTraitItalic@1$kCTFontTraitMonoSpace@1024$kCTFontTraitUIOptimized@4096$kCTFontTraitVertical@2048$kCTFontTransitionalSerifsClass@536870912$kCTFontUIFontAlertHeader@18$kCTFontUIFontApplication@9$kCTFontUIFontControlContent@26$kCTFontUIFontEmphasizedSystem@3$kCTFontUIFontEmphasizedSystemDetail@20$kCTFontUIFontLabel@10$kCTFontUIFontMenuItem@12$kCTFontUIFontMenuItemCmdKey@14$kCTFontUIFontMenuItemMark@13$kCTFontUIFontMenuTitle@11$kCTFontUIFontMessage@23$kCTFontUIFontMiniEmphasizedSystem@7$kCTFontUIFontMiniSystem@6$kCTFontUIFontNone@4294967295$kCTFontUIFontPalette@24$kCTFontUIFontPushButton@16$kCTFontUIFontSmallEmphasizedSystem@5$kCTFontUIFontSmallSystem@4$kCTFontUIFontSmallToolbar@22$kCTFontUIFontSystem@2$kCTFontUIFontSystemDetail@19$kCTFontUIFontToolTip@25$kCTFontUIFontToolbar@21$kCTFontUIFontUser@0$kCTFontUIFontUserFixedPitch@1$kCTFontUIFontUtilityWindowTitle@17$kCTFontUIFontViews@8$kCTFontUIFontWindowTitle@15$kCTFontUIOptimizedTrait@4096$kCTFontUnknownClass@0$kCTFontUserFixedPitchFontType@1$kCTFontUserFontType@0$kCTFontUtilityWindowTitleFontType@17$kCTFontVerticalOrientation@2$kCTFontVerticalTrait@2048$kCTFontViewsFontType@8$kCTFontWindowTitleFontType@15$kCTFramePathFillEvenOdd@0$kCTFramePathFillWindingNumber@1$kCTFrameProgressionLeftToRight@2$kCTFrameProgressionRightToLeft@1$kCTFrameProgressionTopToBottom@0$kCTIdentityMappingCharacterCollection@0$kCTJustifiedTextAlignment@3$kCTLeftTextAlignment@0$kCTLineBoundsExcludeTypographicLeading@1$kCTLineBoundsExcludeTypographicShifts@2$kCTLineBoundsIncludeLanguageExtents@32$kCTLineBoundsUseGlyphPathBounds@8$kCTLineBoundsUseHangingPunctuation@4$kCTLineBoundsUseOpticalBounds@16$kCTLineBreakByCharWrapping@1$kCTLineBreakByClipping@2$kCTLineBreakByTruncatingHead@3$kCTLineBreakByTruncatingMiddle@5$kCTLineBreakByTruncatingTail@4$kCTLineBreakByWordWrapping@0$kCTLineTruncationEnd@1$kCTLineTruncationMiddle@2$kCTLineTruncationStart@0$kCTNaturalTextAlignment@4$kCTParagraphStyleSpecifierAlignment@0$kCTParagraphStyleSpecifierBaseWritingDirection@13$kCTParagraphStyleSpecifierCount@18$kCTParagraphStyleSpecifierDefaultTabInterval@5$kCTParagraphStyleSpecifierFirstLineHeadIndent@1$kCTParagraphStyleSpecifierHeadIndent@2$kCTParagraphStyleSpecifierLineBoundsOptions@17$kCTParagraphStyleSpecifierLineBreakMode@6$kCTParagraphStyleSpecifierLineHeightMultiple@7$kCTParagraphStyleSpecifierLineSpacing@10$kCTParagraphStyleSpecifierLineSpacingAdjustment@16$kCTParagraphStyleSpecifierMaximumLineHeight@8$kCTParagraphStyleSpecifierMaximumLineSpacing@14$kCTParagraphStyleSpecifierMinimumLineHeight@9$kCTParagraphStyleSpecifierMinimumLineSpacing@15$kCTParagraphStyleSpecifierParagraphSpacing@11$kCTParagraphStyleSpecifierParagraphSpacingBefore@12$kCTParagraphStyleSpecifierTabStops@4$kCTParagraphStyleSpecifierTailIndent@3$kCTRightTextAlignment@1$kCTRubyAlignmentAuto@0$kCTRubyAlignmentCenter@2$kCTRubyAlignmentDistributeLetter@4$kCTRubyAlignmentDistributeSpace@5$kCTRubyAlignmentEnd@3$kCTRubyAlignmentInvalid@255$kCTRubyAlignmentLineEdge@6$kCTRubyAlignmentStart@1$kCTRubyOverhangAuto@0$kCTRubyOverhangEnd@2$kCTRubyOverhangInvalid@255$kCTRubyOverhangNone@3$kCTRubyOverhangStart@1$kCTRubyPositionAfter@1$kCTRubyPositionBefore@0$kCTRubyPositionCount@4$kCTRubyPositionInline@3$kCTRubyPositionInterCharacter@2$kCTRunDelegateCurrentVersion@1$kCTRunDelegateVersion1@1$kCTRunStatusHasNonIdentityMatrix@4$kCTRunStatusNoStatus@0$kCTRunStatusNonMonotonic@2$kCTRunStatusRightToLeft@1$kCTTextAlignmentCenter@2$kCTTextAlignmentJustified@3$kCTTextAlignmentLeft@0$kCTTextAlignmentNatural@4$kCTTextAlignmentRight@1$kCTUnderlinePatternDash@512$kCTUnderlinePatternDashDot@768$kCTUnderlinePatternDashDotDot@1024$kCTUnderlinePatternDot@256$kCTUnderlinePatternSolid@0$kCTUnderlineStyleDouble@9$kCTUnderlineStyleNone@0$kCTUnderlineStyleSingle@1$kCTUnderlineStyleThick@2$kCTVersionNumber10_10@458752$kCTVersionNumber10_11@524288$kCTVersionNumber10_12@589824$kCTVersionNumber10_13@655360$kCTVersionNumber10_14@720896$kCTVersionNumber10_15@786432$kCTVersionNumber10_5@131072$kCTVersionNumber10_5_2@131073$kCTVersionNumber10_5_3@131074$kCTVersionNumber10_5_5@131075$kCTVersionNumber10_6@196608$kCTVersionNumber10_6_7@196615$kCTVersionNumber10_7@262144$kCTVersionNumber10_8@327680$kCTVersionNumber10_9@393216$kCTWritingDirectionEmbedding@0$kCTWritingDirectionLeftToRight@0$kCTWritingDirectionNatural@-1$kCTWritingDirectionOverride@2$kCTWritingDirectionRightToLeft@1$kCanonicalCompositionOffSelector@1$kCanonicalCompositionOnSelector@0$kCaseSensitiveLayoutOffSelector@1$kCaseSensitiveLayoutOnSelector@0$kCaseSensitiveLayoutType@33$kCaseSensitiveSpacingOffSelector@3$kCaseSensitiveSpacingOnSelector@2$kCharacterAlternativesType@17$kCharacterShapeType@20$kCircleAnnotationSelector@3$kCommonLigaturesOffSelector@3$kCommonLigaturesOnSelector@2$kCompatibilityCompositionOffSelector@3$kCompatibilityCompositionOnSelector@2$kContextualAlternatesOffSelector@1$kContextualAlternatesOnSelector@0$kContextualAlternatesType@36$kContextualLigaturesOffSelector@19$kContextualLigaturesOnSelector@18$kContextualSwashAlternatesOffSelector@5$kContextualSwashAlternatesOnSelector@4$kCursiveConnectionType@2$kCursiveSelector@2$kDecomposeDiacriticsSelector@2$kDecorativeBordersSelector@4$kDefaultCJKRomanSelector@2$kDefaultLowerCaseSelector@0$kDefaultUpperCaseSelector@0$kDesignComplexityType@18$kDesignLevel1Selector@0$kDesignLevel2Selector@1$kDesignLevel3Selector@2$kDesignLevel4Selector@3$kDesignLevel5Selector@4$kDiacriticsType@9$kDiagonalFractionsSelector@2$kDiamondAnnotationSelector@8$kDingbatsSelector@1$kDiphthongLigaturesOffSelector@11$kDiphthongLigaturesOnSelector@10$kDisplayTextSelector@1$kEngravedTextSelector@2$kExpertCharactersSelector@10$kExponentsOffSelector@9$kExponentsOnSelector@8$kFleuronsSelector@3$kFontAlbanianLanguage@36$kFontAmharicLanguage@85$kFontAmharicScript@28$kFontArabicLanguage@12$kFontArabicScript@4$kFontArmenianLanguage@51$kFontArmenianScript@24$kFontAssameseLanguage@68$kFontAymaraLanguage@134$kFontAzerbaijanArLanguage@50$kFontAzerbaijaniLanguage@49$kFontBasqueLanguage@129$kFontBengaliLanguage@67$kFontBengaliScript@13$kFontBulgarianLanguage@44$kFontBurmeseLanguage@77$kFontBurmeseScript@19$kFontByelorussianLanguage@46$kFontCatalanLanguage@130$kFontChewaLanguage@92$kFontChineseScript@2$kFontCopyrightName@0$kFontCroatianLanguage@18$kFontCustom16BitScript@2$kFontCustom816BitScript@1$kFontCustom8BitScript@0$kFontCustomPlatform@4$kFontCyrillicScript@7$kFontCzechLanguage@38$kFontDanishLanguage@7$kFontDescriptionName@10$kFontDesignerName@9$kFontDesignerURLName@12$kFontDevanagariScript@9$kFontDutchLanguage@4$kFontDzongkhaLanguage@137$kFontEastEuropeanRomanScript@29$kFontEnglishLanguage@0$kFontEsperantoLanguage@94$kFontEstonianLanguage@27$kFontEthiopicScript@28$kFontExtendedArabicScript@31$kFontFaeroeseLanguage@30$kFontFamilyName@1$kFontFarsiLanguage@31$kFontFinnishLanguage@13$kFontFlemishLanguage@34$kFontFrenchLanguage@1$kFontFullName@4$kFontGallaLanguage@87$kFontGeezScript@28$kFontGeorgianLanguage@52$kFontGeorgianScript@23$kFontGermanLanguage@2$kFontGreekLanguage@14$kFontGreekScript@6$kFontGuaraniLanguage@133$kFontGujaratiLanguage@69$kFontGujaratiScript@11$kFontGurmukhiScript@10$kFontHebrewLanguage@10$kFontHebrewScript@5$kFontHindiLanguage@21$kFontHungarianLanguage@26$kFontISO10646_1993Semantics@2$kFontIcelandicLanguage@15$kFontIndonesianLanguage@81$kFontIrishLanguage@35$kFontItalianLanguage@3$kFontJapaneseLanguage@11$kFontJapaneseScript@1$kFontJavaneseRomLanguage@138$kFontKannadaLanguage@73$kFontKannadaScript@16$kFontKashmiriLanguage@61$kFontKazakhLanguage@48$kFontKhmerLanguage@78$kFontKhmerScript@20$kFontKirghizLanguage@54$kFontKoreanLanguage@23$kFontKoreanScript@3$kFontKurdishLanguage@60$kFontLaoLanguage@79$kFontLaotianScript@22$kFontLappishLanguage@29$kFontLastReservedName@255$kFontLatinLanguage@131$kFontLatvianLanguage@28$kFontLettishLanguage@28$kFontLicenseDescriptionName@13$kFontLicenseInfoURLName@14$kFontLithuanianLanguage@24$kFontMacCompatibleFullName@18$kFontMacedonianLanguage@43$kFontMacintoshPlatform@1$kFontMalagasyLanguage@93$kFontMalayArabicLanguage@84$kFontMalayRomanLanguage@83$kFontMalayalamLanguage@72$kFontMalayalamScript@17$kFontMalteseLanguage@16$kFontManufacturerName@8$kFontMarathiLanguage@66$kFontMicrosoftPlatform@3$kFontMicrosoftStandardScript@1$kFontMicrosoftSymbolScript@0$kFontMicrosoftUCS4Script@10$kFontMoldavianLanguage@53$kFontMongolianCyrLanguage@58$kFontMongolianLanguage@57$kFontMongolianScript@27$kFontNepaliLanguage@64$kFontNoLanguageCode@4294967295$kFontNoNameCode@4294967295$kFontNoPlatformCode@4294967295$kFontNoScriptCode@4294967295$kFontNorwegianLanguage@9$kFontOriyaLanguage@71$kFontOriyaScript@12$kFontOromoLanguage@87$kFontPashtoLanguage@59$kFontPersianLanguage@31$kFontPolishLanguage@25$kFontPortugueseLanguage@8$kFontPostScriptCIDName@20$kFontPostscriptName@6$kFontPreferredFamilyName@16$kFontPreferredSubfamilyName@17$kFontPunjabiLanguage@70$kFontQuechuaLanguage@132$kFontRSymbolScript@8$kFontReservedPlatform@2$kFontRomanScript@0$kFontRomanianLanguage@37$kFontRuandaLanguage@90$kFontRundiLanguage@91$kFontRussian@7$kFontRussianLanguage@32$kFontSaamiskLanguage@29$kFontSampleTextName@19$kFontSanskritLanguage@65$kFontSerbianLanguage@42$kFontSimpChineseLanguage@33$kFontSimpleChineseScript@25$kFontSindhiLanguage@62$kFontSindhiScript@31$kFontSinhaleseLanguage@76$kFontSinhaleseScript@18$kFontSlavicScript@29$kFontSlovakLanguage@39$kFontSlovenianLanguage@40$kFontSomaliLanguage@88$kFontSpanishLanguage@6$kFontStyleName@2$kFontSundaneseRomLanguage@139$kFontSwahiliLanguage@89$kFontSwedishLanguage@5$kFontTagalogLanguage@82$kFontTajikiLanguage@55$kFontTamilLanguage@74$kFontTamilScript@14$kFontTatarLanguage@135$kFontTeluguLanguage@75$kFontTeluguScript@15$kFontThaiLanguage@22$kFontThaiScript@21$kFontTibetanLanguage@63$kFontTibetanScript@26$kFontTigrinyaLanguage@86$kFontTradChineseLanguage@19$kFontTrademarkName@7$kFontTraditionalChineseScript@2$kFontTurkishLanguage@17$kFontTurkmenLanguage@56$kFontUighurLanguage@136$kFontUkrainianLanguage@45$kFontUnicodeDefaultSemantics@0$kFontUnicodePlatform@0$kFontUnicodeV1_1Semantics@1$kFontUnicodeV2_0BMPOnlySemantics@3$kFontUnicodeV2_0FullCoverageSemantics@4$kFontUnicodeV4_0VariationSequenceSemantics@5$kFontUnicode_FullRepertoire@6$kFontUninterpretedScript@32$kFontUniqueName@3$kFontUrduLanguage@20$kFontUzbekLanguage@47$kFontVendorURLName@11$kFontVersionName@5$kFontVietnameseLanguage@80$kFontVietnameseScript@30$kFontWelshLanguage@128$kFontYiddishLanguage@41$kFormInterrobangOffSelector@7$kFormInterrobangOnSelector@6$kFractionsType@11$kFullWidthCJKRomanSelector@3$kFullWidthIdeographsSelector@0$kFullWidthKanaSelector@0$kHalfWidthCJKRomanSelector@0$kHalfWidthIdeographsSelector@2$kHalfWidthTextSelector@2$kHanjaToHangulAltOneSelector@7$kHanjaToHangulAltThreeSelector@9$kHanjaToHangulAltTwoSelector@8$kHanjaToHangulSelector@1$kHideDiacriticsSelector@1$kHiraganaToKatakanaSelector@2$kHistoricalLigaturesOffSelector@21$kHistoricalLigaturesOnSelector@20$kHojoCharactersSelector@12$kHyphenToEnDashOffSelector@3$kHyphenToEnDashOnSelector@2$kHyphenToMinusOffSelector@1$kHyphenToMinusOnSelector@0$kHyphensToEmDashOffSelector@1$kHyphensToEmDashOnSelector@0$kIdeographicAltFiveSelector@5$kIdeographicAltFourSelector@4$kIdeographicAltOneSelector@1$kIdeographicAltThreeSelector@3$kIdeographicAltTwoSelector@2$kIdeographicAlternativesType@30$kIdeographicSpacingType@26$kIlluminatedCapsSelector@3$kInequalityLigaturesOffSelector@7$kInequalityLigaturesOnSelector@6$kInferiorsSelector@2$kInitialCapsAndSmallCapsSelector@5$kInitialCapsSelector@4$kInternationalSymbolsSelector@5$kInvertedBoxAnnotationSelector@9$kInvertedCircleAnnotationSelector@4$kInvertedRoundedBoxAnnotationSelector@10$kItalicCJKRomanType@32$kJIS1978CharactersSelector@2$kJIS1983CharactersSelector@3$kJIS1990CharactersSelector@4$kJIS2004CharactersSelector@11$kJUSTCurrentVersion@65536$kJUSTKashidaPriority@0$kJUSTLetterPriority@2$kJUSTNullPriority@3$kJUSTOverrideLimits@16384$kJUSTOverridePriority@32768$kJUSTOverrideUnlimited@8192$kJUSTPriorityCount@4$kJUSTPriorityMask@3$kJUSTSpacePriority@1$kJUSTStandardFormat@0$kJUSTTag@1786082164$kJUSTUnlimited@4096$kJUSTnoGlyphcode@65535$kJUSTpcConditionalAddAction@2$kJUSTpcDecompositionAction@0$kJUSTpcDuctilityAction@4$kJUSTpcGlyphRepeatAddAction@5$kJUSTpcGlyphStretchAction@3$kJUSTpcUnconditionalAddAction@1$kKERNCrossStream@16384$kKERNCrossStreamResetNote@2$kKERNCurrentVersion@65536$kKERNFormatMask@255$kKERNIndexArray@3$kKERNLineEndKerning@2$kKERNLineStart@1$kKERNNoCrossKerning@4$kKERNNoStakeNote@1$kKERNNotApplied@1$kKERNNotesRequested@8$kKERNOrderedList@0$kKERNResetCrossStream@32768$kKERNSimpleArray@2$kKERNStateTable@1$kKERNTag@1801810542$kKERNUnusedBits@7936$kKERNVariation@8192$kKERNVertical@32768$kKERXActionOffsetMask@16777215$kKERXActionTypeAnchorPoints@1073741824$kKERXActionTypeControlPoints@0$kKERXActionTypeCoordinates@2147483648$kKERXActionTypeMask@3221225472$kKERXControlPoint@4$kKERXCrossStream@1073741824$kKERXCrossStreamResetNote@2$kKERXCurrentVersion@131072$kKERXDescending@268435456$kKERXFormatMask@255$kKERXLineEndKerning@2$kKERXLineStart@1$kKERXNoCrossKerning@4$kKERXNoStakeNote@1$kKERXNotApplied@1$kKERXNotesRequested@8$kKERXOrderedList@0$kKERXResetCrossStream@32768$kKERXSimpleArray@2$kKERXStateTable@1$kKERXTag@1801810552$kKERXUnusedBits@268435200$kKERXUnusedFlags@1056964608$kKERXValuesAreLong@1$kKERXVariation@536870912$kKERXVertical@-2147483648$kKanaSpacingType@25$kKanaToRomanizationSelector@4$kKatakanaToHiraganaSelector@3$kLCARCtlPointFormat@1$kLCARCurrentVersion@65536$kLCARLinearFormat@0$kLCARTag@1818452338$kLTAGCurrentVersion@1$kLanguageTagType@39$kLastFeatureType@-1$kLetterCaseType@3$kLigaturesType@1$kLineFinalSwashesOffSelector@7$kLineFinalSwashesOnSelector@6$kLineInitialSwashesOffSelector@5$kLineInitialSwashesOnSelector@4$kLinguisticRearrangementOffSelector@1$kLinguisticRearrangementOnSelector@0$kLinguisticRearrangementType@5$kLogosOffSelector@7$kLogosOnSelector@6$kLowerCaseNumbersSelector@0$kLowerCasePetiteCapsSelector@2$kLowerCaseSmallCapsSelector@1$kLowerCaseType@37$kMORTContextualType@1$kMORTCoverDescending@16384$kMORTCoverIgnoreVertical@8192$kMORTCoverTypeMask@15$kMORTCoverVertical@32768$kMORTCurrInsertBefore@2048$kMORTCurrInsertCountMask@992$kMORTCurrInsertCountShift@5$kMORTCurrInsertKashidaLike@8192$kMORTCurrJustTableCountMask@127$kMORTCurrJustTableCountShift@0$kMORTCurrentVersion@65536$kMORTDoInsertionsBefore@128$kMORTInsertionType@5$kMORTInsertionsCountMask@63$kMORTIsSplitVowelPiece@64$kMORTLigFormOffsetMask@1073741823$kMORTLigFormOffsetShift@2$kMORTLigLastAction@-2147483648$kMORTLigStoreLigature@1073741824$kMORTLigatureType@2$kMORTMarkInsertBefore@1024$kMORTMarkInsertCountMask@31$kMORTMarkInsertCountShift@0$kMORTMarkInsertKashidaLike@4096$kMORTMarkJustTableCountMask@16256$kMORTMarkJustTableCountShift@7$kMORTRearrangementType@0$kMORTSwashType@4$kMORTTag@1836020340$kMORTraCDx@6$kMORTraCDxA@8$kMORTraCDxAB@12$kMORTraCDxBA@13$kMORTraDCx@7$kMORTraDCxA@9$kMORTraDCxAB@14$kMORTraDCxBA@15$kMORTraDx@2$kMORTraDxA@3$kMORTraDxAB@10$kMORTraDxBA@11$kMORTraNoAction@0$kMORTraxA@1$kMORTraxAB@4$kMORTraxBA@5$kMORXCoverDescending@1073741824$kMORXCoverIgnoreVertical@536870912$kMORXCoverLogicalOrder@268435456$kMORXCoverTypeMask@255$kMORXCoverVertical@-2147483648$kMORXCurrentVersion@131072$kMORXTag@1836020344$kMathSymbolsSelector@6$kMathematicalExtrasType@15$kMathematicalGreekOffSelector@11$kMathematicalGreekOnSelector@10$kMonospacedNumbersSelector@0$kMonospacedTextSelector@1$kNLCCharactersSelector@13$kNoAlternatesSelector@0$kNoAnnotationSelector@0$kNoCJKItalicRomanSelector@0$kNoCJKSymbolAlternativesSelector@0$kNoFractionsSelector@0$kNoIdeographicAlternativesSelector@0$kNoOrnamentsSelector@0$kNoRubyKanaSelector@0$kNoStyleOptionsSelector@0$kNoStylisticAlternatesSelector@0$kNoTransliterationSelector@0$kNonFinalSwashesOffSelector@9$kNonFinalSwashesOnSelector@8$kNormalPositionSelector@0$kNumberCaseType@21$kNumberSpacingType@6$kOPBDControlPointFormat@1$kOPBDCurrentVersion@65536$kOPBDDistanceFormat@0$kOPBDTag@1869636196$kOrdinalsSelector@3$kOrnamentSetsType@16$kOverlappingCharactersType@13$kPROPALDirectionClass@2$kPROPANDirectionClass@6$kPROPBNDirectionClass@19$kPROPCSDirectionClass@7$kPROPCanHangLTMask@16384$kPROPCanHangRBMask@8192$kPROPCurrentVersion@196608$kPROPDirectionMask@31$kPROPENDirectionClass@3$kPROPESDirectionClass@4$kPROPETDirectionClass@5$kPROPIsFloaterMask@32768$kPROPLDirectionClass@0$kPROPLREDirectionClass@13$kPROPLRODirectionClass@14$kPROPNSMDirectionClass@18$kPROPNumDirectionClasses@20$kPROPONDirectionClass@11$kPROPPDFDirectionClass@17$kPROPPSDirectionClass@8$kPROPPairOffsetMask@3840$kPROPPairOffsetShift@8$kPROPPairOffsetSign@7$kPROPRDirectionClass@1$kPROPRLEDirectionClass@15$kPROPRLODirectionClass@16$kPROPRightConnectMask@128$kPROPSDirectionClass@9$kPROPSENDirectionClass@12$kPROPTag@1886547824$kPROPUseRLPairMask@4096$kPROPWSDirectionClass@10$kPROPZeroReserved@96$kParenthesisAnnotationSelector@5$kPartiallyConnectedSelector@1$kPeriodAnnotationSelector@6$kPeriodsToEllipsisOffSelector@11$kPeriodsToEllipsisOnSelector@10$kPiCharactersSelector@2$kPreventOverlapOffSelector@1$kPreventOverlapOnSelector@0$kProportionalCJKRomanSelector@1$kProportionalIdeographsSelector@1$kProportionalKanaSelector@1$kProportionalNumbersSelector@1$kProportionalTextSelector@0$kQuarterWidthNumbersSelector@3$kQuarterWidthTextSelector@4$kRareLigaturesOffSelector@5$kRareLigaturesOnSelector@4$kRebusPicturesOffSelector@9$kRebusPicturesOnSelector@8$kRequiredLigaturesOffSelector@1$kRequiredLigaturesOnSelector@0$kRomanNumeralAnnotationSelector@7$kRomanizationToHiraganaSelector@5$kRomanizationToKatakanaSelector@6$kRoundedBoxAnnotationSelector@2$kRubyKanaOffSelector@3$kRubyKanaOnSelector@2$kRubyKanaSelector@1$kRubyKanaType@28$kSFNTLookupSegmentArray@4$kSFNTLookupSegmentSingle@2$kSFNTLookupSimpleArray@0$kSFNTLookupSingleTable@6$kSFNTLookupTrimmedArray@8$kSFNTLookupVector@10$kSTClassDeletedGlyph@2$kSTClassEndOfLine@3$kSTClassEndOfText@0$kSTClassOutOfBounds@1$kSTKCrossStreamReset@8192$kSTLigActionMask@16383$kSTMarkEnd@8192$kSTNoAdvance@16384$kSTRearrVerbMask@15$kSTSetMark@32768$kSTXHasLigAction@8192$kScientificInferiorsSelector@4$kShowDiacriticsSelector@0$kSimplifiedCharactersSelector@1$kSlashToDivideOffSelector@5$kSlashToDivideOnSelector@4$kSlashedZeroOffSelector@5$kSlashedZeroOnSelector@4$kSmallCapsSelector@3$kSmartQuotesOffSelector@9$kSmartQuotesOnSelector@8$kSmartSwashType@8$kSquaredLigaturesOffSelector@13$kSquaredLigaturesOnSelector@12$kStyleOptionsType@19$kStylisticAltEightOffSelector@17$kStylisticAltEightOnSelector@16$kStylisticAltEighteenOffSelector@37$kStylisticAltEighteenOnSelector@36$kStylisticAltElevenOffSelector@23$kStylisticAltElevenOnSelector@22$kStylisticAltFifteenOffSelector@31$kStylisticAltFifteenOnSelector@30$kStylisticAltFiveOffSelector@11$kStylisticAltFiveOnSelector@10$kStylisticAltFourOffSelector@9$kStylisticAltFourOnSelector@8$kStylisticAltFourteenOffSelector@29$kStylisticAltFourteenOnSelector@28$kStylisticAltNineOffSelector@19$kStylisticAltNineOnSelector@18$kStylisticAltNineteenOffSelector@39$kStylisticAltNineteenOnSelector@38$kStylisticAltOneOffSelector@3$kStylisticAltOneOnSelector@2$kStylisticAltSevenOffSelector@15$kStylisticAltSevenOnSelector@14$kStylisticAltSeventeenOffSelector@35$kStylisticAltSeventeenOnSelector@34$kStylisticAltSixOffSelector@13$kStylisticAltSixOnSelector@12$kStylisticAltSixteenOffSelector@33$kStylisticAltSixteenOnSelector@32$kStylisticAltTenOffSelector@21$kStylisticAltTenOnSelector@20$kStylisticAltThirteenOffSelector@27$kStylisticAltThirteenOnSelector@26$kStylisticAltThreeOffSelector@7$kStylisticAltThreeOnSelector@6$kStylisticAltTwelveOffSelector@25$kStylisticAltTwelveOnSelector@24$kStylisticAltTwentyOffSelector@41$kStylisticAltTwentyOnSelector@40$kStylisticAltTwoOffSelector@5$kStylisticAltTwoOnSelector@4$kStylisticAlternativesType@35$kSubstituteVerticalFormsOffSelector@1$kSubstituteVerticalFormsOnSelector@0$kSuperiorsSelector@1$kSwashAlternatesOffSelector@3$kSwashAlternatesOnSelector@2$kSymbolLigaturesOffSelector@17$kSymbolLigaturesOnSelector@16$kTRAKCurrentVersion@65536$kTRAKTag@1953653099$kTRAKUniformFormat@0$kTallCapsSelector@5$kTextSpacingType@22$kThirdWidthNumbersSelector@2$kThirdWidthTextSelector@3$kTitlingCapsSelector@4$kTraditionalAltFiveSelector@9$kTraditionalAltFourSelector@8$kTraditionalAltOneSelector@5$kTraditionalAltThreeSelector@7$kTraditionalAltTwoSelector@6$kTraditionalCharactersSelector@0$kTraditionalNamesCharactersSelector@14$kTranscodingCompositionOffSelector@5$kTranscodingCompositionOnSelector@4$kTransliterationType@23$kTypographicExtrasType@14$kUnconnectedSelector@0$kUnicodeDecompositionType@27$kUpperAndLowerCaseSelector@0$kUpperCaseNumbersSelector@1$kUpperCasePetiteCapsSelector@2$kUpperCaseSmallCapsSelector@1$kUpperCaseType@38$kVerticalFractionsSelector@1$kVerticalPositionType@10$kVerticalSubstitutionType@4$kWordFinalSwashesOffSelector@3$kWordFinalSwashesOnSelector@2$kWordInitialSwashesOffSelector@1$kWordInitialSwashesOnSelector@0$nameFontTableTag@1851878757$nonGlyphID@65535$os2FontTableTag@1330851634$sizeof_sfntCMapEncoding@8$sizeof_sfntCMapExtendedSubHeader@12$sizeof_sfntCMapHeader@4$sizeof_sfntCMapSubHeader@6$sizeof_sfntDescriptorHeader@8$sizeof_sfntDirectory@12$sizeof_sfntInstance@4$sizeof_sfntNameHeader@6$sizeof_sfntNameRecord@12$sizeof_sfntVariationAxis@20$sizeof_sfntVariationHeader@16$variationFontTableTag@1719034226$'''
misc.update({})
