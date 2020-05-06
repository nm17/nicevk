from pathlib import Path

from vkbottle import User
import dotenv

nicevk_folder = Path.home().joinpath("nicevk").absolute()

env = dotenv.dotenv_values(str(nicevk_folder.joinpath(".env")))

user = User(env["TOKEN"])
