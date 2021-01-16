from click import secho
from typer import Typer

from config_helpers import save_config
from credentials_helper import set_password, delete_password
from tcli.typer_app import TyperApp


class CredentialsApp(TyperApp):
    def on_create_app(self, app: Typer, *args, **kwargs) -> Typer:
        @app.command()
        def set(user_name: str, password: str):
            """Configure the credentials the CLI commands run under."""
            set_password(user_name, password)
            self.config.username = user_name
            save_config(self.config)

            secho(f"Username: {self.config.username}", fg="green")

        @app.command()
        def delete(user_name: str):
            """Delete stored CLI credentials."""
            delete_password(user_name)
            self.config.username = ""
            save_config(self.config)

        return app
