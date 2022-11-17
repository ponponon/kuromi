import os
import time
from pathlib import Path
import click
from loguru import logger


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', help='The person to greet.')
def main(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == '__main__':
    main()
