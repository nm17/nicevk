import asyncio
from vkbottle import Message
from nicevk.api import user, commands

commands.append(".type <text> - just typing the text")


@user.on.message_handler(text=".type <text>")
async def help_(ans: Message, text: str):
    if not text:
        return await ans.api.messages.edit(ans.peer_id, ans.id,
                                           "I need something to type")
    if ' ' in text:  # to prevent messageWasntModified error
        text = text.replace(' ', 'ᅠ')  # invisible char
    else:
        pass

    mes = ''
    for char in text:
        mes += '|'
        await ans.api.messages.edit(ans.peer_id, ans.id, mes)
        await asyncio.sleep(0.04)
        mes = mes[:-1] + char
        await ans.api.messages.edit(ans.peer_id, ans.id, mes)
        await asyncio.sleep(0.02)