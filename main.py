import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()
token = "MTAwNTA2MjY5NTY5MjgwNDExNg.GhrJhK.twywvtBXskthJZ-TxR1twVKneMGiqPDoRPew-s"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.content.startswith("경민아"):
        await message.channel.send("저 바빠유 이따 연락해유!")
    elif message.content.startswith("?롤"):
        message_content = message.content.replace("?롤 ", "")
        plusurl = message_content.replace(" ", "")
        embed = discord.Embed(title=message_content + "님의 플레이어 정보")
        embed.set_footer(text="솔로랭크 기준 티어입니다. | 랭크 정보가 없을 시 출력되지 않습니다.")
        await message.channel.send(embed=embed)

client.run(token)
