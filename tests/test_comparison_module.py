import pytest
from comparison_module.result_comparator import compare_results

def test_compare_results():
    result1 = {"test1": "result1", "test2": "result2"}
    result2 = {"test1": "result1", "test2": "different"}
    comparison = compare_results(result1, result2)
    assert "test1" in comparison["matching"]
    assert "test2" in comparison["differing"]