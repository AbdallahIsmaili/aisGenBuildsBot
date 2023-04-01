import discord
from discord import app_commands
from discord.ext import commands

class MyArtifacts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('MyArtifacts.py is ready!')

    @app_commands.command(name="crimson", description="ارتيفاكت الكريمزون.")
    async def crimson(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__Crimson witch of flames | ارتيفاكت__", color=discord.Color.dark_red())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/71adfe450e57328660b6a2dee07a2433_6931520162347674420.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.add_field(name="الشخصيات المناسبة :",
                                value="> Hu Tao \n > Diluc \n > Klee \n > Yanfie \n > Yoe mia \n > Dehya ",
                                inline=False)

        await interactions.response.send_message(embed=embed_message)


async def setup(client):
    await client.add_cog(MyArtifacts(client))
