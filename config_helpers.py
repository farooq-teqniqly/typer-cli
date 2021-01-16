import codecs
import os

import jsonpickle

from tcli import CliConfig

config_file_name = "tcli.config"
encoding = "utf-8"


def save_config(config: CliConfig):
    with codecs.open(config_file_name, "w", encoding) as config_file:
        config_file.write(jsonpickle.encode(config))


def read_config() -> CliConfig:
    if os.path.exists(config_file_name):
        with codecs.open(config_file_name, "r+", encoding) as config_file:
            cli_config: CliConfig = jsonpickle.decode(config_file.read())
            return cli_config

    return CliConfig()
