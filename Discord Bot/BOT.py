import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Ne-am conectat ca {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startwith('$salut'):
        await message.chanel.sed('Salut!')

client.run(os.getenv('TOKEN'))