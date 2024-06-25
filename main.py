import argparse
from dns_module.dns_functions import dns_lookup

def main():
    parser = argparse.ArgumentParser(description="Network Debugging Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # DNS lookup command
    dns_parser = subparsers.add_parser("dns", help="Perform DNS lookup")
    dns_parser.add_argument("domain", help="Domain name to lookup")
    dns_parser.add_argument("--type", default="A", help="DNS record type (default: A)")

    args = parser.parse_args()

    if args.command == "dns":
        result = dns_lookup(args.domain, args.type)
        print(result)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()