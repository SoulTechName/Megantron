import discord
import asyncio as ay
import time

client = discord.Client()
prefix = "||"


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event

async def on_message(message):
    # checks for the message starting with help #
    # and if it does, places a list of commands #
    # in the authors discord inbox #
    if message.content.startswith(prefix + 'help'):
        for servers in client.servers:
            for members in servers.members:
                if members == message.author:
                    await client.send_message(members, "A list of commands: "
                                                       "```"
                                                       " ||activate - Joins the voice call and plays a sexy voice\n "
                                                       "||meganSpam - Special event for the voice call\n "
                                                       "||help - gets help (I think)\n"
                                                       "```")

    # Checks if the activate command is called and #
    # if it is, joins the voice call and plays the #
    # inputed file #
    elif message.content.startswith(prefix + 'activate'):
        voice = await client.join_voice_channel(client.get_channel("249599549826400256"))
        player = voice.create_ffmpeg_player('My_sex_voice.wav')
        player.start()
        time.sleep(3)
        player.stop()
        await discord.VoiceClient.disconnect(voice)

    # Checks if a specific user says stop and if they do #
    # The bot PMs them telling them never #
    elif (message.content.startswith("stop") or message.content.startswith("STOP")) and message.author == message.author:
        for servers in client.servers:
            for members in servers.members:
                if members == message.author:
                    await client.send_message(members, "Never.")

    # checks if the message is megan_spam #
    # and if it is joins the voice chat and #
    # plays the inputed file #
    elif message.content.startswith(prefix + 'megan_spam'):
        voice = await client.join_voice_channel(client.get_channel("249599549826400256"))
        player = voice.create_ffmpeg_player("")
        player.start()

    # Checks if a specific user sends a message #
    # and if they do, adds a reaction to the #
    # message #
    elif str(message.author) == "Renz#1208":
        await client.add_reaction(message, "megan:271342548436385792")


client.run('MjcxMTAyNTUwMTU2MTE1OTc4.C2Bj8w.nZUA545iYLu9Oo8d_oe72bE-ITg')