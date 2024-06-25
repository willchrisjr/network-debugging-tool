import requests
import json

def http_request(url, method='GET', headers=None, data=None, json_data=None):
    try:
        # Convert data to JSON if it's a dictionary
        if isinstance(data, dict):
            data = json.dumps(data)
            headers = headers or {}
            headers['Content-Type'] = 'application/json'

        response = requests.request(method, url, headers=headers, data=data, json=json_data)
        
        # Try to parse JSON response
        try:
            content = response.json()
            content = json.dumps(content, indent=2)  # Pretty print JSON
        except json.JSONDecodeError:
            content = response.text[:500]  # First 500 characters if not JSON

        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': content
        }
    except requests.RequestException as e:
        return f"Error: {str(e)}"