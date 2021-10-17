import discord

list_of_commands = ["help", "join", "play"]

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
    print(f"{str(message.author)}: {str(message.content)}")

    if str(message.content).startswith("."):
        if str(message.content) == ".join":
            if str(message.author.voice) != "None":
                await message.author.voice.channel.connect()
            else:
                await message.channel.send("You are not connected to voice channel.")
        elif str(message.content) == ".help":
            await message.channel.send("List of commands:" + "".join(str(" " + x) for x in list_of_commands) + ".")
        else:
            await message.channel.send("Unknown command.")
            print('Unknown command')

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await channel.send(f"Wellcome {member.name}!")

client.run(token)