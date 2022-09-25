from discord.ext import commands
import os
from os import system
import jishaku

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    client.load_extension("jishaku")
    system("cls")
    system("title Jishaku")
    print("Jishaku succesfully loaded!")

client.run("token here")
