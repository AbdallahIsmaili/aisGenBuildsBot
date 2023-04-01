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
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/614cfe6b23c3a4674f0ad14e1266b60f_2608004253608321026.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم ناهيدا":
        embed = discord.Embed(title="__تفريم ناهيدا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/11/02/8009863/ca49d4f17590634cd41e513c595f0ca1_5171604966312186724.jpg?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,jpg")

        await message.channel.send(embed=embed)

    # MIKA

    elif message.content == "موارد ميكا":
        embed = discord.Embed(title="__موارد ميكا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/a6b8f72287f83c88c7a6850b8cd16858_5155317919275070487.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

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
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/974d59b8750940d8dfea35e5cdf4baae_8670450094759768747.png?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

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
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/aed29c37958a5ce4602b9f0b6f29268d_6154979107884120724.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

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
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/b861c069e5e25eb76640e0ffbdeca1db_955352576478979170.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

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
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/77dae8a7a2a9984a5f00524ae8de5465_6879006731556604081.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

    elif message.content == "تفريم وندرر":
        embed = discord.Embed(title="__تفريم وندرر__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2022/12/03/8009863/e29b32ba47ff72e656c0962e497116b2_6543044235353336388.jpg?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

    # CYNO

    elif message.content == "موارد ساينو":
        embed = discord.Embed(title="__موارد ساينو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/302ea68b374756a102512ea8a9b04018_8386615514960740958.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

   #YOIMIYA
    elif message.content == "موارد يويميا":
            embed = discord.Embed(title="__موارد يويميا__")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/bec0c32b11f81f87baedae9213ab4d32_6341263185804256233.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

            await message.channel.send(embed=embed)

    # BENNETT

    elif message.content == "موارد بينيت":
      embed = discord.Embed(title="__موارد بينيت__")

      embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/7caabe884634205043f3bc030d57ab10_1309927053145784557.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

      await message.channel.send(embed=embed)

    # YEA MIKO

    elif message.content == "موارد ميكو":
        embed = discord.Embed(title="__موارد ياي ميكو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/302fe024b020e976aea36f28aa93c46d_1153123279695482214.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

   #RAIDEN SHOGUN

    elif message.content == "موارد رايدن":
         embed = discord.Embed(title="__موارد رايدن شوقن__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/d82d9d3e904b049f0f6a27c99fdbe19f_2919988696851374250.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # GANYU
    elif message.content == "موارد قانيو":
         embed = discord.Embed(title="__موارد قانيو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/c53b7ccd20447d57c7039d4c6c854039_4863047902747308858.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # Tartaglia
    elif message.content == "موارد تشايلد":
         embed = discord.Embed(title="__موارد تشايلد__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/169f5cdcd0c7ca7edbafdaa35766b728_2570323969436774721.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # Xingqiu
    elif message.content == "موارد سينق شو":
         embed = discord.Embed(title="__موارد سينق شو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/f512b6ed01d599af2fd4dca7291eda71_8636933875889902119.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

   # Nilou
    elif message.content == "موارد نيلو":
         embed = discord.Embed(title="__موارد نيلو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/7f17f9928f45e86bfec94d477dd9554f_1040071117977094375.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # Sucrose
    elif message.content == "موارد سكروز":
         embed = discord.Embed(title="__موارد سكروز__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/02a50cfc67a7157eba00b6bcc0afc5ce_6937901798231875693.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

   # Sangonomiya Kokomi
    elif message.content == "موارد كوكمي":
         embed = discord.Embed(title="__موارد كوكمي__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/af63df8be8f89153091ac0a49df97791_8973992811730286955.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # KLEE
    elif message.content == "موارد كلي":
        embed = discord.Embed(title="__موارد كلي__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/52b1ef07dcafaf11482fb2f553f9afa5_5591470909480967973.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

    # BARBARA
    elif message.content == "موارد باربرا":
        embed = discord.Embed(title="__موارد باربرا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/126ac64d719f68e77d6ed64d8cef3f72_7048901298276534524.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

    # BEIDOU
    elif message.content == "موارد بيدو":
        embed = discord.Embed(title="__موارد بيدو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/2548c6a56c4387dc2470ed0ab2fdc4d7_243515016471484769.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

    # LAYLE
    elif message.content == "موارد ليلى":
         embed = discord.Embed(title="__موارد ليلى__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/80b0c4488ab1b1a08a27bf6782c578ee_3371293778014234881.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # HU TAO
    elif message.content == "موارد هو تاو":
         embed = discord.Embed(title="__موارد هو تاو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/95faec5d8ebb1bcae96865ad55a1ed48_6657823024455990259.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # Shikanoin Heizou
    elif message.content == "موارد هايزو":
         embed = discord.Embed(title="__موارد هايزو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/47ee18ab920db5fd2f6d4bc4df24d412_1275719158030813521.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # KAMISATO AYAKA
    elif message.content == "موارد اياكا":
         embed = discord.Embed(title="__موارد كاميساتو اياكا__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/c7d52def57a85c90c22709f89131ce69_3063921203868673691.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # KAMISATO AYATO
    elif message.content == "موارد اياتو":
         embed = discord.Embed(title="__موارد كاميساتو اياتو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/15336e5a564d622229aa77c40485295e_3621691282596003113.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # EULA
    elif message.content == "موارد ايولا":
         embed = discord.Embed(title="__موارد ايولا__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/45982519c9a8f97fb73ae659b2951ecd_8326576383755874594.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # KAEYA
    elif message.content == "موارد كايا":
         embed = discord.Embed(title="__موارد كايا__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/b6170d1424fdd542ac183d6a2863d27e_3170939090025214175.png?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

         await message.channel.send(embed=embed)

         # ALBEDO
    elif message.content == "موارد البيدو":
        embed = discord.Embed(title="__موارد البيدو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/0a98ad2da089baacdef185d61f9724e3_8856281966813199903.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

        # DILUC
    elif message.content == "موارد ديلوك":
        embed = discord.Embed(title="__موارد ديلوك__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/71e8b7885e33d1b5c3e9697fa29d529d_60829646212494725.png?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

        await message.channel.send(embed=embed)

        # KAZUHA
    elif message.content == "موارد كازوها":
            embed = discord.Embed(title="__موارد كازوها__")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/c41be11db40382dcb7bc916772669c4e_2058006580695017027.png?x-oss-process=image%2Fquality%2Cq_80%2Fauto-orient%2C0%2Finterlace%2C1%2Fformat%2Cwebp")

            await message.channel.send(embed=embed)

        # ZHONGLI
    elif message.content == "موارد زونقلي":
            embed = discord.Embed(title="__موارد زونقلي __")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/da8ef7572bf48e57aaf3affb62fbfbdc_4419659133928639206.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

            await message.channel.send(embed=embed)

        # YELAN
    elif message.content == "موارد يلان":
            embed = discord.Embed(title="__موارد يلان __")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/50d3d1df39b84bd581a54f7cc8ecd561_1709080505120157707.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

            await message.channel.send(embed=embed)

   # YANFEI
    elif message.content == "موارد يانفي":
            embed = discord.Embed(title="__موارد يانفي__")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/840c85cdc71bc4a123ae2d718fd20736_3297101534346426278.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

            await message.channel.send(embed=embed)

   # YUN JIN
    elif message.content == "موارد يون جين":
            embed = discord.Embed(title="__موارد يون جين__")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/1f3227e933ce8baa769b1ec949aa02d3_6803745259426715106.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

            await message.channel.send(embed=embed)

   # JEAN
    elif message.content == "موارد جين":
            embed = discord.Embed(title="__موارد جين__")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/6e9f9458d74c5ffdf27496f42a7ac762_8048325657181957339.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

            await message.channel.send(embed=embed)

   # ITTO
    elif message.content == "موارد ايتو":
            embed = discord.Embed(title="__موارد اراتاتكي ايتو__")

            embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/d05f843b240407e7615889478eaf45d5_931956076823895080.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

            await message.channel.send(embed=embed)

    # FISCHAL

    elif message.content == "موارد فيشل":
        embed = discord.Embed(title="__موارد فيشل__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/64e5befba2ce243fd3bad8ba4dd05aa8_921069753820886590.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

    # AMBER

    elif message.content == "موارد امبر":
        embed = discord.Embed(title="__موارد امبر__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/20abaa8be5418389864ae405134923ac_4896704772107211565.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

   # DIONA

    elif message.content == "موارد ديونا":
        embed = discord.Embed(title="__موارد ديونا__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/cc6990cd500db9b26348c8126bffaa6f_3066383773903303620.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

   # DORI

    elif message.content == "موارد دوري":
        embed = discord.Embed(title="__موارد دوري__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/2b59a30a177336228fd0af740bf24483_3237185797643878359.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

   # COLLEI

    elif message.content == "موارد كولي":
        embed = discord.Embed(title="__موارد كولي__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/178770daf6f203b496c6edbf72ca5c41_5660118875246964005.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

   # CHONGYUN

    elif message.content == "موارد شونق يون":
        embed = discord.Embed(title="__موارد شونق يون__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/3bb2082baf8e90e62e1d14edabc9c6bb_2410357627532043290.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

   # CANDACE

    elif message.content == "موارد كانديس":
        embed = discord.Embed(title="__موارد كانديس__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/7651a5e15ef03aa13aa141457a611804_3585482333520743051.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

  # GOROU

    elif message.content == "موارد قورو":
        embed = discord.Embed(title="__موارد قورو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/e9a3a1a928c84a13a04e67920ee0497e_3654643107933556950.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

        # CANDACE

    elif message.content == "موارد الوي":
        embed = discord.Embed(title="__موارد الوي__")

        embed.set_image(
                url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/0b09dfa8129d4ae822eb7877226bced1_1829146854296330841.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

  # XIAO

    elif message.content == "موارد شاو":
        embed = discord.Embed(title="__موارد شاو__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/04ac45a94ef9deafc54a606ad4193c56_4195411413336792247.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

  # XINYAN

    elif message.content == "موارد شنيان":
        embed = discord.Embed(title="__موارد شنبان__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/84007d4ccd672804bb451dcdcca06a38_4845688648017396707.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)


  # XIANGLING

    elif message.content == "موارد شانقلنق":
        embed = discord.Embed(title="__موارد شانقلنق__")

        embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/7dc7f72915a8ab29613e13b370dbb9db_7728549447730978681.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        await message.channel.send(embed=embed)

    # VENTI
    elif message.content == "موارد فنتي":
         embed = discord.Embed(title="__موارد فنتي__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/4f3fd8646086b3a88988dcc30c653653_1256351017765150802.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # TIGHANRI
    elif message.content == "موارد تيناري":
         embed = discord.Embed(title="__موارد تيناري__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/0dcf05e4f4c50159ec4c59f1f5adae49_6477651438960354490.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # THOMA
    elif message.content == "موارد ثوما":
         embed = discord.Embed(title="__موارد ثوما__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/38dc7b66ab417e18a5142c0a3a0b6cbf_4210120329846258625.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # SHENHE
    elif message.content == "موارد شينهي":
         embed = discord.Embed(title="__موارد شينهي__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/034868531fd514779261ed86616dd09d_3810799396067989507.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # SAYU
    elif message.content == "موارد سايو":
         embed = discord.Embed(title="__موارد سايو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/cc80da0286beff520387d5b4b953e9ae_1423132479450419878.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # SARA
    elif message.content == "موارد سارا":
         embed = discord.Embed(title="__موارد كوجو سارا__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/85ad52af19ea8dd0d3abb3529bb76184_6286441946408100415.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # RAZOR
    elif message.content == "موارد ريزور":
         embed = discord.Embed(title="__موارد ريزور__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/8af58df61b40060bdd0052501b7d2e5b_2459624156911636744.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # ROSARIA
    elif message.content == "موارد روزاريا":
         embed = discord.Embed(title="__موارد روزاريا__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/3c313fa9350e86304dbdd1d0f7a4d5e7_5351428299773422184.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # QIQI
    elif message.content == "موارد شي شي":
         embed = discord.Embed(title="__موارد شي شي__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/07ca261689aa57979ab0da3961bafcdb_9053978689686239200.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # NINGGUANG
    elif message.content == "موارد نينق وانق":
         embed = discord.Embed(title="__موارد نينق وانق__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/f8f452b4c74d19bdc2cf93de327effe2_6453074242066224090.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # NOELLE
    elif message.content == "موارد نويل":
         embed = discord.Embed(title="__موارد نويل__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/cca89e5d9ec371ea201a9e11b454f65c_6993482272717872010.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # MONA
    elif message.content == "موارد مونى":
         embed = discord.Embed(title="__موارد مونى__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/ef253ae281f9c95b60e477b673d6d106_800724069418710074.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # LISA
    elif message.content == "موارد ليسا":
         embed = discord.Embed(title="__موارد ليسا__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/04/01/229749002/dbdae14a95b4260c9ef8363456107f91_3112004734829455244.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # KEQINE
    elif message.content == "موارد كتشنق":
         embed = discord.Embed(title="__موارد كتشنق__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/ec9e281a0dc9dc4a5102e292150530d8_8774543238591981557.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

         await message.channel.send(embed=embed)

    # KUKI
    elif message.content == "موارد شينوبو":
         embed = discord.Embed(title="__موارد كوكي شينوبو__")

         embed.set_image(
            url="https://upload-os-bbs.hoyolab.com/upload/2023/03/31/229749002/af800c5e6ec35cb06bdded3d22113482_1901183383169359056.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

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
