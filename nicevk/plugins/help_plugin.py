from vkbottle import Message

from nicevk.api import user


@user.on.message_handler(text=".help")
async def help_(ans: Message):
    await ans.api.messages.edit(ans.peer_id, ans.id, "тест")