#!/usr/bin/env python3
"""Module to execute asyncio.Tasks concurrently."""
import asyncio
from typing import List
import importlib

# Dynamically import the module
tasks_module = importlib.import_module("3-tasks")
task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return the delays in ascending order.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

