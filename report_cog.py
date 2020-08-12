from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord

bot = Bot(command_prefix=">")
Client = Bot('!')

mods_chat = XXXXXXXXXXXXXXXXXX
logs_chat = XXXXXXXXXXXXXXXXXX
muted_role_id = XXXXXXXXXXXXXXXXXX
mod_role_id = XXXXXXXXXXXXXXXXXX


important_roles = [	"2000+",
					"1900+",
					"1800+",
					"1700+",
					"1600+",
					"Grand Champion",
					"Champion 3",
					"Champion 2",
					"Champion 1",
					"Diamond 3",
					"Diamond 2",
					"Diamond 1",
					"Platinum 1-3",
					"Gold 1-3",
					"Silver 1-3",
					"Bronze 1-3",
					"Irish",
					"Non-Irish",
					"PS4",
					"PC",
					"Xbox",
					"Community Ping",
					"RLIS Stream",
					"USE BOT TO SET ROLES",
					]
all_roles = {}

class report(commands.Cog):

	@commands.command()
	async def mute(self, ctx, *args):

		if ctx.message.channel.id != mods_chat:
			return

		muted_role = ctx.guild.get_role(muted_role_id)
		
		user = ctx.message.mentions[0]	

		await discord.Member.add_roles(user, muted_role)

		reason = ""
		for word in args[1:-1]:
			reason += word + " "

		date = args[-1]
		punishment = "muted"
		logs_channel = get(ctx.guild.channels, id = logs_chat)
		await self.logs(reason, user, ctx.message.author, punishment, logs_channel, date)

	@commands.command()
	async def kick(self, ctx, *args):

		if ctx.message.channel.id != mods_chat:
			return

		for r in ctx.message.author.roles:
			if r.id == mod_role_id:
				await ctx.send("Sorry! Moderators cannot kick people. If it's an urgent issue, tag an Operator or Admin.")
				return

		user = ctx.message.mentions[0]

		reason = ""
		for word in args[1:]:
			reason += word + " "

		await user.kick()

		logs_channel = get(ctx.guild.channels, id = logs_chat)
		punishment = "kicked"
		await self.logs(reason, user, ctx.message.author, punishment, logs_channel)

	@commands.command()
	async def ban(self, ctx, *args):

		if ctx.message.channel.id != mods_chat:
			return

		for r in ctx.message.author.roles:
			if r.id == mod_role_id:
				await ctx.send("Sorry! Moderators cannot ban people. If it's an urgent issue, tag an Operator or Admin.")
				return

		user = ctx.message.mentions[0]

		reason = ""
		for word in args[1:]:
			reason += word + " "

		await user.ban()

		logs_channel = get(ctx.guild.channels, id = logs_chat)
		punishment = "banned"
		await self.logs(reason, user, ctx.message.author, punishment, logs_channel)


	async def logs(self, reason, user, staff, punishment, logs_channel, date="None"):

		embed = discord.Embed(colour=0x72ff72)
		embed.set_author(name="{} was {}".format(user, punishment))
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_footer(text='{} by {}'.format(punishment, staff), icon_url=staff.avatar_url)
		embed.add_field(name="Reason", value=reason)
		embed.add_field(name="End of punishment", value=date)

		await logs_channel.send(embed=embed)


	@commands.command()
	async def members(self, ctx):

		if ctx.message.channel.id == mods_chat:
			for r in ctx.guild.roles:
				if r.name in important_roles:
					all_roles[r] = 0

			for m in ctx.guild.members:
				for r in m.roles:
					if r.name in important_roles:
						all_roles[r] += 1

			msg = ""
			for key in sorted(all_roles):
				msg += "{} : {}\n".format(key, all_roles[key])

			msg = "```\n" + msg + "\n```" + str(len(all_roles)) + " roles"
			await ctx.message.author.send(msg)

		else:
			return

def setup(bot):
    print("setup")
    bot.add_cog(report(bot))
    bot.remove_command("help")