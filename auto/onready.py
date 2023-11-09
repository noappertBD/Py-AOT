import contextlib
import discord
import asyncio
from db.setup import Users


def setup(bot, v, config):
    activities = [
        discord.Activity(type=discord.ActivityType.competing, name=f"version {v}"),
        discord.Activity(type=discord.ActivityType.watching, name="BlueDistrict"),
        discord.Activity(
            type=discord.ActivityType.playing,
            name="MàJ Moderation",
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

        if server is not None:
            members = server.members

            # Parcourir tous les membres et les mettre à jour dans la bdd
            for member in members:
                verify = Users.selectBy(userId=member.id)
                if not member.bot:
                    if verify.count() == 0:
                        Users(
                            arrivedAt=member.joined_at.strftime("%d-%m-%Y %H:%M:%S"),
                            pseudo=member.name,
                            userId=member.id,
                            isMuted=str(False),
                            isThere=str(True),
                            isBanned=str(False),
                            warns=0,
                            kicks=0,
                            bans=0,
                        )
                        print(f"{member.name} a été enregistré")
                    else:
                        if verify[0].isThere != str(True):
                            verify[0].isThere = str(True)
                            print(f"{member.name} a été édité [isThere > True]")
                        if verify[0].pseudo != member.name:
                            verify[0].pseudo = member.name
                            print(f"{member.name} a été édité [pseudo remis à jour]")

            def search(nom_recherche):
                for membre in members:
                    if membre.name == nom_recherche:
                        return True
                return False

            isReallyThere = Users.selectBy(isThere=str(True))
            for user in isReallyThere:
                if not search(user.pseudo):
                    user.isThere = str(False)
                    print(f"{user.pseudo} a été édité [isThere > False]")
        else:
            print("Serveur introuvable.")
        bot.loop.create_task(change_activity())
