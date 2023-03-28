import discord
from discord import app_commands
from discord.ext import commands
import random

class Builds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('Builds.py is ready!')

    @app_commands.command(name="ayaka_f2p", description="عرض بيلد شخصية اياكا.")
    async def ayaka_f2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        ayaka_f2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089800120482136154/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089751851219550218/character_info_overview.png",
            "https://media.discordapp.net/attachments/1063698601949282354/1089630271726440618/character_info_overview.png?width=491&height=430",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089619229663313971/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089549884350279799/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089904533523681300/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089549884350279799/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089472753192677466/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089371479944208455/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089263939856121987/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Ayaka build f2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(ayaka_f2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="ayaka_p2p", description="عرض بيلد شخصية اياكا.")
    async def ayaka_p2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        ayaka_p2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089405523939561593/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089999777967636621/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089405523939561593/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Ayaka build p2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(ayaka_p2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)


# RAIDEN

    @app_commands.command(name="raiden_f2p", description="عرض بيلد شخصية بال.")
    async def raiden_f2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        raiden_f2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698658358472764/1089196240144711760/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089810351404625940/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089342053361655948/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Raiden build f2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(raiden_f2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="raiden_p2p", description="عرض بيلد شخصية بال.")
    async def raiden_p2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        raiden_p2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089233989321105560/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698658358472764/1089352315363926096/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089547124426936422/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089586486581674144/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089989635859546122/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089958113215512707/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Raiden build p2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(raiden_p2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)





# NAHIDA

    @app_commands.command(name="nahida_f2p", description="عرض بيلد شخصية ناهيدا.")
    async def nahida_f2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        nahida_f2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089985651266568303/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089933834944000000/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698658358472764/1089573355457368175/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089395097327648778/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Nahida build f2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(nahida_f2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="nahida_p2p", description="عرض بيلد شخصية ناهيدا.")
    async def nahida_p2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        nahida_p2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089647464497295390/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089432586616590346/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Nahida build p2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(nahida_p2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)


# YELAN

    @app_commands.command(name="yelan_f2p", description="عرض بيلد شخصية يلان.")
    async def yelan_f2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        yelan_f2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089550793599897631/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Yelan build f2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(yelan_f2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="yelan_p2p", description="عرض بيلد شخصية يلان.")
    async def yelan_p2p(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        yelan_p2p_builds = [
            "https://cdn.discordapp.com/attachments/1063698629833007145/1089986620486320218/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698601949282354/1089933961528094751/character_info_overview.png",
            "https://cdn.discordapp.com/attachments/1063698658358472764/1089763978168782911/character_info_overview.png"
        ]

        embed_message = discord.Embed(title="__Yelan build p2p__", color=discord.Color.random())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        random_url = random.choice(yelan_p2p_builds)
        embed_message.set_image(url=random_url)

        embed_message.set_footer(text="يرجى فتح الصورة بالضغط عليها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

async def setup(client):
    await client.add_cog(Builds(client))