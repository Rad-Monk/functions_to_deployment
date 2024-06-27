import click
from mylib.bot import scrape


@click.command()
@click.option("--name", help="web pade we wanna scrape")
@click.option("--length", help="number of sentences you want back")
def cli(name="Microsoft", length=2):
    result = scrape(name, length)
    click.echo(click.style(f"{result}", fg="green"))


if __name__ == "__main__":
    cli()
