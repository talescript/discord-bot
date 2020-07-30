import discord

try:
    import config
    SERVER_ID = config.SERVER_ID
    TOKEN = config.TOKEN
except ModuleNotFoundError:
    SERVER_ID = process.env.SERVER_ID
    TOKEN = process.env.TOKEN

"""
    User settings -> Developer Mode: Turn on
    Click on the Server (top left) -> Server settings -> Widget
                                   -> Server ID
"""
CSS_GRID = "https://developer.mozilla.org/en-US/docs/Web/CSS/grid"
CSS_FLEX = "https://developer.mozilla.org/en-US/docs/Web/CSS/flex"
KEVIN = "https://www.kevinpowell.co/"



client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    """ Welcomes new members in the general channel 
    """
    for channel in member.guild.channels:
        if str(channel) == "general":
            await client.send.message(f"Welcome {member.mention} to the server")

@client.event
async def on_mod(message):
    """ Only certain users are allowed in this function 
    """
    valid_users = []
    if str(message.author) in valid_users:
        pass

@client.event
async def on_message(message):
    """ Commands can only be run in the following channels
    """
    server_id = client.get_guild(SERVER_ID)
    channels = ["off-topic"]
    restricted_words = []

    if message.author == client.user:
        return

    for word in restricted_words:
        if message.content.count(word) > 0:
            #await message.channel.purge(limit=1)  ## needs more permissions
            await message.channel.send("Clean up your language you dirty rotten scoundrel")
    
    if message.content == "!help": 
        embed = discord.Embed(title="Bot commands", description="If you press my buttons in the right order I will help you")
        embed.add_field(name="!kevin", value="Shows kevin's website")
        embed.add_field(name="!grid", value="MDN Docs on grid")
        embed.add_field(name="!flex", value="MDN Docs on flex")
        embed.add_field(name="!users", value="It tells you how many users are in the server.")

        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels:

        if message.content.find("alright") != -1:
            await message.channel.send("'Alright, Alright, Alright' Matthew McConaughey")

        elif message.content == "!users":
            await message.channel.send(f"Number of users {server_id.member_count}")
        elif message.content == "!grid":
            await message.channel.send(f"{CSS_GRID}") 
        elif message.content == "!flex":
            await message.channel.send(f"{CSS_FLEX}")
        elif message.content == "!kevin":
            await message.channel.send(f"{KEVIN}")

    else:
        # await message.channel.send(f"You can head over to #off-topic to issue commands") 
        print(f"User {message.author}... commands can not be ran in this channel")



if __name__ == "__main__":
    client.run(TOKEN)
