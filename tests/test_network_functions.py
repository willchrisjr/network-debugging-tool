import unittest
from unittest.mock import patch
from network_module.network_functions import ping, traceroute

class TestNetworkFunctions(unittest.TestCase):

    @patch('subprocess.check_output')
    def test_ping_success(self, mock_check_output):
        mock_check_output.return_value = b'Ping successful'
        result = ping('example.com')
        self.assertEqual(result, 'Ping successful')

    @patch('subprocess.check_output')
    def test_ping_failure(self, mock_check_output):
        from subprocess import CalledProcessError
        mock_check_output.side_effect = CalledProcessError(1, 'ping')
        result = ping('nonexistent.example.com')
        self.assertTrue(result.startswith("Error: Unable to ping"))

    @patch('subprocess.check_output')
    def test_traceroute_success(self, mock_check_output):
        mock_check_output.return_value = b'Traceroute successful'
        result = traceroute('example.com')
        self.assertEqual(result, 'Traceroute successful')

    @patch('subprocess.check_output')
    def test_traceroute_failure(self, mock_check_output):
        from subprocess import CalledProcessError
        mock_check_output.side_effect = CalledProcessError(1, 'traceroute')
        result = traceroute('nonexistent.example.com')
        self.assertTrue(result.startswith("Error: Unable to perform traceroute"))

if __name__ == '__main__':
    unittest.main()