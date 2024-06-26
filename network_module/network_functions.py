import subprocess
import platform
import socket
import ssl
import OpenSSL
import smtplib
from concurrent.futures import ThreadPoolExecutor
from logging_module.logger import logger
from utils.rate_limiter import RateLimiter

@RateLimiter(max_calls=20, time_frame=60)  # Limit to 20 pings per minute
def ping(host, count=4):
    logger.info(f"Pinging {host} with count {count}")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), host]
    
    if ':' in host:  # IPv6 address
        command = ['ping6' if platform.system().lower() != 'windows' else 'ping', '-6', param, str(count), host]
    
    try:
        output = subprocess.check_output(command, timeout=10).decode()
        logger.debug(f"Ping output: {output}")
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Ping failed: {str(e)}")
        return f"Error: Unable to ping {host}"
    except subprocess.TimeoutExpired:
        logger.error(f"Ping timed out")
        return f"Error: Ping to {host} timed out"

@RateLimiter(max_calls=10, time_frame=60)  # Limit to 10 traceroutes per minute
def traceroute(host):
    logger.info(f"Performing traceroute to {host}")
    if platform.system().lower() == 'windows':
        command = ['tracert']
    else:
        command = ['traceroute']
        if ':' in host:  # IPv6 address
            command = ['traceroute6']
    
    command.append(host)
    try:
        output = subprocess.check_output(command, timeout=30).decode()
        logger.debug(f"Traceroute output: {output}")
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Traceroute failed: {str(e)}")
        return f"Error: Unable to perform traceroute to {host}"
    except subprocess.TimeoutExpired:
        logger.error(f"Traceroute timed out")
        return f"Error: Traceroute to {host} timed out"

@RateLimiter(max_calls=5, time_frame=60)  # Limit to 5 port scans per minute
def port_scan(host, ports):
    logger.info(f"Scanning ports for {host}: {ports}")
    open_ports = []
    def check_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            logger.debug(f"Port {port} is open")
            open_ports.append(port)
        sock.close()

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(check_port, ports)
    
    return open_ports

@RateLimiter(max_calls=10, time_frame=60)  # Limit to 10 SSL cert validations per minute
def validate_ssl_cert(hostname, port=443):
    logger.info(f"Validating SSL certificate for {hostname}:{port}")
    try:
        cert = ssl.get_server_certificate((hostname, port))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        
        subject = x509.get_subject()
        issuer = x509.get_issuer()
        not_before = x509.get_notBefore().decode('ascii')
        not_after = x509.get_notAfter().decode('ascii')

        result = {
            'subject': dict(subject.get_components()),
            'issuer': dict(issuer.get_components()),
            'version': x509.get_version(),
            'serialNumber': x509.get_serial_number(),
            'notBefore': not_before,
            'notAfter': not_after
        }
        logger.debug(f"SSL certificate validation result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error validating SSL certificate: {str(e)}")
        return f"Error: Unable to validate SSL certificate - {str(e)}"

@RateLimiter(max_calls=5, time_frame=60)  # Limit to 5 SMTP relay checks per minute
def check_smtp_relay(host, port=25):
    logger.info(f"Checking for open SMTP relay on {host}:{port}")
    try:
        with smtplib.SMTP(host, port, timeout=10) as server:
            server.ehlo()
            if server.has_extn('STARTTLS'):
                server.starttls()
                server.ehlo()
            server.docmd('MAIL FROM:', '<test@example.com>')
            code, message = server.docmd('RCPT TO:', '<test@example.com>')
            if code == 250:
                logger.warning(f"Potential open relay detected on {host}:{port}")
                return f"Warning: Potential open relay detected on {host}:{port}"
            else:
                logger.info(f"No open relay detected on {host}:{port}")
                return f"No open relay detected on {host}:{port}"
    except Exception as e:
        logger.error(f"Error checking SMTP relay: {str(e)}")
        return f"Error checking SMTP relay on {host}:{port}: {str(e)}"