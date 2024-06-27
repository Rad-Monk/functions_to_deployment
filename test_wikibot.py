from wikibot import cli
from mylib.bot import scrape
from click.testing import CliRunner


def test_scrape():
    assert "Microsoft" in scrape("Microsoft")


def test_cli_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ["--name", "Facebook", "--length", "3"])
    assert result.exit_code == 0
    assert "facebook" in result.output
