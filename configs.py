import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "1615127"))
  API_HASH = os.environ.get("API_HASH", "566474478c929ad4bd441c0bd269531c")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6318429756:AAHKYzltAqO9K2pjG2739liar-4k_eBGOmU
")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shorturlsxyzbot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002100631240"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "shorturls.zyx")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "712573408"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Zoroxtobot:dhj0BqA8i3LdxAM2@zorox.u8fbufy.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001997021949")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002093432457"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Rockstar](https://t.me/Reddotmovies)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Reddotmovies)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
