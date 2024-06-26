import unittest
from unittest.mock import patch, mock_open
from scripting_module.script_runner import run_script

class TestScripting(unittest.TestCase):
    @patch('yaml.safe_load')
    @patch('dns_module.dns_functions.dns_lookup')
    @patch('http_module.http_functions.http_request')
    @patch('network_module.network_functions.ping')
    @patch('network_module.network_functions.traceroute')
    def test_run_script(self, mock_traceroute, mock_ping, mock_http, mock_dns, mock_yaml_load):
        mock_yaml_load.return_value = {
            'tasks': [
                {'type': 'dns', 'domain': 'example.com'},
                {'type': 'http', 'url': 'https://api.github.com'},
                {'type': 'ping', 'host': 'google.com'},
                {'type': 'traceroute', 'host': 'cloudflare.com'}
            ]
        }
        mock_dns.return_value = ['192.0.2.1']
        mock_http.return_value = {'status_code': 200}
        mock_ping.return_value = 'Ping successful'
        mock_traceroute.return_value = 'Traceroute successful'

        with patch('builtins.open', mock_open(read_data="dummy data")):
            results = run_script('dummy_script.yaml')

        self.assertEqual(len(results), 4)
        self.assertEqual(results[0]['result'], ['192.0.2.1'])
        self.assertEqual(results[1]['result']['status_code'], 200)
        self.assertEqual(results[2]['result'], 'Ping successful')
        self.assertEqual(results[3]['result'], 'Traceroute successful')

if __name__ == '__main__':
    unittest.main()