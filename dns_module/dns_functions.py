import dns.resolver

def dns_lookup(domain, record_type='A'):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except dns.resolver.NXDOMAIN:
        return f"Error: Domain {domain} does not exist"
    except dns.resolver.NoAnswer:
        return f"Error: No {record_type} record found for {domain}"
    except dns.exception.DNSException as e:
        return f"Error: DNS query failed: {str(e)}"