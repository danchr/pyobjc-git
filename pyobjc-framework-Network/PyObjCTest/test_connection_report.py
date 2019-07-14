from PyObjCTools.TestSupport import *
import sys
import objc

if sys.maxsize > 2 ** 32:
    import Network

    nw_establishment_report_access_block_t = b'v@'
    nw_report_resolution_enumerator_t = objc._C_BOOL + b'@QI@@'
    nw_report_protocol_enumerator_t = objc._C_BOOL + b'@QQ'
    nw_data_transfer_report_collect_block_t = b'v@'

    class TestConnectionReport (TestCase):
        def test_constants(self):
            self.assertEqual(Network.nw_report_resolution_source_query, 1)
            self.assertEqual(Network.nw_report_resolution_source_cache, 2)
            self.assertEqual(Network.nw_report_resolution_source_expired_cache, 3)

            self.assertEqual(nw_data_transfer_report_state_collecting, 1)
            self.assertEqual(nw_data_transfer_report_state_collected, 2)

        @min_os_level('10.15')
        def test_contants10_15(self):
            self.assertIsInstance(Network.NW_ALL_PATHS, objc.objc_object)


        @min_os_level('10.15')
        def test_functions10_15(self):
            self.assertArgIsBlock(Network.nw_connection_access_establishment_report, 1, nw_establishment_report_access_block_t)

            Network.nw_establishment_report_get_duration_milliseconds
            Network.nw_establishment_report_get_attempt_started_after_milliseconds
            Network.nw_establishment_report_get_previous_attempt_count
            Network.nw_establishment_report_get_used_proxy
            Network.nw_establishment_report_get_proxy_configured

            self.assertResultIsRetained(Network.nw_establishment_report_copy_proxy_endpoint)

            self.assertArgIsBlock(Network.nw_establishment_report_enumerate_resolutions, 1, nw_report_resolution_enumerator_t)

            self.assertArgIsBlock(Network.nw_establishment_report_enumerate_protocols, 1, nw_report_protocol_enumerator_t)

            self.assertResultIsRetained(Network.nw_data_transfer_report_t)

            Network.nw_data_transfer_report_state_t

            self.assertArgIsBlock(Network.nw_data_transfer_report_collect, 2, nw_data_transfer_report_collect_block_t)

            Network.nw_data_transfer_report_get_duration_milliseconds
            Network.nw_data_transfer_report_get_path_count
            Network.nw_data_transfer_report_get_received_ip_packet_count
            Network.nw_data_transfer_report_get_sent_ip_packet_count
            Network.nw_data_transfer_report_get_received_transport_byte_count
            Network.nw_data_transfer_report_get_received_transport_duplicate_byte_count
            Network.nw_data_transfer_report_get_received_transport_out_of_order_byte_count
            Network.nw_data_transfer_report_get_sent_transport_byte_count
            Network.nw_data_transfer_report_get_sent_transport_retransmitted_byte_count
            Network.nw_data_transfer_report_get_transport_smoothed_rtt_milliseconds
            Network.nw_data_transfer_report_get_transport_minimum_rtt_milliseconds
            Network.nw_data_transfer_report_get_transport_rtt_variance
            Network.nw_data_transfer_report_get_received_application_byte_count
            Network.nw_data_transfer_report_get_sent_application_byte_count

            self.assertResultIsRetained(Network.nw_data_transfer_report_copy_path_interface)


if __name__ == "__main__":
    main()
