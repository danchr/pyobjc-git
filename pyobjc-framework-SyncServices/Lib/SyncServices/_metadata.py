# This file is generated by objective.metadata
#
# Last update: Tue Feb 28 21:05:36 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$ISyncAvailabilityChangedNotification$ISyncChangePropertyActionKey$ISyncChangePropertyClear$ISyncChangePropertyNameKey$ISyncChangePropertySet$ISyncChangePropertyValueIsDefaultKey$ISyncChangePropertyValueKey$ISyncClientTypeApplication$ISyncClientTypeDevice$ISyncClientTypePeer$ISyncClientTypeServer$ISyncErrorDomain$ISyncInvalidArgumentsException$ISyncInvalidEntityException$ISyncInvalidRecordException$ISyncInvalidRecordIdentifiersKey$ISyncInvalidRecordReasonsKey$ISyncInvalidRecordsKey$ISyncInvalidSchemaException$ISyncRecordEntityNameKey$ISyncServerUnavailableException$ISyncSessionCancelledException$ISyncSessionUnavailableException$ISyncUnsupportedEntityException$'''
enums = '''$ISyncChangeTypeAdd@1$ISyncChangeTypeDelete@3$ISyncChangeTypeModify@2$ISyncChangeTypeNone@0$ISyncServerDisabledReasonByPreference@1001$ISyncServerDisabledReasonNone@1000$ISyncServerDisabledReasonSharedNetworkHome@1002$ISyncServerDisabledReasonUnknown@1004$ISyncServerDisabledReasonUnresponsive@1003$ISyncSessionClientAlreadySyncingError@100$ISyncSessionDriverChangeAccepted@1$ISyncSessionDriverChangeError@3$ISyncSessionDriverChangeIgnored@2$ISyncSessionDriverChangeRefused@0$ISyncSessionDriverFatalError@300$ISyncSessionDriverModeFast@1$ISyncSessionDriverModeRefresh@3$ISyncSessionDriverModeSlow@2$ISyncSessionDriverPullFailureError@201$ISyncSessionDriverRegistrationError@200$ISyncSessionUserCanceledSessionError@101$ISyncStatusCancelled@5$ISyncStatusErrors@4$ISyncStatusFailed@6$ISyncStatusNever@7$ISyncStatusRunning@1$ISyncStatusSuccess@2$ISyncStatusWarnings@3$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('ISyncClient', b'canPullChangesForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncClient', b'canPushChangesForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncClient', b'formatsRelationships', {'retval': {'type': 'Z'}})
    r('ISyncClient', b'isEnabledForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncClient', b'setEnabled:forEntityNames:', {'arguments': {2: {'type': 'Z'}}})
    r('ISyncClient', b'setFormatsRelationships:', {'arguments': {2: {'type': 'Z'}}})
    r('ISyncClient', b'setShouldReplaceClientRecords:forEntityNames:', {'arguments': {2: {'type': 'Z'}}})
    r('ISyncClient', b'setShouldSynchronize:withClientsOfType:', {'arguments': {2: {'type': 'Z'}}})
    r('ISyncClient', b'setSyncAlertHandler:selector:', {'arguments': {3: {'sel_of_type': b'v@:@@'}}})
    r('ISyncClient', b'shouldReplaceClientRecordsForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncClient', b'shouldSynchronizeWithClientsOfType:', {'retval': {'type': 'Z'}})
    r('ISyncManager', b'clientWithIdentifier:needsSyncing:', {'arguments': {3: {'type': 'Z'}}})
    r('ISyncManager', b'isEnabled', {'retval': {'type': 'Z'}})
    r('ISyncManager', b'registerSchemaWithBundlePath:', {'retval': {'type': 'Z'}})
    r('ISyncRecordSnapshot', b'recordIdentifierForReference:isModified:', {'arguments': {3: {'type': '^Z', 'type_modifier': b'o'}}})
    r('ISyncSession', b'beginSessionInBackgroundWithClient:entityNames:target:selector:', {'arguments': {5: {'sel_of_type': b'v@:@@'}}})
    r('ISyncSession', b'beginSessionInBackgroundWithClient:entityNames:target:selector:lastAnchors:', {'arguments': {5: {'sel_of_type': b'v@:@@'}}})
    r('ISyncSession', b'clientLostRecordWithIdentifier:shouldReplaceOnNextSync:', {'arguments': {3: {'type': 'Z'}}})
    r('ISyncSession', b'isCancelled', {'retval': {'type': 'Z'}})
    r('ISyncSession', b'prepareToPullChangesForEntityNames:beforeDate:', {'retval': {'type': 'Z'}})
    r('ISyncSession', b'prepareToPullChangesInBackgroundForEntityNames:target:selector:', {'arguments': {4: {'sel_of_type': b'v@:@@'}}})
    r('ISyncSession', b'shouldPullChangesForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncSession', b'shouldPushAllRecordsForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncSession', b'shouldPushChangesForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncSession', b'shouldReplaceAllRecordsOnClientForEntityName:', {'retval': {'type': 'Z'}})
    r('ISyncSessionDriver', b'handlesSyncAlerts', {'retval': {'type': 'Z'}})
    r('ISyncSessionDriver', b'setHandlesSyncAlerts:', {'arguments': {2: {'type': 'Z'}}})
    r('ISyncSessionDriver', b'startAsynchronousSync:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('ISyncSessionDriver', b'sync', {'retval': {'type': 'Z'}})
    r('NSObject', b'changedRecordsForEntityName:moreComing:error:', {'arguments': {3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'changesForEntityName:moreComing:error:', {'arguments': {3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'identifiersForRecordsToDeleteForEntityName:moreComing:error:', {'arguments': {3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didNegotiateAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didPullAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didPushAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didReceiveSyncAlertAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didRegisterClientAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willFinishSessionAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willNegotiateAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willPullAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willPushAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'syncWithClient:inBackground:handler:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type': 'Z'}, 5: {'type': '^@', 'type_modifier': b'o'}}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'applyChange:forEntityName:remappedRecordIdentifier:formattedRecord:error:', {'required': True, 'retval': {'type': 'i'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': '^@', 'type_modifier': b'o'}, 5: {'type': '^@', 'type_modifier': b'o'}, 6: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'changedRecordsForEntityName:moreComing:error:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'changesForEntityName:moreComing:error:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'clientDescriptionURL', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'clientIdentifier', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'deleteAllRecordsForEntityName:error:', {'required': True, 'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'entityNamesToPull', {'required': False, 'retval': {'type': b'@'}})
    r('NSObject', b'entityNamesToSync', {'required': False, 'retval': {'type': b'@'}})
    r('NSObject', b'identifiersForRecordsToDeleteForEntityName:moreComing:error:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'isEqual:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'lastAnchorForEntityName:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'nextAnchorForEntityName:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:didApplyChange:toManagedObject:inSyncSession:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:didCancelSyncSession:error:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:didCommitChanges:inSyncSession:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:didFinishSyncSession:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:didPullChangesInSyncSession:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:didPushChangesInSyncSession:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:willApplyChange:toManagedObject:inSyncSession:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:willDeleteRecordWithIdentifier:inSyncSession:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:willPullChangesInSyncSession:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:willPushChangesInSyncSession:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinator:willPushRecord:forManagedObject:inSyncSession:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}}})
    r('NSObject', b'persistentStoreCoordinatorShouldStartSyncing:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'preferredSyncModeForEntityName:', {'required': True, 'retval': {'type': b'i'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'recordsForEntityName:moreComing:error:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'schemaBundleURLs', {'required': True, 'retval': {'type': b'@'}})
    r('NSObject', b'sessionBeginTimeout', {'required': False, 'retval': {'type': b'd'}})
    r('NSObject', b'sessionPullChangesTimeout', {'required': False, 'retval': {'type': b'd'}})
    r('NSObject', b'shouldApplyRecord:withRecordIdentifier:', {'required': True, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'supportedEntityNames', {'required': True, 'retval': {'type': b'@'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'attributedStringForIdentityPropertiesWithNames:inRecord:comparisonRecords:firstLineAttributes:secondLineAttributes:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}, 6: {'type': b'@'}}})
    r('NSObject', b'attributedStringForPropertiesWithNames:inRecord:comparisonRecords:defaultAttributes:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}}})
    r('NSObject', b'changedRecordsForEntityName:moreComing:error:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'changesForEntityName:moreComing:error:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'entityNamesToPull', {'retval': {'type': b'@'}})
    r('NSObject', b'entityNamesToSync', {'retval': {'type': b'@'}})
    r('NSObject', b'identifiersForRecordsToDeleteForEntityName:moreComing:error:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^Z', 'type_modifier': b'o'}, 4: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'lastAnchorForEntityName:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'nextAnchorForEntityName:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'sessionBeginTimeout', {'retval': {'type': b'd'}})
    r('NSObject', b'sessionDriver:didNegotiateAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didPullAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didPushAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didReceiveSyncAlertAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didRegisterClientAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willFinishSessionAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willNegotiateAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willPullAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willPushAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': '^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriverDidCancelSession:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'sessionDriverDidFinishSession:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'sessionDriverWillCancelSession:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'sessionPullChangesTimeout', {'retval': {'type': b'd'}})
finally:
    objc._updatingMetadata(False)
protocols={'ISyncSessionDriverDelegate': objc.informal_protocol('ISyncSessionDriverDelegate', [objc.selector(None, 'sessionDriver:willPullAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:willPushAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:didRegisterClientAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:willFinishSessionAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:willNegotiateAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:didPullAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriverDidFinishSession:', b'v@:@', isRequired=False), objc.selector(None, 'sessionDriver:didNegotiateAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:didPushAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:didReceiveSyncAlertAndReturnError:', b'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriverWillCancelSession:', b'v@:@', isRequired=False), objc.selector(None, 'sessionDriverDidCancelSession:', b'v@:@', isRequired=False)]), 'ISyncSessionDriverDataSourceOptionalMethods': objc.informal_protocol('ISyncSessionDriverDataSourceOptionalMethods', [objc.selector(None, 'entityNamesToSync', b'@@:', isRequired=False), objc.selector(None, 'sessionPullChangesTimeout', b'd@:', isRequired=False), objc.selector(None, 'sessionBeginTimeout', b'd@:', isRequired=False), objc.selector(None, 'nextAnchorForEntityName:', b'@@:@', isRequired=False), objc.selector(None, 'changesForEntityName:moreComing:error:', b'@@:@^Z^@', isRequired=False), objc.selector(None, 'changedRecordsForEntityName:moreComing:error:', b'@@:@^Z^@', isRequired=False), objc.selector(None, 'identifiersForRecordsToDeleteForEntityName:moreComing:error:', b'@@:@^Z^@', isRequired=False), objc.selector(None, 'entityNamesToPull', b'@@:', isRequired=False), objc.selector(None, 'lastAnchorForEntityName:', b'@@:@', isRequired=False)]), 'SyncUIHelperInformalProtocol': objc.informal_protocol('SyncUIHelperInformalProtocol', [objc.selector(None, 'attributedStringForIdentityPropertiesWithNames:inRecord:comparisonRecords:firstLineAttributes:secondLineAttributes:', b'@@:@@@@@', isRequired=False), objc.selector(None, 'attributedStringForPropertiesWithNames:inRecord:comparisonRecords:defaultAttributes:', b'@@:@@@@', isRequired=False)])}
expressions = {}

# END OF FILE
