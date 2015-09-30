from PyObjCTools.TestSupport import *
from QTKit import *

try:
    unicode
except NameError:
    unicode = str

class TestQTExportOptions (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(QTExportOptionsAppleM4VCellular, unicode)
        self.assertIsInstance(QTExportOptionsAppleM4V480pSD, unicode)
        self.assertIsInstance(QTExportOptionsAppleM4ViPod, unicode)
        self.assertIsInstance(QTExportOptionsAppleM4VAppleTV, unicode)
        self.assertIsInstance(QTExportOptionsAppleM4VWiFi, unicode)
        self.assertIsInstance(QTExportOptionsAppleM4V720pHD, unicode)
        self.assertIsInstance(QTExportOptionsQuickTimeMovie480p, unicode)
        self.assertIsInstance(QTExportOptionsQuickTimeMovie720p, unicode)
        self.assertIsInstance(QTExportOptionsQuickTimeMovie1080p, unicode)
        self.assertIsInstance(QTExportOptionsAppleM4A, unicode)

if __name__ == "__main__":
    main()