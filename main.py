import time

import discord
from discord.ext import tasks

intents = discord.Intents.default()

client = discord.Client(intents=intents)

overwatch = time.strptime('2025-06-24 20:00:00', '%Y-%m-%d %H:%M:%S')
apex = time.strptime('2025-06-24 19:00:00', '%Y-%m-%d %H:%M:%S')

def format_time(seconds):
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0 or days > 0:
        parts.append(f"{hours}h")
    if minutes > 0 or hours > 0 or days > 0:
        parts.append(f"{minutes}m")
    return ' '.join(parts)

apex_channel_id = 1387106562786459788
overwatch_channel_id = 1387106497909227560

server_id = 791318411345920000

apex_channel = None
overwatch_channel = None

@client.event
async def on_ready():

    global apex_channel, overwatch_channel

    print(f'Logged in as {client.user}')
    server = client.get_guild(server_id)
    apex_channel = server.get_channel(apex_channel_id)
    overwatch_channel = server.get_channel(overwatch_channel_id)
    update_timers.start()

@tasks.loop(seconds=60)
async def update_timers():

    time_until_overwatch = time.mktime(overwatch) - time.time()
    time_until_apex = time.mktime(apex) - time.time()

    await overwatch_channel.edit(name=f"overwatch {format_time(time_until_overwatch)}")
    await apex_channel.edit(name=f"apex {format_time(time_until_apex)}")

    


client.run('im too lazy to set up a token im just going to manually paste it here when i clone to my server and im sure nothing will go wrong and theres no way ill accidentally push it to github')