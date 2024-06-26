import asyncio
import aiohttp
from dns_module.dns_functions import dns_lookup
from http_module.http_functions import http_request
from network_module.network_functions import ping, traceroute, port_scan, validate_ssl_cert, check_smtp_relay
from logging_module.logger import logger

async def async_dns_lookup(domain, record_type='A'):
    return await asyncio.to_thread(dns_lookup, domain, record_type)

async def async_http_request(url, method='GET', headers=None, data=None, json_data=None):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, headers=headers, data=data, json=json_data) as response:
            return {
                'status_code': response.status,
                'headers': dict(response.headers),
                'content': await response.text()
            }

async def async_ping(host, count=4):
    return await asyncio.to_thread(ping, host, count)

async def async_traceroute(host):
    return await asyncio.to_thread(traceroute, host)

async def async_port_scan(host, ports):
    return await asyncio.to_thread(port_scan, host, ports)

async def async_validate_ssl_cert(hostname, port=443):
    return await asyncio.to_thread(validate_ssl_cert, hostname, port)

async def async_check_smtp_relay(host, port=25):
    return await asyncio.to_thread(check_smtp_relay, host, port)

async def run_concurrent_operations(operations):
    tasks = [asyncio.create_task(op) for op in operations]
    return await asyncio.gather(*tasks)

# Usage example:
# async def main():
#     operations = [
#         async_dns_lookup('example.com'),
#         async_http_request('https://example.com'),
#         async_ping('example.com'),
#         async_traceroute('example.com'),
#         async_port_scan('example.com', [80, 443]),
#         async_validate_ssl_cert('example.com'),
#         async_check_smtp_relay('example.com')
#     ]
#     results = await run_concurrent_operations(operations)
#     for result in results:
#         print(result)
#
# asyncio.run(main())