import discord
from discord import app_commands
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('MyCog.py is ready!')

    @app_commands.command(name="avatar", description="View my discord avatar.")
    async def avatar(self, interactions: discord.Interaction, member: discord.Member=None):
        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        avatar_embed = discord.Embed(title=f"{member.name}'s Avatar", color=discord.Color.random())
        avatar_embed.set_image(url=member.avatar)
        avatar_embed.set_footer(text=f"Requested by {interactions.user.name}", icon_url=interactions.user.avatar)

        await interactions.response.send_message(embed=avatar_embed)

    # @app_commands.command(name="embed", description="simple embed.")
    # async def embed(self, interactions: discord.Interaction, member: discord.Member=None):
    #
    #     if member is None:
    #         member = interactions.user
    #     elif member is not None:
    #         member = member
    #
    #
    #     embed_message = discord.Embed(title="Title of embed", description="Description of embed", color=discord.Color.red())
    #
    #     embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)
    #     embed_message.set_thumbnail(url=member.guild.icon)
    #     embed_message.set_image(url=member.guild.icon)
    #     embed_message.add_field(name="Field name", value="Field value", inline=False)
    #     embed_message.set_footer(text="This is the footer", icon_url=member.avatar)
    #
    #     await interactions.response.send_message(embed=embed_message)


    @app_commands.command(name="xingqui", description="عرض معلومات بناء شخصية شينغشو.")
    async def xingqui(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__Xingqiu (Off-Field DPS) | بناء__", color=discord.Color.blue())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_thumbnail(url="https://dk2dv4ezy246u.cloudfront.net/widgets/sLrag8fYCtT_large.jpg")

        embed_message.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2023/02/10/135704791/cb7c75c9b96fed2bf966d68d09d209fa_4584696412287163334.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.add_field(name="Primordial Jade Cutter",
        value=" \n حتوي على نسبة Crit RATE عالية \n هذا السلاح هو أفضل خيار هجومي لـ C6 Xingqiu \n طالما أن متطلبات ER متوفرة وغير موصى بها لغير C6 Xingqiu",
        inline=False)

        embed_message.add_field(name="Favonius Sword", value=" يحتوي هذا السلاح على نسبة إعادة شحن طاقة عالية جدًا بنسبة 61.3٪ \n  كما أنه يتمتع بميزة القدرة على شحن فريقك بالكامل \n وهو خيار قوي حتى في مستوى الصقل r1.", inline=False)

        embed_message.add_field(name="Sacrificial Sword",
                                value=" يحتوي هذا السلاح على نفس  نسبة إعادة شحن طاقة عالية جدًا ايضا \n  ويوفر لك دمج اعلى بقليل من السلاح السابق.",
                                inline=False)

        embed_message.add_field(name="اسلحة بديلة:",
                                value="Mistplitter Reforged, Aminoma Kaguchi",
                                inline=False)

        embed_message.add_field(name="أفضل الارتيفاكت:",
                                value="اربع قطع Emblem of Severed Destiny: \n > إعادة شحن الطاقة + 20٪ \n > يزيد الضرر الناتج عن تفاعل العناصر بنسبة 25٪ من إعادة شحن الطاقة. يمكن الحصول على 75٪ ضرر كحد أقصى بهذه الطريقة.",
                                inline=False)

        embed_message.add_field(name="ثاني أفضل الارتيفاكت:",
                                value="Noblesse Oblige: 4x: \n > ضرر الالتيميت + 20٪ \n > يزيد الضرر الناتج عن استخدام الالتيميت يزيد هجوم جميع أعضاء الفريق بنسبة 20٪ لمدة 12 ث. لا يمكن تكديس هذا التأثير.",
                                inline=False)

        embed_message.add_field(name="ثالث أفضل مجموعة أثرية:",
                                value="Invert Depth: 2x \n > مكافأة Hydro DMG + 15٪ \n > Noblesse Oblige: 2x \n > ضرر الالتيميت + 20٪",
                                inline=False)

        embed_message.add_field(name="أولوية الإحصائيات الرئيسية:",
                                value="الساعة: انرجي (شحن طاقة) \n الكأس: هايدرو دماج \n التاج: crit Rate/crit DMG",
                                inline=False)

        embed_message.add_field(name="الأولوية الفرعية",
                                value="> إعادة شحن الطاقة \n > CRate / CDMG \n > ATK%",
                                inline=False)

        embed_message.add_field(name="التلنتات:",
                                value="> الالتيميت \n > المهارة الأساسية \n > الهجوم العادي",
                                inline=False)

        embed_message.set_footer(text="This is the footer", icon_url=member.avatar)

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="ayaka", description="عرض معلومات بناء شخصية اياكا.")
    async def ayaka(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__Ayaka (Main DPS) | بناء__", color=discord.Color.lighter_grey())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_thumbnail(url="https://static.wikia.nocookie.net/gensin-impact/images/b/be/Icon_Emoji_Paimon%27s_Paintings_Kamisato_Ayaka_8.png/revision/latest/scale-to-width-down/250?cb=20220422085921")

        embed_message.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/21/135704791/5b7242b777698a65a17f5377e89716ed_7279453830196285054.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.add_field(name="Primordial Jade Cutter",
                                value="يحتوي على نسبة Crit RATE عالية \n هذا السلاح هو أفضل خيار هجومي لـ Ayaka \n طالما أن متطلبات ER متوفرة.",
                                inline=False)

        embed_message.add_field(name="Summit Shaper",
                                value=" يزيد من هجوم Ayaka بنسبة 28٪ \n يحتوي على نسبة Crit DMG عالية \n ويرفع مستوى الهجمات الوحدات بنسبة 10٪",
                                inline=False)

        embed_message.add_field(name="اسلحة بديلة:",
                                value="Amenoma Kageuchi, Mistsplitter Reforged, Blackcliff Longsword",
                                inline=False)

        embed_message.add_field(name="أفضل الارتيفاكت:",
                                value="4x Blizzard Strayer: \n > زيادة هجوم الكريو بنسبة 35٪ \n > إذا تم استخدام التفاعلات المجمدة في آخر 2.5 ثانية ، فستحصل على 15٪ من الهجوم الإضافي كـ CRate. يمكن الحصول على 45٪ CRate كحد أقصى.",
                                inline=False)

        embed_message.add_field(name="ثاني أفضل الارتيفاكت:",
                                value="2x Blizzard Strayer + 2x Heart of Depth: \n > زيادة هجوم الكريو بنسبة 15٪ \n > زيادة الضرر الناتج عن التفاعلات الكريوية بنسبة 30٪",
                                inline=False)

        embed_message.add_field(name="ثالث أفضل مجموعة أثرية:",
                                value="4x Heart of Depth: \n > زيادة الضرر الناتج عن التفاعلات الكريوية بنسبة 15٪ \n > إعادة شحن الطاقة بنسبة 20٪",
                                inline=False)

        embed_message.add_field(name="أولوية الإحصائيات الرئيسية:",
                                value="هجوم (ATK) \n > نسبة الضرر الحرج (Crit DMG)  \n > Crit Rate \n > طاقة إعادة الشحن (ER)",
                                inline=False)

        embed_message.add_field(name="طور ترقية التصنيفات:",
                                value="Normal Attack \n > lemental Burst \n > Elemental Skill",
                                inline=False)

        embed_message.set_footer(text="يمكن تغيير البناء وفقًا للتفضيلات الشخصية للمستخدم")

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="hutao", description="عرض معلومات بناء شخصية هوتاو.")
    async def hutao(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__Hu Tao (Main DPS) | بناء__", color=discord.Color.red())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_thumbnail(
            url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/97e2e37c-5240-4a8c-9104-8adc507b5971/dekqnix-16b0f536-b305-4e6b-9376-5ff6530194b8.png/v1/fill/w_500,h_500,q_80,strp/icon_commission__hu_tao_by_melodreamm_dekqnix-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTAwIiwicGF0aCI6IlwvZlwvOTdlMmUzN2MtNTI0MC00YThjLTkxMDQtOGFkYzUwN2I1OTcxXC9kZWtxbml4LTE2YjBmNTM2LWIzMDUtNGU2Yi05Mzc2LTVmZjY1MzAxOTRiOC5wbmciLCJ3aWR0aCI6Ijw9NTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.SjY_eI35y2QKLSvxVmnw-Tr5QsNBI52r7dWFzG0mM3M")

        embed_message.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/02/07/135704791/3531f00435ec8f8d95d04376cf05de6d_7352601156437108807.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.add_field(name="Staff of Homa",
                                value="أفضل سلاح لـ Hu Tao لأنه يحتوي على نسبة Crit DMG عالية جدًا \n يعطيها نسبة إضافية من الـ Max HP",
                                inline=False)

        embed_message.add_field(name="Dragon's Bane",
                                value="يعد سلاح Dragon's Bane مناسبًا لشخصيات الأنوم الذين يعتمدون على هجمات القوى الإلهية، حيث يحصلون على زيادة في الهجمات ضد الوحوش الأنوم بنسبة 20%، كما يحتوي السلاح على قوة القوى الإلهية المطورة والتي تزيد من قوة الهجمات النارية بنسبة 20%.",
                                inline=False)

        embed_message.add_field(name="Primordial Jade Winged-Spear",
                                value="سلاح جيد آخر بسبب النسبة العالية من الـ Crit Rate \n مفيد إذا لم يكن لديك سلاح Staff of Homa",
                                inline=False)

        embed_message.add_field(name="Deathmatch",
                                value="سلاح آخر مفيد لـ Hu Tao \n يحتوي على نسبة عالية من الـ Crit Rate و ATK \n ويعطي مكافأة إضافية للـ Elemental Mastery في معركة 1v1",
                                inline=False)

        embed_message.add_field(name="أسلحة بديلة:",
                                value="Prototype Grudge, Crescent Pike",
                                inline=False)

        embed_message.add_field(name="أفضل الارتيفاكت:",
                                value="2 قطعة Crimson Witch of Flames + 2 قطعة Heart of Depth: \n > يعطيها نسبة إضافية من الـ Pyro DMG وـ Crit DMG \n > يزيد الضرر الناتج عن التفاعل بين العناصر",
                                inline=False)

        embed_message.add_field(name="ثاني أفضل الارتيفاكت:",
                                value="4 قطع Crimson Witch of Flames: \n > يعطيها نسبة إضافية من الـ Pyro DMG \n > يزيد الضرر الناتج عن التفاعل بين العناصر بنسبة 15%",
                                inline=False)

        embed_message.add_field(name="ثالث أفضل مجموعة أثرية:",
                                value="2 قطعة Crimson Witch of Flames + 2 قطعة Gladiator's Finale: \n > يزيد الـ ATK \n > يزيد الضرر الناتج عن التفاعل بين العناصر",
                                inline=False)

        embed_message.add_field(name="أولوية الإحصائيات الرئيسية:",
                                value="الساعة: ATK% \n الكأس: Pyro DMG \n التاج: Crit DMG",
                                inline=False)

        embed_message.add_field(name="أولوية الإحصائيات الثانوية:",
                                value="Crit Rate > Energy Recharge > Elemental Mastery",
                                inline=False)

        embed_message.add_field(name="مواهب:",
                                value="قدرة الفأس الملتهبة (E) > قدرة الانتقام الموتوف (Q) > قدرة الاتحاد الأخير (Passive)",
                                inline=False)

        embed_message.set_footer(text="يمكن تغيير البناء وفقًا للتفضيلات الشخصية للمستخدم")

        await interactions.response.send_message(embed=embed_message)

    @app_commands.command(name="cyno", description="عرض معلومات بناء شخصية سينو.")
    async def cyno(self, interactions: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interactions.user
        elif member is not None:
            member = member

        embed_message = discord.Embed(title="__Cyno (DPS) | بناء__", color=discord.Color.red())

        embed_message.set_author(name=f"Requested by {member.name}", icon_url=member.avatar)

        embed_message.set_thumbnail(
            url="https://static.wikia.nocookie.net/gensin-impact/images/0/05/Icon_Emoji_Paimon%27s_Paintings_18_Cyno_3.png/revision/latest/scale-to-width-down/250?cb=20221020052700")

        embed_message.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/01/135704791/f10adf6b84c3ffc5a24d37882e54539e_4572522418184772856.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        embed_message.add_field(name="Staff of the Scarlet Sands",
                                value="الشخصية المجهزة تحصل على 52% من EM الخاص بها كهجوم إضافي. عندما يصيب مهارة السكل الخصم، سيتم الحصول على تأثير لمدة 10 ثوانٍ: سيحصل الشخصية المجهزة على 28% من EM الخاص بها كهجوم إضافي. يصل إلى حد أقصى 3 مرات.",
                                inline=False)

        embed_message.add_field(name="Staff of Homa",
                                value="أفضل سلاح لـ Hu Tao لأنه يحتوي على نسبة Crit DMG عالية جدًا \n يعطيها نسبة إضافية من الـ Max HP",
                                inline=False)

        embed_message.add_field(name="Dragon's Bane",
                                value="يعد سلاح Dragon's Bane مناسبًا لشخصيات الأنوم الذين يعتمدون على هجمات القوى الإلهية، حيث يحصلون على زيادة في الهجمات ضد الوحوش الأنوم بنسبة 20%، كما يحتوي السلاح على قوة القوى الإلهية المطورة والتي تزيد من قوة الهجمات النارية بنسبة 20%.",
                                inline=False)

        embed_message.add_field(name="Primordial Jade Winged-Spear",
                                value="سلاح جيد آخر بسبب النسبة العالية من الـ Crit Rate \n مفيد إذا لم يكن لديك سلاح Staff of Homa",
                                inline=False)

        embed_message.add_field(name="Deathmatch",
                                value="سلاح آخر مفيد لـ Hu Tao \n يحتوي على نسبة عالية من الـ Crit Rate و ATK \n ويعطي مكافأة إضافية للـ Elemental Mastery في معركة 1v1",
                                inline=False)

        embed_message.add_field(name="أسلحة بديلة:",
                                value="Blackcliff Pole, White Tassel",
                                inline=False)

        embed_message.add_field(name="أفضل الارتيفاكت / Gilded Dreams:",
                                value="> تأثير من قطعتين: يزيد الهجوم بنسبة 18 بالمائة. \n > تأثير من أربع قطع: عند إلقاء مهارة عنصرية ، إذا كان لدى الشخصية 15 طاقة أو أكثر ، فإنها تفقد 15 طاقة ويزداد ضرر الهجوم العادي / المشحون / الغاطس بنسبة 50 بالمائة لمدة 10 ثوانٍ.",
                                inline=False)

        embed_message.add_field(name="ثاني أفضل الارتيفاكت / thundering fury:",
                                value="> تأثير من قطعتين: Electro DMG Bonus +15%. \n > تأثير من أربع قطع: يزيد الضرر الناتج عن Overloaded ، Electro-Charged ،  Superconduct ، وHyperbloom بنسبة 40٪ ، ومكافأة الضرر الناتج عن Aggravate تزداد بنسبة 20٪. عندما يتم تشغيل Quicken أو التفاعلات الأولية المذكورة أعلاه ، يتم تقليل تقليل مهارة العناصر بمقدار 1 ثانية. يمكن أن يحدث مرة واحدة فقط كل 0.8 ثانية..",
                                inline=False)

        embed_message.add_field(name="أولوية الإحصائيات الرئيسية:",
                                value="الساعة: ATK/EM \n الكأس: Electro DMG \n التاج: Crit DMG/ Rate",
                                inline=False)

        embed_message.add_field(name="أولوية الإحصائيات الثانوية:",
                                value="Crit Rate/DMG > ATK/EM > ER",
                                inline=False)

        embed_message.add_field(name="مواهب:",
                                value="Elemental Burst Q > Elemental Skil E > Normal Attack",
                                inline=False)

        await interactions.response.send_message(embed=embed_message, ephemeral=True)


async def setup(client):
    await client.add_cog(MyCog(client))
