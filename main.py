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