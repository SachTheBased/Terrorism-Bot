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
id = input("Enter your id: ")
headers = {"Authorization": token}
vanity = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

print("""Welcome to Terrorism SB!!!

Prefix -> $""")

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
          if data['t'] == 'MESSAGE_CREATE' and data['d']['author']['id']:
            if data['d']['content'].startswith("$help"):
              await ctx.delete_message()
              if len(data['d']['content'].split()) == 1:
                await ctx.send(f"{vanity}https://tt.sachsthebased.repl.co/help/main_.html")
        
loop = asyncio.get_event_loop()
loop.run_until_complete(main(token))
loop.close()
