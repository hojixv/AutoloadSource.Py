from discord.ext import commands
import random

host = commands.Bot(command_prefix='>', self_bot=True)

user_id = 1197304673288323193
async def on_ready():
    print(f'Connected as {host.user.name}')

@host.event
async def on_message(message):
    member = message.author
    if member.id == user_id:
        await message.channel.send(f'<@{user_id}> {random.choice(replies)}')

host.run('', bot=False)
