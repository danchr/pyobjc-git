# This file is generated by objective.metadata
#
# Last update: Sat Jun  8 17:12:51 2019

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
constants = '''$CWBSSIDDidChangeNotification$CWCountryCodeDidChangeNotification$CWErrorDomain$CWLinkDidChangeNotification$CWLinkQualityDidChangeNotification$CWLinkQualityNotificationRSSIKey$CWLinkQualityNotificationTransmitRateKey$CWModeDidChangeNotification$CWPowerDidChangeNotification$CWSSIDDidChangeNotification$CWScanCacheDidUpdateNotification$CWServiceDidChangeNotification$CoreWLANFrameworkVersionNumber@d$kCWAssocKey8021XProfile$kCWAssocKeyPassphrase$kCWBSSIDDidChangeNotification$kCWCountryCodeDidChangeNotification$kCWErrorDomain$kCWIBSSKeyChannel$kCWIBSSKeyPassphrase$kCWIBSSKeySSID$kCWLinkDidChangeNotification$kCWModeDidChangeNotification$kCWPowerDidChangeNotification$kCWSSIDDidChangeNotification$kCWScanKeyBSSID$kCWScanKeyDwellTime$kCWScanKeyMerge$kCWScanKeyRestTime$kCWScanKeySSID$kCWScanKeyScanType$'''
enums = '''$CWEventTypeBSSIDDidChange@3$CWEventTypeCountryCodeDidChange@4$CWEventTypeLinkDidChange@5$CWEventTypeLinkQualityDidChange@6$CWEventTypeModeDidChange@7$CWEventTypeNone@0$CWEventTypePowerDidChange@1$CWEventTypeRangingReportEvent@10$CWEventTypeSSIDDidChange@2$CWEventTypeScanCacheUpdated@8$CWEventTypeVirtualInterfaceStateChanged@9$CoreWLANFrameworkVersionNumber2_0@200$kCWAPFullErr@-3913$kCWAssociationDeniedErr@-3909$kCWAuthAlgUnsupportedErr@-3910$kCWAuthenticationAlgorithmUnsupportedErr@-3910$kCWChallengeFailureErr@-3912$kCWChannelBand2GHz@1$kCWChannelBand5GHz@2$kCWChannelBandUnknown@0$kCWChannelWidth160MHz@4$kCWChannelWidth20MHz@1$kCWChannelWidth40MHz@2$kCWChannelWidth80MHz@3$kCWChannelWidthUnknown@0$kCWCipherKeyFlagsMulticast@4$kCWCipherKeyFlagsNone@0$kCWCipherKeyFlagsRx@16$kCWCipherKeyFlagsTx@8$kCWCipherKeyFlagsUnicast@2$kCWCipherSuiteRejectedErr@-3923$kCWDSSSOFDMUnsupportedErr@-3916$kCWEAPOLErr@1$kCWErr@-3931$kCWError@-3931$kCWFormatErr@-3904$kCWHTFeaturesNotSupported@-3926$kCWHTFeaturesNotSupportedErr@-3926$kCWIBSSModeSecurityNone@0$kCWIBSSModeSecurityWEP104@2$kCWIBSSModeSecurityWEP40@1$kCWIPCError@-3929$kCWIPCFailureErr@-3929$kCWInterfaceModeHostAP@3$kCWInterfaceModeIBSS@2$kCWInterfaceModeNone@0$kCWInterfaceModeStation@1$kCWInterfaceStateAssociating@3$kCWInterfaceStateAuthenticating@2$kCWInterfaceStateInactive@0$kCWInterfaceStateRunning@4$kCWInterfaceStateScanning@1$kCWInvalidAKMPErr@-3920$kCWInvalidAuthSeqNumErr@-3911$kCWInvalidAuthenticationSequenceNumberErr@-3911$kCWInvalidFormatErr@-3904$kCWInvalidGroupCipherErr@-3918$kCWInvalidInfoElementErr@-3917$kCWInvalidInformationElementErr@-3917$kCWInvalidPMKErr@-3924$kCWInvalidPairwiseCipherErr@-3919$kCWInvalidParameterErr@-3900$kCWInvalidRSNCapabilitiesErr@-3922$kCWKeychainDomainNone@0$kCWKeychainDomainSystem@2$kCWKeychainDomainUser@1$kCWNoErr@0$kCWNoMemErr@-3901$kCWNoMemoryErr@-3901$kCWNotSupportedErr@-3903$kCWOpModeHostAP@2$kCWOpModeIBSS@1$kCWOpModeMonitorMode@3$kCWOpModeStation@0$kCWOpNotPermitted@-3930$kCWOperationNotPermittedErr@-3930$kCWPCOTransitionTimeNotSupported@-3927$kCWPCOTransitionTimeNotSupportedErr@-3927$kCWPHYMode11A@0$kCWPHYMode11B@1$kCWPHYMode11G@2$kCWPHYMode11N@3$kCWPHYMode11a@1$kCWPHYMode11ac@5$kCWPHYMode11b@2$kCWPHYMode11g@3$kCWPHYMode11n@4$kCWPHYModeNone@0$kCWParamErr@-3900$kCWReassociationDeniedErr@-3908$kCWRefNotBoundErr@-3928$kCWReferenceNotBoundErr@-3928$kCWScanTypeActive@0$kCWScanTypeFast@2$kCWScanTypePassive@1$kCWSecurityDynamicWEP@6$kCWSecurityEnterprise@10$kCWSecurityModeDynamicWEP@4$kCWSecurityModeOpen@0$kCWSecurityModeWEP@1$kCWSecurityModeWPA2_Enterprise@6$kCWSecurityModeWPA2_PSK@3$kCWSecurityModeWPA_Enterprise@5$kCWSecurityModeWPA_PSK@2$kCWSecurityModeWPS@7$kCWSecurityNone@0$kCWSecurityPersonal@5$kCWSecurityWEP@1$kCWSecurityWPA2Enterprise@9$kCWSecurityWPA2Personal@4$kCWSecurityWPA3Enterprise@12$kCWSecurityWPA3Personal@11$kCWSecurityWPA3Transition@13$kCWSecurityWPAEnterprise@7$kCWSecurityWPAEnterpriseMixed@8$kCWSecurityWPAPersonal@2$kCWSecurityWPAPersonalMixed@3$kCWShortSlotUnsupportedErr@-3915$kCWSupplicantTimeoutErr@-3925$kCWTimeoutErr@-3905$kCWUknownErr@-3902$kCWUnknownErr@-3902$kCWUnspecifiedFailureErr@-3906$kCWUnsupportedCapabilitiesErr@-3907$kCWUnsupportedRSNVersionErr@-3921$kCWUnsupportedRateSetErr@-3914$'''
misc.update({'kCWSecurityUnknown': sel32or64(2147483647, 9223372036854775807), 'CWEventTypeUnknown': sel32or64(2147483647, 9223372036854775807)})
misc.update({})
functions={'CWKeychainFindWiFiPassword': (sel32or64(b'li@^@', b'iq@^@'), '', {'arguments': {2: {'type_modifier': 'o'}}}), 'CWKeychainSetEAPIdentity': (sel32or64(b'l^{__CFData=}^{OpaqueSecIdentityRef=}', b'i^{__CFData=}^{OpaqueSecIdentityRef=}'),), 'CWKeychainSetEAPUsernameAndPassword': (sel32or64(b'l^{__CFData=}^{__CFString=}^{__CFString=}', b'i^{__CFData=}^{__CFString=}^{__CFString=}'),), 'CWKeychainDeleteWiFiEAPUsernameAndPassword': (sel32or64(b'li@', b'iq@'),), 'CWKeychainDeletePassword': (sel32or64(b'l^{__CFData=}', b'i^{__CFData=}'),), 'CWKeychainCopyEAPIdentityList': (sel32or64(b'l^^{__CFArray=}', b'i^^{__CFArray=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CWKeychainCopyWiFiEAPIdentity': (sel32or64(b'li@^^{OpaqueSecIdentityRef=}', b'iq@^^{OpaqueSecIdentityRef=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CWKeychainSetWiFiEAPUsernameAndPassword': (sel32or64(b'li@@@', b'iq@@@'),), 'CWKeychainFindWiFiEAPUsernameAndPassword': (sel32or64(b'li@^@^@', b'iq@^@^@'), '', {'arguments': {2: {'type_modifier': 'o'}, 3: {'type_modifier': 'o'}}}), 'CWKeychainCopyEAPUsernameAndPassword': (sel32or64(b'l^{__CFData=}^^{__CFString=}^^{__CFString=}', b'i^{__CFData=}^^{__CFString=}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}, 2: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CWKeychainSetPassword': (sel32or64(b'l^{__CFData=}^{__CFString=}', b'i^{__CFData=}^{__CFString=}'),), 'CWKeychainCopyPassword': (sel32or64(b'l^{__CFData=}^^{__CFString=}', b'i^{__CFData=}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CWKeychainDeleteEAPUsernameAndPassword': (sel32or64(b'l^{__CFData=}', b'i^{__CFData=}'),), 'CWKeychainCopyEAPIdentity': (sel32or64(b'l^{__CFData=}^^{OpaqueSecIdentityRef=}', b'i^{__CFData=}^^{OpaqueSecIdentityRef=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CWKeychainDeleteWiFiPassword': (sel32or64(b'li@', b'iq@'),), 'CWMergeNetworks': (b'@@',), 'CWKeychainSetWiFiPassword': (sel32or64(b'li@@', b'iq@@'),), 'CWKeychainSetWiFiEAPIdentity': (sel32or64(b'li@^{OpaqueSecIdentityRef=}', b'iq@^{OpaqueSecIdentityRef=}'),)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'CW8021XProfile', b'alwaysPromptForPassword', {'retval': {'type': b'Z'}})
    r(b'CW8021XProfile', b'isEqualToProfile:', {'retval': {'type': b'Z'}})
    r(b'CW8021XProfile', b'setAlwaysPromptForPassword:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWChannel', b'isEqualToChannel:', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'alwaysRememberNetworks', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'disconnectOnLogout', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'isEqualToConfiguration:', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'rememberJoinedNetworks', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'requireAdminForIBSSCreation', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'requireAdminForNetworkChange', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'requireAdminForPowerChange', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'requireAdministratorForAssociation', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'requireAdministratorForIBSSMode', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'requireAdministratorForPower', {'retval': {'type': b'Z'}})
    r(b'CWConfiguration', b'setAlwaysRememberNetworks:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWConfiguration', b'setDisconnectOnLogout:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWConfiguration', b'setRequireAdminForIBSSCreation:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWConfiguration', b'setRequireAdminForNetworkChange:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWConfiguration', b'setRequireAdminForPowerChange:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWInterface', b'associateToEnterpriseNetwork:identity:username:password:error:', {'retval': {'type': b'Z'}, 'arguments': {6: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'associateToNetwork:parameters:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'associateToNetwork:password:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'commitConfiguration:authorization:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'commitConfiguration:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'deviceAttached', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'enableIBSSWithParameters:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'isEqualToInterface:', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'power', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'powerOn', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'powerSave', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'scanForNetworksWithName:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'scanForNetworksWithName:includeHidden:error:', {'arguments': {3: {'type': 'Z'}, 4: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'scanForNetworksWithParameters:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'scanForNetworksWithSSID:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'scanForNetworksWithSSID:includeHidden:error:', {'arguments': {3: {'type': 'Z'}, 4: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'serviceActive', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'setChannel:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'setPairwiseMasterKey:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'setPower:error:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'Z'}, 3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'setWEPKey:flags:index:error:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'setWLANChannel:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'startIBSSModeWithSSID:security:channel:password:error:', {'retval': {'type': b'Z'}, 'arguments': {6: {'type_modifier': b'o'}}})
    r(b'CWInterface', b'supportsAES_CCM', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsHostAP', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsIBSS', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsMonitorMode', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsPMGT', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsShortGI20MHz', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsShortGI40MHz', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsTKIP', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsTSN', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsWEP', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsWME', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsWPA', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsWPA2', {'retval': {'type': b'Z'}})
    r(b'CWInterface', b'supportsWoW', {'retval': {'type': b'Z'}})
    r(b'CWMutableConfiguration', b'rememberJoinedNetworks', {'retval': {'type': b'Z'}})
    r(b'CWMutableConfiguration', b'requireAdministratorForAssociation', {'retval': {'type': b'Z'}})
    r(b'CWMutableConfiguration', b'requireAdministratorForIBSSMode', {'retval': {'type': b'Z'}})
    r(b'CWMutableConfiguration', b'requireAdministratorForPower', {'retval': {'type': b'Z'}})
    r(b'CWMutableConfiguration', b'setRememberJoinedNetworks:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWMutableConfiguration', b'setRequireAdministratorForAssociation:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWMutableConfiguration', b'setRequireAdministratorForIBSSMode:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWMutableConfiguration', b'setRequireAdministratorForPower:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CWNetwork', b'ibss', {'retval': {'type': b'Z'}})
    r(b'CWNetwork', b'isEqualToNetwork:', {'retval': {'type': b'Z'}})
    r(b'CWNetwork', b'isIBSS', {'retval': {'type': b'Z'}})
    r(b'CWNetwork', b'supportsPHYMode:', {'retval': {'type': b'Z'}})
    r(b'CWNetwork', b'supportsSecurity:', {'retval': {'type': b'Z'}})
    r(b'CWNetworkProfile', b'isEqualToNetworkProfile:', {'retval': {'type': b'Z'}})
    r(b'CWWiFiClient', b'startMonitoringEventWithType:error:', {'retval': {'type': b'Z'}})
    r(b'CWWiFiClient', b'stopMonitoringAllEventsAndReturnError:', {'retval': {'type': b'Z'}})
    r(b'CWWiFiClient', b'stopMonitoringEventWithType:error:', {'retval': {'type': b'Z'}})
    r(b'CWWirelessProfile', b'isEqualToProfile:', {'retval': {'type': b'Z'}})
    r(b'NSObject', b'bssidDidChangeForWiFiInterfaceWithName:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'clientConnectionInterrupted', {'required': False, 'retval': {'type': b'v'}})
    r(b'NSObject', b'clientConnectionInvalidated', {'required': False, 'retval': {'type': b'v'}})
    r(b'NSObject', b'countryCodeDidChangeForWiFiInterfaceWithName:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'linkDidChangeForWiFiInterfaceWithName:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'linkQualityDidChangeForWiFiInterfaceWithName:rssi:transmitRate:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'i', b'q')}, 4: {'type': b'd'}}})
    r(b'NSObject', b'modeDidChangeForWiFiInterfaceWithName:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'powerStateDidChangeForWiFiInterfaceWithName:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'scanCacheUpdatedForWiFiInterfaceWithName:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ssidDidChangeForWiFiInterfaceWithName:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
