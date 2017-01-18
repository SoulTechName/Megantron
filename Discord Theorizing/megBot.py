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
    user_list = client.get_all_members()
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

    elif message.content.startswith(prefix + 'activate'):
        voice = await client.join_voice_channel(client.get_channel("249599549826400256"))
        player = voice.create_ffmpeg_player('My_sex_voice.wav')
        player.start()
        time.sleep(3)
        player.stop()
        await discord.VoiceClient.disconnect(voice)

    elif (message.content.contains("stop") or message.content.contains("STOP")) and message.author == "Renz#1208":
        for servers in client.servers:
            for members in servers.members:
                if members == message.author:
                    client.send_message(members, "Never.")


    elif message.content.startswith(prefix + 'megan_spam'):
        voice = await client.join_voice_channel(client.get_channel("249599549826400256"))
        player = voice.create_ffmpeg_player("")
        player.start()

    elif str(message.author) == "Renz#1208":
        await client.add_reaction(message, "megan:271290371659530240")


client.run('MjcxMTAyNTUwMTU2MTE1OTc4.C2Bj8w.nZUA545iYLu9Oo8d_oe72bE-ITg')