from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "6011060332"))
    API_HASH = getenv("API_HASH", "2714bb3f30047b5ee5de230df7fed021")
    BOT_TOKEN = getenv("BOT_TOKEN", "6128248580:AAEvDCI97ZTihO2zksL7MQuRsY2BmWbQodo")

config = Config()
