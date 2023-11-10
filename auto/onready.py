import contextlib
import discord
import asyncio
from db.setup import Users


def setup(bot, v, config):
    activities = [
        discord.Activity(type=discord.ActivityType.competing, name=f"version {v}"),
        discord.Activity(type=discord.ActivityType.watching, name="Académie Lierge"),
        discord.Activity(
            type=discord.ActivityType.playing,
            name="by Aleod_BD",
        ),
    ]

    async def change_activity():
        while True:
            for activity in activities:
                with contextlib.suppress(ConnectionResetError):
                    await bot.change_presence(activity=activity)
                await asyncio.sleep(10)

    @bot.event
    async def on_ready():
        print(f"Connecté au flux: {bot.user}")
        server_id = config[2]  # Remplacez par l'ID de votre serveur
        server = bot.get_guild(server_id)
        bot.loop.create_task(change_activity())
