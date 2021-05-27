import asyncio
import datetime
import discord
import datetime
from discord.embeds import Embed
from discord.ext import commands
from datetime import date, timedelta, datetime, tzinfo, timezone 

loadtime = 15
timestamp = datetime.now()
datatime = timestamp.strftime(r"%b %d, %Y %H:%M:%S")
date_for_log_join = "%b %d, %Y %H:%M:%S"


Bot = commands.Bot(command_prefix="//")

@Bot.command()
async def msg (ctx,*,arg):
    await ctx.message.delete()
    await ctx.send(arg)

@Bot.command()
async def kick (ctx, member:discord.Member,*,reason):
    await ctx.message.delete()
    channel = Bot.get_channel(845335403431067648)
    moder = ctx.message.author
    moderid = ctx.message.author.id
    if not member:
        emb = discord.Embed(title=f'Кик с сервера ● Не указан участник', timestamp=ctx.message.created_at)
        emb.add_field(name=f'Ты не указал пользователя которого нужно кикнуть.')
        emb.set_footer(text='ID: ' + str(member.id))
        await ctx.send(emb=Embed)
        return
    emb = discord.Embed(title=f'Кик с сервера ● Успешно', timestamp=ctx.message.created_at)
    emb.add_field(name=f'Мут выдан.', value=f'Участник: {member} успешно кикнут с сервера.')
    emb.add_field(name=f'Выдан модератором: ', value=f'{moder.mention}, ({moderid})')
    emb.add_field(name=f'По причине: ', value=f'`{reason}`')
    emb.set_footer(text='ID нарушителя: ' + str(member.id))
    await member.send(f'Привет, тебя кикнули с сервера FullWix. Тебя кикнул: {moder} ({moderid}, по причине: {reason}. Обжаловать наказание можно в группе вк (https://vk.com/fullwixvk) или напиши мне в лс Fulavik#6092.')
    await channel.send(embed=emb)
    await member.kick(reason=f'Кикнутый: {member}, модератор: {moder} ({moderid}), по причине: {reason}')

@Bot.command()
async def setnickname (ctx, nickname):
    member = discord.Member
    await ctx.message.delete()
    await member.edit(nick=nickname)
	
@Bot.command()
async def ban (ctx, member:discord.Member,*,reason):
    await ctx.message.delete()
    channel = Bot.get_channel()

@Bot.command()
async def info (ctx):
    await ctx.message.delete()
    emb = discord.Embed(title=f'Информация о сервере')

@Bot.event
async def on_ready():
    channel = Bot.get_channel(845002283103682580)
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game("Бот запускается..."))
    await asyncio.sleep(5)
    print('Бот запустился.')
    await channel.send('`Бот успешно запущен.`')
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft: fullwix.ml"))

@Bot.event
async def on_member_join(member):
    channel_join_unjoin = Bot.get_channel(819149113786236948)
    memberid = member.id
    emblog = discord.Embed(title=f'Новый участник ● {member}')
    emblog.add_field(name=f'Имя участника: {member}', value=f'ID: {memberid}')
    emblog.add_field(name='Зарегестрировался в Дискорде: ', value=member.created_at.strftime(date_for_log_join), inline=False)
    emblog.set_author(name=str(member), icon_url=member.avatar_url)
    emblog.set_thumbnail(url=member.avatar_url)
    emblog.set_footer(text='ID: ' + str(member.id))
    await channel_join_unjoin.send(embed=emblog)
    embmember = discord.Embed(title=f'Приветствую тебя на FullWix')
    embmember.add_field(name=f'Приветствую тебя на дискорд сервере проекта FullWix', value=f'Советую ознакомиться со всеми правилами в канале #информация-и-правила🧾, #🎤новости👷. Если тебе автоматически не выдалась роль в канале #🔒тык🔓 или хочешь задать вопрос администрации напиши в канал #🆘помощь🆘.')
    await member.send(embed=embmember)

@Bot.event
async def on_member_remove(member):
    channel_join_unjoin = Bot.get_channel(819149113786236948)
    memberid = member.id
    emblog = discord.Embed(title=f'Участник покинул сервер ● {member}')
    emblog.add_field(name=f'Имя участника: ', value=f'{member}')
    emblog.add_field(name=f'Зарегестрировался в Дискорде: ', value=member.created_at.strftime(date_for_log_join))
    emblog.set_author(name=str(member), icon_url=member.avatar_url)
    emblog.set_thumbnail(url=member.avatar_url)
    emblog.set_footer(text='ID: ' + str(member.id))
    await channel_join_unjoin.send(embed=emblog)


Bot.run('ODQ0OTk4MDc3MjIzNTM0NjQy.YKajyA.USXUbvwx41Jl8goP8PyQ2p364-A')