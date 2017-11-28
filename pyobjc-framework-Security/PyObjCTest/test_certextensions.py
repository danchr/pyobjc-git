from PyObjCTools.TestSupport import *
import Security
class Testcertextensions (TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, 'GNT_OtherNamed'))
        self.assertFalse(hasattr(Security, 'GNT_RFC822Named'))
        self.assertFalse(hasattr(Security, 'GNT_DNSNamed'))
        self.assertFalse(hasattr(Security, 'GNT_X400Addressd'))
        self.assertFalse(hasattr(Security, 'GNT_DirectoryNamed'))
        self.assertFalse(hasattr(Security, 'GNT_EdiPartyNamed'))
        self.assertFalse(hasattr(Security, 'GNT_URId'))
        self.assertFalse(hasattr(Security, 'GNT_IPAddressd'))
        self.assertFalse(hasattr(Security, 'GNT_RegisteredID'))
        self.assertFalse(hasattr(Security, 'CE_OtherName'))
        self.assertFalse(hasattr(Security, 'CE_GeneralName'))
        self.assertFalse(hasattr(Security, 'CE_GeneralNames'))
        self.assertFalse(hasattr(Security, 'CE_AuthorityKeyID'))
        self.assertFalse(hasattr(Security, 'CE_KU_DigitalSignature'))
        self.assertFalse(hasattr(Security, 'CE_KU_NonRepudiation'))
        self.assertFalse(hasattr(Security, 'CE_KU_KeyEncipherment'))
        self.assertFalse(hasattr(Security, 'CE_KU_DataEncipherment'))
        self.assertFalse(hasattr(Security, 'CE_KU_KeyAgreement'))
        self.assertFalse(hasattr(Security, 'CE_KU_KeyCertSign'))
        self.assertFalse(hasattr(Security, 'CE_KU_CRLSign'))
        self.assertFalse(hasattr(Security, 'CE_KU_EncipherOnly'))
        self.assertFalse(hasattr(Security, 'CE_KU_DecipherOnly'))
        self.assertFalse(hasattr(Security, 'CE_CR_Unspecified'))
        self.assertFalse(hasattr(Security, 'CE_CR_KeyCompromise'))
        self.assertFalse(hasattr(Security, 'CE_CR_CACompromise'))
        self.assertFalse(hasattr(Security, 'CE_CR_AffiliationChanged'))
        self.assertFalse(hasattr(Security, 'CE_CR_Superseded'))
        self.assertFalse(hasattr(Security, 'CE_CR_CessationOfOperation'))
        self.assertFalse(hasattr(Security, 'CE_CR_CertificateHold'))
        self.assertFalse(hasattr(Security, 'CE_CR_RemoveFromCRL'))
        self.assertFalse(hasattr(Security, 'CE_ExtendedKeyUsage'))
        self.assertFalse(hasattr(Security, 'CE_BasicConstraints'))
        self.assertFalse(hasattr(Security, 'SecCEBasicConstraints'))
        self.assertFalse(hasattr(Security, 'CE_PolicyQualifierInfo'))
        self.assertFalse(hasattr(Security, 'CE_PolicyInformation'))
        self.assertFalse(hasattr(Security, 'CE_CertPolicies'))
        self.assertFalse(hasattr(Security, 'CE_CD_Unspecified'))
        self.assertFalse(hasattr(Security, 'CE_CD_KeyCompromise'))
        self.assertFalse(hasattr(Security, 'CE_CD_CACompromise'))
        self.assertFalse(hasattr(Security, 'CE_CD_AffiliationChanged'))
        self.assertFalse(hasattr(Security, 'CE_CD_Superseded'))
        self.assertFalse(hasattr(Security, 'CE_CD_CessationOfOperation'))
        self.assertFalse(hasattr(Security, 'CE_CD_CertificateHold'))
        self.assertFalse(hasattr(Security, 'CE_CDNT_FullNamed'))
        self.assertFalse(hasattr(Security, 'CE_CDNT_NameRelativeToCrlIssuer'))
        self.assertFalse(hasattr(Security, 'CE_DistributionPointName'))
        self.assertFalse(hasattr(Security, 'CE_CRLDistributionPoint'))
        self.assertFalse(hasattr(Security, 'CE_CRLDistPointsSyntax'))
        self.assertFalse(hasattr(Security, 'CE_AccessDescription'))
        self.assertFalse(hasattr(Security, 'CE_AuthorityInfoAccess'))
        self.assertFalse(hasattr(Security, 'CE_SemanticsInformation'))
        self.assertFalse(hasattr(Security, 'CE_QC_Statement'))
        self.assertFalse(hasattr(Security, 'CE_QC_Statements'))
        self.assertFalse(hasattr(Security, 'CE_IssuingDistributionPoint'))
        self.assertFalse(hasattr(Security, 'CE_GeneralSubtree'))
        self.assertFalse(hasattr(Security, 'CE_GeneralSubtrees'))
        self.assertFalse(hasattr(Security, 'CE_NameConstraints'))
        self.assertFalse(hasattr(Security, 'CE_PolicyMapping'))
        self.assertFalse(hasattr(Security, 'CE_PolicyMappings'))
        self.assertFalse(hasattr(Security, 'CE_PolicyConstraints'))
        self.assertFalse(hasattr(Security, 'DT_AuthorityKeyIDd'))
        self.assertFalse(hasattr(Security, 'DT_SubjectKeyIDd'))
        self.assertFalse(hasattr(Security, 'DT_KeyUsaged'))
        self.assertFalse(hasattr(Security, 'DT_SubjectAltNamed'))
        self.assertFalse(hasattr(Security, 'DT_IssuerAltNamed'))
        self.assertFalse(hasattr(Security, 'DT_ExtendedKeyUsaged'))
        self.assertFalse(hasattr(Security, 'DT_BasicConstraintsd'))
        self.assertFalse(hasattr(Security, 'DT_CertPoliciesd'))
        self.assertFalse(hasattr(Security, 'DT_NetscapeCertTyped'))
        self.assertFalse(hasattr(Security, 'DT_CrlNumberd'))
        self.assertFalse(hasattr(Security, 'DT_DeltaCrld'))
        self.assertFalse(hasattr(Security, 'DT_CrlReasond'))
        self.assertFalse(hasattr(Security, 'DT_CrlDistributionPointsd'))
        self.assertFalse(hasattr(Security, 'DT_IssuingDistributionPointd'))
        self.assertFalse(hasattr(Security, 'DT_AuthorityInfoAccessd'))
        self.assertFalse(hasattr(Security, 'DT_Otherd'))
        self.assertFalse(hasattr(Security, 'DT_QC_Statementsd'))
        self.assertFalse(hasattr(Security, 'DT_NameConstraintsd'))
        self.assertFalse(hasattr(Security, 'DT_PolicyMappingsd'))
        self.assertFalse(hasattr(Security, 'DT_PolicyConstraintsd'))
        self.assertFalse(hasattr(Security, 'DT_InhibitAnyPolicy'))
        self.assertFalse(hasattr(Security, 'CE_Data'))
        self.assertFalse(hasattr(Security, 'CE_DataAndType'))

if __name__ == "__main__":
    main()
