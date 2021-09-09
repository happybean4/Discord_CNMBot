import asyncio
import discord
import datetime
from discord.ext import commands
import scheduleParse
from school_guide import *
import pytz
app = commands.Bot(command_prefix='&')


schedule = scheduleParse.schedule()

token = "token"
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


@app.command(name = '학사일정')
async def yearSchedule(ctx):
    embed = discord.Embed(title='학사일정표', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')

    n = 3
    for i in range(12):
        embed.add_field(name=str(n if n < 13 else n-12)+'월', value='\n'.join(schedule[n-3]), inline=True)
        n+=1
    await ctx.send(embed = embed)


@app.command(name = '1학기학사일정')
async def firstTermSchedule(ctx):
    embed = discord.Embed(title='1학기 학사일정', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')

    n = 3
    for i in range(6):
        embed.add_field(name=str(n if n < 13 else n-12)+'월', value='\n'.join(schedule[n-3]), inline=True)
        n+=1
    await ctx.send(embed = embed)

@app.command(name = '2학기학사일정')
async def secondTermSchedule(ctx):
    embed = discord.Embed(title='2학기 학사일정', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')

    n = 9
    for i in range(6):
        embed.add_field(name=str(n if n < 13 else n-12)+'월', value='\n'.join(schedule[n-3]), inline=True)
        n+=1
    await ctx.send(embed = embed)

@app.command(name = '이번달학사일정') # fixing
async def monthSchedule(ctx):
    month = int(datetime.date.today().isoformat()[5:7])
    embed = discord.Embed(title=str(month)+'월 학사일정', description=" ", color=0x00ff56)
    embed.set_author(name="충남중학교", url='https://chungnamms.djsch.kr/scheduleH/list.do?section=1&schdYear=2021')
    if month < 3:
        embed.add_field(name='일정', value='\n'.join(schedule[9+month]), inline=True)
    else:
        embed.add_field(name='일정', value='\n'.join(schedule[month+2]), inline=True)
    await ctx.send(embed = embed)




@app.command(name = '자가진단',pass_context = True)
async def selfCheck(ctx):
    embed = discord.Embed(color=0x00ff56)
    embed.set_author(name="자가진단 하러가기", url='https://hcs.eduro.go.kr/#/loginHome')
    await ctx.send(embed = embed)

@app.command(name = '시간표')
async def sigan(ctx):
    embed = discord.Embed(color=0x00ff56)
    embed.set_author(name="시간표 보러가기", url='http://xn--s39aj90b0nb2xw6xh.kr/')
    await ctx.send(embed = embed)

@app.event
async def on_message(message):
    await app.process_commands(message)
    if message.author.bot:
        return None
    msg = message.content #msg == "" or message.content == ""

    if msg == "&공지":
        embed = discord.Embed(title="**고정된 공지**", description="충남중학교 공지 입니다", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x8cb3ff)
        intcon = 1
        fixedNotis = school_gtcon()
        while intcon <= fixedNotis:            
            # print(intcon)
            noti = notify(intcon)
            embed.add_field(name="{}".format(noti[0]),value="[바로가기!](<{}>)".format(noti[1]),inline=True)
            intcon = intcon + 1
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("▶️")
        await msg.add_reaction("❌")
        def check(reaction, user):
            if user.bot == 1:
                return None
            return user == message.author and str(reaction.emoji) == '▶️' or user == message.author and str(reaction.emoji) == '❌'
        try:
            reaction, user = await app.wait_for('reaction_add', timeout=10000.0, check=check)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            if str(reaction.emoji) == "▶️":
                await msg.delete()
                embed = discord.Embed(title="**공지**", description="충남중학교 공지 입니다", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x8cb3ff)
                intcon = 1
                while intcon < 11:
                    intvalue = intcon +fixedNotis
                    #print(intvalue)
                    embed.add_field(name="{}".format(school_gt(intvalue)),value="[바로가기!](<{}>)".format(school_gu(intvalue)),inline=True)
                    intcon = intcon + 1
                    #print(intvalue)
                embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)

            if str(reaction.emoji) == "❌":
                await msg.delete()
    
            
app.run(token)
