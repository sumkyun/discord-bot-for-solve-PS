import discord
import loltier

client = discord.Client()
token = "OTkwMTM1MzExNTc1MTc5MzI1.Gs-MoJ.dNTT2ETgEr0yilgJj22KlbFFdEEbIWA1iFg3L4"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.content.startswith("경민아"):
        await message.channel.send("저 바빠유 이따 연락해유!")
    
    await loltier.loltier(message) # 이렇게 해도 되고
    
    if message.content.startswith("?롤"):
        await loltier.loltier(message) # 이렇게 해도 되고
    

client.run(token)