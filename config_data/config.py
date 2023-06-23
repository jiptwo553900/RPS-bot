from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Telegram bot token


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    """
    :param path: path to file with environment values
    :return: instance of Config class for TG bot
    """
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))
