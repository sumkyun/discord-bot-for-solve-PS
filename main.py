import discord

client = discord.Client()
token = "MTAwNTA2MjY5NTY5MjgwNDExNg.GLD2Yn.6fISZrU6AsTeYp8P5lqGhMW2MwrBA-0-JFPgkg"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.content.startswith("경민아"):
        await message.channel.send("저 바빠유 이따 연락해유!")

client.run(token)