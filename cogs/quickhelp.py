import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


guild_ids = [764805300229636107]


class quickhelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ping", description="Sends Thingy", guild_ids=guild_ids)
    async def _ping(self, ctx):
       await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(quickhelp(bot))