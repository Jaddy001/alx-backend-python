#!/usr/bin/env python3
"""
Module 9-element_length
Defines a function to get the length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements and their lengths."""
    return [(i, len(i)) for i in lst]

