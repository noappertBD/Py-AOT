import discord

def setup(bot):
    @bot.slash_command(description="Affiche le ping du bot")
    async def ping(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.respond(
                "Les commandes slash ne sont pas autorisées en message privé."
            )
            return
        embed = discord.Embed(
            title="Pong 🏓",
            color=0x2265BF,
        )
        embed.add_field(
            name="Latence", value=f"{round(bot.latency * 1000, 1)}ms !", inline=False
        )
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon)
        await ctx.respond(embed=embed, ephemeral=True)
