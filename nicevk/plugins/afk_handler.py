import time
from datetime import timedelta

from vkbottle import Message
from nicevk.api import state, save_state, user


@user.middleware.middleware_handler()
async def answer(ans: Message):
    print("Asd")
    domain = str((await user.api.users.get(fields="domain"))[0].domain)
    if (
        (len(domain) > 1 and domain in ans.text)
        or str(user.user_id) in ans.text
    ):
        if not state["afk"] or not state["afk"]["status"] or str(ans.chat_id) in state["afk"]["mentioned"]:
            return True
        diff = str(timedelta(seconds=(time.time() - state["afk"]["time"])))
        if state["afk"]["reason"]:
            await ans("I am afk (for {}): {}".format(diff, state["afk"]["reason"]))
        else:
            await ans("I am afk (for {}), contact me later".format(diff))
        state["afk"]["mentioned"].append(str(ans.chat_id))
        save_state()
        return True
    print(ans.text, str((await user.api.users.get(fields="domain"))[0].domain))
    return True