# Network Debugging Tool

## Overview

The Network Debugging Tool is a comprehensive command-line utility that combines DNS server, HTTP server, and Shell functionalities to provide a robust set of network diagnostic and testing capabilities. This tool is designed for network administrators, developers, and IT professionals who need a versatile, all-in-one solution for network troubleshooting and analysis.

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


