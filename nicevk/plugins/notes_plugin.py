from vkbottle import Message

from nicevk.api import user, commands, state, save_state

commands.extend([".notes <name> - get note by name", ".notes - get all notes", ".save-note <name> <text> - save/edit note"])


@user.on.message_handler(text=".notes")
async def lsit_notes(ans: Message):
    await ans.api.messages.edit(ans.peer_id, ans.id, f"Available notes:\n\n" + "\n".join(state["notes"].keys()))


@user.on.message_handler(text=".notes <name>")
async def get_notes(ans: Message, name: str):
    if name in state["notes"].keys():
        await ans.api.messages.edit(ans.peer_id, ans.id, f"Note '{name}'\n\n{state['notes'][name]}")
    else:
        await ans.api.messages.edit(ans.peer_id, ans.id, f"Note '{name}' is not found")


@user.on.message_handler(text=".save-note <name> <text>")
async def save_notes(ans: Message, name: str, text: str):
    state["notes"][name] = text
    await ans.api.messages.edit(ans.peer_id, ans.id, f"Note '{name}' saved!")
    save_state()
