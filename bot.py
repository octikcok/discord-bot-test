import discord

intents = discord.Intents.default()
intents.message_content = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}已經上線惹owo')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTA3Mzk2MzM1MjY3MTQwNDA3Mg.GCEEfD.SXclCj1hAr8kOp9TjEg6G-ESSfNKQVce0nUkS4')