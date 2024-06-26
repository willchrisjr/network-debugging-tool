# cli_dashboard.py

import time
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich import box
from cli.cli_handler import NetworkDebuggingTool
import threading

class CLIDashboard:
    def __init__(self):
        self.console = Console()
        self.tool = NetworkDebuggingTool()
        self.layout = self.make_layout()
        self.results = []

    def make_layout(self):
        layout = Layout(name="root")
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", size=16),
            Layout(name="footer")
        )
        layout["main"].split_row(
            Layout(name="side"),
            Layout(name="body", ratio=2)
        )
        return layout

    def generate_menu(self):
        menu_table = Table(box=box.SIMPLE, expand=True)
        menu_table.add_column("Command", style="cyan", no_wrap=True)
        menu_table.add_column("Description", style="magenta")
        
        menu_items = [
            ("dns", "Perform DNS lookup"),
            ("http", "Send HTTP request"),
            ("ping", "Ping a host"),
            ("traceroute", "Perform traceroute"),
            ("portscan", "Scan ports on a host"),
            ("sslcert", "Validate SSL certificate"),
            ("smtprelay", "Check for open SMTP relay"),
            ("quit", "Exit the dashboard")
        ]
        
        for command, description in menu_items:
            menu_table.add_row(command, description)
        
        return Panel(menu_table, title="Menu", border_style="green")

    def generate_header(self):
        return Panel("Network Debugging Tool Dashboard", style="bold white on blue")

    def generate_footer(self):
        return Panel("Enter a command or 'quit' to exit", style="bold white on blue")

    def generate_results(self):
        results_table = Table(box=box.SIMPLE, expand=True)
        results_table.add_column("Command", style="cyan", no_wrap=True)
        results_table.add_column("Result", style="green")
        
        for command, result in self.results[-5:]:  # Show last 5 results
            results_table.add_row(command, str(result)[:50] + "..." if len(str(result)) > 50 else str(result))
        
        return Panel(results_table, title="Recent Results", border_style="yellow")

    def update(self, live):
        self.layout["header"].update(self.generate_header())
        self.layout["side"].update(self.generate_menu())
        self.layout["body"].update(self.generate_results())
        self.layout["footer"].update(self.generate_footer())

    def run_command(self, command, args):
        if command == "dns":
            return self.tool.run_dns(args)
        elif command == "http":
            return self.tool.run_http(args)
        elif command == "ping":
            return self.tool.run_ping(args)
        elif command == "traceroute":
            return self.tool.run_traceroute(args)
        elif command == "portscan":
            return self.tool.run_portscan(args)
        elif command == "sslcert":
            return self.tool.run_sslcert(args)
        elif command == "smtprelay":
            return self.tool.run_smtp_relay_check(args)
        else:
            return "Unknown command"

    def input_thread(self):
        while True:
            command = input()
            if command.lower() == 'quit':
                break
            args = command.split()
            if args:
                command = args.pop(0)
                result = self.run_command(command, args)
                self.results.append((command, result))

    def run(self):
        with Live(self.layout, refresh_per_second=4, screen=True):
            input_thread = threading.Thread(target=self.input_thread, daemon=True)
            input_thread.start()
            
            while input_thread.is_alive():
                self.update(None)
                time.sleep(0.25)

if __name__ == "__main__":
    dashboard = CLIDashboard()
    dashboard.run()