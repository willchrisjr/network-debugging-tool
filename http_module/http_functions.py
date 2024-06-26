import requests
import json
from logging_module.logger import logger
from utils.rate_limiter import RateLimiter

@RateLimiter(max_calls=30, time_frame=60)  # Limit to 30 HTTP requests per minute
def http_request(url, method='GET', headers=None, data=None, json_data=None):
    logger.info(f"Performing HTTP {method} request to {url}")
    try:
        response = requests.request(method, url, headers=headers, data=data, json=json_data, timeout=10)
        response.raise_for_status()
        
        try:
            content = response.json()
            content = json.dumps(content, indent=2)
        except json.JSONDecodeError:
            content = response.text[:500]

        result = {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': content
        }
        logger.debug(f"HTTP request result: {result}")
        return result
    except requests.RequestException as e:
        logger.error(f"HTTP request failed: {str(e)}")
        return f"Error: HTTP request failed: {str(e)}"