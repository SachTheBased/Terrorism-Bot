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

async def heartbeat(ws, interval):
  while True:
    await asyncio.sleep(interval / 1000)
    await ws.send_json({"op": 1,"d": "null"})

async def main(token):
  async with aiohttp.ClientSession() as session:
    # Yes I use v6, cope harder you discord.py coders
    async with session.ws_connect("wss://gateway.discord.gg?v=6&encoding=json") as ws:
      await ws.send_json({""})
      async for messages in ws:
        ctx = discord.Context(json.load(messages))
