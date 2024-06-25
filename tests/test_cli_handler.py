import unittest
from unittest.mock import patch
from io import StringIO
from cli.cli_handler import NetworkDebuggingTool

class TestCLIHandler(unittest.TestCase):

    def setUp(self):
        self.tool = NetworkDebuggingTool()

    @patch('sys.stdout', new_callable=StringIO)
    def test_dns_command(self, mock_stdout):
        with patch('dns_module.dns_functions.dns_lookup', return_value=['192.0.2.1']):
            self.tool.run(['dns', 'example.com'])
        self.assertIn('192.0.2.1', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_http_command(self, mock_stdout):
        mock_response = {'status_code': 200, 'headers': {}, 'content': '{"key": "value"}'}
        with patch('http_module.http_functions.http_request', return_value=mock_response):
            self.tool.run(['http', 'https://api.example.com'])
        self.assertIn('200', mock_stdout.getvalue())
        self.assertIn('key', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_ping_command(self, mock_stdout):
        with patch('network_module.network_functions.ping', return_value='Ping successful'):
            self.tool.run(['ping', 'example.com'])
        self.assertIn('Ping successful', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_traceroute_command(self, mock_stdout):
        with patch('network_module.network_functions.traceroute', return_value='Traceroute successful'):
            self.tool.run(['traceroute', 'example.com'])
        self.assertIn('Traceroute successful', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()