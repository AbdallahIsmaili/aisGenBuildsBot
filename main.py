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
