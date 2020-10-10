import discord
from captcha.image import ImageCaptcha
import requests
import asyncio
import time
from json import loads
import random
##경태잡것봇
client = discord.Client()

@client.event
async def on_ready():
    print("Angcord 봇이 정상적으로 실행되었습니다.")
    print(client.user.id)
    print("ready")
    game = discord.Game("경태 코딩 연습")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!!안녕"):
        await message.channel.send("하이")

    if message.content.startswith("안원주"):
        await message.channel.send("빙신 ㅋㅋ")

    if message.content.startswith("함승현"):
        await message.channel.send("멍청해")

    if message.content.startswith("박경태"):
        await message.channel.send("귀여워")

    if message.content.startswith("박채은"):
        await message.channel.send("혜지야")

    if message.content.startswith("인정"):
        await message.channel.send("ㄹㅇㅋㅋ")

    if message.content.startswith("전상민"):
        await message.channel.send("탈모는 취급하지 않습니다.")

    if message.content.startswith("돼지"):
        await message.channel.send("꿀꿀")

    if message.content.startswith("홍준우"):
        await message.channel.send("최효원")

    if message.content.startswith("햄코드"):
        await message.channel.send("발로란트 ㅈ밥")

    if message.content.startswith("시발"):
        await message.channel.send("욕 하지 마라 시2발련아")

    if message.content.startswith("!!사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!!채팅청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[7:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")

    if message.content.startswith("!!help"):
        embed = discord.Embed(title="AngCord Commands", description="AngCord의 명령어 목록", color=0x00ff00)
        embed.add_field(name="서버 명령어", value="!!핑, !!채팅청소", inline=False)
        embed.add_field(name="기타 명령어", value="!!사진, !!안녕", inline=False)
        embed.add_field(name="인증 명령어", value="!!인증", inline=False)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)

    if message.content == "!!핑":
        la = client.latency
        await message.channel.send(f'{str(round(la * 1000))}ms')


@client.event
async def on_message(message):
    if message.content.startswith("!!인증"): #명령어 !!인증
        a = ""
        Captcha_img = ImageCaptcha()
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Captcha_img.write(a, name)

        await message.channel.send(f"""{message.author.mention} 아래 숫자를 10초 내에 입력해라. """)
        await message.channel.send(file=discord.File(name))

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check) # 제한시간 10초
        except:
            await message.channel.purge(limit=3)
            chrhkEmbed = discord.Embed(title=':x: 인증실패', color=0xFF0000)
            chrhkEmbed.add_field(name='닉네임', value=message.author, inline=False)
            chrhkEmbed.add_field(name='이유', value='시간초과', inline=False)
            await message.channel.send(embed=chrhkEmbed)
            print(f'{message.author} 님이 시간초과로 인해 인증을 실패함.')
        if msg.content == a:
            role = discord.utils.get(message.guild.roles, name="『❤️』 트수")
            await message.channel.purge(limit=4)
            tjdrhdEmbed = discord.Embed(title='인증성공', color=0x04FF00)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='5초후 인증역할이 부여될 듯ㅋ.', value='** **', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=tjdrhdEmbed)
            time.sleep(5)
            await message.author.add_roles(role)
        else:
            await message.channel.purge(limit=4)
            tlfvoEmbed = discord.Embed(title=':x: 인증실패', color=0xFF0000)
            tlfvoEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tlfvoEmbed.add_field(name='이유', value='잘못된 숫자', inline=False)
            await message.channel.send(embed=tlfvoEmbed)
            print(f'{message.author} 님이 잘못된 숫자로 인해 인증을 실패함ㅋㅋㅋ.')


client.run("NzYxMTg5ODc4MTU1MTgyMTEw.X3W_UQ.rrfFD5gkfFXbB9kcaQeGHoB5Yes")