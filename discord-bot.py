import discord
from discord.ext import commands
intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print("Bot is ready")
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'привет, {member.name}! добро пожаловать на сервер!')
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def commands(ctx):
    await ctx.send('команды бота:\n/ping: проверка работы бота\n/kalc+: сумма двух чисел\n/kalc-: разность двух чисел\n/kalc*: произведение двух чисел\n/kalc/: частное двух чисел')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('/kalc+'):
        try:
            numbers = message.content.split()
            a = int(numbers[1])
            b = int(numbers[2])
            c = a + b
            await message.channel.send(f'сумма чисел {a} и {b} = {c}')
        except:
            await message.channel.send('неправильный ввод данных!')
    if message.content.startswith('/kalc-'):
        try:
            numbers = message.content.split()
            a = int(numbers[1])
            b = int(numbers[2])
            c = a - b
            await message.channel.send(f'разность чисел {a} и {b} = {c}')
        except:
            await message.channel.send('неправильный ввод данных!')
    if message.content.startswith('/kalc*'):
        try:
            numbers = message.content.split()
            a = int(numbers[1])
            b = int(numbers[2])
            c = a * b
            await message.channel.send(f'произведение чисел {a} и {b} = {c}')
        except:
            await message.channel.send('неправильный ввод данных!')
    if message.content.startswith('/kalc/'):
        try:
            numbers = message.content.split()
            a = int(numbers[1])
            b = int(numbers[2])
            c = a / b
            await message.channel.send(f'частное чисел {a} и {b} = {c}')
        except:
            await message.channel.send('неправильный ввод данных!')

    await bot.process_commands(message)

bot.run('token')
