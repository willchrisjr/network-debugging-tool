import dns.resolver
from logging_module.logger import logger

def dns_lookup(domain, record_type='A'):
    logger.info(f"Performing DNS lookup for {domain} with record type {record_type}")
    try:
        if record_type == 'A':
            ipv4_answers = dns.resolver.resolve(domain, 'A')
            ipv6_answers = dns.resolver.resolve(domain, 'AAAA')
            result = [f"IPv4: {str(rdata)}" for rdata in ipv4_answers] + [f"IPv6: {str(rdata)}" for rdata in ipv6_answers]
        else:
            answers = dns.resolver.resolve(domain, record_type)
            result = [str(rdata) for rdata in answers]
        logger.debug(f"DNS lookup result: {result}")
        return result
    except dns.resolver.NXDOMAIN:
        logger.warning(f"Domain {domain} does not exist")
        return f"Error: Domain {domain} does not exist"
    except dns.resolver.NoAnswer:
        logger.warning(f"No {record_type} record found for {domain}")
        return f"Error: No {record_type} record found for {domain}"
    except dns.exception.DNSException as e:
        logger.error(f"DNS query failed: {str(e)}")
        return f"Error: DNS query failed: {str(e)}"