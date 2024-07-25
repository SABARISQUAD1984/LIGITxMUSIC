from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6799458147"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/a19810b838fb13e875d54.jpg")
START_IMG = getenv("https://graph.org/file/a19810b838fb13e875d54.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ITZZSABARISQUAD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ITZLOVETIME")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6953174731").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
