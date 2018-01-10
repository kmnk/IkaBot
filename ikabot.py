import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("Hello IkaBot!"):
        if client.user == message.author: return

        m = "Hello " + message.author.name + " !!"

        await client.send_message(message.channel, m)

def read_token():
    with open('TOKEN') as f:
        arr = [line.rstrip() for line in f]

    return arr[0]

client.run(read_token())
