import random
from abc import abstractmethod, ABC
from copy import copy

from vk_api import VkApi
from vk_api.longpoll import Event


class LongPollPlugin(ABC):
    def __init__(self, api: VkApi):
        super().__init__()
        self.api = api
        self.commands = {}
        self.event_handlers = []

    @abstractmethod
    def on_event(self, event: Event):
        pass

    def answer(self, event: Event, message: str):
        data = copy(event.__dict__)
        data.pop("message", None)
        data.pop("type", None)
        data.pop("random_id", None)
        self.api.messages.send(message=message, random_id=random.randint(0, 999999), **data)

    def delete(self, event: Event, spam: bool = False):
        self.api.messages.delete(message_ids=event.message_id, spam=spam)

    def edit(self, event: Event, message: str):
        data = copy(event.__dict__)
        data.pop("type", None)
        data.pop("message", None)
        self.api.messages.edit(**data, message=message)
