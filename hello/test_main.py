import pytest
import sys
from .main import main_typer


def run_main(*args):
    from typer import Typer
    from typer.testing import CliRunner

    app = Typer()
    app.command()(main_typer)
    runner = CliRunner()
    return runner.invoke(app, args)


def test_main(caplog):
    result = run_main("world", "--count", "3")
    assert(result.exit_code == 0)
