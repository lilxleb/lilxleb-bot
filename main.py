import discord
import sys
import os
import datetime
from discord.ext import commands
from datetime import datetime

client = commands.Bot(command_prefix = '#')

token = "token"

@client.event
async def on_ready():
	print(f"ALERT: Bot has been started at {datetime.now()}")

for filename in os.listdir("./extensions"):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')
		print(f"ALERT: {filename[:-3]} has been loaded as a startup procedure at {datetime.now()}")
print(f"ALERT: Bot has been loaded at {datetime.now()}")

client.run(token)
