# This file is generated by objective.metadata
#
# Last update: Thu Aug  1 08:02:52 2019

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
misc.update({'CMQuaternion': objc.createStructType('CMQuaternion', b'{_CMQuaternion=dddd}', ['x', 'y', 'z', 'w']), 'CMMagneticField': objc.createStructType('CMMagneticField', b'{_CMMagneticField=ddd}', ['x', 'y', 'z']), 'CMCalibratedMagneticField': objc.createStructType('CMCalibratedMagneticField', b'{_CMCalibratedMagneticField={_CMMagneticField=ddd}i}', ['field', 'accuracy']), 'CMRotationRate': objc.createStructType('CMRotationRate', b'{_CMRotationRate=ddd}', ['x', 'y', 'z']), 'CMRotationMatrix': objc.createStructType('CMRotationMatrix', b'{_CMRotationMatrix=ddddddddd}', ['m11', 'm12', 'm13', 'm21', 'm22', 'm23', 'm31', 'm32', 'm33']), 'CMAcceleration': objc.createStructType('CMAcceleration', b'{_CMAcceleration=ddd}', ['x', 'y', 'z'])})
constants = '''$CMErrorDomain$'''
enums = '''$CMAttitudeReferenceFrameXArbitraryCorrectedZVertical@2$CMAttitudeReferenceFrameXArbitraryZVertical@1$CMAttitudeReferenceFrameXMagneticNorthZVertical@4$CMAttitudeReferenceFrameXTrueNorthZVertical@8$CMAuthorizationStatusAuthorized@3$CMAuthorizationStatusDenied@2$CMAuthorizationStatusNotDetermined@0$CMAuthorizationStatusRestricted@1$CMErrorDeviceRequiresMovement@101$CMErrorInvalidAction@108$CMErrorInvalidParameter@107$CMErrorMotionActivityNotAuthorized@105$CMErrorMotionActivityNotAvailable@104$CMErrorMotionActivityNotEntitled@106$CMErrorNULL@100$CMErrorNotAuthorized@111$CMErrorNotAvailable@109$CMErrorNotEntitled@110$CMErrorTrueNorthNotAvailable@102$CMErrorUnknown@103$CMMagneticFieldCalibrationAccuracyHigh@2$CMMagneticFieldCalibrationAccuracyLow@0$CMMagneticFieldCalibrationAccuracyMedium@1$CMMagneticFieldCalibrationAccuracyUncalibrated@-1$CMMotionActivityConfidenceHigh@2$CMMotionActivityConfidenceLow@0$CMMotionActivityConfidenceMedium@1$CMPedometerEventTypePause@0$CMPedometerEventTypeResume@1$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'CMAccelerometerData', b'acceleration', {'retval': {'type': b'{_CMAcceleration=ddd}'}})
    r(b'CMAltimeter', b'isRelativeAltitudeAvailable', {'retval': {'type': b'Z'}})
    r(b'CMAttitude', b'quaternion', {'retval': {'type': b'{_CMQuaternion=dddd}'}})
    r(b'CMAttitude', b'rotationMatrix', {'retval': {'type': b'{_CMRotationMatrix=ddddddddd}'}})
    r(b'CMDeviceMotion', b'gravity', {'retval': {'type': b'{_CMAcceleration=ddd}'}})
    r(b'CMDeviceMotion', b'magneticField', {'retval': {'type': b'{_CMCalibratedMagneticField={_CMMagneticField=ddd}i}'}})
    r(b'CMDeviceMotion', b'rotationRate', {'retval': {'type': b'{_CMRotationRate=ddd}'}})
    r(b'CMDeviceMotion', b'userAcceleration', {'retval': {'type': b'{_CMAcceleration=ddd}'}})
    r(b'CMGyroData', b'rotationRate', {'retval': {'type': b'{_CMRotationRate=ddd}'}})
    r(b'CMMagnetometerData', b'magneticField', {'retval': {'type': b'{_CMMagneticField=ddd}'}})
    r(b'CMMotionActivity', b'automotive', {'retval': {'type': b'Z'}})
    r(b'CMMotionActivity', b'cycling', {'retval': {'type': b'Z'}})
    r(b'CMMotionActivity', b'running', {'retval': {'type': b'Z'}})
    r(b'CMMotionActivity', b'stationary', {'retval': {'type': b'Z'}})
    r(b'CMMotionActivity', b'unknown', {'retval': {'type': b'Z'}})
    r(b'CMMotionActivity', b'walking', {'retval': {'type': b'Z'}})
    r(b'CMMotionActivityManager', b'isActivityAvailable', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isAccelerometerActive', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isAccelerometerAvailable', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isDeviceMotionActive', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isDeviceMotionAvailable', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isGyroActive', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isGyroAvailable', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isMagnetometerActive', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'isMagnetometerAvailable', {'retval': {'type': b'Z'}})
    r(b'CMMotionManager', b'setShowsDeviceMovementDisplay:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CMMotionManager', b'showsDeviceMovementDisplay', {'retval': {'type': b'Z'}})
    r(b'CMMovementDisorderManager', b'isAvailable', {'retval': {'type': b'Z'}})
    r(b'CMPedometer', b'isCadenceAvailable', {'retval': {'type': b'Z'}})
    r(b'CMPedometer', b'isDistanceAvailable', {'retval': {'type': b'Z'}})
    r(b'CMPedometer', b'isFloorCountingAvailable', {'retval': {'type': b'Z'}})
    r(b'CMPedometer', b'isPaceAvailable', {'retval': {'type': b'Z'}})
    r(b'CMPedometer', b'isPedometerEventTrackingAvailable', {'retval': {'type': b'Z'}})
    r(b'CMPedometer', b'isStepCountingAvailable', {'retval': {'type': b'Z'}})
    r(b'CMPedometer', b'queryPedometerDataFromDate:toDate:withHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CMPedometer', b'startPedometerEventUpdatesWithHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CMPedometer', b'startPedometerUpdatesFromDate:withHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CMSensorRecorder', b'isAccelerometerRecordingAvailable', {'retval': {'type': b'Z'}})
    r(b'CMSensorRecorder', b'isAuthorizedForRecording', {'retval': {'type': b'Z'}})
    r(b'CMStepCounter', b'isStepCountingAvailable', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
