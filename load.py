import discord

from discord.ext import commands

import asyncio

intents = discord.Intents.default()

client = commands.Bot(command_prefix='>', intents=intents, self_bot=True)

game_name = ""

stream_name = ""

stream_url = "https://www.twitch.tv/smiley2_0"

snipes = {}

@client.event

async def on_ready():

    print(f'Bot connected as {client.user.name}')

    try:

        await client.change_presence(activity=discord.Streaming(name=stream_name, url=stream_url))

    except discord.Forbidden as e:

        print(f"Error: Cannot change presence - {e}")


@client.event

async def on_message_delete(message):

    snipes[message.channel.id] = message

@client.command(name='game')

async def game(ctx, *, game_name_here):

    global game_name

    game_name = game_name_here

    game = discord.Game(game_name)

    try:

        await client.change_presence(status=discord.Status.online, activity=game)

    except discord.Forbidden as e:

        print(f"Error: Cannot change presence - {e}")

    await ctx.send(f'Game set to {game_name}')

@client.command(name='stream')

async def stream(ctx, *, stream_name_here):

    global stream_name

    stream_name = stream_name_here

    try:

        await client.change_presence(activity=discord.Streaming(name=stream_name, url=stream_url))

    except discord.Forbidden as e:

        print(f"Error: Cannot change presence - {e}")

    await ctx.send(f'Stream name set to {stream_name}')

@client.command(name='game_reset')

async def game_reset(ctx):

    global game_name

    game_name = ""

    try:

        await client.change_presence(status=discord.Status.online, activity=None)

    except discord.Forbidden as e:

        print(f"Error: Cannot change presence - {e}")

    await ctx.send(f'Game reset')

@client.command(name='watching')

async def watching(ctx, *, activity_name):

    try:

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity_name))

    except discord.Forbidden as e:

        print(f"Error: Cannot change presence - {e}")

    await ctx.send(f'Watching {activity_name}')

@client.command(name='listening')

async def listening(ctx, *, activity_name):

    try:

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_name))

    except discord.Forbidden as e:

        print(f"Error: Cannot change presence - {e}")

    await ctx.send(f'Listening to {activity_name}')

@client.command(name='spam')

async def spam(ctx, message: str, count: int, delay: float):

    msg = await ctx.send(f"Spamming {message} {count} times with a delay of {delay} seconds...")

    for i in range(count):

        await ctx.send(message)

        await asyncio.sleep(delay)

    await msg.delete()

@client.command(name='snipe')

async def snipe(ctx):

    channel_id = ctx.channel.id

    if channel_id in snipes:

        msg = snipes[channel_id]

        await ctx.send(f"Deleted message from {msg.author}: {msg.content}")

        del snipes[channel_id]

    else:

        await ctx.send("No deleted message to snipe!")

groupchat_name = ''

gc_speed = 0.77

@client.command(name='gc')

async def groupchat(ctx, *, name):

    global toggle_groupchat, groupchat_name, number

    await ctx.message.delete()

    groupchat_name = name

    toggle_groupchat = True

    number = 1

    await update_channel_name(ctx.channel)

@client.command(name='stop')

async def stop(ctx):

    global toggle_groupchat

    await ctx.message.delete()

    toggle_groupchat = False

async def update_channel_name(channel):

    global toggle_groupchat, groupchat_name, number, gc_speed

    while toggle_groupchat:

        try:

            await channel.edit(name=f'{groupchat_name} {number}')

            number += 1

            await asyncio.sleep(gc_speed)  # wait for gc_speed seconds

        except discord.Forbidden:

            print("I don't have permission to edit the channel name.")

            break

        except discord.HTTPException as e:

            print(f"Error editing channel name: {e.status} {e.text}")

            break

class Colors:

    red = "\x1b[1;31m"

    green = "\x1b[1;32m"

    white = "\x1b[1;37m"

    orange = "\x1b[0;33m"

# Initialize counters

valid = 0

invalid = 0

total = 0

# Define the regions list

regions = [

    "brazil", "hongkong", "india", 

    "japan", "rotterdam", "russia", "singapore", 

    "southafrica","sydney", "us-central", "us-east", 

    "us-south", "us-west"

]

def get_cookies():

    """Fetch cookies from Discord with French locale."""

    r = requests.get("https://discord.com")

    cookie = r.cookies.get_dict()

    cookie["locale"] = "fr"

    return cookie

def get_headers(token, callid):

    """Generate request headers with the given token and call ID."""

    return {

        "authority": "discord.com",

        "method": "PATCH",

        "path": f"/api/v9/channels/{callid}/call",

        "scheme": "https",

        "accept": "*/*",

        "accept-encoding": "gzip, deflate, br",

        "accept-language": "fr-FR, fr;q=0.9",

        "authorization": token,

        "content-length": "21",

        "content-type": "application/json",

        "origin": "https://discord.com",

        "referer": f"https://discord.com/channels/@me/{callid}",

        "sec-fetch-dest": "empty",

        "sec-fetch-mode": "cors",

        "sec-fetch-site": "same-origin",

        "sec-gpc": "1",

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",

        "x-debug-options": "bugReporterEnabled",

        "x-discord-locale": "fr",

        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMDg5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="

    }

@client.command(name='rfuck')

async def region_change(ctx, token: str, callid: str):

    global valid, invalid, total

    await ctx.send("Starting the region change process...")

    headers = get_headers(token, callid)

    try:

        while True:

            region = random.choice(regions)

            r = requests.patch(f"https://discord.com/api/v9/channels/{callid}/call", 

                               headers=headers, 

                               cookies=get_cookies(), 

                               json={"region": region})

            if r.status_code == 204:

                valid += 1

                total += 1

                await ctx.send(f"{Colors.green}Successfully set region to {region} ({valid}/{total}){Colors.white}")

            else:

                invalid += 1

                total += 1

                try:

                    error_message = r.json()

                except ValueError:

                    error_message = "Unknown error"

                await ctx.send(f"{Colors.red}Failed to set region: {error_message} ({invalid}/{total}){Colors.white}")

            

            # Add a delay to respect rate limits

            await asyncio.sleep(6)  # Adjust sleep time according to your needs (e.g., 0.5 seconds)

    except KeyboardInterrupt:

        await ctx.send("Process stopped by user.")

    except Exception as e:

        await ctx.send(f"{Colors.orange}An error occurred: {e}{Colors.white}")
reacting = False
custom_emoji = '☠️'
@client.command(name='react', help='Toggle reactions on or off')

async def react(ctx, toggle: str):

    global reacting

    if toggle.lower() == 'on':

        reacting = True

        print("Reactions are now enabled.")

        await ctx.message.add_reaction(custom_emoji)

    elif toggle.lower() == 'off':

        reacting = False

        print("Reactions are now disabled.")

        await ctx.message.add_reaction(custom_emoji)

    else:

        await ctx.send("Invalid command usage. Use `>react on` or `>react off`.")

@client.command(name='cr', help='Set a custom emoji for reactions')

async def set_emoji(ctx, emoji: str):

    global custom_emoji

    custom_emoji = emoji

    print(f"Custom emoji set to {custom_emoji}")

    await ctx.message.add_reaction(custom_emoji)

@client.event

async def on_message(message):

    if message.author == client.user and reacting:

        await message.add_reaction(custom_emoji)

    await client.process_commands(message)
client.run("Token", bot=False)
