import subprocess
import platform
from logging_module.logger import logger

def ping(host, count=4):
    logger.info(f"Pinging {host} with count {count}")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    
    # If it's an IPv6 address, use the appropriate ping command
    if ':' in host:
        command = ['ping6' if platform.system().lower() != 'windows' else 'ping', '-6', param, str(count), host]
    
    try:
        output = subprocess.check_output(command).decode()
        logger.debug(f"Ping output: {output}")
        return output
    except subprocess.CalledProcessError:
        logger.error(f"Unable to ping {host}")
        return f"Error: Unable to ping {host}"

def traceroute(host):
    logger.info(f"Performing traceroute to {host}")
    if platform.system().lower() == 'windows':
        command = ['tracert']
    else:
        command = ['traceroute']
        if ':' in host:
            command = ['traceroute6']
    
    command.append(host)
    try:
        output = subprocess.check_output(command).decode()
        logger.debug(f"Traceroute output: {output}")
        return output
    except subprocess.CalledProcessError:
        logger.error(f"Unable to perform traceroute to {host}")
        return f"Error: Unable to perform traceroute to {host}"