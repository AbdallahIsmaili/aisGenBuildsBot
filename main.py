# import random
import discord
from discord.ext import commands
import os
import asyncio
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

bot_status = cycle(["Type in '$help' for help ", "Type in '$build' for characters builds", "Type in '$ping' for see your internet conection speed"])

client.remove_command("help")

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity = discord.Game(next(bot_status)))

@client.event
async def on_ready():
    await client.tree.sync()
    print("Success: Bot is connected to Discord")
    change_status.start()


#
# class SelectMenu(discord.ui.View):
#     def __init__(self):
#         super().__init__()
#         self.select = discord.ui.Select(placeholder="Choose a Category...", options=self.options)
#         self.select.add_option(label="Characters", value="1", description="Characters infos")
#         self.select.add_option(label="Builds", value="2", description="Characters Builds")
#         self.select.add_option(label="Weapons", value="3", description="Weapons infos")
#         self.select.add_option(label="Artifacts", value="4", description="Artifacts infos")
#         self.select.add_option(label="Materials", value="5", description="Materials, Bosses and Domains")
#         self.add_child(self.select)
#
#     async def on_select(self, interaction: discord.Interaction, select: discord.ui.Select,):
#         if select.values[0] == "1":
#             await interaction.response.send_message(content='Characters infos')
#
#         elif select.values[0] == "2":
#             await interaction.response.send_message(content='Characters Builds')
#
#         elif select.values[0] == "3":
#             await interaction.response.send_message(content='Weapons infos')
#
#         elif select.values[0] == "4":
#             await interaction.response.send_message(content='Artifacts infos')
#
#         elif select.values[0] == "5":
#             await interaction.response.send_message(content='Materials, Bosses and Domains')
#
# @client.tree.command(name="category", description="Choose a category")
# async def category(interaction: discord.Interaction):
#     select_menu = SelectMenu()
#     await interaction.response.send_message(content="Select a category", view=select_menu)
#     await select_menu.wait()



@client.event
async def on_message(message):

    if message.content == "موارد ناهيدا":
        embed = discord.Embed(title="__موارد ناهيدا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/11/02/8009863/55d12a011269c2555e0bbab20b7b35f2_399522707123728967.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم ناهيدا":
        embed = discord.Embed(title="__تفريم ناهيدا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/11/02/8009863/55d12a011269c2555e0bbab20b7b35f2_399522707123728967.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    # MIKA

    elif message.content == "موارد ميكا":
        embed = discord.Embed(title="__موارد ميكا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/17/8009863/0ff3a3d4bb005c84fbfb9606477d2e8b_5405532243862875230.jpeg")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم ميكا":
        embed = discord.Embed(title="__تفريم ميكا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/17/8009863/a4414070ac168b3aa5fda5b28b27478c_2165131203885823379.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg")

        await message.channel.send(embed=embed)

    # DEHYA

    elif message.content == "موارد ديهيا":
        embed = discord.Embed(title="__موارد ديهيا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/02/23/8009863/60cbf0c807876c88530f1f006cc0f865_9068560319547316940.jpeg")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم ديهيا":
        embed = discord.Embed(title="__تفريم ديهيا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/02/23/8009863/be6be9682a3774c223871910445f4fb5_7121756865639388480.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg")

        await message.channel.send(embed=embed)

    # YAO YAO

    elif message.content == "موارد ياوياو":
        embed = discord.Embed(title="__موارد ياوياو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/01/16/8009863/1f5e9660016aa7d80079ce65c0973031_1911012795828672739.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم ياوياو":
        embed = discord.Embed(title="__تفريم ياوياو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/01/16/8009863/535414db3ad83e73c7b5985b1dc84ec1_458318167116439262.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    # ALHAITHAM

    elif message.content == "موارد الهيثم":
        embed = discord.Embed(title="__موارد الهيثم__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/01/20/8009863/fd89106aa2db3002f2637fe627f770ff_1777674659175936634.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم الهيثم":
        embed = discord.Embed(title="__تفريم الهيثم__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/01/20/8009863/48b1c318251be8386c1bf7447d42d2d2_5683158854411627436.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    # FAROZAN

    elif message.content == "موارد فاروزان":
        embed = discord.Embed(title="__موارد فاروزان__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/12/04/8009863/48ffa44f6fea4e2ed178a942387a8b57_8184980271641875672.jpeg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم فاروزان":
        embed = discord.Embed(title="__تفريم فاروزان__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/12/04/8009863/027ba065bfddce008463abfd609c2aed_3897789474657798211.jpeg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    # WONDERER

    elif message.content == "موارد وندرر":
        embed = discord.Embed(title="__موارد وندرر__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/12/02/8009863/8dba097750646e388ce1feb163beaae1_8283861053769186135.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم وندرر":
        embed = discord.Embed(title="__تفريم وندرر__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/12/03/8009863/e29b32ba47ff72e656c0962e497116b2_6543044235353336388.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)



class SelectTest(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="ayaka", description="ayaka build"),
            discord.SelectOption(label="hutao", description="hutao build"),
            discord.SelectOption(label="raiden shogun", description="raiden shogun build")
        ]
        super().__init__(placeholder="choose a character?", options=options, min_values=1, max_values=1)


    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{self.values[0]} build")

class SelectView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectTest())

@client.tree.command(name="build", description="Choose a character")
async def build(ctx: commands.Context):
    await ctx.send("click on the dropdown below", view=SelectView())














@client.tree.command(name="ping", description="Show the bot's latency in ms.")
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong! {bot_latency} ms.")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start("TOKEN")



asyncio.run(main())