import os
import signal
from pathlib import Path

import click
from click.core import Context
from click.exceptions import ClickException


#TODO: add relevant options in this group
@click.option(
    '--topo', 
    default=os.getcwd, 
    help="Path to directory containing topology files (i.e. .rtf and .prm)"
)
def topo(input):
    os.path.join(os.getcwd, input)
    click.echo("Searching for topology files in: " + str(os.path.join(os.getcwd, input)))


def main():
    pass

if __name__ == "__main__":
    main()