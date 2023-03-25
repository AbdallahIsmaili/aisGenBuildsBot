import discord
from discord.ext import commands

class MyArtifacts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('MyArtifacts.py is ready!')

    @commands.command()
    async def crimson(self, ctx):
        embed_message = discord.Embed(title="__Crimson witch of flames | ارتيفاكت__", color=discord.Color.dark_red())

        embed_message.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

        embed_message.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2022/07/22/69529472/84149b7329c829cf5f7fb1c0123aa3bd_7222137357418033695.PNG?x-oss-process=image%2Fresize%2Cs_1000%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.add_field(name="قطعتان :",
                                value="رفع ضرر عنصر البايرو بنسبة 15%",
                                inline=False)

        embed_message.add_field(name="اربع قطع", value="زيادة ضرر تفاعل الانفجار او الاحتراق بنسبة 40% و تفاعل التبخر و الانصهار بنسبة 15%, عند استخدام قدرة السكل, ستزداد نسبة ضرر عنصر البايرو 50% اضافة ل15% السابقة لمدة 10 ثواني, ثلاث ستاكات كحد اقصى.", inline=False)

        embed_message.add_field(name="الشخصيات المناسبة :",
                                value="> Hu Tao \n > Diluc \n > Klee \n > Yanfie \n > Yoe mia \n > Dehya ",
                                inline=False)

        await ctx.send(embed=embed_message)


async def setup(client):
    await client.add_cog(MyArtifacts(client))
