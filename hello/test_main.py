import pytest
import sys
from . import main


def run_main(*args):
    from typer import Typer
    from typer.testing import CliRunner

    app = Typer()
    app.command()(main)
    runner = CliRunner()
    return runner.invoke(app, args)


def test_main(caplog):
    result = run_main()
    assert(result.exit_code == 0)
