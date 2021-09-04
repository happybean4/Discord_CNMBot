import asyncio
import discord

app = discord.Client()

token = "ODgzMTY1ODc3MTQ1NTc1NDc0.YTF-UQ.f9_LK1thkvFui34_3QhuRjE2WPc"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("충남중학교") #새로운 코드
    await app.change_presence(status=discord.Status.online, activity=game) #바뀜

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    
            
app.run(token)
