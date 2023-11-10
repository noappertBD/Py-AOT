import discord
from auto import onready
from commands.classic import ping, say, servinfo, userinfo
from db.setup import *

set = [
    [
        "MTA0MDM2NTI0MDYzNTg4NzcxOA.GAgJsX.myKInNGENRaBEAtKK2VQ2RszRJZEp-hmEgqDJY",
        1040365240635887718,
        "dev",
    ],
    [
        "MTE3MjEzOTk2NzYxNTYxNTAzNw.GswdGF.C1mzQbvE3CzU8d1z2pSc5_gQ_DAzfW2YPrZdyg",
        871727190499262537,
        "main",
    ],
]

config = set[0]
v = "0.10"

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)


onready.setup(bot, v, config)

ping.setup(bot)
say.setup(bot)
servinfo.setup(bot, config)
userinfo.setup(bot)
# Lancement de discord.py
bot.run(config[0])
