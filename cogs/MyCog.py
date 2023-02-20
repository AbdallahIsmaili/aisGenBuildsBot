import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('MyCog.py is ready!')

    @commands.command()
    async def embed(self, ctx):
        embed_message = discord.Embed(title="Title of embed", description="Description of embed", color=discord.Color.red())

        embed_message.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Field name", value="Field value", inline=False)
        embed_message.set_footer(text="This is the footer", icon_url=ctx.author.avatar)

        await ctx.send(embed = embed_message)

    @commands.command()
    async def xingqui(self, ctx):
        embed_message = discord.Embed(title="Xingqiu (Off-Field DPS) | بناء", description="Primordial Jade Cutter \n حتوي على نسبة Crit RATE عالية \n هذا السلاح هو أفضل خيار هجومي لـ C6 Xingqiu \n طالما أن متطلبات ER متوفرة وغير موصى بها لغير C6 Xingqiu",
                                      color=discord.Color.dark_blue())

        embed_message.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

        embed_message.set_thumbnail(url="https://dk2dv4ezy246u.cloudfront.net/widgets/sLrag8fYCtT_large.jpg")

        embed_message.set_image(url="https://w0.peakpx.com/wallpaper/893/65/HD-wallpaper-video-game-genshin-impact-xingqiu-genshin-impact.jpg")

        embed_message.add_field(name="Favonius Sword", value=" يحتوي هذا السلاح على نسبة إعادة شحن طاقة عالية جدًا بنسبة 61.3٪ \n  كما أنه يتمتع بميزة القدرة على شحن فريقك بالكامل \n وهو خيار قوي حتى في مستوى الصقل r1.", inline=False)

        embed_message.set_footer(text="This is the footer", icon_url=ctx.author.avatar)

        await ctx.send(embed=embed_message)


async def setup(client):
    await client.add_cog(MyCog(client))
