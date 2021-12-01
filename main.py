import os
from dotenv import load_dotenv
import discord
import random
import asyncio
from discord.ext import commands
from discord import message
from discord.utils import get
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="YourControls v2.6.3"))
slash = SlashCommand(bot, sync_commands=True)

guild_ids = [764805300229636107]
ready = False

#Load Cogs
@bot.command()
async def load(ctx, extention):
    bot.load_extension(f'cogs.{extention}')
#Unload Cogs
@bot.command()
async def unload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')

@bot.event
async def on_ready():
    global ready
    print("Ready!")
    ready = True

@slash.slash(name="ping", description="Shows bot latency", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(f"🌍 Ping is `{round(bot.latency * 1000)}ms`")





bot.run(token)