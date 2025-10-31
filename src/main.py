import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} conectou e esta ativo')

@bot.command()
async def ping(ctx:commands.Context):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(name= 'dice')
async def roll_dice(ctx:commands.Context, sides:int):
    if sides <= 1:
        await ctx.send("o dado precisa de pelo menos 2 lados")
        return
    roll = random.randint(1, sides)
    await ctx.send(f'🎲 {ctx.author.mention} rolou um d{sides} e tirou **{roll}**!')

@bot.command(name= 'cdice')
async def complex_dice(ctx:commands.Context, *,expression: str):
    pattern = r'(\d+)d(\d+)(?:\s*([+-])\s*(\d+))?'
    match = re.match(pattern, expression)

    if not match:
        await ctx.send(f"a expressão \"{expression}\" não é valida, use algo como 3d20 + 2")
        return

    dices = int(match.group(1))
    dice_sides = int(match.group(2))
    modifier_sign = match.group(3)
    modifier_value = match.group(4)

    modifier = 0

    if modifier_sign and modifier_value:
        modifier = int(modifier_value)
        if modifier_sign == '-':
            modifier = -modifier

    rolls = [random.randint(1, dice_sides ) for i in range(dices)]
    total = sum(rolls) + modifier

    rolls_str = ' + '.join(str(r) for r in rolls)

    if modifier > 0:
        await ctx.send(f'🎲 **Resultado:** ({rolls_str}) + {modifier} = **{total}**')
    elif modifier < 0:
        await ctx.send(f'🎲 **Resultado:** ({rolls_str}) - {abs(modifier)} = **{total}**')
    else:
        await ctx.send(f'🎲 **Resultado:** ({rolls_str}) = **{total}**')

bot.run(TOKEN)