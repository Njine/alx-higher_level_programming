#!/usr/bin/python3
"""
This modules contains a class
that inherits from int
"""


class MyInt(int):
    """Rspond inverse to Equal and Not Equal."""

    def __eq__(self, other):
        """Return inverse of Equal."""
        return (not super().__eq__(other))

    def __ne__(self, other):
        """Return inverse of not equal."""
        return (not super().__ne__(other))
