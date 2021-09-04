import asyncio
import discord
from discord.ext import commands
import random
from bs4 import BeautifulSoup
import urllib
import urllib.request
import pickle
import operator
import requests
from json import loads
from urllib.request import Request, urlopen
app = commands.Bot(command_prefix='&')

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


    
@app.command(name = '자가진단',pass_context = True)
async def selfCheck(ctx):
    embed = discord.Embed(color=0x00ff56)
    embed.set_author(name="자가진단 하러가기", url='https://hcs.eduro.go.kr/#/loginHome')
    await ctx.send(embed = embed)
@app.command(name = 'UBD', pass_context = True)
async def ubd(ctx,*,a):
    s = float(a) / 170000
    await ctx.send(str(a)+" = "+str(s)+"UBD")

@app.event
async def on_message(message):
    await app.process_commands(message)
    if message.author.bot:
        return None
    
            
app.run(token)
