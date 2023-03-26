import discord
from discord import app_commands
from discord.ext import commands

class MyWeapons(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('MyWeapons.py is ready!')

    @app_commands.command(name="staff_of_homa", description="سلاح staff of homa.")
    async def staff_of_homa(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__Staff Of Homa | سلاح__", color=discord.Color.dark_red())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2021/11/07/167269489/57ff19f6ced179e27ecac72d225412f9_8108049312602663019.jpg?x-oss-process=image%2Fresize%2Cs_1000%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.add_field(name="معلومات السلاح :",
                                value="> Type: \n > رمح \n LVL90: \n > Base ATK: 608 | Crit DMG: 66.2%",
                                inline=False)

        embed_message.add_field(name="مهارة السلاح", value="يزيد من هجوم المستخدم بناءً على Max HP مما يجعله سلاحًا ممتازًا للشخصيات التي تحتاج إلى ATK و HP. إذا كانت نقاطك الصحية أقل من 50٪ ، فإن مكافأة الهجوم تزداد اعتمادًا على جودة السلاح. ستزيد نقاط الصحة بنسبة 20٪. بالإضافة إلى ذلك ، تقدم مكافأة هجوم على أساس 0.8٪ من الحد الأقصى لصحة الشخصية. عندما تكون نقاط صحة العامل أقل من 50٪ ، تتم زيادة مكافأة الهجوم هذه بنسبة 1٪ إضافية من الحد الأقصى للصحة.", inline=False)

        embed_message.add_field(name="أفضل مستخدم :",
                                value="> Hu Tao ",
                                inline=False)

        embed_message.add_field(name="الشخصيات المناسبة :",
                                value="> Hu Tao \n > Xiao \n > Zhongli \n > Xiangling \n > Raiden shogun \n > Candace ",
                                inline=False)

        embed_message.set_footer(text="الماتيريال الازم توفرها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="engulfing_lightning", description="سلاح engulfing lightning.")
    async def engulfing_lightning(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__Engulfing Lightning | سلاح__", color=discord.Color.dark_purple())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/03/07/8009863/1093078a80ea9fd2424cddc7689af3d1_7949519603753924734.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg")

        embed_message.add_field(name="Weapon Information:",
                                value="> Type: \n > رمح \n LVL90: \n > Base ATK: 608 | Energy Recharge: 55.1%",
                                inline=False)

        embed_message.add_field(name="Weapon Ability",
                                value="يزيد الهجوم 28.8٪. عندما تكون صحة المالك أقل من 50٪ ، تزداد إعادة شحن الطاقة بنسبة 30٪. بالإضافة إلى ذلك ، عندما تكون طاقة المالك أقل من 100٪ ، فإنه يكتسب مكافأة إضافية بنسبة 0.6٪ من الضرر الناتج عن كل 1٪ من الطاقة المفقودة ، بحد أقصى 18٪ مكافأة ضرر.",
                                inline=False)

        embed_message.add_field(name="أفضل مستخدم :",
                                value="> Raiden Shogun ",
                                inline=False)

        embed_message.add_field(name="الشخصيات المناسبة :",
                                value="> Raiden Shogun \n > Yun jin \n > Zhongli \n > Xiangling \n > Rosaria \n > Mika ",
                                inline=False)

        embed_message.set_footer(text="الماتيريال الازم توفرها", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)


async def setup(client):
    await client.add_cog(MyWeapons(client))
