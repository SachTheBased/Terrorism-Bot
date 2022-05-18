import os
import json
import discord

try:
  import aiohttp
  import asyncio
except:
  os.system("pip install aiohttp")
  import aiohttp
  import asyncio

token = input("Enter token: ")
headers = {"Authorization": token}
sachs = discord.User(headers)
vanity = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

try: os.system('clear')
except: os.system('cls')

print("""Welcome to Terrorism SB!!!

Prefix -> $
      
Devs Against Nukers""")

async def heartbeat(ws, interval):
  while True:
    await asyncio.sleep(interval / 1000)
    await ws.send_json({"op": 1,"d": "null"})

async def main(token):
  async with aiohttp.ClientSession() as session:
    # Yes I use v6, cope harder you discord.py coders
    async with session.ws_connect("wss://gateway.discord.gg?v=6&encoding=json") as ws:
      await ws.send_json({"op": 2,"d": {"token": token, "properties": {"$os": "linux","$browser": "my_library","$device": "my_library"}}})
      async for messages in ws:
        data = json.loads(messages.data)
        ctx = discord.Context(json.loads(messages.data), headers = headers)
        if data["op"] == 10:
          asyncio.ensure_future(heartbeat(ws, data['d']['heartbeat_interval']))
        elif data["op"] == 0:
          if data['t'] == 'MESSAGE_CREATE':
            if data['d']['content'].startswith("$help"):
              await ctx.delete_message()
              if len(data['d']['content'].split()) == 1:
                await ctx.send(f"{vanity}https://tt.sachsthebased.repl.co/help/_main_.html")
              else:
                if data['d']['content'].split()[1].lower() == 'exploits' or data['d']['content'].split()[1].lower() == 'exp' or data['d']['content'].split()[1].lower() == 'exploit':
                  await ctx.send(f"{vanity}https://tt.sachsthebased.repl.co/help/exploits.html")
                elif data['d']['content'].split()[1].lower() == 'utilities' or data['d']['content'].split()[1].lower() == 'utils' or data['d']['content'].split()[1].lower() == 'util' or data['d']['content'].split()[1].lower() == 'utility':
                  await ctx.send(f"{vanity}https://tt.sachsthebased.repl.co/help/utils.html")
                elif data['d']['content'].split()[1].lower() == 'nuke':
                  # Kids don't get into nuking
                  # Atleast i didn't make this fast you guys can salvage your dms
                  await ctx.send(f"```LMAO WIGGA TRIED TO NUKE!!!```")
                  tasks = []
                  dms = await sachs.get_channels()
                  """
                  for dm in dms:
                    dee_m = discord.Context({'d': {'id': dm['id']}}, headers = headers)
                    await dee_m.send("This is what happens when you try to nuke")
                  """
                  for dm in dms:
                    tasks.append(asyncio.create_task(sachs.delete_channel(dm['id'])))
                  await asyncio.gather(*tasks)
            elif data['d']['content'].startswith("$spam"):
              content = 7 + len(data['d']['content'].split()[1])
              if data['d']['content'].split()[1] == 'inf':
                while True:
                  tasks = []
                  for i in range(7):
                    tasks.append(asyncio.create_task(ctx.send(data['d']['content'][content:])))
                  await asyncio.gather(*tasks)
              else:
                tasks = []
                for i in range(int(data['d']['content'].split()[1])):
                  tasks.append(asyncio.create_task(ctx.send(data['d']['content'][content:])))
                await asyncio.gather(*tasks)
            
        
loop = asyncio.get_event_loop()
loop.run_until_complete(main(token))
loop.close()