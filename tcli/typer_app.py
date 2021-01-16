from abc import ABC, abstractmethod

from typer import Typer

from tcli import CliConfig


class TyperApp(ABC):
    def __init__(self, config: CliConfig):
        self.config = config

    def create_app(self, *args, **kwargs) -> Typer:
        app = Typer(*args, **kwargs)
        self.on_create_app(app, *args, **kwargs)
        return app

    @abstractmethod
    def on_create_app(self, app: Typer, *args, **kwargs):
        pass
