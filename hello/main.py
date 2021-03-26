import sys
import logging
import click


logger = logging.getLogger()


@click.command()
@click.option("--target", help="hello target")
@click.option("--count", default=1, help="how many times?")
def main(target: str, count: int):
    for i in range(count):
        sys.stdout.write(f"hello stdout {target}\n")
        logger.debug("hello debug %s", target)
        logger.info("hello info %s", target)
        logger.warning("hello warning %s", target)


if __name__ == "__main__":
    main()
