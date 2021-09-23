import discord
from discord.ext import commands
from discord.utils import get
import random

advertising_channel = 000000000000000000
target_channel = 000000000000000000

stream_ping_role = 000000000000000000

mod_role = 000000000000000000
op_role = 000000000000000000
admin_role = 000000000000000000

iel_role = 000000000000000000
tl_role = 000000000000000000

permitted_roles = [mod_role, op_role, admin_role, iel_role, tl_role, test_role_ID]


class Stream(commands.Cog, name="Stream Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="twitch", aliases=["Twitch", "IEL", "iel", "TL", "tl"])
    async def twitch(self, ctx):

        stream_perm = False

        for role in ctx.author.roles:
            if role.id in permitted_roles:
                stream_perm = True
                break

        if stream_perm == False:
            await ctx.channel.send(f"{ctx.author.mention} you do not have the perms to use this command.")            

        elif ctx.channel.id == advertising_channel and stream_perm:
            target = get(ctx.guild.channels, id=target_channel)
            role_ping = ctx.guild.get_role(stream_ping_role)
            await target.send(f"{role_ping.mention}")
        else:
            await ctx.channel.send(f"{ctx.author.mention} you cannot use this command in this channel.")
  

        await ctx.message.delete()


def setup(bot):
    print("setup")
    bot.add_cog(Stream(bot))
    bot.remove_command("help")
