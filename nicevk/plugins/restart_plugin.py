import asyncio
import subprocess
from functools import wraps

from vkbottle import Message, VKError

from nicevk.api import user, commands, state, save_state

commands.append(".restart - restart nicevk")


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@coro
async def on_start():
    if (
        state.get("restart", None) is not None
        and state["restart"]["last_message"] is not None
    ):
        try:
            await user.api.messages.edit(
                *state["restart"]["last_message"], "Successfully restarted nicevk"
            )
        except VKError:
            pass
        state["restart"]["last_message"] = None
        save_state()


@user.on.message_handler(text=".restart")
async def help_(ans: Message):
    state["restart"] = {}
    state["restart"]["last_message"] = (ans.peer_id, ans.id)
    save_state()
    subprocess.Popen(["nicevk"])


on_start()
