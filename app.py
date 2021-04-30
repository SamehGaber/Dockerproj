#!/usr/bin/venv python
import click 

@click.command()
def hello():
    click.echo('hellpw world!')

if __name__ == '__main__':
    hello()
