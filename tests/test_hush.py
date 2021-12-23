"""Tests for the hush package."""

from __future__ import annotations

from hush import dummy


def test_dummy() -> None:
    """Test the dummy() function."""
    assert dummy(1, 2) == 3
