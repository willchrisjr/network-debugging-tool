# Network Debugging Tool

## Overview

The Network Debugging Tool is a comprehensive command-line utility that combines my previous projects domains using a DNS server, HTTP server, and Shell functionalities to provide a robust set of network diagnostic and testing capabilities. This tool is designed for network administrators, developers, and IT professionals who need a versatile, all-in-one solution for network troubleshooting and analysis.

## Features

- **DNS Lookup**: Perform DNS queries for various record types (A, AAAA, MX, TXT, etc.)
- **HTTP Request Testing**: Send HTTP requests with customizable methods, headers, and body
- **Network Diagnostics**: Run ping, traceroute, and port scans
- **Command-Line Interface**: User-friendly CLI for easy interaction
- **Extensible Architecture**: Modular design for easy addition of new features

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Steps

1. Clone the repository:

git clone https://github.com/yourusername/network-debugging-tool.git
cd network-debugging-tool


2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


3. Install the required dependencies:
pip install -r requirements.txt


4. Run the tool:
python main.py


## Usage

After starting the tool, you'll be presented with a command prompt. Here are some example commands:

- DNS lookup:
dns lookup example.com A


- HTTP GET request:
http get https://api.example.com/data


- Ping a host:
ping google.com


- For a full list of commands, type:
help


## Project Structure

network-debugging-tool/
│
├── main.py
├── dns_module/
│   ├── init.py
│   └── dns_functions.py
├── http_module/
│   ├── init.py
│   └── http_functions.py
├── network_module/
│   ├── init.py
│   └── network_functions.py
├── cli/
│   ├── init.py
│   └── cli_handler.py
├── tests/
│   ├── test_dns.py
│   ├── test_http.py
│   └── test_network.py
├── requirements.txt
├── setup.py
└── README.md


## Development Roadmap

- [x] Project Setup and Architecture
- [x] DNS Lookup Module
- [x] HTTP Request Testing Module
- [x] Network Diagnostics Module
- [x] Command-Line Interface
- [ ] Integration and Testing
- [ ] Documentation and Packaging
- [ ] Advanced Features
- [ ] Security and Optimization
- [ ] Release and Maintenance

-----------------------------

## Usage

After installation, you can use the tool from the command line:

### DNS Lookup

To perform a DNS lookup:

python main.py dns example.com


To specify a different record type:

python main.py dns example.com --type MX

### HTTP Request

To perform an HTTP GET request:
python main.py http https://api.github.com


To specify a different HTTP method:

python main.py http https://api.github.com --method POST


Note: For methods other than GET, you might need to provide headers and data, which we'll implement in future updates.


### Ping

To ping a host:
python main.py ping google.com


To specify the number of ping requests:

python main.py ping google.com --count 8


### Traceroute

To perform a traceroute to a host:

python main.py traceroute google.com


Note: The traceroute command might require administrative privileges on some systems.


### HTTP Request

To perform an HTTP GET request:
python main.py http https://api.github.com


To perform a POST request with JSON data:

python main.py http https://httpbin.org/post --method POST --json '{"key": "value"}'


To include custom headers:

python main.py http https://api.github.com --headers '{"Authorization": "token YOUR_TOKEN"}'


To send form data:

python main.py http https://httpbin.org/post --method POST --data 'key1=value1&key2=value2'


## Usage

The Network Debugging Tool provides a user-friendly command-line interface for various network diagnostics tasks.

### General Help

To see all available commands and general usage information:
python main.py -h


### Command-Specific Help

To get help for a specific command, use the `-h` option after the command:

python main.py dns -h
python main.py http -h
python main.py ping -h
python main.py traceroute -h


### Examples

1. DNS Lookup:
python main.py dns example.com
python main.py dns example.com --type MX


2. HTTP Request:
python main.py http https://api.github.com
python main.py http https://httpbin.org/post --method POST --json '{"key": "value"}'


3. Ping:
python main.py ping google.com
python main.py ping google.com --count 8


4. Traceroute:
python main.py traceroute google.com


For more detailed information on each command, please refer to the command-specific help.

## Running Tests

To run the unit tests for this project, use the following command from the project root directory:
python -m unittest discover tests


This will discover and run all the tests in the `tests` directory.

## New Features

### Logging System
The tool now includes a comprehensive logging system for debugging and auditing purposes. Logs are stored in the `logs` directory.

### IPv6 Support
All relevant functions now support IPv6, including DNS lookups, ping, and traceroute.

### Scripting and Automation
You can now run a series of network tests using a YAML script file. Here's an example of a script file:

```yaml
tasks:
  - type: dns
    domain: example.com
    record_type: A
  - type: http
    url: https://api.github.com
    method: GET
  - type: ping
    host: google.com
    count: 4
  - type: traceroute
    host: cloudflare.com
Advanced Network Diagnostics
The tool now includes port scanning and SSL certificate validation capabilities.

Usage
Running a Script
python main.py script path/to/your/script.yaml
Port Scanning
python main.py portscan example.com --ports 80,443,8080
SSL Certificate Validation
python main.py sslcert example.com
Installation
Make sure to install the new dependencies:

pip install -r requirements.txt
For more detailed information on each command, please refer to the command-specific help:

python main.py <command> -h


### Result Comparison
You can now compare results from two different runs:
python main.py compare result1.json result2.json


### Advanced Network Diagnostics
The tool now includes a check for open SMTP relays:

python main.py smtprelay example.com


## Running Tests

To run all tests:

python -m unittest discover tests


For more detailed information on each command, please refer to the command-specific help:

python main.py <command> -h

## Graphical User Interface

The Network Debugging Tool now includes a simple graphical user interface. To launch the GUI version of the tool, use the following command:
python main.py --gui


The GUI provides easy-to-use interfaces for DNS lookup, HTTP requests, ping, and traceroute operations. Results are displayed in a scrollable text area at the bottom of the window.
Update requirements.txt to include Tkinter (if not already included in your Python installation):
dnspython==2.3.0
requests==2.31.0
pyyaml==6.0
pyOpenSSL==23.1.1
tk==0.1.0

## CLI Dashboard

The Network Debugging Tool now includes an interactive CLI dashboard. To launch the dashboard version of the tool, use the following command:
python main.py --dashboard


The CLI dashboard provides a menu of available commands and displays recent results. It offers a more interactive and user-friendly interface while maintaining the benefits of a command-line tool.

To use the dashboard:
1. Enter commands as you would in the regular CLI (e.g., "dns example.com")
2. Recent results will be displayed in the dashboard
3. Type 'quit' to exit the dashboard

Update requirements.txt to include the new dependency:

dnspython==2.3.0
requests==2.31.0
pyyaml==6.0
pyOpenSSL==23.1.1
rich==10.12.0