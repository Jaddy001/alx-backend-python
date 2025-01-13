#!/usr/bin/env python3
"""Module to measure runtime of asynchronous functions."""
import time
import importlib

# Dynamically import the module
concurrent_coroutines = importlib.import_module("1-concurrent_coroutines")
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of wait_n.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average runtime per coroutine.
    """
    start_time = time.time()
    wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n

