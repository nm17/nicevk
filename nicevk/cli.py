import asyncio
import os
import sys
from pathlib import Path
import runpy
import psutil


def run():
    from nicevk.api import nicevk_folder, user, env, solve_captcha, logger

    a = [(Path(__file__).parent / "plugins"), nicevk_folder]
    logger.enable("vkbottle")

    for proc in psutil.process_iter():
        if "nicevk" in proc.name() and proc.pid != os.getpid():
            proc.kill()

    for plugin in a:
        sys.path.insert(0, plugin)
        for file in plugin.glob("*.py"):
            runpy.run_path(str(file))

    if env.get("RUCAPTCHA_TOKEN", None) is not None:
        user.error_handler.add_error_handler(14, solve_captcha)

    user.run_polling()


if __name__ == "__main__":
    run()
