#!/usr/bin/python3
"""Class that avoids dynmaically created attributes."""


class LockedClass:
    """Prevent the user from dynamically creating new instance attributes."""

    __slots__ = ['first_name']

    def __init__(self):
        """Initialize method."""
        pass
