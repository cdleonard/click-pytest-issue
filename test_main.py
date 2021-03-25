import pytest


def main(*args, **kwargs):
    import logging
    logging.info("main args=%r kwargs=%r", args, kwargs)



def run_main(*args):
    from typer import Typer
    from typer.testing import CliRunner

    app = Typer()
    app.command()(main)
    return CliRunner().invoke(app, *args)


def test_main(caplog):
    run_main(["--hello", "world"])
