import discord
from discord import app_commands
from discord.ext import commands

class Boss(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('Bosses.py is ready!')

    @app_commands.command(name="weakly_bosses", description="عرض معلومات البوسات الاسبوعية.")
    async def weakly_bosses(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__ألبوسات الاسبوعية__", color=discord.Color.dark_red())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2023/01/27/8009863/13ebeb0fc25544f85fa38dc0a3df75fa_6259355686552113902.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="normal_bosses", description="عرض معلومات البوسات اليومية.")
    async def normal_bosses(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__ألبوسات العادية__", color=discord.Color.dark_red())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/01/27/8009863/1d3df612a5911c1630c99af070873894_4839278243486211737.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="enemy", description="عرض معلومات الاعداء.")
    async def enemy(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__الاعداء__", color=discord.Color.dark_red())

        embed_message.set_author(name=f"Requested by {member}", icon_url=member.avatar)

        embed_message.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/01/27/8009863/8bd693c5ad6f9cd079b7217ec4d1ac2b_4245404404338141484.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

async def setup(client):
    await client.add_cog(Boss(client))