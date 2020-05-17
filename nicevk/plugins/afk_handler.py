from vkbottle import Message
from nicevk.api import state, save_state
import time


@bot.on.chat_mention()
async def answer(ans: Message):
    if not state["afk"]:
        return
    if state["afk"]["status"]:
        if str(ans.chat_id) in state["afk"]["mentioned"]:
            return
        diff = time.strftime('%H:%M:%S', (time.time() - state["afk"]["time"]))
        if state["afk"]["reason"]:
            await ans("I am afk (for {}): {}".format(diff, afk["afk"]["reason"]))
        else:
            await ans("I am afk (for {}), contact me later".format(diff))
        state["afk"]["mentioned"].append(str(ans.chat_id))
        save_state()
    else:
        return

