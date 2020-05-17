import asyncio
import os
import sys
from functools import wraps
from pathlib import Path

import psutil

from nicevk.api import nicevk_folder, user, env, solve_captcha, logger, coro

from runpy import run_path


@logger.catch
def run():
    a = [(Path(__file__).parent / "plugins"), nicevk_folder]
    logger.enable("vkbottle")

    for proc in psutil.process_iter():
        if "nicevk" in proc.name() and proc.pid != os.getpid():
            proc.kill()

    for plugin in a:
        sys.path.insert(0, plugin)
        for file in plugin.glob("*.py"):
            run_path(str(file))

    if env.get("RUCAPTCHA_TOKEN", None) is not None:
        user.error_handler.add_error_handler(14, solve_captcha)

    user.run_polling()


if __name__ == "__main__":
    run()
