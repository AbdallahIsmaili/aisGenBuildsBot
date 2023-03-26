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

    @commands.hybrid_command(name="test", description="This is test command")
    async def test(self, ctx: commands.Context):
        await ctx.send("/ayaka")




async def setup(client):
    await client.add_cog(HelpCommand(client))









# import discord
# from discord import app_commands
# from discord.ext import commands
# from discord.ui import View, Select
#
#
# class HelpSelect(Select):
#     def __init__(self, bot: commands.Bot):
#         super().__init__(
#             placeholder="Choose a Category",
#             options=[
#                 discord.SelectOption(
#                     label='Characters', description='Characters infos'
#                 ) for cog_name, cog in bot.cogs.items() if cog.__cog_commands__ and cog_name not in ['Jishaku']
#             ]
#         )
#
#         self.bot = bot
#
#     async def callback(self, interaction: discord.Interaction) -> None:
#         cog = self.bot.get_cog(self.values[0])
#         assert cog
#
#         commands_mixer = []
#         for i in cog.walk_commands():
#             commands_mixer.append(i)
#
#         for i in cog.walk_app_commands():
#             commands_mixer.append(i)
#
#         embed = discord.Embed(
#             title=f"{cog.__cog_name__} Commands",
#             description='\n'.join(
#                 f"**{command.name}**: `{command.description}`"
#                 for command in commands_mixer
#             )
#         )
#         await interaction.response.send_message(
#             embed=embed,
#             ephemeral=True
#         )
#
# class HelpCommand(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.Cog.listener()
#     async def on_ready(self):
#         await self.bot.tree.sync()
#         print('HelpCommand.py is ready!')
#
#     @commands.hybrid_command(name="help", description="قائمة المساعدة.")
#     async def help(self, ctx: commands.Context):
#
#         help_embed = discord.Embed(title="__aiGenshin Builds | Help Directory__", description="Select a category from the dropdown to view commands specific to that category.", color=discord.Color.gold())
#
#         help_embed.set_author(name="aiGenshin_Builds")
#
#         help_embed.set_thumbnail(
#             url="https://yoolk.ninja/wp-content/uploads/2021/08/Games-GenshinImpact-1024x1024.png")
#
#         help_embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2020/10/genshin-impact-beginning.jpg?q=50&fit=contain&w=1140&h=&dpr=1.5")
#
#         help_embed.add_field(name="Categories",
#                                 value=">  Builds \n > Characters \n > Weapons \n > Artifacts \n > Materials & Bosses",
#                                 inline=False)
#
#         view = View().add_item(HelpSelect(self.bot))
#
#
#         await ctx.send(embed=help_embed, view=view)
#
#
#     @commands.hybrid_command(name="test", description="This is test command")
#     async def test(self, ctx: commands.Context):
#         await ctx.send(10)
#
#
#
#
# async def setup(bot):
#     await bot.add_cog(HelpCommand(bot))