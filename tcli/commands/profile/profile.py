import typer
from typer import Typer

from credentials_helper import ensure_password_is_set
from tcli.typer_app import TyperApp


class ProfileApp(TyperApp):
    def on_create_app(self, app: Typer, *args, **kwargs) -> Typer:
        @app.command()
        @ensure_password_is_set(self.config.username)
        def set(name: str, about: str):
            typer.secho(
                f"Profile set. Name: {name}, About: {about}, Username: {self.config.username}"
            )

        return app
