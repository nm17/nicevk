import asyncio
import os
import sys
from functools import wraps
from pathlib import Path

import psutil

from nicevk.api import nicevk_folder, user, state, save_state

from runpy import run_path


def run():
    a = [(Path(__file__).parent / "plugins"), nicevk_folder]

    for proc in psutil.process_iter():
        if "nicevk" in proc.name() and proc.pid != os.getpid():
            proc.kill()

    for plugin in a:
        sys.path.insert(0, plugin)
        for file in plugin.glob("*.py"):
            run_path(str(file))

    user.run_polling()
