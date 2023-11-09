import discord
from auto import *
from db.setup import *

set = [
    [
        "MTA0MDM2NTI0MDYzNTg4NzcxOA.GAgJsX.myKInNGENRaBEAtKK2VQ2RszRJZEp-hmEgqDJY",
        1026567302499532882,
        1026567300448534579,
        "dev",
    ],
    [
        "MTE3MjEzOTk2NzYxNTYxNTAzNw.GswdGF.C1mzQbvE3CzU8d1z2pSc5_gQ_DAzfW2YPrZdyg",
        871727190499262537,
        871727190499262534,
        "main",
    ],
]

config = set[1]
v = 0.10

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

# Lancement de discord.py
bot.run(config[0])
