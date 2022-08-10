import discord
import baekjoon

client = discord.Client()
token = r"MTAwNTA2MjY5NTY5MjgwNDExNg.GvrngO.ia"+r"NYmyKUyMLVnu9_2d2Oyf5Oia4Rx95J2aAtIU" # 앵글리에
# token = r'OTkwMTM1MzExNTc1MTc5MzI1.GnE7Uj.n'+r'G-F7r3uXCYHgqbEs2nXwo8r0GBHT7Y6j_6Nsc' # 내거

bot_log=1006707877400031283 # 앵글리에의 기억

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.author == client.user:
            return
    if message.channel.id==bot_log:
        await message.delete()
    await baekjoon.on_message(message)


client.run(token)