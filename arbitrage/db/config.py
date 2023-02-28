from typing import List

from arbitrage.settings import settings

ROOT_PATH = "arbitrage.db.models"

MODELS_MODULES: List[str] = [
    f"{ROOT_PATH}.users",
    f"{ROOT_PATH}.deals",
    f"{ROOT_PATH}.chat",
]  # noqa: WPS407

TORTOISE_CONFIG = {  # noqa: WPS407
    "connections": {
        "default": str(settings.db_url),
    },
    "apps": {
        "models": {
            "models": MODELS_MODULES + ["aerich.models"],
            "default_connection": "default",
        },
    },
}
