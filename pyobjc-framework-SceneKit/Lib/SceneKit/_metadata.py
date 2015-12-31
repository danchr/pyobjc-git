# This file is generated by objective.metadata
#
# Last update: Thu Dec 31 12:54:45 2015

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'SCNVector4': objc.createStructType('SCNVector4', sel32or64(b'{SCNVector4=ffff}', b'{SCNVector4=dddd}'), ['x', 'y', 'z', 'w']), 'SCNVector3': objc.createStructType('SCNVector3', sel32or64(b'{SCNVector3=fff}', b'{SCNVector3=ddd}'), ['x', 'y', 'z'])})
constants = '''$SCNConsistencyElementIDErrorKey$SCNConsistencyElementTypeErrorKey$SCNConsistencyLineNumberErrorKey$SCNDetailedErrorsKey$SCNErrorDomain$SCNGeometrySourceSemanticBoneIndices$SCNGeometrySourceSemanticBoneWeights$SCNGeometrySourceSemanticColor$SCNGeometrySourceSemanticEdgeCrease$SCNGeometrySourceSemanticNormal$SCNGeometrySourceSemanticTexcoord$SCNGeometrySourceSemanticVertex$SCNGeometrySourceSemanticVertexCrease$SCNHitTestBackFaceCullingKey$SCNHitTestBoundingBoxOnlyKey$SCNHitTestClipToZRangeKey$SCNHitTestFirstFoundOnlyKey$SCNHitTestIgnoreChildNodesKey$SCNHitTestIgnoreHiddenNodesKey$SCNHitTestRootNodeKey$SCNHitTestSortResultsKey$SCNLightAttenuationEndKey$SCNLightAttenuationFalloffExponentKey$SCNLightAttenuationStartKey$SCNLightShadowFarClippingKey$SCNLightShadowNearClippingKey$SCNLightSpotInnerAngleKey$SCNLightSpotOuterAngleKey$SCNLightTypeAmbient$SCNLightTypeDirectional$SCNLightTypeOmni$SCNLightTypeSpot$SCNLightingModelBlinn$SCNLightingModelConstant$SCNLightingModelLambert$SCNLightingModelPhong$SCNModelTransform$SCNModelViewProjectionTransform$SCNModelViewTransform$SCNNormalTransform$SCNParticlePropertyAngle$SCNParticlePropertyAngularVelocity$SCNParticlePropertyBounce$SCNParticlePropertyCharge$SCNParticlePropertyColor$SCNParticlePropertyContactNormal$SCNParticlePropertyContactPoint$SCNParticlePropertyFrame$SCNParticlePropertyFrameRate$SCNParticlePropertyFriction$SCNParticlePropertyLife$SCNParticlePropertyOpacity$SCNParticlePropertyPosition$SCNParticlePropertyRotationAxis$SCNParticlePropertySize$SCNParticlePropertyVelocity$SCNPhysicsShapeKeepAsCompoundKey$SCNPhysicsShapeScaleKey$SCNPhysicsShapeTypeBoundingBox$SCNPhysicsShapeTypeConcavePolyhedron$SCNPhysicsShapeTypeConvexHull$SCNPhysicsShapeTypeKey$SCNPhysicsTestBackfaceCullingKey$SCNPhysicsTestCollisionBitMaskKey$SCNPhysicsTestSearchModeAll$SCNPhysicsTestSearchModeAny$SCNPhysicsTestSearchModeClosest$SCNPhysicsTestSearchModeKey$SCNPreferLowPowerDeviceKey$SCNPreferredDeviceKey$SCNPreferredRenderingAPIKey$SCNProgramMappingChannelKey$SCNProjectionTransform$SCNSceneEndTimeAttributeKey$SCNSceneExportDestinationURL$SCNSceneFrameRateAttributeKey$SCNSceneSourceAnimationImportPolicyDoNotPlay$SCNSceneSourceAnimationImportPolicyKey$SCNSceneSourceAnimationImportPolicyPlay$SCNSceneSourceAnimationImportPolicyPlayRepeatedly$SCNSceneSourceAnimationImportPolicyPlayUsingSceneTimeBase$SCNSceneSourceAssetAuthorKey$SCNSceneSourceAssetAuthoringToolKey$SCNSceneSourceAssetContributorsKey$SCNSceneSourceAssetCreatedDateKey$SCNSceneSourceAssetDirectoryURLsKey$SCNSceneSourceAssetModifiedDateKey$SCNSceneSourceAssetUnitKey$SCNSceneSourceAssetUnitMeterKey$SCNSceneSourceAssetUnitNameKey$SCNSceneSourceAssetUpAxisKey$SCNSceneSourceCheckConsistencyKey$SCNSceneSourceConvertToYUpKey$SCNSceneSourceConvertUnitsToMetersKey$SCNSceneSourceCreateNormalsIfAbsentKey$SCNSceneSourceFlattenSceneKey$SCNSceneSourceOverrideAssetURLsKey$SCNSceneSourceStrictConformanceKey$SCNSceneSourceUseSafeModeKey$SCNSceneStartTimeAttributeKey$SCNSceneUpAxisAttributeKey$SCNShaderModifierEntryPointFragment$SCNShaderModifierEntryPointGeometry$SCNShaderModifierEntryPointLightingModel$SCNShaderModifierEntryPointSurface$SCNViewTransform$'''
constants = constants + '$SCNMatrix4Identity@%s$'%(sel32or64('{CATransform3D=ffffffffffffffff}', '{CATransform3D=dddddddddddddddd}'),)
constants = constants + '$SCNVector4Zero@%s$'%(sel32or64('{SCNVector4=ffff}', '{SCNVector4=dddd}'),)
constants = constants + '$SCNVector3Zero@%s$'%(sel32or64('{SCNVector3=fff}', '{SCNVector3=ddd}'),)
enums = '''$SCNActionTimingModeEaseIn@1$SCNActionTimingModeEaseInEaseOut@3$SCNActionTimingModeEaseOut@2$SCNActionTimingModeLinear@0$SCNAntialiasingModeMultisampling16X@4$SCNAntialiasingModeMultisampling2X@1$SCNAntialiasingModeMultisampling4X@2$SCNAntialiasingModeMultisampling8X@3$SCNAntialiasingModeNone@0$SCNBillboardAxisAll@7$SCNBillboardAxisX@1$SCNBillboardAxisY@2$SCNBillboardAxisZ@4$SCNBlendModeAdd@1$SCNBlendModeAlpha@0$SCNBlendModeMultiply@3$SCNBlendModeReplace@5$SCNBlendModeScreen@4$SCNBlendModeSubtract@2$SCNBufferFrequencyPerFrame@0$SCNBufferFrequencyPerNode@1$SCNBufferFrequencyPerShadable@2$SCNChamferModeBack@2$SCNChamferModeBoth@0$SCNChamferModeFront@1$SCNClamp@1$SCNClampToBorder@3$SCNConsistencyInvalidArgumentError@1002$SCNConsistencyInvalidCountError@1001$SCNConsistencyInvalidURIError@1000$SCNConsistencyMissingAttributeError@1004$SCNConsistencyMissingElementError@1003$SCNConsistencyXMLSchemaValidationError@1005$SCNCullBack@0$SCNCullFront@1$SCNDebugOptionNone@0$SCNDebugOptionShowBoundingBoxes@2$SCNDebugOptionShowLightExtents@8$SCNDebugOptionShowLightInfluences@4$SCNDebugOptionShowPhysicsFields@16$SCNDebugOptionShowPhysicsShapes@1$SCNDebugOptionShowWireframe@32$SCNFilterModeLinear@2$SCNFilterModeNearest@1$SCNFilterModeNone@0$SCNGeometryPrimitiveTypeLine@2$SCNGeometryPrimitiveTypePoint@3$SCNGeometryPrimitiveTypeTriangleStrip@1$SCNGeometryPrimitiveTypeTriangles@0$SCNLinearFiltering@2$SCNMirror@4$SCNMorpherCalculationModeAdditive@1$SCNMorpherCalculationModeNormalized@0$SCNNearestFiltering@1$SCNNoFiltering@0$SCNParticleBirthDirectionConstant@0$SCNParticleBirthDirectionRandom@2$SCNParticleBirthDirectionSurfaceNormal@1$SCNParticleBirthLocationSurface@0$SCNParticleBirthLocationVertex@2$SCNParticleBirthLocationVolume@1$SCNParticleBlendModeAdditive@0$SCNParticleBlendModeAlpha@4$SCNParticleBlendModeMultiply@2$SCNParticleBlendModeReplace@5$SCNParticleBlendModeScreen@3$SCNParticleBlendModeSubtract@1$SCNParticleEventBirth@0$SCNParticleEventCollision@2$SCNParticleEventDeath@1$SCNParticleImageSequenceAnimationModeAutoReverse@2$SCNParticleImageSequenceAnimationModeClamp@1$SCNParticleImageSequenceAnimationModeRepeat@0$SCNParticleInputModeOverDistance@1$SCNParticleInputModeOverLife@0$SCNParticleInputModeOverOtherProperty@2$SCNParticleModifierStagePostCollision@3$SCNParticleModifierStagePostDynamics@1$SCNParticleModifierStagePreCollision@2$SCNParticleModifierStagePreDynamics@0$SCNParticleOrientationModeBillboardScreenAligned@0$SCNParticleOrientationModeBillboardViewAligned@1$SCNParticleOrientationModeBillboardYAligned@3$SCNParticleOrientationModeFree@2$SCNParticleSortingModeDistance@2$SCNParticleSortingModeNone@0$SCNParticleSortingModeOldestFirst@3$SCNParticleSortingModeProjectedDepth@1$SCNParticleSortingModeYoungestFirst@4$SCNPhysicsBodyTypeDynamic@1$SCNPhysicsBodyTypeKinematic@2$SCNPhysicsBodyTypeStatic@0$SCNPhysicsCollisionCategoryDefault@1$SCNPhysicsCollisionCategoryStatic@2$SCNPhysicsFieldScopeInsideExtent@0$SCNPhysicsFieldScopeOutsideExtent@1$SCNProgramCompilationError@1$SCNReferenceLoadingPolicyImmediate@0$SCNReferenceLoadingPolicyOnDemand@1$SCNRenderingAPIMetal@0$SCNRenderingAPIOpenGLCore32@2$SCNRenderingAPIOpenGLCore41@3$SCNRenderingAPIOpenGLLegacy@1$SCNRepeat@2$SCNSceneSourceStatusComplete@16$SCNSceneSourceStatusError@-1$SCNSceneSourceStatusParsing@4$SCNSceneSourceStatusProcessing@12$SCNSceneSourceStatusValidating@8$SCNShadowModeDeferred@1$SCNShadowModeForward@0$SCNShadowModeModulated@2$SCNTransparencyModeAOne@0$SCNTransparencyModeRGBZero@1$SCNWrapModeClamp@1$SCNWrapModeClampToBorder@3$SCNWrapModeMirror@4$SCNWrapModeRepeat@2$'''
misc.update({'SCNPhysicsCollisionCategoryAll': sel32or64(4294967295, 18446744073709551615)})
misc.update({})
functions={'SCNMatrix4IsIdentity': (sel32or64(b'B{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}'),), 'SCNVector4Make': (sel32or64(b'{SCNVector4=ffff}ffff', b'{SCNVector4=dddd}dddd'),), 'SCNMatrix4EqualToMatrix4': (sel32or64(b'B{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'B{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'SCNMatrix4MakeTranslation': (sel32or64(b'{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}ddd'),), 'SCNMatrix4FromMat4': (sel32or64(b'{CATransform3D=ffffffffffffffff}{_matrix_float4x4=[4$]}', b'{CATransform3D=dddddddddddddddd}{_matrix_float4x4=[4$]}'),), 'SCNMatrix4Scale': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),), 'SCNMatrix4MakeRotation': (sel32or64(b'{CATransform3D=ffffffffffffffff}ffff', b'{CATransform3D=dddddddddddddddd}dddd'),), 'SCNVector4FromGLKVector4': (sel32or64(b'{SCNVector4=ffff}(_GLKVector4={=ffff}{=ffff}{=ffff}[4f])', b'{SCNVector4=dddd}(_GLKVector4={=ffff}{=ffff}{=ffff}[4f])'),), 'SCNVector4ToFloat4': (sel32or64(b'${SCNVector4=ffff}', b'${SCNVector4=dddd}'),), 'SCNVector3EqualToVector3': (sel32or64(b'B{SCNVector3=fff}{SCNVector3=fff}', b'B{SCNVector3=ddd}{SCNVector3=ddd}'),), 'SCNMatrix4ToGLKMatrix4': (sel32or64(b'(_GLKMatrix4={=ffffffffffffffff}[16f]){CATransform3D=ffffffffffffffff}', b'(_GLKMatrix4={=ffffffffffffffff}[16f]){CATransform3D=dddddddddddddddd}'),), 'SCNMatrix4ToMat4': (sel32or64(b'{_matrix_float4x4=[4$]}{CATransform3D=ffffffffffffffff}', b'{_matrix_float4x4=[4$]}{CATransform3D=dddddddddddddddd}'),), 'SCNVector4EqualToVector4': (sel32or64(b'B{SCNVector4=ffff}{SCNVector4=ffff}', b'B{SCNVector4=dddd}{SCNVector4=dddd}'),), 'SCNMatrix4MakeScale': (sel32or64(b'{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}ddd'),), 'SCNMatrix4FromGLKMatrix4': (sel32or64(b'{CATransform3D=ffffffffffffffff}(_GLKMatrix4={=ffffffffffffffff}[16f])', b'{CATransform3D=dddddddddddddddd}(_GLKMatrix4={=ffffffffffffffff}[16f])'),), 'SCNMatrix4Invert': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'SCNVector4ToGLKVector4': (sel32or64(b'(_GLKVector4={=ffff}{=ffff}{=ffff}[4f]){SCNVector4=ffff}', b'(_GLKVector4={=ffff}{=ffff}{=ffff}[4f]){SCNVector4=dddd}'),), 'SCNMatrix4Rotate': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}ffff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}dddd'),), 'SCNVector3ToGLKVector3': (sel32or64(b'(_GLKVector3={=fff}{=fff}{=fff}[3f]){SCNVector3=fff}', b'(_GLKVector3={=fff}{=fff}{=fff}[3f]){SCNVector3=ddd}'),), 'SCNVector3Make': (sel32or64(b'{SCNVector3=fff}fff', b'{SCNVector3=ddd}ddd'),), 'SCNVector4FromFloat4': (sel32or64(b'{SCNVector4=ffff}$', b'{SCNVector4=dddd}$'),), 'SCNVector3FromGLKVector3': (sel32or64(b'{SCNVector3=fff}(_GLKVector3={=fff}{=fff}{=fff}[3f])', b'{SCNVector3=ddd}(_GLKVector3={=fff}{=fff}{=fff}[3f])'),), 'SCNMatrix4Mult': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}'),), 'SCNMatrix4Translate': (sel32or64(b'{CATransform3D=ffffffffffffffff}{CATransform3D=ffffffffffffffff}fff', b'{CATransform3D=dddddddddddddddd}{CATransform3D=dddddddddddddddd}ddd'),)}
aliases = {'SCNClampToBorder': 'SCNWrapModeClampToBorder', 'SCNNearestFiltering': 'SCNFilterModeNearest', 'SCNRepeat': 'SCNWrapModeRepeat', 'SCNClamp': 'SCNWrapModeClamp', 'SCNLinearFiltering': 'SCNFilterModeLinear', 'SCNNoFiltering': 'SCNFilterModeNone', 'SCNQuaternion': 'SCNVector4', 'SCNMatrix4': 'CATransform3D', 'SCNMirror': 'SCNWrapModeMirror', 'SCN_EXTERN': 'FOUNDATION_EXTERN'}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'CAAnimation', b'setUsesSceneTimeBase:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CAAnimation', b'usesSceneTimeBase', {'retval': {'type': b'Z'}})
    r(b'NSObject', b'actionForKey:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'addAnimation:forKey:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'addModifierForProperties:atStage:withBlock:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^^v'}, 2: {'type': sel32or64(b'^I', b'^Q')}, 3: {'type': sel32or64(b'i', b'q')}, 4: {'type': sel32or64(b'i', b'q')}, 5: {'type': b'f'}}}}}})
    r(b'NSObject', b'animationEventWithKeyTime:block:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'Z'}}}}}})
    r(b'NSObject', b'animationForKey:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'animationKeys', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'autoenablesDefaultLighting', {'required': True, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'completionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'NSObject', b'context', {'required': True, 'retval': {'type': b'^v'}})
    r(b'NSObject', b'currentTime', {'required': True, 'retval': {'type': b'd'}})
    r(b'NSObject', b'customActionWithDuration:actionBlock:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': sel32or64(b'f', b'd')}}}}}})
    r(b'NSObject', b'customFieldWithEvaluationBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'{SCNVector3=ddd}'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'{SCNVector3=ddd}'}, 2: {'type': b'{SCNVector3=ddd}'}, 3: {'type': b'f'}, 4: {'type': b'f'}, 5: {'type': b'd'}}}}}})
    r(b'NSObject', b'delegate', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'didFinishPlayback', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'NSObject', b'entriesPassingTest:', {'arguments': {2: {'callable': {'retval': {'type': b'Z'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'o^Z'}}}}}})
    r(b'NSObject', b'geometrySourceWithNormals:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 1}}})
    r(b'NSObject', b'geometrySourceWithTextureCoordinates:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 1}}})
    r(b'NSObject', b'geometrySourceWithVertices:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 1}}})
    r(b'NSObject', b'getBoundingBoxMin:max:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': sel32or64(b'^{SCNVector3=fff}', b'^{SCNVector3=ddd}'), 'type_modifier': b'o'}, 3: {'type': sel32or64(b'^{SCNVector3=fff}', b'^{SCNVector3=ddd}'), 'type_modifier': b'o'}}})
    r(b'NSObject', b'getBoundingSphereCenter:radius:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': sel32or64(b'^{SCNVector3=fff}', b'^{SCNVector3=ddd}'), 'type_modifier': b'o'}, 3: {'type': sel32or64(b'^f', b'^d'), 'type_modifier': b'o'}}})
    r(b'NSObject', b'handleBindingOfBufferNamed:frequency:usingBlock:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}}}}})
    r(b'NSObject', b'handleBindingOfSymbol:usingBlock:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'I'}, 2: {'type': b'I'}, 3: {'type': b'@'}, 4: {'type': b'@'}}}, 'type': b'@?'}}})
    r(b'NSObject', b'handleEvent:forProperties:withBlock:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^^v'}, 2: {'type': sel32or64(b'^I', b'^Q')}, 3: {'type': sel32or64(b'^I', b'^Q')}, 4: {'type': sel32or64(b'i', b'q')}}}}}})
    r(b'NSObject', b'handleUnbindingOfSymbol:usingBlock:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'I'}, 2: {'type': b'I'}, 3: {'type': b'@'}, 4: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NSObject', b'hasActions', {'required': True, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'hitTest:options:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': sel32or64(b'{CGPoint=ff}', b'{CGPoint=dd}')}, 3: {'type': b'@'}}})
    r(b'NSObject', b'isAffectedByGravity', {'retval': {'type_override': 'Z'}})
    r(b'NSObject', b'isAnimationForKeyPaused:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'isJitteringEnabled', {'required': True, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'isNodeInsideFrustum:withPointOfView:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'isPlaying', {'required': True, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'isPositional', {'retval': {'type_override': 'Z'}})
    r(b'NSObject', b'loops', {'required': True, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'overlaySKScene', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'pauseAnimationForKey:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'physicsWorld:didBeginContact:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'physicsWorld:didEndContact:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'physicsWorld:didUpdateContact:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'playAudioSource:waitForCompletion:', {'arguments': {3: {'type_override': 'Z'}}})
    r(b'NSObject', b'pointOfView', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'prepareObject:shouldAbortBlock:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@?'}}})
    r(b'NSObject', b'prepareObjects:withCompletionHandler:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@?'}}})
    r(b'NSObject', b'program', {'required': False, 'retval': {'type': b'@'}})
    r(b'NSObject', b'program:bindValueForSymbol:atLocation:programID:renderer:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'I'}, 5: {'type': b'I'}, 6: {'type': b'@'}}})
    r(b'NSObject', b'program:handleError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'program:unbindValueForSymbol:atLocation:programID:renderer:', {'required': False, 'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'I'}, 5: {'type': b'I'}, 6: {'type': b'@'}}})
    r(b'NSObject', b'programIsOpaque:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'projectPoint:', {'required': True, 'retval': {'type': sel32or64(b'{SCNVector3=fff}', b'{SCNVector3=ddd}')}, 'arguments': {2: {'type': sel32or64(b'{SCNVector3=fff}', b'{SCNVector3=ddd}')}}})
    r(b'NSObject', b'removeActionForKey:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'removeAllActions', {'required': True, 'retval': {'type': b'v'}})
    r(b'NSObject', b'removeAllAnimations', {'required': True, 'retval': {'type': b'v'}})
    r(b'NSObject', b'removeAnimationForKey:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'removeAnimationForKey:fadeOutDuration:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'f', b'd')}}})
    r(b'NSObject', b'renderNode:renderer:arguments:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'NSObject', b'renderer:didApplyAnimationsAtTime:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'd'}}})
    r(b'NSObject', b'renderer:didRenderScene:atTime:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'd'}}})
    r(b'NSObject', b'renderer:didSimulatePhysicsAtTime:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'd'}}})
    r(b'NSObject', b'renderer:updateAtTime:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'd'}}})
    r(b'NSObject', b'renderer:willRenderScene:atTime:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'd'}}})
    r(b'NSObject', b'resumeAnimationForKey:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'runAction:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'runAction:completionHandler:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@?'}}})
    r(b'NSObject', b'runAction:forKey:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'runAction:forKey:completionHandler:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@?'}}})
    r(b'NSObject', b'runBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NSObject', b'runBlock:queue:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NSObject', b'scene', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'sceneTime', {'required': True, 'retval': {'type': b'd'}})
    r(b'NSObject', b'sceneWithOptions:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'NSObject', b'sceneWithOptions:statusHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}, 2: {'type': sel32or64(b'i', b'q')}, 3: {'type': b'@'}, 4: {'type': b'o^Z'}}}}}})
    r(b'NSObject', b'sceneWithURL:options:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'NSObject', b'setAffectedByGravity:', {'arguments': {2: {'type_override': 'Z'}}})
    r(b'NSObject', b'setAutoenablesDefaultLighting:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'Z'}}})
    r(b'NSObject', b'setBoundingBoxMin:max:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': sel32or64(b'^{SCNVector3=fff}', b'^{SCNVector3=ddd}'), 'type_modifier': b'n'}, 3: {'type': sel32or64(b'^{SCNVector3=fff}', b'^{SCNVector3=ddd}'), 'type_modifier': b'n'}}})
    r(b'NSObject', b'setCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NSObject', b'setCurrentTime:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setDelegate:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setDidFinishPlayback:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NSObject', b'setJitteringEnabled:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'Z'}}})
    r(b'NSObject', b'setLoops:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'Z'}}})
    r(b'NSObject', b'setOverlaySKScene:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setPlaying:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'Z'}}})
    r(b'NSObject', b'setPointOfView:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setPositional:', {'arguments': {2: {'type_override': 'Z'}}})
    r(b'NSObject', b'setProgram:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setScene:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setSceneTime:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'd'}}})
    r(b'NSObject', b'setShaderModifiers:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setShouldStream:', {'arguments': {2: {'type_override': 'Z'}}})
    r(b'NSObject', b'setShowsStatistics:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'Z'}}})
    r(b'NSObject', b'setTechnique:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setTimingFunction:', {'arguments': {2: {'callable': {'retval': {'type': b'f'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}}}}}})
    r(b'NSObject', b'setUsesDefaultMomentOfInertia:', {'arguments': {2: {'type_override': 'Z'}}})
    r(b'NSObject', b'setWillStartPlayback:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NSObject', b'shaderModifiers', {'required': False, 'retval': {'type': b'@'}})
    r(b'NSObject', b'shouldStream', {'retval': {'type_override': 'Z'}})
    r(b'NSObject', b'showsStatistics', {'required': True, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'technique', {'required': True, 'retval': {'type': b'@'}})
    r(b'NSObject', b'timingFunction', {'retval': {'callable': {'retval': {'type': b'f'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}}}}})
    r(b'NSObject', b'transformConstraintInWorldSpace:withBlock:', {'arguments': {3: {'callable': {'retval': {'type': b'{CATransform3D=dddddddddddddddd}'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'{CATransform3D=dddddddddddddddd}'}}}}}})
    r(b'NSObject', b'unprojectPoint:', {'required': True, 'retval': {'type': sel32or64(b'{SCNVector3=fff}', b'{SCNVector3=ddd}')}, 'arguments': {2: {'type': sel32or64(b'{SCNVector3=fff}', b'{SCNVector3=ddd}')}}})
    r(b'NSObject', b'usesDefaultMomentOfInertia', {'retval': {'type_override': 'Z'}})
    r(b'NSObject', b'willStartPlayback', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'NSObject', b'writeBytes:length:', {'arguments': {2: {'type': 'n^v', 'c_array_length_in_arg': 3}, 3: {'type': sel32or64(b'I', b'Q')}}})
    r(b'NSObject', b'writeImage:withSceneDocumentURL:originalImageURL:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'NSObject', b'writeToURL:options:delegate:progressHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}, 2: {'type': b'@'}, 3: {'type': b'o^Z'}}}}}})
    r(b'SCNAction', b'customActionWithDuration:actionBlock:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': sel32or64(b'f', b'd')}}}}}})
    r(b'SCNAction', b'playAudioSource:waitForCompletion:', {'arguments': {3: {'type': 'Z'}}})
    r(b'SCNAction', b'rotateToX:y:z:duration:shortestUnitArc:', {'arguments': {6: {'type': b'Z'}}})
    r(b'SCNAction', b'runBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SCNAction', b'runBlock:queue:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SCNAction', b'setTimingFunction:', {'arguments': {2: {'callable': {'retval': {'type': b'f'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}}}}}})
    r(b'SCNAction', b'timingFunction', {'retval': {'callable': {'retval': {'type': b'f'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}}}}})
    r(b'SCNAnimationEvent', b'animationEventWithKeyTime:block:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'Z'}}}}}})
    r(b'SCNAudioSource', b'didFinishPlayback', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'SCNAudioSource', b'isPositional', {'retval': {'type': 'Z'}})
    r(b'SCNAudioSource', b'setDidFinishPlayback:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'SCNAudioSource', b'setPositional:', {'arguments': {2: {'type': 'Z'}}})
    r(b'SCNAudioSource', b'setShouldStream:', {'arguments': {2: {'type': 'Z'}}})
    r(b'SCNAudioSource', b'setWillStartPlayback:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'SCNAudioSource', b'shouldStream', {'retval': {'type': 'Z'}})
    r(b'SCNAudioSource', b'willStartPlayback', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'SCNCamera', b'automaticallyAdjustsZRange', {'retval': {'type': b'Z'}})
    r(b'SCNCamera', b'setAutomaticallyAdjustsZRange:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNCamera', b'setUsesOrthographicProjection:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNCamera', b'usesOrthographicProjection', {'retval': {'type': b'Z'}})
    r(b'SCNGeometrySource', b'floatComponents', {'retval': {'type': b'Z'}})
    r(b'SCNGeometrySource', b'geometrySourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:', {'arguments': {5: {'type': b'Z'}}})
    r(b'SCNGeometrySource', b'geometrySourceWithNormals:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'SCNGeometrySource', b'geometrySourceWithTextureCoordinates:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'SCNGeometrySource', b'geometrySourceWithVertices:count:', {'arguments': {2: {'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'SCNLight', b'castsShadow', {'retval': {'type': b'Z'}})
    r(b'SCNLight', b'setCastsShadow:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNLookAtConstraint', b'gimbalLockEnabled', {'retval': {'type': b'Z'}})
    r(b'SCNLookAtConstraint', b'setGimbalLockEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNMaterial', b'isDoubleSided', {'retval': {'type': b'Z'}})
    r(b'SCNMaterial', b'isLitPerPixel', {'retval': {'type': b'Z'}})
    r(b'SCNMaterial', b'locksAmbientWithDiffuse', {'retval': {'type': b'Z'}})
    r(b'SCNMaterial', b'readsFromDepthBuffer', {'retval': {'type': b'Z'}})
    r(b'SCNMaterial', b'setDoubleSided:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNMaterial', b'setLitPerPixel:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNMaterial', b'setLocksAmbientWithDiffuse:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNMaterial', b'setReadsFromDepthBuffer:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNMaterial', b'setWritesToDepthBuffer:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNMaterial', b'writesToDepthBuffer', {'retval': {'type': b'Z'}})
    r(b'SCNNode', b'castsShadow', {'retval': {'type': b'Z'}})
    r(b'SCNNode', b'childNodeWithName:recursively:', {'arguments': {3: {'type': b'Z'}}})
    r(b'SCNNode', b'isHidden', {'retval': {'type': b'Z'}})
    r(b'SCNNode', b'isPaused', {'retval': {'type': b'Z'}})
    r(b'SCNNode', b'setCastsShadow:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNNode', b'setHidden:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNNode', b'setPaused:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNParticleSystem', b'addModifierForProperties:atStage:withBlock:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^^v'}, 2: {'type': sel32or64(b'^I', b'^Q')}, 3: {'type': sel32or64(b'i', b'q')}, 4: {'type': sel32or64(b'i', b'q')}, 5: {'type': b'f'}}}}}})
    r(b'SCNParticleSystem', b'affectedByGravity', {'retval': {'type': b'Z'}})
    r(b'SCNParticleSystem', b'affectedByPhysicsFields', {'retval': {'type': b'Z'}})
    r(b'SCNParticleSystem', b'handleEvent:forProperties:withBlock:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^^v'}, 2: {'type': sel32or64(b'^I', b'^Q')}, 3: {'type': sel32or64(b'^I', b'^Q')}, 4: {'type': sel32or64(b'i', b'q')}}}}}})
    r(b'SCNParticleSystem', b'isBlackPassEnabled', {'retval': {'type': b'Z'}})
    r(b'SCNParticleSystem', b'isLightingEnabled', {'retval': {'type': b'Z'}})
    r(b'SCNParticleSystem', b'isLocal', {'retval': {'type': b'Z'}})
    r(b'SCNParticleSystem', b'loops', {'retval': {'type': b'Z'}})
    r(b'SCNParticleSystem', b'particleDiesOnCollision', {'retval': {'type': b'Z'}})
    r(b'SCNParticleSystem', b'setAffectedByGravity:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNParticleSystem', b'setAffectedByPhysicsFields:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNParticleSystem', b'setBlackPassEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNParticleSystem', b'setLightingEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNParticleSystem', b'setLocal:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNParticleSystem', b'setLoops:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNParticleSystem', b'setParticleDiesOnCollision:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNPhysicsBody', b'allowsResting', {'retval': {'type': b'Z'}})
    r(b'SCNPhysicsBody', b'applyForce:atPosition:impulse:', {'arguments': {4: {'type': b'Z'}}})
    r(b'SCNPhysicsBody', b'applyForce:impulse:', {'arguments': {3: {'type': b'Z'}}})
    r(b'SCNPhysicsBody', b'applyTorque:impulse:', {'arguments': {3: {'type': b'Z'}}})
    r(b'SCNPhysicsBody', b'isAffectedByGravity', {'retval': {'type': 'Z'}})
    r(b'SCNPhysicsBody', b'isResting', {'retval': {'type': b'Z'}})
    r(b'SCNPhysicsBody', b'setAffectedByGravity:', {'arguments': {2: {'type': 'Z'}}})
    r(b'SCNPhysicsBody', b'setAllowsResting:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNPhysicsBody', b'setUsesDefaultMomentOfInertia:', {'arguments': {2: {'type': 'Z'}}})
    r(b'SCNPhysicsBody', b'usesDefaultMomentOfInertia', {'retval': {'type': 'Z'}})
    r(b'SCNPhysicsField', b'customFieldWithEvaluationBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'{SCNVector3=ddd}'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'{SCNVector3=ddd}'}, 2: {'type': b'{SCNVector3=ddd}'}, 3: {'type': b'f'}, 4: {'type': b'f'}, 5: {'type': b'd'}}}}}})
    r(b'SCNPhysicsField', b'isActive', {'retval': {'type': b'Z'}})
    r(b'SCNPhysicsField', b'isExclusive', {'retval': {'type': b'Z'}})
    r(b'SCNPhysicsField', b'setActive:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNPhysicsField', b'setExclusive:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNPhysicsField', b'setUsesEllipsoidalExtent:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNPhysicsField', b'usesEllipsoidalExtent', {'retval': {'type': b'Z'}})
    r(b'SCNProgram', b'handleBindingOfBufferNamed:frequency:usingBlock:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}}}}})
    r(b'SCNProgram', b'isOpaque', {'retval': {'type': b'Z'}})
    r(b'SCNProgram', b'setOpaque:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNScene', b'isPaused', {'retval': {'type': b'Z'}})
    r(b'SCNScene', b'sceneWithURL:options:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'SCNScene', b'setPaused:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNScene', b'writeToURL:options:delegate:progressHandler:', {'retval': {'type': b'Z'}, 'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}, 2: {'type': b'@'}, 3: {'type': b'o^Z'}}}}}})
    r(b'SCNSceneSource', b'entriesPassingTest:', {'arguments': {2: {'callable': {'retval': {'type': b'Z'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'o^Z'}}}}}})
    r(b'SCNSceneSource', b'sceneWithOptions:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'SCNSceneSource', b'sceneWithOptions:statusHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'f'}, 2: {'type': sel32or64(b'i', b'q')}, 3: {'type': b'@'}, 4: {'type': b'o^Z'}}}}}})
    r(b'SCNSphere', b'isGeodesic', {'retval': {'type': b'Z'}})
    r(b'SCNSphere', b'setGeodesic:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNTechnique', b'handleBindingOfSymbol:usingBlock:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'I'}, 2: {'type': b'I'}, 3: {'type': b'@'}, 4: {'type': b'@'}}}}}})
    r(b'SCNText', b'isWrapped', {'retval': {'type': b'Z'}})
    r(b'SCNText', b'setWrapped:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNTransaction', b'completionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}})
    r(b'SCNTransaction', b'disableActions', {'retval': {'type': b'Z'}})
    r(b'SCNTransaction', b'setCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'SCNTransaction', b'setDisableActions:', {'arguments': {2: {'type': b'Z'}}})
    r(b'SCNTransformConstraint', b'transformConstraintInWorldSpace:withBlock:', {'arguments': {2: {'type': b'Z'}, 3: {'callable': {'retval': {'type': b'{CATransform3D=dddddddddddddddd}'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'{CATransform3D=dddddddddddddddd}'}}}}}})
    r(b'SCNView', b'allowsCameraControl', {'retval': {'type': b'Z'}})
    r(b'SCNView', b'setAllowsCameraControl:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
