import unittest
from unittest.mock import patch
from dns_module.dns_functions import dns_lookup

class TestDNSFunctions(unittest.TestCase):

    @patch('dns.resolver.resolve')
    def test_dns_lookup_success(self, mock_resolve):
        mock_resolve.return_value = ['192.0.2.1']
        result = dns_lookup('example.com', 'A')
        self.assertEqual(result, ['192.0.2.1'])

    @patch('dns.resolver.resolve')
    def test_dns_lookup_nxdomain(self, mock_resolve):
        from dns.resolver import NXDOMAIN
        mock_resolve.side_effect = NXDOMAIN()
        result = dns_lookup('nonexistent.example.com', 'A')
        self.assertTrue(result.startswith("Error: Domain nonexistent.example.com does not exist"))

    @patch('dns.resolver.resolve')
    def test_dns_lookup_no_answer(self, mock_resolve):
        from dns.resolver import NoAnswer
        mock_resolve.side_effect = NoAnswer()
        result = dns_lookup('example.com', 'AAAA')
        self.assertTrue(result.startswith("Error: No AAAA record found for example.com"))

if __name__ == '__main__':
    unittest.main()