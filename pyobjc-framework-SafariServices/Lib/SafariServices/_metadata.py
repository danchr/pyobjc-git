# This file is generated by objective.metadata
#
# Last update: Sun Feb  4 13:44:14 2018

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
constants = '''$$'''
enums = '''$SFErrorLoadingInterrupted@3$SFErrorNoAttachmentFound@2$SFErrorNoExtensionFound@1$SFSafariServicesVersion10_0@0$SFSafariServicesVersion10_1@1$SFSafariServicesVersion11_0@2$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'additionalRequestHeadersForURL:completionHandler', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NSObject', b'validateContextMenuItemWithCommand:inPage:userInfo:validationHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NSObject', b'validateToolbarItemInWindow:validationHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'SFContentBlockerManager', b'getStateOfContentBlockerWithIdentifier:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'SFContentBlockerManager', b'reloadContentBlockerWithIdentifier:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFContentBlockerState', b'isEnabled', {'retval': {'type': 'Z'}})
    r(b'SFContentBlockerState', b'setEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'SFSafariApplication', b'dispatchMessageWithName:toExtensionWithIdentifier:userInfo:completionHandler:', {'arguments': {5: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariApplication', b'getActiveWindowWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariApplication', b'getHostApplicationWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariApplication', b'openWindowWithURL:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariApplication', b'showPreferencesForExtensionWithIdentifier:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariExtensionManager', b'getStateOfSafariExtensionWithIdentifier:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'SFSafariExtensionState', b'isEnabled', {'retval': {'type': 'Z'}})
    r(b'SFSafariPage', b'getPagePropertiesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariPageProperties', b'isActive', {'retval': {'type': 'Z'}})
    r(b'SFSafariPageProperties', b'usesPrivateBrowsing', {'retval': {'type': 'Z'}})
    r(b'SFSafariTab', b'activateWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'SFSafariTab', b'getActivePageWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariTab', b'getPagesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariToolbarItem', b'setEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'SFSafariToolbarItem', b'setEnabled:withBadgeText:', {'arguments': {2: {'type': 'Z'}}})
    r(b'SFSafariWindow', b'getActiveTabWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariWindow', b'getToolbarItemWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'SFSafariWindow', b'openTabWithURL:makeActiveIfPossible:completionHandler:', {'arguments': {3: {'type': 'Z'}, 4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
