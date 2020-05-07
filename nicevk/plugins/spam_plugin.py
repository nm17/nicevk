from vkbottle import Message

from nicevk.api import user, commands

commands.append(".spam <amount> <text> - spam chat with messages")


@user.on.message_handler(text=".spam <amount> <text>")
async def help_(ans: Message, amount: str, text: str):
    amount = int(amount)
    await user.api.messages.delete([ans.id], delete_for_all=True)
    for i in range(amount):
        await ans(text)
