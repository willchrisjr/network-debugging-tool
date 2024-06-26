import unittest
from unittest.mock import patch
from dns_module.dns_functions import dns_lookup
from network_module.network_functions import ping, traceroute

class TestIPv6(unittest.TestCase):
    @patch('dns.resolver.resolve')
    def test_dns_lookup_ipv6(self, mock_resolve):
        mock_resolve.return_value = ['2001:db8::1']
        result = dns_lookup('example.com', 'AAAA')
        self.assertIn('2001:db8::1', result)

    @patch('subprocess.check_output')
    def test_ping_ipv6(self, mock_check_output):
        mock_check_output.return_value = b'Ping successful'
        result = ping('2001:db8::1')
        self.assertEqual(result, 'Ping successful')

    @patch('subprocess.check_output')
    def test_traceroute_ipv6(self, mock_check_output):
        mock_check_output.return_value = b'Traceroute successful'
        result = traceroute('2001:db8::1')
        self.assertEqual(result, 'Traceroute successful')

if __name__ == '__main__':
    unittest.main()