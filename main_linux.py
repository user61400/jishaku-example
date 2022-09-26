# stdlib
import os

# discord.py
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  await client.load_extension('jishaku')
  os.system("clear")
  print("Jishaku succesfully loaded!")

  
client.run("token here")
