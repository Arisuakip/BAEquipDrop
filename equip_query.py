from os import urandom
from PIL import Image, ImageSequence
import requests
import re
import os
from io import BytesIO
import datetime
from .baEquip import *
import nonebot
from hoshino import Service

sv = Service('equipQuery', help_="装备掉落查询")
t = str(datetime.date.today())
getList()
@sv.on_keyword("查掉落")
async def exper(bot,ev):
    order = str(ev.message).split(" ")[0]
    if order != "查掉落":
        return
    equipName = str(ev.message).split(" ")[1]
    id = nameToId(equipName)
    if id == -1:
        warns = "查询格式为:t2装备种类\n装备种类参考:帽子|手套|鞋子|背包|徽章|符咒|发卡|手表"
        await bot.send(ev,warns,at_sender=True)
        return
    s = getStr(equipName)
    s = f"装备:{equipName}的掉落分布为:\n" + s
    await bot.send(ev, s,at_sender=True)
