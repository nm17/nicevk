from vkbottle import Message

from nicevk.api import user, commands
from nicevk.utils import edit


@user.on.message_handler(text=".help")
async def help_(ans: Message):
    await edit(
        ans.peer_id, ans.id,
        "Available commands:\n\n" + "\n".join(commands)
    )
