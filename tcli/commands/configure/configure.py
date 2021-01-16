import codecs
import jsonpickle

import keyring
from typer import Typer, secho

from config_helpers import save_config
from credentials_helper import set_password
from tcli import CliConfig


def create_app(cli_config: CliConfig, *args, **kwargs):
    app = Typer(help="Configure the CLI.")

    @app.command()
    def credentials(user_name: str, password: str):
        """Configure the credentials the CLI commands run under."""
        set_password(user_name, password)
        cli_config.username = user_name
        save_config(cli_config)

        secho(f"Username: {cli_config.username}", fg="green")

    return app
