import aiohttp
import asyncio

class Context:
  def __init__(self, context, headers):
    self.context = context
    self.headers = headers
    self.api = "https://discord.com/api/v9"

  async def send(self, msg):
    async with aiohttp.ClientSession() as session:
      while True:
        async with session.post(f'{self.api}/channels/{self.context["d"]["channel_id"]}/messages', headers = self.headers, json = {'content': msg}) as message:
          if message.status == 429:
            message = await message.json()
            asyncio.sleep(message['retry_after'])
          else:
            break

  async def delete_message(self):
    async with aiohttp.ClientSession() as session:
      while True:
        async with session.delete(f'{self.api}/channels/{self.context["d"]["channel_id"]}/messages/{self.context["d"]["id"]}', headers = self.headers) as delete:
          if delete.status == 429:
            delete = await delete.json()
            asyncio.sleep(delete['retry_after'])
          else:
            break
