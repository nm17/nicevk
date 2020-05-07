from datetime import datetime

from vkbottle import Message

from nicevk.api import user, commands, nicevk_folder

import wget

import runpy

commands.append(".dl_mod <url> - download and execute plugin")


@user.on.message_handler(text=".dl_mod <url>")
async def help_(ans: Message, url: str):
    await ans.api.messages.edit(ans.peer_id, ans.id, f"Downloading...")

    out_path = (
        nicevk_folder / f"module_{datetime.now().isoformat().replace('.', ' ')}.py"
    )
    wget.download(url.strip(), out=out_path)

    runpy.run_path(out_path)

    await ans.api.messages.edit(
        ans.peer_id, ans.id, f"Downloaded and loaded the plugin"
    )
