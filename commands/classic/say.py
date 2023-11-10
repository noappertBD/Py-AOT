import discord


def setup(bot):
    @bot.slash_command(description="Affiche le ping du bot")
    async def say(
        ctx,
        message: discord.Option(
            description="Ecrire un message à travers le bot",
        ),
    ):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.respond(
                "Les commandes slash ne sont pas autorisées en message privé."
            )
            return

        await ctx.respond("Votre message a été envoyé ✅", ephemeral=True)
        await ctx.send(message)
