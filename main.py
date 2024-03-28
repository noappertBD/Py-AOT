import discord
from auto import onready
from commands.classic import ping, say, servinfo, userinfo, embed
from db.setup import *

set = [
    [
        <str:token bot>,
        <int:Channel ID for welcoming>,
        "dev",
    ],
    [
        <str:token bot (dev)>,
        <int:Test Channel ID for welcoming>,
        "main",
    ],
]

config = set[0]
v = "0.11"

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)


onready.setup(bot, v, config)

ping.setup(bot)
say.setup(bot)
servinfo.setup(bot, config)
userinfo.setup(bot)
embed.setup(bot)
# Lancement de discord.py
bot.run(config[0])
