import pytest
import sys
from .main import main


def run_main(*args):
    from click.testing import CliRunner

    runner = CliRunner()
    return runner.invoke(main)


def test_main(caplog):
    result = run_main("world", "--count", "3")
    assert result.exit_code == 0
