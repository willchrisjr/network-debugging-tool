import argparse
import json
from dns_module.dns_functions import dns_lookup
from http_module.http_functions import http_request
from network_module.network_functions import ping, traceroute

class NetworkDebuggingTool:
    def __init__(self):
        self.parser = self.create_parser()

    def create_parser(self):
        parser = argparse.ArgumentParser(
            description="Network Debugging Tool",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  DNS lookup:
    %(prog)s dns example.com
    %(prog)s dns example.com --type MX

  HTTP request:
    %(prog)s http https://api.github.com
    %(prog)s http https://httpbin.org/post --method POST --json '{"key": "value"}'

  Ping:
    %(prog)s ping google.com
    %(prog)s ping google.com --count 8

  Traceroute:
    %(prog)s traceroute google.com
            """
        )
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # DNS lookup command
        dns_parser = subparsers.add_parser("dns", help="Perform DNS lookup")
        dns_parser.add_argument("domain", help="Domain name to lookup")
        dns_parser.add_argument("--type", default="A", help="DNS record type (default: A)")

        # HTTP request command
        http_parser = subparsers.add_parser("http", help="Perform HTTP request")
        http_parser.add_argument("url", help="URL to send request to")
        http_parser.add_argument("--method", default="GET", help="HTTP method (default: GET)")
        http_parser.add_argument("--headers", help="HTTP headers in JSON format")
        http_parser.add_argument("--data", help="Request body data")
        http_parser.add_argument("--json", help="JSON data to send in the request body")

        # Ping command
        ping_parser = subparsers.add_parser("ping", help="Ping a host")
        ping_parser.add_argument("host", help="Host to ping")
        ping_parser.add_argument("--count", type=int, default=4, help="Number of ping requests to send (default: 4)")

        # Traceroute command
        traceroute_parser = subparsers.add_parser("traceroute", help="Perform traceroute to a host")
        traceroute_parser.add_argument("host", help="Host to traceroute")

        return parser

    def run(self, args=None):
        args = self.parser.parse_args(args)

        if args.command == "dns":
            result = dns_lookup(args.domain, args.type)
            self.print_result(result)
        elif args.command == "http":
            headers = json.loads(args.headers) if args.headers else None
            json_data = json.loads(args.json) if args.json else None
            result = http_request(args.url, method=args.method, headers=headers, data=args.data, json_data=json_data)
            self.print_result(result)
        elif args.command == "ping":
            result = ping(args.host, args.count)
            self.print_result(result)
        elif args.command == "traceroute":
            result = traceroute(args.host)
            self.print_result(result)
        else:
            self.parser.print_help()

    def print_result(self, result):
        if isinstance(result, dict):
            print(json.dumps(result, indent=2))
        elif isinstance(result, list):
            for item in result:
                print(item)
        else:
            print(result)

def main():
    tool = NetworkDebuggingTool()
    tool.run()

if __name__ == "__main__":
    main()