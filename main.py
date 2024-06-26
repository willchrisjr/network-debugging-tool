import sys
from cli.cli_handler import main as cli_main
from cli_dashboard import CLIDashboard

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--dashboard":
        dashboard = CLIDashboard()
        dashboard.run()
    else:
        cli_main()