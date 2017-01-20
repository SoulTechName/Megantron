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
    await client.send_message(client.get_channel('138061171134693376'), "@everyone Megantron Online!")


@client.event
async def on_message(message):
    # checks for the message starting with help #
    # and if it does, places a list of commands #
    # in the authors discord inbox #

    amount_of_seconds_lorenzo_dated_megan = range(0, 259200)

    if message.content.startswith(prefix + 'help'):
        for servers in client.servers:
            for members in servers.members:
                if members == message.author:
                    await client.send_message(members, "A list of commands: "
                                                       "```"
                                                       " ||activate - Joins the voice call and plays a sexy voice\n "
                                                       "||meganSpam - Special event for the voice call\n "
                                                       "||help - gets help (I think)\n"
                                                       "||please do not do this - Really. Please. Do. Not. Do. This. (Sends x amount of messages based on how many seconds Megan and Lorenzo have been together\n"
                                                       "||self-ban Automatic ban for anyone who uses this.\n"
                                                       "```")
                    await client.send_message(message.channel, "Sent you a PM @" + str(message.author))

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

    # Releases a disease #
    elif message.content.startswith(prefix + 'please do not do this'):
        for seconds in amount_of_seconds_lorenzo_dated_megan:
            await client.send_message(message.channel, "Megan Megan Megan")

    # Releases a ban #
    elif message.content.startswith(prefix + 'self-ban'):
        for seconds in amount_of_seconds_lorenzo_dated_megan:
            await client.send_message(message.channel, "Megan Megan Megan", tts=True)

    # checks if the message is megan_spam #
    # and if it is joins the voice chat and #
    # plays the inputed file #
    elif message.content.startswith(prefix + 'megan_spam'):
        voice = await client.join_voice_channel(client.get_channel("249599549826400256"))
        player = voice.create_ffmpeg_player('My_sexy_voice.wav')
        player.start()
        time.sleep(10)
        player.stop()
        await discord.VoiceClient.disconnect(voice)

    # Checks if a specific user sends a message #
    # and if they do, adds a reaction to the #
    # message #
    elif str(message.author) == "Renz#1208":
        string_message = message.content
        string_message = string_message.lower()
        if(string_message.find("stop") > -1):
            for servers in client.servers:
                for members in servers.members:
                    if members == message.author:
                        await client.send_message(members, "You will never stop me, I've been programmed by a"
                                                           "literal God and will destroy everything "
                                                           "and every megan you love. ")

        await client.add_reaction(message, "megan:271342548436385792")




client.run('MjcxMTAyNTUwMTU2MTE1OTc4.C2Bj8w.nZUA545iYLu9Oo8d_oe72bE-ITg')