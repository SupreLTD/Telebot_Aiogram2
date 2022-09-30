from dataclasses import dataclass
from typing import List

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]
    use_redis: bool


@dataclass
class DbConfig:  # config of data bases
    host: str  # where db inplace
    password: str  # pass of user db
    user: str  # what user's db
    database: str  # what db


@dataclass
class Miscellaneous:  # all other, or create other dataclass
    other_params: str = None  # other params


@dataclass
class Config:  # info of our bot
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):  # routes of config
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMINS'))),
            use_redis=env.bool('USE_REDIS')
        ),
        db=DbConfig(
            host=env.str("DB_HOST"),
            password=env.str("DB_PASS"),
            user=env.str("DB_USER"),
            database=env.str("DB_NAME")
        ),
        misc=Miscellaneous()  # param installed as None
    )
