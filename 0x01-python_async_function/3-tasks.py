#!/usr/bin/env python3
"""Module to create asyncio.Task objects."""
import asyncio
import importlib

# Dynamically import the module
basic_async_syntax = importlib.import_module("0-basic_async_syntax")
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum delay for the coroutine.

    Returns:
        asyncio.Task: Task object for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

