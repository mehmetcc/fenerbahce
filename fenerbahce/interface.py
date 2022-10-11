
from code import interact
import click

from next_match import next_match
from last_match import last_match


@click.group()
def interface():
    """Find information on past and future games of Fenerbahçe's Professional Football Team"""
    pass


@click.command()
def next():
    """Show information on the next game"""
    info = next_match()
    click.echo(info)


@click.command()
def last():
    """Show information on the last game"""
    info = last_match()
    click.echo(info)


interface.add_command(next)
interface.add_command(last)


if __name__ == '__main__':
    interface()
