import http.client
import json
import discord
import datetime

tier_image_urls=[None]+['https://media.discordapp.net/attachments/1006707877400031283/1006719572541460611/1.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719572918939740/2.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719573283831878/3.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719573661339668/4.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719574189813880/5.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719574747660308/6.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719575318073465/7.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719575825592350/8.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719576320528454/9.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006719576769310850/10.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835716241772635/11.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835716573106247/12.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835716900270200/13.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835717168713778/14.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835717856563200/15.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835718263422976/16.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835718682845235/17.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835719001604127/18.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835719383302154/19.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835719773360158/20.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835800291422219/21.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835800786337822/22.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835801075753000/23.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835801419690015/24.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835801738444800/25.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835802090774558/26.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835802455683162/27.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835802799607848/28.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835803181297674/29.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835803600719892/30.png?width=397&height=508','https://media.discordapp.net/attachments/1006707877400031283/1006835825843118150/31.png?width=397&height=508']
bot_log=1006707877400031283 # 앵글리에
# bot_log=1006710158417727633 # 내거


def get_profile_by_id(id):
    conn = http.client.HTTPSConnection("solved.ac")
    headers = { 'Content-Type': "application/json" }
    conn.request("GET", "/api/v3/user/show?handle="+id, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def get_problems():
    conn = http.client.HTTPSConnection("solved.ac")
    headers = { 'Content-Type': "application/json" }
    conn.request("GET", r"/api/v3/search/problem?query=*s2..p5%20s%23100..%20lang%3Ako%20solvable%3Atrue%20!s%40kkhmsg30%20!s%40tndyd0706%20!s%40dandelion51&page=1&sort=random", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def is_solved(problem, id):
    conn = http.client.HTTPSConnection("solved.ac")
    headers = { 'Content-Type': "application/json" }
    conn.request("GET", f"/api/v3/search/problem?query=id%3A{problem}%20s%40{id}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return bool(json.loads(data.decode("utf-8"))['count'])

async def on_message(message):
    key=message.content.split()[0] # 첫 단어
    args=message.content.split()[1:] # 나머지 단어 리스트
    if key=='경민아':
        try:
            # 비어있을때
            if len(args)==0:
                await message.reply('흥! 어쩌라구요!')
            
            # 세 문제 정하기
            if len(args)==1 and args[0]=='문제줘':
                today=datetime.datetime.today().strftime(r"%Y%m%d")
                messages=[m async for m in message.guild.get_channel(bot_log).history(limit=1)]
                if messages[0].content==today:
                    await message.reply('아까 알려줬자나유!', embed=messages[0].embeds[0])
                else:

                    data=get_problems()
                    embed=discord.Embed(title='오늘의 문제', description=f"""**{data['items'][0]['titleKo']}** - [{data['items'][0]['problemId']}](https://www.acmicpc.net/problem/{data['items'][0]['problemId']})
                    **{data['items'][1]['titleKo']}** - [{data['items'][1]['problemId']}](https://www.acmicpc.net/problem/{data['items'][1]['problemId']})
                    **{data['items'][2]['titleKo']}** - [{data['items'][2]['problemId']}](https://www.acmicpc.net/problem/{data['items'][2]['problemId']})""")

                    await message.guild.get_channel(bot_log).send(today, embed=embed)
                    await message.reply(embed=embed)
            
            # 풀었는지 판별하기
            if len(args)==3 and (args[2]=='풀었어'):
                if is_solved(args[0], args[1]) or is_solved(args[1], args[0]):
                    await message.reply('진짜넹')
                else:
                    await message.reply('거짓말 치지 마유!')

            # 백준 프로필 정보
            if len(args)==2 and (args[1]=='티어' or args[1]=='정보' or args[1]=='프로필'):
                data=get_profile_by_id(args[0])

                embed=discord.Embed(title=args[0])
                embed.add_field(name="맞은 문제",value=f"{data['solvedCount']}")
                embed.add_field(name="레이팅",value=f"{data['rating']}")
                embed.set_thumbnail(url=tier_image_urls[data['tier']])

                await message.reply(embed=embed)

        except Exception as e:
            await message.reply('흥! 코드 제대로 짜세유!\nError:'+str(e))