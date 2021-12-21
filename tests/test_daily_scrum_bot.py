from typer.testing import CliRunner

from daily_scrum_bot.main import app

runner = CliRunner()


def test_daily_scrum_bot():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout
