from vkbottle import Message

from nicevk.api import user, commands

import subprocess

commands.append(".neofetch")


@user.on.message_handler(text=".neofetch")
async def help_(ans: Message):
    rst = subprocess.run(["neofetch", "os", "distro", "uptime", "disk", "wm", "memory"], capture_output=True)

    await ans.api.messages.edit(ans.peer_id, ans.id, rst.stdout.decode("utf-8"))
