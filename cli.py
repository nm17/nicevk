import asyncio
import os
from functools import wraps
from glob import glob
import vk_api
from typer import Typer


import importlib

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll
from vkbottle import User

app = Typer()


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@app.command()
def main():
    data = dict(login="...")

    api = VkApi(token="...")

    poll = VkLongPoll(api)

    blueprints = []

    plugins = {}
    commands = ["help"]

    for file in glob(os.path.join(os.path.dirname(os.path.abspath(__file__))) + "/plugins/*.py"):
        name = os.path.splitext(os.path.basename(file))[0]
        # add package prefix to name, if required
        plugin = importlib.import_module(f"plugins.{name}")
        # enable plugin plugin

    poll.listen()


if __name__ == '__main__':
    app()
