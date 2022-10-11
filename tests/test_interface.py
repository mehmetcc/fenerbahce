import click
from click.testing import CliRunner
import pytest

from fenerbahce.interface import interface, next, last


def test_interface():
    runner = CliRunner()
    result = runner.invoke(interface)
    assert result.exit_code == 0


def test_next():
    runner = CliRunner()
    result = runner.invoke(next)
    assert result.exit_code == 0
    assert result is not None


def test_last():
    runner = CliRunner()
    result = runner.invoke(last)
    assert result.exit_code == 0
    assert result is not None
