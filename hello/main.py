import typer


def main_typer(target=typer.Argument(help="hello target", count=typer.Argument(1, help="how many times?")):
    for i in range(count):
        sys.stdout.write(f"hello stdout {target}\n")
        logger.debug("hello debug %s", target)
        logger.info("hello info %s", target)
        logger.warning("hello warning %s", target)


if __name__ == "__main__":
    typer.run(main)
