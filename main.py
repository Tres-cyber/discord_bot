import discord
from TOKEN import TOKEN

class DiscordBot(discord.Client):
    async def on_ready(self):
        print("We have logged in {0.user}".format(self))

    async def on_message(self, message):
        # Detect that it is not send by self
        if message.author == self.user:
            return

        # Detect if message starts with prefix
        if not message.content.startswith("$"):
            return

        if v := message.author.voice:
            vc = await v.channel.connect(timeout = 60, reconnect = True)
        else:
            await message.channel.send(f"{message.author.name} is not in a VC")

if __name__ == "__main__":
    DiscordBot().run(TOKEN)
