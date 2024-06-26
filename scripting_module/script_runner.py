import yaml
from dns_module.dns_functions import dns_lookup
from http_module.http_functions import http_request
from network_module.network_functions import ping, traceroute
from logging_module.logger import logger

def run_script(script_file):
    logger.info(f"Running script from file: {script_file}")
    with open(script_file, 'r') as file:
        script = yaml.safe_load(file)
    
    results = []
    for task in script['tasks']:
        logger.debug(f"Executing task: {task}")
        if task['type'] == 'dns':
            result = dns_lookup(task['domain'], task.get('record_type', 'A'))
        elif task['type'] == 'http':
            result = http_request(task['url'], method=task.get('method', 'GET'),
                                  headers=task.get('headers'), data=task.get('data'),
                                  json_data=task.get('json'))
        elif task['type'] == 'ping':
            result = ping(task['host'], task.get('count', 4))
        elif task['type'] == 'traceroute':
            result = traceroute(task['host'])
        else:
            logger.warning(f"Unknown task type: {task['type']}")
            result = f"Error: Unknown task type {task['type']}"
        
        results.append({
            'task': task,
            'result': result
        })
    
    return results