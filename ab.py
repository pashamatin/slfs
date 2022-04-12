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
		em = "❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎"
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
		await event.edit("""𝚜𝚎𝚗𝚍 𝚢𝚘𝚞𝚛 𝚎𝚖𝚘𝚓𝚒 𝚗𝚎𝚡𝚝 𝚝𝚘 𝚝𝚑𝚎 𝚝𝚒𝚖𝚎 𝚕𝚒𝚔𝚎 : \nemoji ♥️ 💛 ✝️ """)
	if "emoji" in event.raw_text:
		emo = event.raw_text.replace("emoji",'')
		await event.edit(f"""𝕐𝕠𝕦𝕣 𝕖𝕞𝕠𝕛𝕚 𝕊𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝𝕝𝕪 𝕔𝕙𝕒𝕟𝕘𝕖𝕕 \n{emo}""")
		c = open("emoji.txt","w")
		c.write(str(emo))
		c.close()

@aiocron.crontab('*/1 * * * *')
async def s():
	x = open("emoji.txt")
	emoji = x.readline()
	x.close()
	iran = pytz.timezone("Asia/Tehran")
	time=str(datetime.now(iran).strftime("▹%H⦂%M"))+" "+str(random.choice(emoji.split()))
	fonts = [
    {"0":"𝟘","1":"𝟙","2":"𝟚","3":"𝟛","4":"𝟜","5":"𝟝","6":"𝟞","7":"𝟟","8":"𝟠","9":"𝟡"},
    {"0":"𝟎","1":"𝟏","2":"𝟐","3":"𝟑","4":"𝟒","5":"𝟓","6":"𝟔","7":"𝟕","8":"𝟖","9":"𝟗"},
    ]
	for i , j in random.choice(fonts).items():
		time = time.replace(i, j)

	await unknown(UpdateProfileRequest(last_name=time, about=str(time)))
# ============= #
unknown.start()
s.start()
unknown.run_until_disconnected()
asyncio.get_event_loop().run_forever()