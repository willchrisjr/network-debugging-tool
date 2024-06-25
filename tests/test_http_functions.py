import unittest
from unittest.mock import patch, Mock
from http_module.http_functions import http_request

class TestHTTPFunctions(unittest.TestCase):

    @patch('requests.request')
    def test_http_request_success(self, mock_request):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.return_value = {'key': 'value'}
        mock_request.return_value = mock_response

        result = http_request('https://api.example.com')
        self.assertEqual(result['status_code'], 200)
        self.assertEqual(result['headers'], {'Content-Type': 'application/json'})
        self.assertIn('key', result['content'])

    @patch('requests.request')
    def test_http_request_error(self, mock_request):
        from requests.exceptions import RequestException
        mock_request.side_effect = RequestException('An error occurred')

        result = http_request('https://api.example.com')
        self.assertTrue(result.startswith("Error: An error occurred"))

if __name__ == '__main__':
    unittest.main()