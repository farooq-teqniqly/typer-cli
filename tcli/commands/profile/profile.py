import typer

from credentials_helper import ensure_password_is_set
from tcli import CliConfig


def create_app(cli_config: CliConfig, *args, **kwargs):
    app = typer.Typer(help="Manage profiles.")

    @app.command()
    @ensure_password_is_set(cli_config.username)
    def set(name: str, about: str):
        typer.secho(
            f"Profile set. Name: {name}, About: {about}, Username: {cli_config.username}"
        )

    return app
