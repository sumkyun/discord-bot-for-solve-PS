import http.client
import random
import json
import discord
import datetime

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
    json.loads(data.decode("utf-8"))

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
            if len(args)==0: # 나머지 단어가 비어있을 때
                await message.reply('흥! 어쩌라구요!')
            
            if len(args)==1 and args[0]=='문제줘':
                data=get_problems()
                Max=2*max(len(data['items'][i]['titleKo']) for i in range(3))
                emptystr=[' '*(Max-len(data['items'][i]['titleKo'])) for i in range(3)]
                embed=discord.Embed(title='오늘의 문제', description=f"""**{data['items'][0]['titleKo']}** - [{data['items'][0]['problemId']}](https://www.acmicpc.net/problem/{data['items'][0]['problemId']})
                **{data['items'][1]['titleKo']}** - [{data['items'][1]['problemId']}](https://www.acmicpc.net/problem/{data['items'][1]['problemId']})
                **{data['items'][2]['titleKo']}** - [{data['items'][2]['problemId']}](https://www.acmicpc.net/problem/{data['items'][2]['problemId']})""")
                # embed.add_field(name=data['items'][0]['titleKo'], value=str(data['items'][0]['problemId']),inline=True)
                # embed.add_field(name=data['items'][1]['titleKo'], value=str(data['items'][1]['problemId']),inline=True)
                # embed.add_field(name=data['items'][2]['titleKo'], value=str(data['items'][2]['problemId']),inline=True)
                
                await message.reply(embed=embed)

            if len(args)==3 and (args[2]=='풀었어'):
                if is_solved(args[0], args[1]) or is_solved(args[1], args[0]):
                    await message.reply('진짜넹')
                else:
                    await message.reply('거짓말 치지 마유!')


            if len(args)==2 and (args[1]=='티어' or args[1]=='정보' or args[1]=='프로필'):
                data=get_profile_by_id(args[0])

                embed=discord.Embed(title=args[0])
                image=discord.File(f'C://MyData//code//discord//coding//images//tier//{data["tier"]}.png',filename=f'{data["tier"]}.png')
                embed.add_field(name="맞은 문제",value=f"{data['solvedCount']}")
                embed.add_field(name="레이팅",value=f"{data['rating']}")
                embed.set_thumbnail(url=f"attachment://{data['tier']}.png")
                
                await message.reply(embed=embed, file=image)
        except Exception as e:
            await message.reply('흥! 코드 제대로 짜세유!\nError:'+str(e))