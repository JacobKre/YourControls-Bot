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

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, override_type=True)

guild_ids = [764805300229636107]
ready = False

async def changePres():
    await bot.wait_until_ready()
    statuses = ["/help", "Flying With Friends"]
    await bot.change_presence()
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=f"{status}"))

        await asyncio.sleep(6)
bot.loop.create_task(changePres())

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

@slash.slash(name="idban", description="Permanently removes a member from the server", guild_ids=guild_ids, options=[
    create_option(
        name="id",
        description="ID of member to ban",
        option_type=3,
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
async def _idban(ctx, id: str, reason: str):
    user = await bot.fetch_user(id)
    embed = discord.Embed(title="Member Banned", color=discord.Color.red())
    embed.add_field(name="Member:", value=f"{user.mention}\n**ID**: {user.id}", inline=False)
    embed.add_field(name="Banned By:", value=f"{ctx.author.mention}", inline=False)
    embed.add_field(name="Reason:", value=f"{reason}", inline=False)

    embed2 = discord.Embed(title=f"You Have Been Banned From {ctx.guild.name}", color=0xd92c0d)
    embed2.add_field(name="Reason:", value=f"{reason}", inline=False)
    embed2.add_field(name="Banned By:", value=f"{ctx.author.mention}", inline=False)
    await ctx.guild.ban(user, reason=reason, delete_message_days=1)
    await ctx.send(embed=embed)
    await user.send(embed=embed2)

@slash.slash(name="unban", description="Unbans a member from the server", guild_ids=guild_ids, options=[
    create_option(
        name="id",
        description="ID of member to ban",
        option_type=3,
        required=True
    )
])
@slash.permission(guild_id=764805300229636107,
                  permissions=[
                      create_permission(764805300229636107,
                                        SlashCommandPermissionType.ROLE, False),
                      create_permission(767844644498440193,
                                        SlashCommandPermissionType.ROLE, True)
                  ])
async def _unban(ctx, id: str):
    user = await bot.fetch_user(id)
    embed = discord.Embed(title="Member Unbanned", color=discord.Color.green())
    embed.add_field(name="Member:", value=f"{user.mention}\n**ID**: {user.id}", inline=False)
    embed.add_field(name="Unbanned By:", value=f"{ctx.author.mention}", inline=False)

    embed2 = discord.Embed(title=f"You Have Been Unbanned From {ctx.guild.name}", color=0xd92c0d)
    embed2.add_field(name="Unbanned By:", value=f"{ctx.author.mention}", inline=False)
    await ctx.guild.unban(user)
    await ctx.send(embed=embed)
    await user.send(embed=embed2)

@slash.slash(name="clear", description="Removes a specified number of messages", guild_ids=guild_ids, options=[
    create_option(
        name="amount",
        description="Number of messages to remove",
        option_type=4,
        required=True
    )
])
@slash.permission(guild_id=764805300229636107,
                  permissions=[
                      create_permission(764805300229636107,
                                        SlashCommandPermissionType.ROLE, False),
                      create_permission(767844644498440193,
                                        SlashCommandPermissionType.ROLE, True)
                  ])
async def _clear(ctx, amount):
    if amount > 50:
        embed = discord.Embed(description = f"⚠️ **Please choose a smaller number of messages to remove. (Max 50)**.", color = discord.Color.from_rgb(255, 234, 0))
        await ctx.send(embed=embed)
        await asyncio.sleep(6)
        await ctx.channel.purge(limit=1)
    else:
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(description = f"♻ **{amount} Messages Removed**.", color = discord.Color.green())
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=1)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)