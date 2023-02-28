# createSchema.py
from tortoise import Tortoise, run_async

from arbitrage.db.config import MODELS_MODULES
from arbitrage.settings import settings


async def connect():
    await Tortoise.init(
        db_url=str(settings.db_url),
        modules={"models": MODELS_MODULES + ["aerich.models"]},
    )


async def main():
    await connect()
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(main())
