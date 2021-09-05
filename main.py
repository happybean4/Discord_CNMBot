import asyncio
import discord
import datetime
from discord.ext import commands
import scheduleParse
app = commands.Bot(command_prefix='&')


schedule = scheduleParse.schedule()

token = "비밀코드"
calcResult = 0
class Administrator(commands.Cog, name="관리자"):
    def __init__(self, app):
        self.app = app
@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("충남중학교") #새로운 코드
    await app.change_presence(status=discord.Status.online, activity=game) #바뀜


def setup(app):
    app.add_cog(Administrator(app))


@app.command(name = '연간행사')
async def yearSchedule(ctx):
    embed = discord.Embed(title='연간행사표', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')

    n = 3
    for i in range(12):
        embed.add_field(name=str(n if n < 13 else n-12)+'월', value='\n'.join(schedule[n-3]), inline=True)
        n+=1
    await ctx.send(embed = embed)

@app.command(name = '1학기행사')
async def firstTermSchedule(ctx):
    embed = discord.Embed(title='연간행사표', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')

    n = 3
    for i in range(6):
        embed.add_field(name=str(n if n < 13 else n-12)+'월', value='\n'.join(schedule[n-3]), inline=True)
        n+=1
    await ctx.send(embed = embed)

@app.command(name = '2학기행사')
async def secondTermSchedule(ctx):
    embed = discord.Embed(title='연간행사표', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')

    n = 9
    for i in range(6):
        embed.add_field(name=str(n if n < 13 else n-12)+'월', value='\n'.join(schedule[n-3]), inline=True)
        n+=1
    await ctx.send(embed = embed)

@app.command(name = '이달의행사')
async def monthSchedule(ctx):
    month = int(datetime.today.month.isoformat())
    embed = discord.Embed(title=str(month)+'월행사표', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')
    if month < 3:
        embed.add_field(name='행사', value='\n'.join(schedule[9+month]), inline=True)
    else:
        embed.add_field(name='행사', value='\n'.join(schedule[month+2]), inline=True)

@app.command(name = '자가진단',pass_context = True)
async def selfCheck(ctx):
    embed = discord.Embed(color=0x00ff56)
    embed.set_author(name="자가진단 하러가기", url='https://hcs.eduro.go.kr/#/loginHome')
    await ctx.send(embed = embed)

@app.event
async def on_message(message):
    await app.process_commands(message)
    if message.author.bot:
        return None
    
            
app.run(token)
