# In comparison_module/result_comparator.py

import json
from logging_module.logger import logger

def compare_results(result1, result2):
    logger.info("Comparing results from two runs")
    
    if isinstance(result1, dict) and isinstance(result2, dict):
        return compare_dicts(result1, result2)
    elif isinstance(result1, list) and isinstance(result2, list):
        return compare_lists(result1, result2)
    else:
        return compare_strings(str(result1), str(result2))

def compare_dicts(dict1, dict2):
    all_keys = set(dict1.keys()) | set(dict2.keys())
    differences = {}
    
    for key in all_keys:
        if key not in dict1:
            differences[key] = (None, dict2[key])
        elif key not in dict2:
            differences[key] = (dict1[key], None)
        elif dict1[key] != dict2[key]:
            differences[key] = (dict1[key], dict2[key])
    
    return differences

def compare_lists(list1, list2):
    return {
        'only_in_first': list(set(list1) - set(list2)),
        'only_in_second': list(set(list2) - set(list1)),
        'common': list(set(list1) & set(list2))
    }

def compare_strings(str1, str2):
    if str1 == str2:
        return "Results are identical"
    else:
        return f"Results differ:\nFirst result: {str1}\nSecond result: {str2}"