#!/usr/bin/env python3
"""
Module 8-make_multiplier
Defines a function that returns a function to multiply a float by a multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    return lambda x: x * multiplier

