# import random
import discord
from discord.ext import commands
import os
import asyncio
# from discord.ext import tasks
# from itertools import cycle

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

# bot_status = cycle(["Type in '$help' for help ", "Type in '$build' for characters builds", "Type in '$ping' for see your internet conection speed"])

# @tasks.loop(seconds=5)
# async def change_status():
#     await client.change_presence(activity = discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")
    # change_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start("TOKEN")


# @client.command()
# async def ping(ctx):
#     bot_latency = round(client.latency * 1000)
#     await ctx.send(f"Pong!, {bot_latency} ms.")

# @client.command()
# async def hello(ctx):
#     await ctx.send("Hello there!")
#
# @client.command(aliases=["8ball", "eightball", "eight ball", "8 ball"])
# async def magic_eightball(ctx, *, question):
#     with open('responses.txt', 'r') as f:
#         random_responses = f.readlines()
#         response = random.choice(random_responses)
#
#     await ctx.send(response)

asyncio.run(main())