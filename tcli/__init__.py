class CliConfig:
    def __init__(self):
        self.username: str = ""


def create_cli(*args, **kwargs):
    cli_config = read_config()

    app = Typer()
    app.add_typer(configure.create_app(cli_config), name="configure")
    app.add_typer(profile.create_app(cli_config), name="profile")

    return app


from config_helpers import read_config
from typer import Typer
from tcli.commands.configure import configure
from tcli.commands.profile import profile
