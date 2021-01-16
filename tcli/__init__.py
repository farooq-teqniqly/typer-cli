class CliConfig:
    def __init__(self):
        self.username: str = ""


def create_cli(*args, **kwargs):
    cli_config = read_config()

    app = Typer()

    app.add_typer(
        ConfigureApp(cli_config).create_app(
            help="Manage CLI configuration."),
        name="configure")

    app.add_typer(
        ProfileApp(cli_config).create_app(
            help="Manage profiles."),
        name="profile")

    return app


from config_helpers import read_config
from typer import Typer
from tcli.commands.configure.configure import ConfigureApp
from tcli.commands.profile.profile import ProfileApp
