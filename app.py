# Work with Python 3.6
import discord

TOKEN = 'NTIyNDMzNDU2NDE2NzUxNjM1.DvK5-A.e8mWyS48_6ytPPrvpUsZfmD_DcU'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Fuck you'):
        msg = 'Yes I will {0.author.mention}, and you sister too'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('fuck you'):
        msg = 'Yes I will {0.author.mention}, and you sister too'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('comment va ?'):
        msg = 'Super merci bien ! et toi ?:)'.format(message)
        await client.send_message(message.channel, msg)
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)