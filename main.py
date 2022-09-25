from discord.ext import commands
import jishaku

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    await client.load_extension("jishaku")
    print("Logged in as " + client.user)

client.run("token")