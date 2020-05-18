from vkbottle import Message


async def edit(ans: Message, text: str):
    data = ans.__dict__
    keys_to_pop = [
        "message",
        "flags",
        "timestamp",
        "text",
        "random_id",
        "id",
        "conversation_message_id",
        "from_id",
        "date",
        "out",
        "read_state",
        "ref",
        "ref_source",
        "important",
        "reply_message",
        "fwd_messages",
        "action",
    ]
    for key in keys_to_pop:
        data.pop(key, None)
    if ans.geo is not None:
        lat, long = ans.geo.coordinates.latitude, ans.geo.coordinates.longitude
        data["lat"] = lat
        data["long"] = long
    data.pop("geo", None)
    await ans.api.messages.edit(
        message=text,
        attachment=",".join(data.pop("attachments")),
        **data,
        keep_forward_messages=True
    )
