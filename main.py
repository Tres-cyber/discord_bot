import discord
from TOKEN import TOKEN

class DiscordBot(discord.Client):
    async def on_ready(self):
        print("We have logged in {0.user}".format(self))

    async def on_message(self, message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')

        if message.author == self.user:
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

DiscordBot().run(TOKEN)
