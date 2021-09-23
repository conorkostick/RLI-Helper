from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord


welcome_channel = 000000000000000000
roles_channel = 000000000000000000


class Welcome(commands.Cog):

	@commands.Cog.listener()
	async def on_member_join(self, member):
	    role = discord.utils.get(member.guild.roles, name = "USE BOT TO SET ROLES")
	    await discord.Member.add_roles(member, role)
	    welcome = get(member.guild.channels, id = welcome_channel)
	    await welcome.send("Welcome to **RL Ireland** {}!\n\nPlease set your roles over at <#{}> to see the rest of the server!\n\nIf you're looking for any more Irish Rocket League action, make sure to check out our linktree!\n\n<https://linktr.ee/RLIreland>\n\nEnjoy your stay! :soccer: :red_car: :flag_ie:".format(member.mention, roles_channel))
	    await member.send("Hey! Welcome to RL Ireland, the home of Irish Rocket League! :soccer: :race_car: :flag_ie:\n\nWe have a very proud history of online tournaments, leagues, LAN events and a fantastic community to match! :grin:\n\nPlease make sure to set your roles in <#{}> so that you can see the rest of the server!\n\nIf you have any questions about the server, community or what we do here, please do not be afraid to message a member of staff.\n\nThanks and enjoy your stay! :grin: :flag_ie:".format(roles_channel))

def setup(bot):
    print("setup")
    bot.add_cog(Welcome(bot))
    bot.remove_command("help")