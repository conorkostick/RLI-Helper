from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord

role_channel = 0000000000000000000
staff_channel = 0000000000000000000
guild_id = 0000000000000000000

ranks = {   "<:gc3:758784173691109406>":"Grand Champion 3",
            "<:gc2:758784143113846794>":"Grand Champion 2",
            "<:gc1:758784069915377703>":"Grand Champion 1",
            "<:c3:653611932514779156>":"Champion 3",
            "<:c2:653611901703421982>":"Champion 2",
            "<:c1:653611875329638410>":"Champion 1",
            "<:d3:653611847295172612>":"Diamond 3",
            "<:d2:653611809391116298>":"Diamond 2",
            "<:d1:653611766974119957>":"Diamond 1",
            "<:plat:653611724699860992>":"Platinum 1-3",
            "<:gold:653611693007700008>":"Gold 1-3",
            "<:silver:653611657834135572>":"Silver 1-3",
            "<:bronze:653611619880009729>":"Bronze 1-3",
            }

nations = {"🇮🇪":"Irish",
            "🌍":"Non-Irish",
            }

platforms = {"<:steam:653612062592729101>":"PC",
            "<:playstation:653612038135742474>":"PS4",
            "<:xbox:653611983576498191>":"Xbox"
            }

misc_roles = {"🎮":"Community Ping",
                "🎥":"RLI Player Stream",
                "<:RLIS:698999093032386571>": "RLIS Stream",
                "6️⃣": "6mans",
                "❗": "Media Ping"}

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        print("reaction")

        guild = self.bot.get_guild(payload.guild_id)
        user = payload.member
        print(guild)
        print(user)

        if user.bot:
            return
        elif payload.channel_id != role_channel:
            return

        if str(payload.emoji) in ranks:
            role = discord.utils.get(user.guild.roles, name=ranks[str(payload.emoji)])
            print(role)

            for r in user.roles:
                if str(r) in ranks.values():
                    await discord.Member.remove_roles(user, r)

            await discord.Member.add_roles(user, role)
            await user.send("You now have the {} role".format(role))


        elif str(payload.emoji) in nations:
            role = discord.utils.get(user.guild.roles, name=nations[str(payload.emoji)])
            print(role)

            for r in user.roles:
                if str(r) in nations.values():
                    await user.send("We already know your nationality, if it is wrong please message a member of staff")
                    return

            await discord.Member.add_roles(user, role)
            await user.send("You now have the {} role".format(role))

        elif str(payload.emoji) in platforms:
            role = discord.utils.get(user.guild.roles, name=platforms[str(payload.emoji)])
            print(role)
            await discord.Member.add_roles(user, role)
            await user.send("You now have the {} role".format(role))

        elif str(payload.emoji) in misc_roles:
            role = discord.utils.get(user.guild.roles, name=misc_roles[str(payload.emoji)])
            print(role)
            await discord.Member.add_roles(user, role)
            await user.send("You now have the {} role".format(role))


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        print("unreact")

        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        print(guild)
        print(user)

        if user.bot:
            return
        elif payload.channel_id != role_channel:
            return

        if str(payload.emoji) in ranks:
            role = discord.utils.get(user.guild.roles, name=ranks[str(payload.emoji)])
            print(role)

            await discord.Member.remove_roles(user, role)
            await user.send("The {} role has been removed".format(role))

        elif str(payload.emoji) in platforms:
            role = discord.utils.get(user.guild.roles, name=platforms[str(payload.emoji)])
            print(role)

            await discord.Member.remove_roles(user, role)
            await user.send("The {} role has been removed".format(role))

        elif str(payload.emoji) in misc_roles:
            role = discord.utils.get(user.guild.roles, name=misc_roles[str(payload.emoji)])
            print(role)

            await discord.Member.remove_roles(user, role)
            await user.send("The {} role has been removed".format(role))

        elif str(payload.emoji) in nations:

            await user.send("Sorry! You cannot change your nationality, if it is incorrect then please message a member of staff")

        else:
            return

    @commands.command()
    async def roles(self, ctx):

        if ctx.message.channel.id == staff_channel:
            rank = await ctx.guild.get_channel(role_channel).send(

"""__**SET RANK**__\n\nPlease set your rank here\n
You may update your rank as much as you like.
All the staff ask is that you are honest about what rank you have reached **this season** in **competitive games modes**\n
If you want the Supersonic Legend role, you must show proof to a member of staff. You can use <#202592895683919872> for this or send a screenshot to a member of staff\n
If you want to remove your rank you can unreact""")

            for r in ranks.keys():
                await rank.add_reaction(r)

            nationality = await ctx.guild.get_channel(role_channel).send(
"""------------------\n\n__**SET NATIONALITY**__\n\nPlease set your nationality here.\n
If you were born in or live on the **island of Ireland** then you qualify for the Irish role, but we also welcome Non-Irish players to our server too.
Please set your nationality to gain access to the rest of the server""")

            for n in nations.keys():
                await nationality.add_reaction(n)

            platform = await ctx.guild.get_channel(role_channel).send("--------------------\n\n__**SET PLATFORM**__\n\nPlease set your platform here")

            for p in platforms.keys():
                await platform.add_reaction(p)

            misc = await ctx.guild.get_channel(role_channel).send(
"""--------------------\n\n__**OTHER ROLES**__\n
You can add extra roles here\n
React to the 🎮 if you want the **Community Games Night** role
React to the 🚀 if you want the **Custom Games Player** role
React to the <:RLIS:698999093032386571> if you want the **RLIS Stream** role
React to the 6️⃣ if you want the **6mans Ping** role
React to the ❗ if you want the **Media Ping** role

If you want to remove any of these you can unreact""")

            for m in misc_roles.keys():
                await misc.add_reaction(m)


        else:
            return

    @commands.command()
    async def update(self, ctx):

        if ctx.author.id != 00000000000000000:
            return

        else:
            message = await self.bot.get_guild(guild_id).get_channel(role_channel).fetch_message(000000000000000000000)

            delete_emoji = "🚀"
            for r in message.reactions:
                if str(r) == delete_emoji:
                    await message.clear_reaction(r)

            new_msg = """
--------------------\n\n__**OTHER ROLES**__\n
You can add extra roles here\n
React to the 🎮 if you want the **Community Games Night** role
React to the <:RLIS:698999093032386571> if you want the **RLIS Stream** role
React to the 6️⃣ if you want the **6mans Ping** role
React to the ❗ if you want the **Media Ping** role
React to the 🎥 if you want the **RLI Player Stream** role

If you want to remove any of these you can unreact"""
            new_react = "🎥"

            await message.edit(content=new_msg)
            await message.add_reaction(new_react)

    @commands.command()
    async def remove_all_roles(self, ctx):

        if ctx.author.id != 000000000000000000:
            return
        else:
            for member in ctx.guild.members:
                for role in member.roles:
                    if str(role) in ranks.values():
                        try:
                            await discord.Member.remove_roles(member, role)
                        except:
                            continue
            await ctx.send("Finished removing everyone's rank roles")


def setup(bot):
    print("setup")
    bot.add_cog(Roles(bot))
    bot.remove_command("help")
