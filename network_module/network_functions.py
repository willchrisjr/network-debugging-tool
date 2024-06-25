import subprocess
import platform

def ping(host, count=4):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    try:
        output = subprocess.check_output(command).decode()
        return output
    except subprocess.CalledProcessError:
        return f"Error: Unable to ping {host}"

def traceroute(host):
    command = ['tracert'] if platform.system().lower() == 'windows' else ['traceroute']
    command.append(host)
    try:
        output = subprocess.check_output(command).decode()
        return output
    except subprocess.CalledProcessError:
        return f"Error: Unable to perform traceroute to {host}"