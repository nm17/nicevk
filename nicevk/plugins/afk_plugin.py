from vkbottle import Message
from nicevk.api import user, commands, state, save_state
import time

commands.extend(
    [
        ".afk [reason] - makes you afk",
        ".unafk - seems like you are here"
    ]
)

@user.on.message_handler(text=".afk <reason>")
async def afk(ans: Message, reason: str):
    if "afk" not in state.keys():
        state["afk"] = {}
    state["afk"]["status"] = True
    if reason is not None:
        state["afk"]["reason"] = reason
    state["afk"]["time"] = time.time()
    save_state()
    await ans.api.messages.edit(
        ans.peer_id,
        ans.id,
        "I will be back"
    )

@user.on.message_handler(text=".unafk")    
async def afk(ans: Message):
    if "afk" not in state.keys(): # Using unafk without afk
        state["afk"] = {}
    state["afk"]["status"] = False
    del state["afk"]["time"]
    save_state()
    await ans.api.messages.edit(
        ans.peer_id,
        ans.id,
        "I am back"
    )

