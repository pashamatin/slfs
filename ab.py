from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions, events
from datetime import datetime
import pytz ,aiocron, asyncio, random, os
from telethon.tl.functions.account import UpdateProfileRequest
# ============= #
api_id, api_hash = 2909555, "34ca9900dd5223fbc7b3e9a305764c3f"
# ============= #
try:
	if not "emoji.txt" in os.listdir():
		x = open("emoji.txt","w")
		em = "โค๏ธ ๐งก ๐ ๐ ๐ ๐ ๐ค ๐ค ๐ค"
		x.write(str(em))
		x.close()
except:
	None
# ============= #
unknown = TelegramClient("unknoenTime", api_id, api_hash)
# ============= #
@unknown.on(events.NewMessage(outgoing=True))
async def get(event):
	if event.raw_text == "help":
		await event.edit("""๐๐๐๐ ๐ข๐๐๐ ๐๐๐๐๐ ๐๐๐ก๐ ๐๐ ๐๐๐ ๐๐๐๐ ๐๐๐๐ : \nemoji โฅ๏ธ ๐ โ๏ธ """)
	if "emoji" in event.raw_text:
		emo = event.raw_text.replace("emoji",'')
		await event.edit(f"""๐๐ ๐ฆ๐ฃ ๐๐๐ ๐๐ ๐๐ฆ๐๐๐๐ค๐ค๐๐ฆ๐๐๐ช ๐๐๐๐๐๐๐ \n{emo}""")
		c = open("emoji.txt","w")
		c.write(str(emo))
		c.close()

@aiocron.crontab('*/1 * * * *')
async def s():
	x = open("emoji.txt")
	emoji = x.readline()
	x.close()
	iran = pytz.timezone("Asia/Tehran")
	time=str(datetime.now(iran).strftime("โน%Hโฆ%M"))+" "+str(random.choice(emoji.split()))
	fonts = [
    {"0":"๐","1":"๐","2":"๐","3":"๐","4":"๐","5":"๐","6":"๐","7":"๐","8":"๐ ","9":"๐ก"},
    {"0":"๐","1":"๐","2":"๐","3":"๐","4":"๐","5":"๐","6":"๐","7":"๐","8":"๐","9":"๐"},
    ]
	for i , j in random.choice(fonts).items():
		time = time.replace(i, j)

	await unknown(UpdateProfileRequest(last_name=time, about=str(time)))
# ============= #
unknown.start()
s.start()
unknown.run_until_disconnected()
asyncio.get_event_loop().run_forever()