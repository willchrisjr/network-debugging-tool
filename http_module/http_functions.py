import requests

def http_request(url, method='GET', headers=None, data=None):
    try:
        response = requests.request(method, url, headers=headers, data=data)
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text[:200]  # First 200 characters of content
        }
    except requests.RequestException as e:
        return f"Error: {str(e)}"