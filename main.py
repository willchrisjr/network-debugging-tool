import argparse
from dns_module.dns_functions import dns_lookup
from http_module.http_functions import http_request
from network_module.network_functions import ping, traceroute

def main():
    parser = argparse.ArgumentParser(description="Network Debugging Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # DNS lookup command
    dns_parser = subparsers.add_parser("dns", help="Perform DNS lookup")
    dns_parser.add_argument("domain", help="Domain name to lookup")
    dns_parser.add_argument("--type", default="A", help="DNS record type (default: A)")

    # HTTP request command
    http_parser = subparsers.add_parser("http", help="Perform HTTP request")
    http_parser.add_argument("url", help="URL to send request to")
    http_parser.add_argument("--method", default="GET", help="HTTP method (default: GET)")

    # Ping command
    ping_parser = subparsers.add_parser("ping", help="Ping a host")
    ping_parser.add_argument("host", help="Host to ping")
    ping_parser.add_argument("--count", type=int, default=4, help="Number of ping requests to send (default: 4)")

    # Traceroute command
    traceroute_parser = subparsers.add_parser("traceroute", help="Perform traceroute to a host")
    traceroute_parser.add_argument("host", help="Host to traceroute")

    args = parser.parse_args()

    if args.command == "dns":
        result = dns_lookup(args.domain, args.type)
        print(result)
    elif args.command == "http":
        result = http_request(args.url, method=args.method)
        print(result)
    elif args.command == "ping":
        result = ping(args.host, args.count)
        print(result)
    elif args.command == "traceroute":
        result = traceroute(args.host)
        print(result)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()