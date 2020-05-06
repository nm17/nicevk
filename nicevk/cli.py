import asyncio
import sys
from functools import wraps
from pathlib import Path

from nicevk.api import nicevk_folder, user

from runpy import run_path


def run():
    a = [(Path(__file__).parent / "plugins"), nicevk_folder]

    for plugin in a:
        sys.path.insert(0, plugin)
        for file in plugin.glob("*.py"):
            run_path(str(file))

    user.run_polling()
