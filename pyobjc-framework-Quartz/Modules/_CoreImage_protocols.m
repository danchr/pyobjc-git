static void __attribute__((__used__)) use_protocols2(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(CIFilter));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIGaussianGradient));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIHueSaturationValueGradient));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CILinearGradient));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIRadialGradient));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISmoothLinearGradient));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISharpenLuminance));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIUnsharpMask));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICircularScreen));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICMYKHalftone));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDotScreen));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIHatchedScreen));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CILineScreen));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIBicubicScaleTransform));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIEdgePreserveUpsample));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CILanczosScaleTransform));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPerspectiveCorrection));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPerspectiveTransform));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPerspectiveTransformWithExtent));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIStraighten));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CITransitionFilter));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIAccordionFoldTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIBarsSwipeTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICopyMachineTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDisintegrateWithMaskTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDissolveTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIFlashTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIModTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPageCurlTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPageCurlWithShadowTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIRippleTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISwipeTransition));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICompositeOperation));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorClamp));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorControls));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorMatrix));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorPolynomial));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDepthToDisparity));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDisparityToDepth));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIExposureAdjust));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIGammaAdjust));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIHueAdjust));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CILinearToSRGBToneCurve));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISRGBToneCurveToLinear));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CITemperatureAndTint));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIToneCurve));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIVibrance));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIWhitePointAdjust));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorCrossPolynomial));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorCube));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorCubesMixedWithMask));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorCubeWithColorSpace));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorCurves));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorInvert));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorMap));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorMonochrome));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIColorPosterize));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDither));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDocumentEnhancer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIFalseColor));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CILabDeltaE));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMaskToAlpha));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMaximumComponent));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMinimumComponent));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPaletteCentroid));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPalettize));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPhotoEffect));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISepiaTone));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIThermal));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIVignette));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIVignetteEffect));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIXRay));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIAffineClamp));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIAffineTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIEightfoldReflectedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIFourfoldReflectedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIFourfoldRotatedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIFourfoldTranslatedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIGlideReflectedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIKaleidoscope));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIOpTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIParallelogramTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPerspectiveTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISixfoldReflectedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISixfoldRotatedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CITriangleKaleidoscope));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CITriangleTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CITwelvefoldReflectedTile));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIAttributedTextImageGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIAztecCodeGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIBarcodeGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICheckerboardGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICode128BarcodeGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CILenticularHaloGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMeshGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPDF417BarcodeGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIQRCodeGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIRandomGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIStarShineGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIStripesGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISunbeamsGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CITextImageGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIBlendWithMask));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIBloom));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIComicEffect));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIConvolution));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICoreMLModel));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CICrystallize));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDepthOfField));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIEdges));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIEdgeWork));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIGloom));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIHeightFieldFromMask));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIHexagonalPixellate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIHighlightShadowAdjust));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CILineOverlay));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMix));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPixellate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPointillize));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISaliencyMap));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIShadedMaterial));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISpotColor));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CISpotLight));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIBokehBlur));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIBoxBlur));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIDiscBlur));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIGaussianBlur));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMaskedVariableBlur));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMedian));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMorphologyGradient));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMorphologyMaximum));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMorphologyMinimum));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMorphologyRectangleMaximum));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMorphologyRectangleMinimum));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIMotionBlur));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CINoiseReduction));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIZoomBlur));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIKeystoneCorrectionCombined));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIKeystoneCorrectionHorizontal));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIKeystoneCorrectionVertical));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIPerspectiveRotate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIRoundedRectangleGenerator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CIGaborGradients));
    Py_XDECREF(p);
#endif
}
