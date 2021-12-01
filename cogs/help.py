import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


guild_ids = [764805300229636107]


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="aircraft", description="Lists supported aircraft", guild_ids=guild_ids)
    async def _aircraft(self, ctx):
        embed=discord.Embed(color=0x00d0ff)
        embed.add_field(name = "__**Supported Aircraft**__", value = "\u200b\n`• All stock Asobo Aircraft`\n`• Carenado M20R Ovation`\n`• Carenado PA34T Seneca V`\n`• FlyByWire A32NX Development`\n`• FlyByWire A32NX Experimental`\n`• Headwind A330-900`\n`• Heavy Division 78XH`\n`• Hype Performace Group H135`\n`• JPLogistics C152`\n`• JustFlight PA-28R Arrow III`\n`• mixMugz TBM 930`\n`• Mrtommymxr C172`\n`• Mrtommymxr DA42NGX`\n`• Mrtommymxr DA62X`\n`• PMDG DC-6A-B`\n`• RotorSimPilot R44`\n`• Salty Simulations 747-8i`\n`• TheFrett Bonanza G36`\n`• Working Title CJ4`")    
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))