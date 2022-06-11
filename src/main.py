# -*- coding: utf-8 -*-

import os
import json
import aiohttp
import asyncio
from colorama import Fore

token = input("Enter token: ")  # or you can change this to your token

# Setup variables
headers = {"Authorization": token}
api = "https://discord.com/api/v9"
#translator = googletrans.Translator()
with open('settings.json', 'r') as f: settings = json.load(f)
vanity = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

try:
    os.system('clear')
except:
    os.system('cls')


def process_user(user):
    return user.replace('<', '').replace('>', '').replace('@', '').replace('!', '').replace('?', '').replace('&', '')


async def cur_user():
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(f"{api}/users/@me", headers=headers) as usr:
                if usr.status == 429:
                    usr = await usr.json()
                    await asyncio.sleep(usr['retry_after'])
                else:
                    return await usr.json()


async def send(data, session, content):
    while True:
        async with session.post(f"{api}/channels/{data['d']['channel_id']}/messages", headers=headers, data={'content': content}) as msg:
            if msg.status == 429:
                msg = await msg.json()
                await asyncio.sleep(msg['retry_after'])
            else:
                break


async def delete_message(data, session):
    while True:
        async with session.delete(f"{api}/channels/{data['d']['channel_id']}/messages/{data['d']['id']}", headers=headers) as msg:
            if msg.status == 429:
                msg = await msg.json()
                await asyncio.sleep(msg['retry_after'])
            else:
                break


async def purge(data, session, amount):
    count = 0
    while True:
        async with session.get(f"{api}/channels/{data['d']['channel_id']}/messages?limit=100", headers=headers) as prg:
            if prg.status == 429:
                prg = await prg.json()
                await asyncio.sleep(prg['retry_after'])
            else:
                prg = await prg.json()
                break

    for msg in prg:
        print(msg['author']['id'] == data['d']['author']['id'])
        if msg['author']['id'] == data['d']['author']['id']:
            print(msg)
            while True:
                async with session.delete(f"{api}/channels/{data['d']['channel_id']}/messages/{msg['id']}",headers=headers) as del_:
                    print(del_.status)
                    if del_.status == 429:
                        del_ = await msg.json()
                        await asyncio.sleep(del_['retry_after'])
                    else:
                        break
            count+=1

        if count >= amount:
            break


async def get_user(id, session):
    while True:
        async with session.get(f"{api}/users/{id}", headers=headers) as user:
            if user.status == 429:
                user = await user.json()
                await asyncio.sleep(user['retry_after'])
            else:
                return await user.json()


async def heartbeat(ws, interval):
    while True:
        await asyncio.sleep(interval / 1000)
        await ws.send_json({"op": 1, "d": "null"})


async def main(token):
    usr = await cur_user()
    print(f"""{Fore.MAGENTA}████████╗███████╗██████╗ ██████╗  ██████╗ ██████╗ ██╗███████╗███╗   ███╗    ███████╗██████╗ 
{Fore.LIGHTMAGENTA_EX}╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║██╔════╝████╗ ████║    ██╔════╝██╔══██╗
{Fore.BLUE}   ██║   █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝██║███████╗██╔████╔██║    ███████╗██████╔╝
{Fore.LIGHTBLUE_EX}   ██║   ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗██║╚════██║██║╚██╔╝██║    ╚════██║██╔══██╗
{Fore.CYAN}   ██║   ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║██║███████║██║ ╚═╝ ██║    ███████║██████╔╝
{Fore.LIGHTCYAN_EX}   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝    ╚══════╝╚═════╝ 
   Prefix is {settings['Prefix']}
{Fore.LIGHTGREEN_EX}   Connected to {usr['username']}#{usr['discriminator']}{Fore.RESET}""")
    async with aiohttp.ClientSession() as session:
        # Yes I use v6, cope harder you discord.py coders
        async with session.ws_connect("wss://gateway.discord.gg?v=6&encoding=json") as ws:
            await ws.send_json({"op": 2, "d": {"token": token, "properties": {"$os": "linux", "$browser": "my_library","$device": "my_library"}}})
            async for messages in ws:

                data = json.loads(messages.data)

                if data["op"] == 10:
                    asyncio.ensure_future(heartbeat(ws, data['d']['heartbeat_interval']))

                elif data["op"] == 0:
                    if data['t'] == 'MESSAGE_CREATE' and data['d']['author']['id'] == usr['id']:
                        content = data['d']['content']

                        if content.startswith(f"{settings['Prefix']}help"):
                            await delete_message(data, session)
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
                            await delete_message(data, session)
                            msgC = len(data['d']['content'].split()[1]) + len(settings['Prefix']) + 5
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

                        elif content.startswith(f"{settings['Prefix']}purge"):
                            await purge(data, session, int(content.split()[1]))

                        elif content.startswith(f"{settings['Prefix']}userinfo"):
                            await delete_message(data, session)
                            user_id = process_user(content.split()[1])
                            user = await get_user(user_id, session)
                            await send(data, session, f"{vanity}https://SachsSB.sachsthebased.repl.co/user/{user['id']}/{user['username'].replace(' ', '%20')}/test/test/{user['avatar']}")



loop = asyncio.get_event_loop()
loop.run_until_complete(main(token))
loop.close()
