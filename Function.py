import discord
import os
import random
import asyncio
import roles
import channels
import members
import json
import io
import glob
import requests
from discord.ext import commands
from discord.utils import get
from io import BytesIO, StringIO
from discord.ext.commands import has_permissions
from discord.ext.commands import CheckFailure
from host import host
from replit import db
from PIL import Image, ImageChops, ImageDraw, ImageFont


def rolefilter(ctx, member: discord.Member):
    guild = ctx.guild
    if discord.utils.get(guild.roles, id=roles.kp) in member.roles:
        role = 'Cố vấn'
    elif discord.utils.get(guild.roles, id=roles.namdausv) in member.roles:
        role = 'Tổng thống S.U.I'
    elif discord.utils.get(guild.roles, id=roles.bonkerpp) in member.roles:
        role = 'Thủ tướng'
    elif discord.utils.get(guild.roles, id=roles.bonker) in member.roles:
        role = 'Thống tướng'
    elif discord.utils.get(guild.roles, id=roles.truongphong) in member.roles:
        role = 'Đại tướng'
    elif discord.utils.get(guild.roles, id=roles.phophong) in member.roles:
        role = 'Trung tướng'
    elif discord.utils.get(guild.roles, id=roles.botrole) in member.roles:
        role = 'Thiếu tướng'
    elif discord.utils.get(guild.roles, id=roles.suimem) in member.roles:
        role = 'Đại tá'
    elif discord.utils.get(guild.roles, id=roles.viprole) in member.roles:
        role = 'Thanh tra'
    elif discord.utils.get(guild.roles, id=roles.godofsui) in member.roles:
        role = 'Điều tra viên cấp cao'
    elif discord.utils.get(guild.roles, id=roles.suixuyenvutru) in member.roles:
        role = 'Điều tra viên cấp cao'
    elif discord.utils.get(guild.roles, id=roles.suidividoichophep) in member.roles:
        role = 'Điều tra viên'
    elif discord.utils.get(guild.roles, id=roles.suitrieunam) in member.roles:
        role = 'Điều tra viên'
    elif discord.utils.get(guild.roles, id=roles.vanvatdieusui) in member.roles:
        role = 'Đặc vụ'
    elif discord.utils.get(guild.roles, id=roles.canbosui) in member.roles:
        role = 'Đặc vụ'
    else:
        role = 'Nhân viên thường'
    return role

def rankfilter(wallet):    
    rank = 'Chưa có!'
    if wallet < 5000:
      rank = 'Chưa có!'
    elif wallet < 10000:
      rank = "New Bettor"
    elif wallet < 50000:
      rank = "Nghiện cờ bạc"
    elif wallet < 100000:
      rank = "Thần bài"
    elif wallet < 500000:
      rank = "Vua Bịp"
    elif wallet < 1000000:
      rank = "Chúa Tể Bài Bịp"
    elif wallet < 5000000:
      rank = "Cheater?"
    elif wallet < 10000000:
      rank = "HACK TIỀN 99%"
    else:
      rank = "THAM NHŨNG??"  
    return rank

def bgfilter(member):
    background = Image.open("./file/profilecard.png").convert("RGBA")
    with open("./background.json","r") as f:
      bgs = json.load(f)
      
    if str(member.id) in bgs:
      if 'check' in bgs[str(member.id)]:
        if bgs[str(member.id)]['check'] == 1:
          bg = bgs[str(member.id)]['background']
          response = requests.get(bg)
          image_bytes = io.BytesIO(response.content)
          img = image_bytes
          background = Image.open(image_bytes).convert("RGBA")


    with open("./background.json","w") as f:
      json.dump(bgs, f)
    return background

def basefilter(member):
  with open("./background.json","r") as f:
      bgs = json.load(f)
  base = Image.open("./file/profilecard.png").convert("RGBA")
  if str(member.id) in bgs:
    if 'theme' in bgs[str(member.id)]:
      if bgs[str(member.id)]['theme'] == 1:
        base = Image.open("./file/profilecard.png").convert("RGBA")
      if bgs[str(member.id)]['theme'] == 2:
        base = Image.open("./file/profilecard2.png").convert("RGBA")
      if bgs[str(member.id)]['theme'] == 3:
        base = Image.open("./file/profilecard3.png").convert("RGBA")
      if bgs[str(member.id)]['theme'] == 4:
        base = Image.open("./file/profilecard4.png").convert("RGBA")
      if bgs[str(member.id)]['theme'] == 5:
        base = Image.open("./file/profilecard5.png").convert("RGBA")
  with open("./background.json","w") as f:
      json.dump(bgs, f)

  return base