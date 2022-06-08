import os
import json

try:
    import aiohttp
    import asyncio
    import googletrans
except:
    os.system("pip install aiohttp")
    os.system("pip install googletrans")
    import aiohttp
    import asyncio
    import googletrans

translator = googletrans.Translator()

with open('settings.json', 'r') as f: settings = json.load(f)
token = input("Enter token: ")
headers = {"Authorization": token}
api = "https://discord.com/api/v9"
vanity = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

try:
    os.system('clear')
except:
    os.system('cls')

print(f"""Welcome to Terrorism SB!!!

Prefix -> {settings['Prefix']}

Devs Against Nukers <3""")


async def send(data, session, content):
    while True:
        async with session.post(f"{api}/channels/{data['d']['channel_id']}/messages", headers=headers,
                                data={'content': content}) as msg:
            if msg.status_code == 429:
                msg = await msg.json()
                await asyncio.sleep(msg['retry_after'])
            else:
                break


async def heartbeat(ws, interval):
    while True:
        await asyncio.sleep(interval / 1000)
        await ws.send_json({"op": 1, "d": "null"})


async def main(token):
    async with aiohttp.ClientSession() as session:
        # Yes I use v6, cope harder you discord.py coders
        async with session.ws_connect("wss://gateway.discord.gg?v=6&encoding=json") as ws:
            await ws.send_json({"op": 2, "d": {"token": token, "properties": {"$os": "linux", "$browser": "my_library",
                                                                              "$device": "my_library"}}})
            async for messages in ws:

                data = json.loads(messages.data)

                if data["op"] == 10:
                    asyncio.ensure_future(heartbeat(ws, data['d']['heartbeat_interval']))
                elif data["op"] == 0:
                    if data['t'] == 'MESSAGE_CREATE':
                        content = data['d']['content']
                        if content.startswith(f"{settings['Prefix']}help"):

                            if len(content.split()) == 1:
                                await send(data, session, f"{vanity}https://tt.sachsthebased.repl.co/help/_main_.html")
                            else:
                                if content.split()[1].lower() == 'exploits' or data['d']['content'].split()[1].lower() == 'exp' or data['d']['content'].split()[1].lower() == 'exploit':
                                    await send(data, session, f"{vanity}https://tt.sachsthebased.repl.co/help/exploits.html")
                                elif content.split()[1].lower() == 'utilities' or content.split()[1].lower() == 'utils' or content.split()[1].lower() == 'util' or content.split()[1].lower() == 'utility':
                                    await send(data, session, f"{vanity}https://tt.sachsthebased.repl.co/help/utils.html")
                                elif content.split()[1].lower() == 'nuke':
                                    pass

                        elif content.startswith(f"{settings['Prefix']}spam"):
                            msgC = len(data['d']['content'].split()[1]) + len(settings['prefix']) + 5
                            if content.split()[1] == 'inf':
                                while True:
                                    tasks = []
                                    for i in range(7):
                                        tasks.append(asyncio.create_task(send(data, session, content[msgC:])))
                                    await asyncio.gather(*tasks)
                            else:
                                tasks = []
                                for i in range(int(content.split()[1])):
                                    tasks.append(asyncio.create_task(send(data, session, content[msgC:])))
                                await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(token))
loop.close()
