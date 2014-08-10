import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    MKLocalSearchCompletionHandler = b"v@@"

    class TestMKLocalSearch (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKLocalSearch, objc.objc_class)

            self.assertArgIsBlock(MapKit.MKLocationSearch.startWithCompletionHandler_, 0, MKLocalSearchCompletionHandler)
            self.assertResultIsBOOL(MapKit.MKLocationSearch.isSearching)

if __name__ == "__main__":
    main()
