import os
import time
import asyncio
from config import Config
from pyrogram import Client,idle
from rich.console import Console
from rich.table import Table
from MassActionBot.utils.data import LOG_MSG

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.BOT_TOKEN
SUDOES = Config.BAN_PROTECTED
OWNER_ID = Config.OWNER_ID
START_PIC = Config.START_PIC
MONGO_DB = Config.MONGO_DB_URL
SUDOES.append(OWNER_ID)
if not START_PIC:
    START_PIC = "https://graph.org/file/c1c19fee2ac7b458087f7.jpg"
#rich
LOG = Console()

#time
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

#database
mongo = AsyncIOMotorClient(MONGO_DB)
db = mongo.AMSTARK


#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    



async def MassActionBot():
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(START_TEXT)
    LOG.print(header)
    LOG.print("[bold yellow]ɢᴇᴛᴛɪɴɢ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ.....")
    await app.start()
    bot = await app.get_me()
    BOT_ID = bot.id
    BOT_USERNAME = bot.username
    MENTION = bot.mention
    if bot.last_name:
        BOT_NAME = bot.first_name + " " + bot.last_name
    else:
       BOT_NAME = bot.first_name
    await asyncio.sleep(2)
    LOG.print("[bold yellow]ɢᴏᴛ ᴀʟʟ ᴛʜᴇ ɪɴғᴏ......")
    await asyncio.sleep(1)
    LOG.print(f"[bold cyan]ʙᴏᴛ ɪᴅ : {BOT_ID}\nʙᴏᴛ ɴᴀᴍᴇ : {BOT_NAME}\nʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ : {BOT_USERNAME}")
    await asyncio.sleep(0.5)
    


loop = asyncio.get_event_loop()
loop.run_until_complete(MassActionBot())    



    
    

    
    



