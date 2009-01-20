
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABGlobals (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
          self.failUnlessIsInstance(kABCalendarURIsProperty, unicode)

    def testConstants(self):
        self.failUnlessEqual(kABShowAsMask, 07)
        self.failUnlessEqual(kABShowAsPerson, 00)
        self.failUnlessEqual(kABShowAsCompany, 01)
        self.failUnlessEqual(kABNameOrderingMask, 070)
        self.failUnlessEqual(kABDefaultNameOrdering, 0)
        self.failUnlessEqual(kABFirstNameFirst, 040)
        self.failUnlessEqual(kABLastNameFirst, 020)


        self.failUnlessIsInstance(kABUIDProperty, unicode)
        self.failUnlessIsInstance(kABCreationDateProperty, unicode)
        self.failUnlessIsInstance(kABModificationDateProperty, unicode)
        self.failUnlessIsInstance(kABFirstNameProperty, unicode)
        self.failUnlessIsInstance(kABLastNameProperty, unicode)
        self.failUnlessIsInstance(kABFirstNamePhoneticProperty, unicode)
        self.failUnlessIsInstance(kABLastNamePhoneticProperty, unicode)
        self.failUnlessIsInstance(kABNicknameProperty, unicode)
        self.failUnlessIsInstance(kABMaidenNameProperty, unicode)
        self.failUnlessIsInstance(kABBirthdayProperty, unicode)
        self.failUnlessIsInstance(kABOrganizationProperty, unicode)
        self.failUnlessIsInstance(kABJobTitleProperty, unicode)
        self.failUnlessIsInstance(kABHomePageProperty, unicode)
        self.failUnlessIsInstance(kABURLsProperty, unicode)
        self.failUnlessIsInstance(kABHomePageLabel, unicode)
        self.failUnlessIsInstance(kABEmailProperty, unicode)
        self.failUnlessIsInstance(kABEmailWorkLabel, unicode)
        self.failUnlessIsInstance(kABEmailHomeLabel, unicode)
        self.failUnlessIsInstance(kABAddressProperty, unicode)
        self.failUnlessIsInstance(kABAddressStreetKey, unicode)
        self.failUnlessIsInstance(kABAddressCityKey, unicode)
        self.failUnlessIsInstance(kABAddressStateKey, unicode)
        self.failUnlessIsInstance(kABAddressZIPKey, unicode)
        self.failUnlessIsInstance(kABAddressCountryKey, unicode)
        self.failUnlessIsInstance(kABAddressCountryCodeKey, unicode)
        self.failUnlessIsInstance(kABAddressHomeLabel, unicode)
        self.failUnlessIsInstance(kABAddressWorkLabel, unicode)
        self.failUnlessIsInstance(kABOtherDatesProperty, unicode)
        self.failUnlessIsInstance(kABAnniversaryLabel, unicode)
        self.failUnlessIsInstance(kABRelatedNamesProperty, unicode)
        self.failUnlessIsInstance(kABFatherLabel, unicode)
        self.failUnlessIsInstance(kABMotherLabel, unicode)
        self.failUnlessIsInstance(kABParentLabel, unicode)
        self.failUnlessIsInstance(kABBrotherLabel, unicode)
        self.failUnlessIsInstance(kABSisterLabel, unicode)
        self.failUnlessIsInstance(kABChildLabel, unicode)
        self.failUnlessIsInstance(kABFriendLabel, unicode)
        self.failUnlessIsInstance(kABSpouseLabel, unicode)
        self.failUnlessIsInstance(kABPartnerLabel, unicode)
        self.failUnlessIsInstance(kABAssistantLabel, unicode)
        self.failUnlessIsInstance(kABManagerLabel, unicode)
        self.failUnlessIsInstance(kABDepartmentProperty, unicode)
        self.failUnlessIsInstance(kABPersonFlags, unicode)
        self.failUnlessIsInstance(kABPhoneProperty, unicode)
        self.failUnlessIsInstance(kABPhoneWorkLabel, unicode)
        self.failUnlessIsInstance(kABPhoneHomeLabel, unicode)
        self.failUnlessIsInstance(kABPhoneMobileLabel, unicode)
        self.failUnlessIsInstance(kABPhoneMainLabel, unicode)
        self.failUnlessIsInstance(kABPhoneHomeFAXLabel, unicode)
        self.failUnlessIsInstance(kABPhoneWorkFAXLabel, unicode)
        self.failUnlessIsInstance(kABPhonePagerLabel, unicode)
        self.failUnlessIsInstance(kABAIMInstantProperty, unicode)
        self.failUnlessIsInstance(kABAIMWorkLabel, unicode)
        self.failUnlessIsInstance(kABAIMHomeLabel, unicode)
        self.failUnlessIsInstance(kABJabberInstantProperty, unicode)
        self.failUnlessIsInstance(kABJabberWorkLabel, unicode)
        self.failUnlessIsInstance(kABJabberHomeLabel, unicode)
        self.failUnlessIsInstance(kABMSNInstantProperty, unicode)
        self.failUnlessIsInstance(kABMSNWorkLabel, unicode)
        self.failUnlessIsInstance(kABMSNHomeLabel, unicode)
        self.failUnlessIsInstance(kABYahooInstantProperty, unicode)
        self.failUnlessIsInstance(kABYahooWorkLabel, unicode)
        self.failUnlessIsInstance(kABYahooHomeLabel, unicode)
        self.failUnlessIsInstance(kABICQInstantProperty, unicode)
        self.failUnlessIsInstance(kABICQWorkLabel, unicode)
        self.failUnlessIsInstance(kABICQHomeLabel, unicode)
        self.failUnlessIsInstance(kABNoteProperty, unicode)
        self.failUnlessIsInstance(kABMiddleNameProperty, unicode)
        self.failUnlessIsInstance(kABMiddleNamePhoneticProperty, unicode)
        self.failUnlessIsInstance(kABTitleProperty, unicode)
        self.failUnlessIsInstance(kABSuffixProperty, unicode)
        self.failUnlessIsInstance(kABGroupNameProperty, unicode)
        self.failUnlessIsInstance(kABWorkLabel, unicode)
        self.failUnlessIsInstance(kABHomeLabel, unicode)
        self.failUnlessIsInstance(kABOtherLabel, unicode)
        self.failUnlessIsInstance(kABDatabaseChangedNotification, unicode)
        self.failUnlessIsInstance(kABDatabaseChangedExternallyNotification, unicode)
        self.failUnlessIsInstance(kABInsertedRecords, unicode)
        self.failUnlessIsInstance(kABUpdatedRecords, unicode)
        self.failUnlessIsInstance(kABDeletedRecords, unicode)

    def testFunctions(self):
        v = ABLocalizedPropertyOrLabel(kABAssistantLabel)
        self.failUnlessIsInstance(v, unicode)

if __name__ == "__main__":
    main()
