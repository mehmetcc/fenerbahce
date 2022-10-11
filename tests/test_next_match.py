import pytest

from fenerbahce.next_match import next_match


def test_next_match():
    result = next_match()
    assert result is not None