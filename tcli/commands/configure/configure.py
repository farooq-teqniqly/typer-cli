from typer import Typer

from tcli.commands.configure.credentials.credentials import CredentialsApp
from tcli.typer_app import TyperApp


class ConfigureApp(TyperApp):

    def on_create_app(self, app: Typer, *args, **kwargs) -> Typer:
        app.add_typer(
            CredentialsApp(self.config).create_app(
                help="Manage CLI credentials."),
            name="credentials"
        )

        return app
