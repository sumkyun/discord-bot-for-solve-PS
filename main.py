import discord
import baekjoon

client = discord.Client()
token = r"MTAwNTA2MjY5NTY5MjgwNDExNg.G9RYlh."+r"CU5qa5mrYWGzK6jDE5MnS8erx-fUjhu2l0wKgI"
# token = r'OTkwMTM1MzExNTc1MTc5MzI1.GnE7Uj.n'+r'G-F7r3uXCYHgqbEs2nXwo8r0GBHT7Y6j_6Nsc'


@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.author == client.user:
            return
    await baekjoon.on_message(message)


client.run(token)