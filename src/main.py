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


bot.run(TOKEN)