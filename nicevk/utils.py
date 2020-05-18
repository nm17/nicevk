from vkbottle.api import UserApi

api = UserApi.get_current()


def get_params(obj: dict) -> dict:
    return {
        k: v for k, v in obj.items()
        if v is not None and k != "params"
    }


async def edit(
    peer_id: int, msg_id: int,
    text: str, **params
):
    locals().update(params)
    return await api.messages.edit(
        **get_params(locals())
    )
