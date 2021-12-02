import os
from dotenv import load_dotenv
import discord
import random
import asyncio
from discord import message
from discord.utils import get
from discord.ext import commands
from discord_slash import SlashCommand
from discord_components import DiscordComponents, ComponentsBot, Button
from discord_slash.utils.manage_commands import create_option
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType


load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all(), status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Jacob > SafeShows"))
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

@slash.slash(name="ping", description="Sends Thingy", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(f"🌍 Ping is `{round(bot.latency * 1000)}ms`")

@slash.slash(name="kick", description="Remove A Member (They Can Still Rejoin)", guild_ids=guild_ids, options=[
    create_option(
        name="member",
        description="Member to kick",
        option_type=6,
        required=True
    ),
    create_option(
        name="reason",
        description="Reason for kick",
        option_type=3,
        required=True
    ),
])
@slash.permission(guild_id=764805300229636107,
                  permissions=[
                      create_permission(764805300229636107,
                                        SlashCommandPermissionType.ROLE, False),
                      create_permission(767844644498440193,
                                        SlashCommandPermissionType.ROLE, True)
                  ])
async def _kick(ctx, member: discord.Member, reason: str):
    embed = discord.Embed(title="Member Kicked", color=0xd92c0d)
    embed.add_field(
        name="Member:", value=f"{member.mention}\n**ID**: {member.id}", inline=False)
    embed.add_field(name="Kicked By:",
                    value=f"{ctx.author.mention}", inline=False)
    embed.add_field(name="Reason:", value=f"{reason}", inline=False)

    embed2 = discord.Embed(
        title=f"You Have Been Kicked from {ctx.guild.name}", color=0xd92c0d)
    embed2.add_field(name="Reason:", value=f"{reason}", inline=False)
    embed2.add_field(name="Kicked By:",
                     value=f"{ctx.author.mention}", inline=False)
    await member.send(embed=embed2)
    await member.kick()
    await ctx.send(embed=embed)

@slash.slash(name="ban", description="Permanently removes a member from the server", guild_ids=guild_ids, options=[
    create_option(
        name="member",
        description="Member to ban",
        option_type=6,
        required=True
    ),
    create_option(
        name="reason",
        description="Reason for ban",
        option_type=3,
        required=True
    ),
])
@slash.permission(guild_id=764805300229636107,
                  permissions=[
                      create_permission(764805300229636107,
                                        SlashCommandPermissionType.ROLE, False),
                      create_permission(767844644498440193,
                                        SlashCommandPermissionType.ROLE, True)
                  ])
async def _ban(ctx, member: discord.Member, reason: str):
    embed = discord.Embed(title="Member Banned", color=discord.Color.red())
    embed.add_field(name="Member:", value=f"{member.mention}\n**ID**: {member.id}", inline=False)
    embed.add_field(name="Banned By:", value=f"{ctx.author.mention}", inline=False)
    embed.add_field(name="Reason:", value=f"{reason}", inline=False)

    embed2 = discord.Embed(title=f"You Have Been Banned From {ctx.guild.name}", color=0xd92c0d)
    embed2.add_field(name="Reason:", value=f"{reason}", inline=False)
    embed2.add_field(name="Banned By:", value=f"{ctx.author.mention}", inline=False)
    await member.ban(reason=reason, delete_message_days=1)
    await ctx.send(embed=embed)
    await member.send(embed=embed2)

@slash.slash(name="help", description="Shows list of commands", guild_ids=guild_ids)
async def _help(ctx):
        embed=discord.Embed(color=0x00d0ff)
        embed.add_field(name = "__**Help**__", value = "\u200b\n`/aircraft` Gives you a list of the aircraft supported by YourControls\n\n`/install` Shows the instructions on how to install YourControls\n\n`/brokengauge` Shows the list of possible fixes for the > Could not connect to the YourControls gauge")
        await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)