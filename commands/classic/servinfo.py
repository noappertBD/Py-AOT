import discord
import datetime
import time
import pytz

def setup(bot, config):
    @bot.slash_command(description="Affiche les infos du serveur")
    async def servinfo(
        ctx,
    ):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.respond(
                "Les commandes slash ne sont pas autorisées en message privé."
            )
            return
        
        server = ctx.guild
        display_name = server.name
        created_at = datetime.datetime.strptime(str(server.created_at), "%Y-%m-%d %H:%M:%S.%f%z").astimezone(pytz.timezone("Europe/Paris"))
        membot = await server.fetch_member(config[1])
        joined_at = datetime.datetime.strptime(str(membot.joined_at), "%Y-%m-%d %H:%M:%S.%f%z").astimezone(pytz.timezone("Europe/Paris"))
        id = server.id
        guildowner = server.owner
        avatar = server.icon.url
        roles = [f'<@&{role.id}>' for role in server.roles]
        roles.pop(0)

        embed = discord.Embed(
            title="%(servername)s (%(id)s)" % {"servername": display_name, "id": id},
            color=0x2265BF,
        )
        embed.set_thumbnail(url=avatar)
        embed.add_field(
            name="🌱 Serveur créé le:", value="%(a)s\n➜ <t:%(b)s:R>" % {"a": created_at.strftime("%d/%m/%Y à %Hh%M"), "b": int(time.mktime(created_at.timetuple()))}, inline=False
        )
        embed.add_field(
            name="🎟️ Arrivé du bot le:", value="%(a)s\n➜ <t:%(b)s:R>" % {"a": joined_at.strftime("%d/%m/%Y à %Hh%M"), "b": int(time.mktime(joined_at.timetuple()))}, inline=False
        )
        embed.add_field(
            name="🧷 Rôles: [%s]" % len(roles),
            value=", ".join(roles),
            inline=False
        )
        embed.add_field(
            name="🧮 Membres:",
            value="%(membres)s Membres • %(bots)s Bots" % {"membres": len([member for member in server.members if not member.bot]), "bots": len([member for member in server.members if member.bot])},
            inline=False
        )
        embed.add_field(
            name="👑 Owner",
            value=("%s" % guildowner.mention),
            inline=False
        )
        await ctx.respond(embed=embed)
