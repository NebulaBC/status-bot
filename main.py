import asyncio
import os
from dotenv import load_dotenv
import discord
from mcstatus import MinecraftServer
from tabulate import tabulate

def main():
    load_dotenv('config.env')

    bot = discord.Client()

    async def updatestatus():
        await bot.wait_until_ready()
        channelid = int(os.getenv('CHANNEL'))
        sleeptime = int(os.getenv('COOLDOWN'))
        serverip = os.getenv('SERVERIP')
        messageid = os.getenv('MESSAGEID')
        channel = bot.get_channel(channelid)
        msg = await channel.fetch_message(messageid)

        while not bot.is_closed():
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                server = MinecraftServer.lookup(serverip1)
                response = server.status()
                await bot.change_presence(activity=discord.Game(name="Server is online"))
                if response.players.sample is not None:
                    players = [f"{player.name}" for player in response.players.sample]
                    playertable = f'{tabulate(players, tablefmt="rst")}'
                    print(f'Players online\n{playertable.replace(" ", "")}')
                    await msg.edit(f'Players online\n{playertable.replace(" ", "")}')
                else:
                    print("No players currently online")
                    await msg.edit(f'No players currently online')
            except:
                print("Server is offline")
                await msg.edit('Server is offline')
                await bot.change_presence(activity=discord.Game(name="Server is offline"))
            await asyncio.sleep(sleeptime)

    bot.loop.create_task(updatestatus())
    bot.run(os.getenv('TOKEN'))

if __name__ == "__main__":
    main()
