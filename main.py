import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    username = str(message.author.name)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username}: {user_message} ({channel})')
    
    if message.author == client.user:
        return
    
    # if channel == 'sara-bot':
        # if 'hello' in user_message.lower():
        #     await message.channel.send(f'Hello {username}, pal!!')
        #     print('Message Sent!!')
        #     return
        
        # if 'i miss you' in user_message.lower():
        #     await message.channel.send(f'I miss you, too, {username}.')
        #     print('Message Sent!!')
        #     return
        
        # if 'อีควาย' in user_message:
        #     await message.channel.send(f'มึงสิควาย')
        #     print('Message Sent!!')
        #     return

    if message.content.startswith('$hello'):
      await message.channel.send(f'Hello! {username}')

    if message.content.startswith('$help'):
      await message.channel.send('I cannot do anything now. Donate to help me upgrade. 🥰')


keep_alive()
client.run(os.environ['TOKEN'])
