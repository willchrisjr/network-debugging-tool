import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from cli.cli_handler import NetworkDebuggingTool

class NetworkDebuggingToolGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Debugging Tool")
        self.master.geometry("600x400")
        
        self.tool = NetworkDebuggingTool()
        
        self.create_widgets()

    def create_widgets(self):
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both")

        # DNS Tab
        self.dns_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.dns_frame, text="DNS Lookup")
        self.create_dns_tab()

        # HTTP Tab
        self.http_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.http_frame, text="HTTP Request")
        self.create_http_tab()

        # Ping Tab
        self.ping_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.ping_frame, text="Ping")
        self.create_ping_tab()

        # Traceroute Tab
        self.traceroute_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.traceroute_frame, text="Traceroute")
        self.create_traceroute_tab()

        # Output Area
        self.output_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, height=10)
        self.output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def create_dns_tab(self):
        ttk.Label(self.dns_frame, text="Domain:").grid(column=0, row=0, padx=5, pady=5)
        self.dns_domain = ttk.Entry(self.dns_frame, width=40)
        self.dns_domain.grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(self.dns_frame, text="Record Type:").grid(column=0, row=1, padx=5, pady=5)
        self.dns_type = ttk.Combobox(self.dns_frame, values=["A", "AAAA", "MX", "TXT", "CNAME"])
        self.dns_type.set("A")
        self.dns_type.grid(column=1, row=1, padx=5, pady=5)

        ttk.Button(self.dns_frame, text="Lookup", command=self.run_dns_lookup).grid(column=1, row=2, padx=5, pady=5)

    def create_http_tab(self):
        ttk.Label(self.http_frame, text="URL:").grid(column=0, row=0, padx=5, pady=5)
        self.http_url = ttk.Entry(self.http_frame, width=40)
        self.http_url.grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(self.http_frame, text="Method:").grid(column=0, row=1, padx=5, pady=5)
        self.http_method = ttk.Combobox(self.http_frame, values=["GET", "POST", "PUT", "DELETE"])
        self.http_method.set("GET")
        self.http_method.grid(column=1, row=1, padx=5, pady=5)

        ttk.Button(self.http_frame, text="Send Request", command=self.run_http_request).grid(column=1, row=2, padx=5, pady=5)

    def create_ping_tab(self):
        ttk.Label(self.ping_frame, text="Host:").grid(column=0, row=0, padx=5, pady=5)
        self.ping_host = ttk.Entry(self.ping_frame, width=40)
        self.ping_host.grid(column=1, row=0, padx=5, pady=5)

        ttk.Label(self.ping_frame, text="Count:").grid(column=0, row=1, padx=5, pady=5)
        self.ping_count = ttk.Entry(self.ping_frame, width=10)
        self.ping_count.insert(0, "4")
        self.ping_count.grid(column=1, row=1, padx=5, pady=5)

        ttk.Button(self.ping_frame, text="Ping", command=self.run_ping).grid(column=1, row=2, padx=5, pady=5)

    def create_traceroute_tab(self):
        ttk.Label(self.traceroute_frame, text="Host:").grid(column=0, row=0, padx=5, pady=5)
        self.traceroute_host = ttk.Entry(self.traceroute_frame, width=40)
        self.traceroute_host.grid(column=1, row=0, padx=5, pady=5)

        ttk.Button(self.traceroute_frame, text="Traceroute", command=self.run_traceroute).grid(column=1, row=1, padx=5, pady=5)

    def run_dns_lookup(self):
        domain = self.dns_domain.get()
        record_type = self.dns_type.get()
        result = self.tool.run_dns(argparse.Namespace(domain=domain, type=record_type))
        self.display_result(result)

    def run_http_request(self):
        url = self.http_url.get()
        method = self.http_method.get()
        result = self.tool.run_http(argparse.Namespace(url=url, method=method, headers=None, data=None, json=None))
        self.display_result(result)

    def run_ping(self):
        host = self.ping_host.get()
        count = int(self.ping_count.get())
        result = self.tool.run_ping(argparse.Namespace(host=host, count=count))
        self.display_result(result)

    def run_traceroute(self):
        host = self.traceroute_host.get()
        result = self.tool.run_traceroute(argparse.Namespace(host=host))
        self.display_result(result)

    def display_result(self, result):
        self.output_area.delete(1.0, tk.END)
        self.output_area.insert(tk.END, str(result))

def main():
    root = tk.Tk()
    app = NetworkDebuggingToolGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()