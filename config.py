from typing import Optional

from omegaconf import OmegaConf

__config: Optional[OmegaConf] = None


def get_state():
    if __config is None:
        __state = OmegaConf().load("config")
    return __config


def merge_config(other: OmegaConf):
    global __config
    __config = __config.merge(other)
