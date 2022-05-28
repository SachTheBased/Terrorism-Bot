import aiohttp
import asyncio


class Context:
    def __init__(self, context, headers):
        self.context = context
        self.headers = headers
        self.api = "https://discord.com/api/v9"

    async def info(self):
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(f'{self.api}/users/@me', headers=self.headers) as user:
                    if user.status == 429:
                        user = await user.json()
                        asyncio.sleep(user['retry_after'])
                    else:
                        return await user.json()

    async def send(self, msg):
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.post(f'{self.api}/channels/{self.context["d"]["channel_id"]}/messages',
                                        headers=self.headers, json={'content': msg}) as message:
                    if message.status == 429:
                        message = await message.json()
                        asyncio.sleep(message['retry_after'])
                    else:
                        break

    async def delete_message(self):
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.delete(
                        f'{self.api}/channels/{self.context["d"]["channel_id"]}/messages/{self.context["d"]["id"]}',
                        headers=self.headers) as delete:
                    if delete.status == 429:
                        delete = await delete.json()
                        asyncio.sleep(delete['retry_after'])
                    else:
                        break

    async def purge(self, amount, data):
        count = 0
        #id = await self.info()['id']
        print(f'{self.api}/{self.context["d"]["channel_id"]}/messages')
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(f'{self.api}/channels/{data["d"]["channel_id"]}/messages',headers=self.headers) as msg:
                    if msg.status == 429:
                        msg = await msg.json()
                        asyncio.sleep(msg['retry_after'])
                    else:
                        msg = await msg.json()
                        print(msg)
                        break
            for m in msg:
                if m['author']['id'] == "957021168156688395":
                    if count == amount:
                        break
                    while True:
                        async with session.delete(
                                f'{self.api}/channels/{data["d"]["channel_id"]}/messages/{m["id"]}',
                                headers=self.headers) as delete:
                            if delete.status == 429:
                                delete = await delete.json()
                                asyncio.sleep(delete['retry_after'])
                            else:
                                break
                    count += 1


class User:
    def __init__(self, headers):
        self.headers = headers
        self.api = "https://discord.com/api/v9"

    async def get_channels(self):
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(f"{self.api}/users/@me/channels", headers=self.headers) as ch:
                    if ch.status == 429:
                        ch = await ch.json()
                        asyncio.sleep(ch['retry_after'])
                    else:
                        return await ch.json()

    async def delete_channel(self, id):
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.delete(f"{self.api}/users/@me/channels/{id}", headers=self.headers) as ch:
                    if ch.status == 429:
                        ch = await ch.json()
                        asyncio.sleep(ch['retry_after'])
                    else:
                        break
