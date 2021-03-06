from PyObjCTools.TestSupport import *

import CoreServices


class TestDiskSpaceRecovery(TestCase):
    @min_os_level("10.7")
    def test_functions(self):
        self.assertArgIsOut(CoreServices.CSDiskSpaceStartRecovery, 3)
        self.assertArgIsBlock(CoreServices.CSDiskSpaceStartRecovery, 5, b"vZQ@")

        self.assertArgHasType(
            CoreServices.CSDiskSpaceCancelRecovery, 0, b"^{__CFUUID=}"
        )

        self.assertResultHasType(
            CoreServices.CSDiskSpaceGetRecoveryEstimate, objc._C_ULNG_LNG
        )


if __name__ == "__main__":
    main()
