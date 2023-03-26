import discord
from discord import app_commands
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('HelpCommand.py is ready!')

    @app_commands.command(name="help", description="قائمة المساعدة.")
    async def help(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        help_embed = discord.Embed(title="__aiGenshin Builds | Help Directory__", description="Select a category from the dropdown to view commands specific to that category.", color=discord.Color.gold())

        help_embed.set_author(name="aiGenshin_Builds", icon_url=member.avatar)

        help_embed.set_thumbnail(
            url="https://yoolk.ninja/wp-content/uploads/2021/08/Games-GenshinImpact-1024x1024.png")

        help_embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2020/10/genshin-impact-beginning.jpg?q=50&fit=contain&w=1140&h=&dpr=1.5")

        help_embed.add_field(name="Categories",
                                value=">  Builds \n > Characters \n > Weapons \n > Artifacts \n > Materials & Bosses",
                                inline=False)


        await interactions.response.send_message(embed=help_embed)

async def setup(client):
    await client.add_cog(HelpCommand(client))