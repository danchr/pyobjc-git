from PyObjCTools.TestSupport import *

import Security

class TestCipherSuite (TestCase):

    def test_constants(self):
        self.assertEqual(Security.SSL_NULL_WITH_NULL_NULL, 0x0000)
        self.assertEqual(Security.SSL_RSA_WITH_NULL_MD5, 0x0001)
        self.assertEqual(Security.SSL_RSA_WITH_NULL_SHA, 0x0002)
        self.assertEqual(Security.SSL_RSA_EXPORT_WITH_RC4_40_MD5, 0x0003)
        self.assertEqual(Security.SSL_RSA_WITH_RC4_128_MD5, 0x0004)
        self.assertEqual(Security.SSL_RSA_WITH_RC4_128_SHA, 0x0005)
        self.assertEqual(Security.SSL_RSA_EXPORT_WITH_RC2_CBC_40_MD5, 0x0006)
        self.assertEqual(Security.SSL_RSA_WITH_IDEA_CBC_SHA, 0x0007)
        self.assertEqual(Security.SSL_RSA_EXPORT_WITH_DES40_CBC_SHA, 0x0008)
        self.assertEqual(Security.SSL_RSA_WITH_DES_CBC_SHA, 0x0009)
        self.assertEqual(Security.SSL_RSA_WITH_3DES_EDE_CBC_SHA, 0x000A)
        self.assertEqual(Security.SSL_DH_DSS_EXPORT_WITH_DES40_CBC_SHA, 0x000B)
        self.assertEqual(Security.SSL_DH_DSS_WITH_DES_CBC_SHA, 0x000C)
        self.assertEqual(Security.SSL_DH_DSS_WITH_3DES_EDE_CBC_SHA, 0x000D)
        self.assertEqual(Security.SSL_DH_RSA_EXPORT_WITH_DES40_CBC_SHA, 0x000E)
        self.assertEqual(Security.SSL_DH_RSA_WITH_DES_CBC_SHA, 0x000F)
        self.assertEqual(Security.SSL_DH_RSA_WITH_3DES_EDE_CBC_SHA, 0x0010)
        self.assertEqual(Security.SSL_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA, 0x0011)
        self.assertEqual(Security.SSL_DHE_DSS_WITH_DES_CBC_SHA, 0x0012)
        self.assertEqual(Security.SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA, 0x0013)
        self.assertEqual(Security.SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA, 0x0014)
        self.assertEqual(Security.SSL_DHE_RSA_WITH_DES_CBC_SHA, 0x0015)
        self.assertEqual(Security.SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA, 0x0016)
        self.assertEqual(Security.SSL_DH_anon_EXPORT_WITH_RC4_40_MD5, 0x0017)
        self.assertEqual(Security.SSL_DH_anon_WITH_RC4_128_MD5, 0x0018)
        self.assertEqual(Security.SSL_DH_anon_EXPORT_WITH_DES40_CBC_SHA, 0x0019)
        self.assertEqual(Security.SSL_DH_anon_WITH_DES_CBC_SHA, 0x001A)
        self.assertEqual(Security.SSL_DH_anon_WITH_3DES_EDE_CBC_SHA, 0x001B)
        self.assertEqual(Security.SSL_FORTEZZA_DMS_WITH_NULL_SHA, 0x001C)
        self.assertEqual(Security.SSL_FORTEZZA_DMS_WITH_FORTEZZA_CBC_SHA, 0x001D)
        self.assertEqual(Security.TLS_RSA_WITH_AES_128_CBC_SHA, 0x002F)
        self.assertEqual(Security.TLS_DH_DSS_WITH_AES_128_CBC_SHA, 0x0030)
        self.assertEqual(Security.TLS_DH_RSA_WITH_AES_128_CBC_SHA, 0x0031)
        self.assertEqual(Security.TLS_DHE_DSS_WITH_AES_128_CBC_SHA, 0x0032)
        self.assertEqual(Security.TLS_DHE_RSA_WITH_AES_128_CBC_SHA, 0x0033)
        self.assertEqual(Security.TLS_DH_anon_WITH_AES_128_CBC_SHA, 0x0034)
        self.assertEqual(Security.TLS_RSA_WITH_AES_256_CBC_SHA, 0x0035)
        self.assertEqual(Security.TLS_DH_DSS_WITH_AES_256_CBC_SHA, 0x0036)
        self.assertEqual(Security.TLS_DH_RSA_WITH_AES_256_CBC_SHA, 0x0037)
        self.assertEqual(Security.TLS_DHE_DSS_WITH_AES_256_CBC_SHA, 0x0038)
        self.assertEqual(Security.TLS_DHE_RSA_WITH_AES_256_CBC_SHA, 0x0039)
        self.assertEqual(Security.TLS_DH_anon_WITH_AES_256_CBC_SHA, 0x003A)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_NULL_SHA, 0xC001)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_RC4_128_SHA, 0xC002)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA, 0xC003)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, 0xC004)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA, 0xC005)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_NULL_SHA, 0xC006)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, 0xC007)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, 0xC008)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, 0xC009)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, 0xC00A)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_NULL_SHA, 0xC00B)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_RC4_128_SHA, 0xC00C)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA, 0xC00D)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, 0xC00E)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_AES_256_CBC_SHA, 0xC00F)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_NULL_SHA, 0xC010)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_RC4_128_SHA, 0xC011)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, 0xC012)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, 0xC013)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, 0xC014)
        self.assertEqual(Security.TLS_ECDH_anon_WITH_NULL_SHA, 0xC015)
        self.assertEqual(Security.TLS_ECDH_anon_WITH_RC4_128_SHA, 0xC016)
        self.assertEqual(Security.TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA, 0xC017)
        self.assertEqual(Security.TLS_ECDH_anon_WITH_AES_128_CBC_SHA, 0xC018)
        self.assertEqual(Security.TLS_ECDH_anon_WITH_AES_256_CBC_SHA, 0xC019)
        self.assertEqual(Security.TLS_NULL_WITH_NULL_NULL, 0x0000)
        self.assertEqual(Security.TLS_RSA_WITH_NULL_MD5, 0x0001)
        self.assertEqual(Security.TLS_RSA_WITH_NULL_SHA, 0x0002)
        self.assertEqual(Security.TLS_RSA_WITH_RC4_128_MD5, 0x0004)
        self.assertEqual(Security.TLS_RSA_WITH_RC4_128_SHA, 0x0005)
        self.assertEqual(Security.TLS_RSA_WITH_3DES_EDE_CBC_SHA, 0x000A)
        self.assertEqual(Security.TLS_RSA_WITH_NULL_SHA256, 0x003B)
        self.assertEqual(Security.TLS_RSA_WITH_AES_128_CBC_SHA256, 0x003C)
        self.assertEqual(Security.TLS_RSA_WITH_AES_256_CBC_SHA256, 0x003D)
        self.assertEqual(Security.TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA, 0x000D)
        self.assertEqual(Security.TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA, 0x0010)
        self.assertEqual(Security.TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA, 0x0013)
        self.assertEqual(Security.TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, 0x0016)
        self.assertEqual(Security.TLS_DH_DSS_WITH_AES_128_CBC_SHA256, 0x003E)
        self.assertEqual(Security.TLS_DH_RSA_WITH_AES_128_CBC_SHA256, 0x003F)
        self.assertEqual(Security.TLS_DHE_DSS_WITH_AES_128_CBC_SHA256, 0x0040)
        self.assertEqual(Security.TLS_DHE_RSA_WITH_AES_128_CBC_SHA256, 0x0067)
        self.assertEqual(Security.TLS_DH_DSS_WITH_AES_256_CBC_SHA256, 0x0068)
        self.assertEqual(Security.TLS_DH_RSA_WITH_AES_256_CBC_SHA256, 0x0069)
        self.assertEqual(Security.TLS_DHE_DSS_WITH_AES_256_CBC_SHA256, 0x006A)
        self.assertEqual(Security.TLS_DHE_RSA_WITH_AES_256_CBC_SHA256, 0x006B)
        self.assertEqual(Security.TLS_DH_anon_WITH_RC4_128_MD5, 0x0018)
        self.assertEqual(Security.TLS_DH_anon_WITH_3DES_EDE_CBC_SHA, 0x001B)
        self.assertEqual(Security.TLS_DH_anon_WITH_AES_128_CBC_SHA256, 0x006C)
        self.assertEqual(Security.TLS_DH_anon_WITH_AES_256_CBC_SHA256, 0x006D)
        self.assertEqual(Security.TLS_PSK_WITH_RC4_128_SHA, 0x008A)
        self.assertEqual(Security.TLS_PSK_WITH_3DES_EDE_CBC_SHA, 0x008B)
        self.assertEqual(Security.TLS_PSK_WITH_AES_128_CBC_SHA, 0x008C)
        self.assertEqual(Security.TLS_PSK_WITH_AES_256_CBC_SHA, 0x008D)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_RC4_128_SHA, 0x008E)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA, 0x008F)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_AES_128_CBC_SHA, 0x0090)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_AES_256_CBC_SHA, 0x0091)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_RC4_128_SHA, 0x0092)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA, 0x0093)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_AES_128_CBC_SHA, 0x0094)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_AES_256_CBC_SHA, 0x0095)
        self.assertEqual(Security.TLS_PSK_WITH_NULL_SHA, 0x002C)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_NULL_SHA, 0x002D)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_NULL_SHA, 0x002E)
        self.assertEqual(Security.TLS_RSA_WITH_AES_128_GCM_SHA256, 0x009C)
        self.assertEqual(Security.TLS_RSA_WITH_AES_256_GCM_SHA384, 0x009D)
        self.assertEqual(Security.TLS_DHE_RSA_WITH_AES_128_GCM_SHA256, 0x009E)
        self.assertEqual(Security.TLS_DHE_RSA_WITH_AES_256_GCM_SHA384, 0x009F)
        self.assertEqual(Security.TLS_DH_RSA_WITH_AES_128_GCM_SHA256, 0x00A0)
        self.assertEqual(Security.TLS_DH_RSA_WITH_AES_256_GCM_SHA384, 0x00A1)
        self.assertEqual(Security.TLS_DHE_DSS_WITH_AES_128_GCM_SHA256, 0x00A2)
        self.assertEqual(Security.TLS_DHE_DSS_WITH_AES_256_GCM_SHA384, 0x00A3)
        self.assertEqual(Security.TLS_DH_DSS_WITH_AES_128_GCM_SHA256, 0x00A4)
        self.assertEqual(Security.TLS_DH_DSS_WITH_AES_256_GCM_SHA384, 0x00A5)
        self.assertEqual(Security.TLS_DH_anon_WITH_AES_128_GCM_SHA256, 0x00A6)
        self.assertEqual(Security.TLS_DH_anon_WITH_AES_256_GCM_SHA384, 0x00A7)
        self.assertEqual(Security.TLS_PSK_WITH_AES_128_GCM_SHA256, 0x00A8)
        self.assertEqual(Security.TLS_PSK_WITH_AES_256_GCM_SHA384, 0x00A9)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_AES_128_GCM_SHA256, 0x00AA)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_AES_256_GCM_SHA384, 0x00AB)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_AES_128_GCM_SHA256, 0x00AC)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_AES_256_GCM_SHA384, 0x00AD)
        self.assertEqual(Security.TLS_PSK_WITH_AES_128_CBC_SHA256, 0x00AE)
        self.assertEqual(Security.TLS_PSK_WITH_AES_256_CBC_SHA384, 0x00AF)
        self.assertEqual(Security.TLS_PSK_WITH_NULL_SHA256, 0x00B0)
        self.assertEqual(Security.TLS_PSK_WITH_NULL_SHA384, 0x00B1)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_AES_128_CBC_SHA256, 0x00B2)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_AES_256_CBC_SHA384, 0x00B3)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_NULL_SHA256, 0x00B4)
        self.assertEqual(Security.TLS_DHE_PSK_WITH_NULL_SHA384, 0x00B5)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_AES_128_CBC_SHA256, 0x00B6)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_AES_256_CBC_SHA384, 0x00B7)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_NULL_SHA256, 0x00B8)
        self.assertEqual(Security.TLS_RSA_PSK_WITH_NULL_SHA384, 0x00B9)
        self.assertEqual(Security.TLS_AES_128_GCM_SHA256, 0x1301)
        self.assertEqual(Security.TLS_AES_256_GCM_SHA384, 0x1302)
        self.assertEqual(Security.TLS_CHACHA20_POLY1305_SHA256, 0x1303)
        self.assertEqual(Security.TLS_AES_128_CCM_SHA256, 0x1304)
        self.assertEqual(Security.TLS_AES_128_CCM_8_SHA256, 0x1305)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, 0xC023)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384, 0xC024)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256, 0xC025)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384, 0xC026)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, 0xC027)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, 0xC028)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256, 0xC029)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384, 0xC02A)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, 0xC02B)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, 0xC02C)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256, 0xC02D)
        self.assertEqual(Security.TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384, 0xC02E)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, 0xC02F)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, 0xC030)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256, 0xC031)
        self.assertEqual(Security.TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384, 0xC032)
        self.assertEqual(Security.TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256, 0xCCA8)
        self.assertEqual(Security.TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256, 0xCCA9)
        self.assertEqual(Security.TLS_EMPTY_RENEGOTIATION_INFO_SCSV, 0x00FF)
        self.assertEqual(Security.SSL_RSA_WITH_RC2_CBC_MD5, 0xFF80)
        self.assertEqual(Security.SSL_RSA_WITH_IDEA_CBC_MD5, 0xFF81)
        self.assertEqual(Security.SSL_RSA_WITH_DES_CBC_MD5, 0xFF82)
        self.assertEqual(Security.SSL_RSA_WITH_3DES_EDE_CBC_MD5, 0xFF83)
        self.assertEqual(Security.SSL_NO_SUCH_CIPHERSUITE, 0xFFFF)

if __name__ == "__main__":
    main()
