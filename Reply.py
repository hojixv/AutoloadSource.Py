import discord
import time 
import random
import os
import time
from threading import *


client = discord.Client()
token = "W_W_W"
 
name1 = ["Messag1", "messag2", "u get the point"]
user1 = [123456]
name2 = ["Messag1", "messag2", "u get the point"]
user2 = [123456]


@client.event
async def on_message(message):
    if message.author.id in [12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345]:
        await message.channel.trigger_typing()
        time.sleep(0.01)
        await message.channel.send(random.choice(["hey slut shut the fuck up","you're hideous bitch shut up and clean my dogs feces","hey slut come lick my armpits","prostitute stfu slut","bitch shut up","you are ass nigga you wanna be me so bad","why do your armpits smell like that","stop eating horse semen you faggot","stop sending me your butthole in DMs gay boy","why are you drinking tap water out of that goats anus","say something back bitch","you have a green shit ring around your bootyhole","i heard you use snake skin dildos","ill cum in your mouth booty shake ass nigga","type in chat stop fingering your booty hole","i heard you worship cat feces","worthless ass slave","get your head out of that toilet you slut","is it true you eat your dads belly button lint? pedo","fuck up baby fucker","dont you jerk off to elephant penis","hey i heard you eat your own hemorroids","shes only 5 get your dick off of her nipples pedo","you drink porta potty water","hey bitch\nstfu\nyou dogshit ass nigga\nill rip your face apart\nugly ass fucking pedo\nwhy does your dick smell like that\ngay ass faggot loser\n🤡\nfucking freak\nshut up","i\nwill\nrip\nyour\nhead\noff\nof\nyour\nshoulders\npussy\nass\nslime ball","nigga\nshut\nup\npedophile","stfu you dogshit ass nigga you suck\nyour belly button smells like frog anus you dirty ass nigga\nill rape your whole family with a strap on\npathetic ass fucking toad","YOU\nARE\nWEAK\nAS\nFUCK\nPUSSY\nILL\nRIP\nYOUR\nVEINS\nOUT\nOF\nYOUR\nARMS\nFAGGOT\nASS\nPUSSY\nNIGGA\nYOU\nFRAIL\nASS\nLITTLE\nFEMBOY","tranny anus licking buffalo","your elbows stink","frog","ugly ass ostrich","pencil necked racoon","why do your elbows smell like squid testicals","you have micro penis","you have aids","semen sucking blood worm","greasy elbow geek","why do your testicals smell like dead   buffalo appendages","cockroach","Mosquito","bald penguin","cow fucker","cross eyed billy goat","eggplant","sweat gobbler","cuck","penis warlord","slave","my nipples are more worthy than you","hairless dog","alligator","shave your nipples","termite","bald eagle","hippo","cross eyed chicken","spinosaurus rex","deformed cactus","prostitute","come clean my suit","rusty nail","stop eating water balloons","dumb blow dart","shit ball","slime ball","golf ball nose","take that stick of dynamite out of your nose","go clean my coffee mug","hey slave my pitbull just took a shit, go clean his asshole","walking windshield wiper","hornet","homeless pincone","hey hand sanitizer come lick the dirt off my hands","ice cream scooper","aborted fetus","dead child","stop watching child porn and fight back","homeless rodant","hammerhead shark","hey sledgehammer nose","your breath stinks","you cross eyed street lamp","hey pizza face","shave your mullet","shrink ray penis","hey shoe box come hold my balenciagas","rusty cork screw","pig penis","hey cow sniffer","walking whoopee cushion","stop chewing on your shoe laces","pet bullet ant","hey mop come clean my floor","*rapes your ass* now what nigga","hey tissue box i just nutted on your girlfriend come clean it up","watermelon seed","hey tree stump","hey get that fly swatter out of your penis hole","melted crayon","hey piss elbows","piss ball","hey q tip come clean my ears","why is that saxaphone in your anus","stink beetle","bed bug","cross eyed bottle of mustard","hey ash tray","hey stop licking that stop sign","why is that spatula in your anus","hey melted chocolate bar","dumb coconut"])+ f" {message.author.mention}")
        if message.author.id in user1: 
            await message.channel.send(random.choice([name1]))
        if message.author.id in user2: 
            await message.channel.send(random.choice([user2]))
@client.event
async def on_ready():
    os.system("cls")
@client.event
async def on_ready():
    os.system("cls")
    print(f"hey {client.user.name}, auto reply is ready")



 
client.run(token, bot=False)
