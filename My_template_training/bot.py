import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.contrib.fsm_storage.redis import RedisStorage2

from My_template_training.tg_bot.filters.admin import AdminFilter
from My_template_training.tg_bot.handlers.admin import register_admin
from My_template_training.tg_bot.handlers.testing import register_testing
from tg_bot.handlers.start import register_user
from My_template_training.tg_bot.middlewares.db import EnvironmentMiddleware
from tg_bot.handlers.echo import register_echo
from tg_bot.config import load_config

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):  # register all mid, filter, hand; use dispatcher
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_testing(dp)
    register_admin(dp)
    register_user(dp)
    register_echo(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    config = load_config('.env')

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")  # Bot
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()  # if redis is True, or Opera memory use
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config

    register_all_middlewares(dp, config)  # for registered all funcs in dispatcher
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()  # closing storage
        await dp.storage.wait_closed()  # wait  connect to closed
        await dp.bot.session.close()  # bot session is close for async func


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
