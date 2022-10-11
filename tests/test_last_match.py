import pytest

from fenerbahce.last_match import last_match

def test_last_match():
    result = last_match()
    assert result is not None