# This file is generated by objective.metadata
#
# Last update: Sun Jul 28 15:48:09 2019

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
constants = '''$ASAuthorizationAppleIDProviderCredentialRevokedNotification$ASAuthorizationErrorDomain$ASAuthorizationOperationImplicit$ASAuthorizationOperationLogin$ASAuthorizationOperationLogout$ASAuthorizationOperationRefresh$ASAuthorizationScopeEmail$ASAuthorizationScopeFullName$ASCredentialIdentityStoreErrorDomain$ASExtensionErrorDomain$ASWebAuthenticationSessionErrorDomain$'''
enums = '''$ASAuthorizationAppleIDButtonStyleBlack@2$ASAuthorizationAppleIDButtonStyleWhite@0$ASAuthorizationAppleIDButtonStyleWhiteOutline@1$ASAuthorizationAppleIDButtonTypeContinue@1$ASAuthorizationAppleIDButtonTypeDefault@0$ASAuthorizationAppleIDButtonTypeSignIn@0$ASAuthorizationAppleIDProviderCredentialAuthorized@1$ASAuthorizationAppleIDProviderCredentialNotFound@2$ASAuthorizationAppleIDProviderCredentialRevoked@0$ASAuthorizationErrorCanceled@1001$ASAuthorizationErrorFailed@1004$ASAuthorizationErrorInvalidResponse@1002$ASAuthorizationErrorNotHandled@1003$ASAuthorizationErrorUnknown@1000$ASCredentialIdentityStoreErrorCodeInternalError@0$ASCredentialIdentityStoreErrorCodeStoreBusy@2$ASCredentialIdentityStoreErrorCodeStoreDisabled@1$ASCredentialServiceIdentifierTypeDomain@0$ASCredentialServiceIdentifierTypeURL@1$ASExtensionErrorCodeCredentialIdentityNotFound@101$ASExtensionErrorCodeFailed@0$ASExtensionErrorCodeUserCanceled@1$ASExtensionErrorCodeUserInteractionRequired@100$ASUserDetectionStatusLikelyReal@2$ASUserDetectionStatusUnknown@1$ASUserDetectionStatusUnsupported@0$ASWebAuthenticationSessionErrorCodeCanceledLogin@1$ASWebAuthenticationSessionErrorCodePresentationContextInvalid@3$ASWebAuthenticationSessionErrorCodePresentationContextNotProvided@2$'''
misc.update({})
aliases = {'ASAuthorizationAppleIDButtonTypeDefault': 'ASAuthorizationAppleIDButtonTypeSignIn'}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'ASAuthorizationSingleSignOnProvider', b'canPerformAuthorization', {'retval': {'type': b'Z'}})
    r(b'ASCredentialIdentityStoreState', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'ASCredentialIdentityStoreState', b'supportsIncrementalUpdates', {'retval': {'type': b'Z'}})
    r(b'ASWebAuthenticationSession', b'prefersEphemeralWebBrowserSession', {'retval': {'type': b'Z'}})
    r(b'ASWebAuthenticationSession', b'setPrefersEphemeralWebBrowserSession:', {'arguments': {2: {'type': b'Z'}}})
    r(b'ASWebAuthenticationSession', b'start', {'retval': {'type': b'Z'}})
    r(b'ASWebAuthenticationSessionRequest', b'shouldUseEphemeralSession', {'retval': {'type': b'Z'}})
    r(b'ASWebAuthenticationSessionWebBrowserSessionManager', b'wasLaunchedByAuthenticationServices', {'retval': {'type': b'Z'}})
    r(b'NSObject', b'authenticationSessionRequest:didCancelWithError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'authenticationSessionRequest:didCompleteWithCallbackURL:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'authorizationController:didCompleteWithAuthorization:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'authorizationController:didCompleteWithError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'beginAuthorizationWithRequest:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'beginHandlingWebAuthenticationSessionRequest:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'cancelAuthorizationWithRequest:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'cancelWebAuthenticationSessionRequest:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'presentationAnchorForAuthorizationController:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'presentationAnchorForWebAuthenticationSession:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
