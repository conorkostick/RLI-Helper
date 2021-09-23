from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord
import time

import gspread
gc = gspread.service_account(filename="PATH TO MY LOCAL FILE")
sh = gc.open("RLI Helper Sheet").sheet1

class lists(commands.Cog):

	@commands.command()
	async def every_single_person(self, ctx):
		if ctx.author.id != 000000000000000000000:
			ctx.send("Sorry! This is a huge operation for me to do, I'll only do it under Dave Forehead's instruction")

		i=1
		for member in ctx.guild.members:
			sh.update(f"A{i}", [[member.name]])
			i += 1
			time.sleep(1.1)

	@commands.command()
	async def every_single_irish_person(self, ctx):
		if ctx.author.id != 000000000000000000000:
			ctx.send("Sorry! This is a huge operation for me to do, I'll only do it under Dave Forehead's instruction")

		i=1
		for member in ctx.guild.members:
			for role in member.roles:
				if role.name == "Irish":
					sh.update(f"C{i}", [[member.name]])
					i += 1
					time.sleep(1.1)

def setup(bot):
    print("setup")
    bot.add_cog(lists(bot))
    bot.remove_command("help")