import discord
import datetime
import time
import pytz

def setup(bot):
    class Modal(discord.ui.Modal):
        def __init__(self, title: str) -> None:
            super().__init__(title=title)
            self.add_item(discord.ui.InputText(label="Titre", required=False, placeholder="Titre"))
            self.add_item(discord.ui.InputText(label="Description", required=False, placeholder="Description", style=discord.InputTextStyle.long))
            self.add_item(discord.ui.InputText(label="Image", required=False, placeholder="URL"))
            self.add_item(discord.ui.InputText(label="Thumbnail", required=False, placeholder="URL"))
            self.add_item(discord.ui.InputText(label="Fields", required=False, placeholder="titre::description:::titre::description"))

        async def callback(self, interaction: discord.Interaction):
            titre = self.children[0].value
            description = self.children[1].value
            image = self.children[2].value
            thumbnail = self.children[3].value
            fields = self.children[4].value.split(":::")
            embed = discord.Embed(
                title="%(titre)s" % {"titre": titre} if titre is not None else None,
                description="%s" % description if description is not None else None,
                color=0x2265BF,
            )
            for field in fields:
                field = field.split("::")
                embed.add_field(name=field[0] if field[0] is not None else "", value=field[1] if field[1] is not None else "", inline=True)
            embed.set_thumbnail(url=thumbnail if thumbnail is not None else None)
            embed.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon)
            await interaction.response.send_message(embed=embed)

    
    @bot.slash_command(description="Envoyer un embed")
    async def embed(
        ctx,
    ):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.respond(
                "Les commandes slash ne sont pas autorisées en message privé."
            )
            return
        
        modal = Modal(title="Créer un embed")
        await ctx.send_modal(modal)
