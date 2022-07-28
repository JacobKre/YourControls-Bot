import os
from dotenv import load_dotenv
import random
import asyncio
import interactions
from interactions import Client, Intents

load_dotenv()

bot = Client(token=os.getenv('TOKEN'), intents=Intents.GUILD_MESSAGE_CONTENT)

guild_ids = [764805300229636107]
ready = False

async def changePres():
    await bot.wait_until_ready()
    statuses = ["/help", "Flying With Friends"]
    await bot.change_presence(interactions.ClientPresence(activities=[interactions.PresenceActivity(name=random.choice(statuses), type=interactions.PresenceActivityType.GAME)]))
    await asyncio.sleep(6)
bot._loop.create_task(changePres())


@bot.event
async def on_ready():
    global ready
    print("Ready!")
    ready = True

@bot.event
async def on_message(message):
    if ("support" in message.content) and ("737" in message.content) and message.author.id != 776052285235003392:
        await message.reply("Support for the PMDG 737 will come when it comes, if it comes at all. Until then, please be patient and enjoy of the other aircraft YourControls supports.")        

@bot.event
async def on_message(message):
    if ("support" in message.content) and ("737" in message.content) and message.author.id != 776052285235003392:
        await message.reply("Support for the PMDG 737 will come when it comes, if it comes at all. Until then, please be patient and enjoy of the other aircraft YourControls supports.")        
    
@bot.command(name="ping", description="Sends Thingy", scope=guild_ids)
async def _ping(ctx):
    await ctx.send(f"🌍 Ping is `{round(bot.latency * 1000)}ms`")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename}')

bot.start()