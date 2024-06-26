import argparse
import json
from dns_module.dns_functions import dns_lookup
from http_module.http_functions import http_request
from network_module.network_functions import ping, traceroute, port_scan, validate_ssl_cert, check_smtp_relay
from logging_module.logger import logger
from utils.input_validation import validate_domain, validate_ip, validate_url, sanitize_input
from utils.rate_limiter import RateLimiter
from utils.secure_config import SecureConfig

class NetworkDebuggingTool:
    def __init__(self):
        self.parser = self.create_parser()
        self.secure_config = SecureConfig()

    def create_parser(self):
        parser = argparse.ArgumentParser(description="Network Debugging Tool")
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # DNS command
        dns_parser = subparsers.add_parser("dns", help="Perform DNS lookup")
        dns_parser.add_argument("domain", help="Domain to lookup")
        dns_parser.add_argument("--type", default="A", help="DNS record type")

        # HTTP command
        http_parser = subparsers.add_parser("http", help="Send HTTP request")
        http_parser.add_argument("url", help="URL to send request to")
        http_parser.add_argument("--method", default="GET", help="HTTP method")
        http_parser.add_argument("--headers", help="HTTP headers (JSON format)")
        http_parser.add_argument("--data", help="Request body data")
        http_parser.add_argument("--json", help="JSON data to send (JSON format)")

        # Ping command
        ping_parser = subparsers.add_parser("ping", help="Ping a host")
        ping_parser.add_argument("host", help="Host to ping")
        ping_parser.add_argument("--count", type=int, default=4, help="Number of ping requests")

        # Traceroute command
        traceroute_parser = subparsers.add_parser("traceroute", help="Perform traceroute")
        traceroute_parser.add_argument("host", help="Host to traceroute")

        # Port scan command
        portscan_parser = subparsers.add_parser("portscan", help="Scan ports on a host")
        portscan_parser.add_argument("host", help="Host to scan")
        portscan_parser.add_argument("--ports", default="1-1024", help="Port range to scan (e.g., '1-1024' or '80,443,8080')")

        # SSL certificate validation command
        sslcert_parser = subparsers.add_parser("sslcert", help="Validate SSL certificate")
        sslcert_parser.add_argument("hostname", help="Hostname to validate")
        sslcert_parser.add_argument("--port", type=int, default=443, help="Port to use")

        # SMTP relay check command
        smtprelay_parser = subparsers.add_parser("smtprelay", help="Check for open SMTP relay")
        smtprelay_parser.add_argument("host", help="Host to check")
        smtprelay_parser.add_argument("--port", type=int, default=25, help="Port to use")

        return parser

    @RateLimiter(max_calls=100, time_frame=60)  # Limit to 100 calls per minute
    def run(self, args=None):
        args = self.parser.parse_args(args)
        logger.info(f"Running command: {args.command}")

        try:
            if args.command == "dns":
                result = self.run_dns(args)
            elif args.command == "http":
                result = self.run_http(args)
            elif args.command == "ping":
                result = self.run_ping(args)
            elif args.command == "traceroute":
                result = self.run_traceroute(args)
            elif args.command == "portscan":
                result = self.run_portscan(args)
            elif args.command == "sslcert":
                result = self.run_sslcert(args)
            elif args.command == "smtprelay":
                result = self.run_smtp_relay_check(args)
            else:
                logger.warning("No valid command provided")
                self.parser.print_help()
                return

            self.print_result(result)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            print(f"Error: {str(e)}")

    def run_dns(self, args):
        domain = sanitize_input(args.domain)
        if not validate_domain(domain):
            return "Error: Invalid domain name"
        return dns_lookup(domain, args.type)

    def run_http(self, args):
        url = args.url
        if not validate_url(url):
            return "Error: Invalid URL"
        return http_request(url, method=args.method, headers=args.headers, data=args.data, json_data=args.json)

    def run_ping(self, args):
        host = sanitize_input(args.host)
        if not (validate_domain(host) or validate_ip(host)):
            return "Error: Invalid host"
        return ping(host, args.count)

    def run_traceroute(self, args):
        host = sanitize_input(args.host)
        if not (validate_domain(host) or validate_ip(host)):
            return "Error: Invalid host"
        return traceroute(host)

    def run_portscan(self, args):
        host = sanitize_input(args.host)
        if not (validate_domain(host) or validate_ip(host)):
            return "Error: Invalid host"
        ports = self.parse_ports(args.ports)
        return port_scan(host, ports)

    def run_sslcert(self, args):
        hostname = sanitize_input(args.hostname)
        if not validate_domain(hostname):
            return "Error: Invalid hostname"
        return validate_ssl_cert(hostname, args.port)

    def run_smtp_relay_check(self, args):
        host = sanitize_input(args.host)
        if not (validate_domain(host) or validate_ip(host)):
            return "Error: Invalid host"
        return check_smtp_relay(host, args.port)

    def parse_ports(self, ports_str):
        ports = []
        for part in ports_str.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                ports.extend(range(start, end + 1))
            else:
                ports.append(int(part))
        return ports

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