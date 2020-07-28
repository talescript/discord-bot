import discord
import config

"""
    User settings -> Developer Mode: Turn on
    Click on the Server (top left) -> Server settings -> Widget
                                   -> Server ID
"""

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await client.send.message(f"Welcome {member.mention} to the server")

@client.event
async def on_mod(message):
    valid_users = []
    if str(message.author) in valid_users:
        pass

@client.event
async def on_message(message):
    server_id = client.get_guild(config.SERVER_ID)
    channels = ["commands"]

    if message.author == client.user:
        return
    
    if str(message.channel) in channels:

        if message.content.find("alright") != -1:
            await message.channel.send("'Alright, Alright, Alright' Matthew McConaughey")

        elif message.content == "!users":
            await message.channel.send(f"Number of users {server_id.member_count}")

    else:
        print(f"User {message.autor}... commands can not be ran in this channel")

if __name__ == "__main__":
    client.run(config.TOKEN)
