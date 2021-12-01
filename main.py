import os
from dotenv import load_dotenv
import discord
import random
import asyncio
from discord import message
from discord.utils import get
from discord.ext import commands
from discord_slash import SlashCommand
load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all(), status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="YourControls v2.6.3"))
slash = SlashCommand(bot, sync_commands=True, override_type=True)

guild_ids = [764805300229636107]
ready = False

@bot.event
async def on_ready():
    global ready
    print("Ready!")
    ready = True

#Load Cogs
@bot.command()
async def load(ctx, extention):
    bot.load_extension(f'cogs.{extention}')

#Unload Cogs
@bot.command()
async def unload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)