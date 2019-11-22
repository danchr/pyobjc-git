from PyObjCTools.TestSupport import *

import Metal

class MTLStageInputOutputDescriptor (TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLAttributeFormatInvalid, 0)
        self.assertEqual(Metal.MTLAttributeFormatUChar2, 1)
        self.assertEqual(Metal.MTLAttributeFormatUChar3, 2)
        self.assertEqual(Metal.MTLAttributeFormatUChar4, 3)
        self.assertEqual(Metal.MTLAttributeFormatChar2, 4)
        self.assertEqual(Metal.MTLAttributeFormatChar3, 5)
        self.assertEqual(Metal.MTLAttributeFormatChar4, 6)
        self.assertEqual(Metal.MTLAttributeFormatUChar2Normalized, 7)
        self.assertEqual(Metal.MTLAttributeFormatUChar3Normalized, 8)
        self.assertEqual(Metal.MTLAttributeFormatUChar4Normalized, 9)
        self.assertEqual(Metal.MTLAttributeFormatChar2Normalized, 10)
        self.assertEqual(Metal.MTLAttributeFormatChar3Normalized, 11)
        self.assertEqual(Metal.MTLAttributeFormatChar4Normalized, 12)
        self.assertEqual(Metal.MTLAttributeFormatUShort2, 13)
        self.assertEqual(Metal.MTLAttributeFormatUShort3, 14)
        self.assertEqual(Metal.MTLAttributeFormatUShort4, 15)
        self.assertEqual(Metal.MTLAttributeFormatShort2, 16)
        self.assertEqual(Metal.MTLAttributeFormatShort3, 17)
        self.assertEqual(Metal.MTLAttributeFormatShort4, 18)
        self.assertEqual(Metal.MTLAttributeFormatUShort2Normalized, 19)
        self.assertEqual(Metal.MTLAttributeFormatUShort3Normalized, 20)
        self.assertEqual(Metal.MTLAttributeFormatUShort4Normalized, 21)
        self.assertEqual(Metal.MTLAttributeFormatShort2Normalized, 22)
        self.assertEqual(Metal.MTLAttributeFormatShort3Normalized, 23)
        self.assertEqual(Metal.MTLAttributeFormatShort4Normalized, 24)
        self.assertEqual(Metal.MTLAttributeFormatHalf2, 25)
        self.assertEqual(Metal.MTLAttributeFormatHalf3, 26)
        self.assertEqual(Metal.MTLAttributeFormatHalf4, 27)
        self.assertEqual(Metal.MTLAttributeFormatFloat, 28)
        self.assertEqual(Metal.MTLAttributeFormatFloat2, 29)
        self.assertEqual(Metal.MTLAttributeFormatFloat3, 30)
        self.assertEqual(Metal.MTLAttributeFormatFloat4, 31)
        self.assertEqual(Metal.MTLAttributeFormatInt, 32)
        self.assertEqual(Metal.MTLAttributeFormatInt2, 33)
        self.assertEqual(Metal.MTLAttributeFormatInt3, 34)
        self.assertEqual(Metal.MTLAttributeFormatInt4, 35)
        self.assertEqual(Metal.MTLAttributeFormatUInt, 36)
        self.assertEqual(Metal.MTLAttributeFormatUInt2, 37)
        self.assertEqual(Metal.MTLAttributeFormatUInt3, 38)
        self.assertEqual(Metal.MTLAttributeFormatUInt4, 39)
        self.assertEqual(Metal.MTLAttributeFormatInt1010102Normalized, 40)
        self.assertEqual(Metal.MTLAttributeFormatUInt1010102Normalized, 41)
        self.assertEqual(Metal.MTLAttributeFormatUChar4Normalized_BGRA, 42)
        self.assertEqual(Metal.MTLAttributeFormatUChar, 45)
        self.assertEqual(Metal.MTLAttributeFormatChar, 46)
        self.assertEqual(Metal.MTLAttributeFormatUCharNormalized, 47)
        self.assertEqual(Metal.MTLAttributeFormatCharNormalized, 48)
        self.assertEqual(Metal.MTLAttributeFormatUShort, 49)
        self.assertEqual(Metal.MTLAttributeFormatShort, 50)
        self.assertEqual(Metal.MTLAttributeFormatUShortNormalized, 51)
        self.assertEqual(Metal.MTLAttributeFormatShortNormalized, 52)
        self.assertEqual(Metal.MTLAttributeFormatHalf, 53)

        self.assertEqual(Metal.MTLIndexTypeUInt16, 0)
        self.assertEqual(Metal.MTLIndexTypeUInt32, 1)

        self.assertEqual(Metal.MTLStepFunctionConstant, 0)
        self.assertEqual(Metal.MTLStepFunctionPerVertex, 1)
        self.assertEqual(Metal.MTLStepFunctionPerInstance, 2)
        self.assertEqual(Metal.MTLStepFunctionPerPatch, 3)
        self.assertEqual(Metal.MTLStepFunctionPerPatchControlPoint, 4)
        self.assertEqual(Metal.MTLStepFunctionThreadPositionInGridX, 5)
        self.assertEqual(Metal.MTLStepFunctionThreadPositionInGridY, 6)
        self.assertEqual(Metal.MTLStepFunctionThreadPositionInGridXIndexed, 7)
        self.assertEqual(Metal.MTLStepFunctionThreadPositionInGridYIndexed, 8)
