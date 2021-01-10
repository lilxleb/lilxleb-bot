import discord
import sys
import os
import datetime
from discord.ext import commands
from datetime import datetime

class Commands(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("cog has been loaded, what do these bad bois do")

	@commands.command()
	async def bruh(self, ctx):
		await ctx.send("bruh moment sound effect 3 number 3")

	@client.command()
	async def ping(self, ctx):
		await ctx.send(f'Bot is working, latency is {round(bot.latency * 1000)}ms')

	@client.command()
	async def load(self, ctx, extension):
		client.load_extension(f'cogs.{extension}')
		print(f"ALERT: {extension} has been loaded at {datetime.now()}")

	@client.command()
	async def unload(self, ctx, extension):
		client.unload_extension(f'cogs.{extension}')
		print(f"ALERT: {extension} has been unloaded at {datetime.now()}")

	@client.command()
	async def exit(ctx):
		await ctx.send("bravo 6, going dark")
		sys.exit(0)

	@client.command()
	async def clear(self, ctx, amount=0):
		if amount > 0:
			await ctx.channel.purge(limit=amount+1)
			print(f'{amount} messages were cleared in channel {ctx.channel()} at {datetime.now()}')
			await ctx.send(f"{amount} messages was cleared.")
		else:
			await ctx.send("No number variable was passed though.")


def setup(client):
	client.add_cog(Commands(client))