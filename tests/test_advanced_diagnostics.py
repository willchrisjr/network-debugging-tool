import unittest
from unittest.mock import patch
from network_module.network_functions import port_scan, validate_ssl_cert

class TestAdvancedDiagnostics(unittest.TestCase):
    @patch('socket.socket')
    def test_port_scan(self, mock_socket):
        mock_socket.return_value.connect_ex.side_effect = [0, 1, 0]
        result = port_scan('example.com', [80, 443, 8080])
        self.assertEqual(result, [80, 8080])

    @patch('ssl.get_server_certificate')
    @patch('OpenSSL.crypto.load_certificate')
    def test_validate_ssl_cert(self, mock_load_cert, mock_get_cert):
        mock_get_cert.return_value = 'dummy_cert'
        mock_cert = mock_load_cert.return_value
        mock_cert.get_subject.return_value.get_components.return_value = [(b'CN', b'example.com')]
        mock_cert.get_issuer.return_value.get_components.return_value = [(b'O', b'Let\'s Encrypt')]
        mock_cert.get_version.return_value = 2
        mock_cert.get_serial_number.return_value = 12345
        mock_cert.get_notBefore.return_value = b'20230101000000Z'
        mock_cert.get_notAfter.return_value = b'20240101000000Z'

        result = validate_ssl_cert('example.com')

        self.assertEqual(result['subject'], {b'CN': b'example.com'})
        self.assertEqual(result['issuer'], {b'O': b"Let's Encrypt"})
        self.assertEqual(result['version'], 2)
        self.assertEqual(result['serialNumber'], 12345)
        self.assertEqual(result['notBefore'], '20230101000000Z')
        self.assertEqual(result['notAfter'], '20240101000000Z')

if __name__ == '__main__':
    unittest.main()