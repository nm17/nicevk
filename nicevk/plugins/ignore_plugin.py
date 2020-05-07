from vkbottle import Message

from nicevk.api import user, commands, state, save_state

commands.extend(
    [
        ".ignore <username> - delete all messages from specified user",
        ".rm-ignore <username>",
    ]
)


@user.on.message_handler(text=".ignore <username>")
async def help_(ans: Message, username: str):
    if state.get("ignore", None) is None:
        state["ignore"] = []

    state["ignore"] = [
        *state["ignore"],
        (
            await ans.api.utils.resolve_screen_name(screen_name=username.strip())
        ).object_id,
    ]
    save_state()
    await ans.api.messages.edit(ans.peer_id, ans.id, "User ignored")


@user.on.message_handler(text=".rm-ignore <username>")
async def help_(ans: Message, username: str):
    if state.get("ignore", None) is None:
        state["ignore"] = []

    try:
        del state["ignore"][
            state["ignore"].index(
                (
                    await ans.api.utils.resolve_screen_name(
                        screen_name=username.strip()
                    )
                ).object_id
            )
        ]
    except ValueError:
        await ans.api.messages.edit(ans.peer_id, ans.id, "That user is not muted")
    else:
        await ans.api.messages.edit(ans.peer_id, ans.id, "User removed from ignore")
    finally:
        save_state()


@user.on.message_handler()
async def middleware(message: Message):
    if message.from_id in state.get("ignore", []):
        await message.api.messages.delete([message.id])
