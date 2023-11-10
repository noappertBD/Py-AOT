import discord
import datetime
import time
import pytz

def setup(bot):
    @bot.slash_command(description="Affiche le ping du bot")
    async def userinfo(
        ctx,
        membre: discord.Option(
            discord.Member,
            description="Ecrire un message à travers le bot",
        ),
    ):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.respond(
                "Les commandes slash ne sont pas autorisées en message privé."
            )
            return
        
        display_name = membre.display_name
        created_at = datetime.datetime.strptime(str(membre.created_at), "%Y-%m-%d %H:%M:%S.%f%z").astimezone(pytz.timezone("Europe/Paris"))
        joined_at = datetime.datetime.strptime(str(membre.joined_at), "%Y-%m-%d %H:%M:%S.%f%z").astimezone(pytz.timezone("Europe/Paris"))
        id = membre.id
        guildadmin = membre.guild_permissions.administrator
        mention = membre.mention
        avatar = membre.display_avatar.url
        roles = [f'<@&{role.id}>' for role in membre.roles]
        roles.pop(0)

        embed = discord.Embed(
            title="Informations sur `%s`" % display_name,
            description="`%s`" % id, 
            color=0x2265BF,
        )
        embed.set_thumbnail(url=avatar)
        embed.add_field(
            name="🌱 Compte créé le:", value="%(a)s\n➜ <t:%(b)s:R>" % {"a": created_at.strftime("%d/%m/%Y à %Hh%M"), "b": int(time.mktime(created_at.timetuple()))}, inline=False
        )
        embed.add_field(
            name="🎟️ Arrivé sur le serveur le:", value="%(a)s\n➜ <t:%(b)s:R>" % {"a": joined_at.strftime("%d/%m/%Y à %Hh%M"), "b": int(time.mktime(joined_at.timetuple()))}, inline=False
        )
        embed.add_field(
            name="🧷 Rôles: [%s]" % len(roles),
            value=", ".join(roles)
        )
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon)
        await ctx.respond(embed=embed)
