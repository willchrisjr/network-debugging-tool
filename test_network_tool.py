import asyncio
import sys
import time
import argparse
from cli.cli_handler import NetworkDebuggingTool
from utils.async_operations import (
    async_dns_lookup,
    async_http_request,
    async_ping,
    async_traceroute,
    async_port_scan,
    async_validate_ssl_cert,
    async_check_smtp_relay,
    run_concurrent_operations
)

async def run_async_tests():
    print("Running async tests...")
    operations = [
        async_dns_lookup('example.com'),
        async_http_request('https://example.com'),
        async_ping('example.com'),
        async_traceroute('example.com'),
        async_port_scan('example.com', [80, 443]),
        async_validate_ssl_cert('example.com'),
        async_check_smtp_relay('smtp.gmail.com')
    ]
    results = await run_concurrent_operations(operations)
    return results

def run_cli_tests():
    print("Running CLI tests...")
    tool = NetworkDebuggingTool()
    
    tests = [
        ("dns", ["example.com", "--type", "A"]),
        ("http", ["https://example.com"]),
        ("ping", ["example.com", "--count", "2"]),
        ("traceroute", ["example.com"]),
        ("portscan", ["example.com", "--ports", "80,443"]),
        ("sslcert", ["example.com"]),
        ("smtprelay", ["smtp.gmail.com"])
    ]
    
    results = []
    for command, args in tests:
        result = tool.run([command] + args)
        results.append(result)
    
    return results

def run_tests(test_type):
    start_time = time.time()
    if test_type in ['all', 'cli']:
        cli_results = run_cli_tests()
        print_results("CLI", cli_results)
    
    if test_type in ['all', 'async']:
        async_results = asyncio.run(run_async_tests())
        print_results("Async", async_results)
    
    end_time = time.time()
    print(f"Total test time: {end_time - start_time:.2f} seconds")

def print_results(test_type, results):
    print(f"\n{test_type} Test Results:")
    passed = sum(1 for r in results if r is not None and not isinstance(r, Exception))
    failed = len(results) - passed
    
    for i, result in enumerate(results):
        status = "Success" if result is not None and not isinstance(result, Exception) else "Failure"
        print(f"Test {i + 1}: {status}")
        print(result)
        print("-" * 50)
    
    print(f"Summary: {passed} passed, {failed} failed")

def main():
    parser = argparse.ArgumentParser(description="Run Network Debugging Tool tests")
    parser.add_argument("--type", choices=['all', 'cli', 'async'], default='all',
                        help="Type of tests to run (default: all)")
    args = parser.parse_args()

    print(f"Starting Network Debugging Tool tests ({args.type})...")
    run_tests(args.type)
    print("All tests completed.")

if __name__ == "__main__":
    main()