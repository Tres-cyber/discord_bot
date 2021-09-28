import discord
import random
from TOKEN import TOKEN


client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == '$hello':
        await message.channel.send(f'Hellu {username}! ')
        return
    elif user_message.lower() == '$bye':
        await message.channel.send(f'UwU {username}')
        return
    elif user_message.lower() == '$fuckyou':
        await message.channel.send(f'fuck you{username}')
        return
    elif user_message.lower() == '$random':
        response = f'This is ur number: {random.randrange(10000)}'
        await message.channel.send(response)
        return

    if message.channel.lower() == '!anywhere':
        await message.channel.send('Hellu I\'m here')
        return

client.run(TOKEN)

