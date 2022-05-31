import asyncio
import os
from dotenv import load_dotenv
import discord
bot = discord.Client()
load_dotenv('config.env')

@bot.event
async def on_ready():
    channelid = int(os.getenv('CHANNEL'))
    channel = bot.get_channel(channelid)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Message sent. Please ^C to exit")
    await channel.send("Grab the ID of this message and input it in config.env as MESSAGEID")

bot.run(os.getenv('TOKEN'))
