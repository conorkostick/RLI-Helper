from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import random
import discord

vintage_facts = [
                "***Did you know...***\nDFH stadium stands for Dave Forehead stadium!",
                "***Did you know...***\nDave Forehead actually lives in a shed!",
                "***Did you know...***\nSo far 9 players have played under the name “Team Forehead” they are: Enwrong, Daithi, Mayday, Tully, XDarkArcticX, SeeNaRee, Eddi, Durkan and Fusure",
                "***Did you know...***\nRL Ireland was founded by Joseph and Darcy.",
                "***Did you know...***\nRL Ireland was first set up as a facebook page on the 28th December 2015.",
                "***Did you know...***\nBarzey shares the same birthday as Rocket League! :smile:",
                "***Did you know...***\nDaithi has 2 LAN wins under his belt... and 0 friends!!! :joy:",
                "***Did you know...***\nTully is an All-Ireland garlic bread eating champion :joy:",
                "***Did you know...***\nThat the scarab is banned from competitive play due to it’s cubeular hitbox which allows it to hit the ball much harder than any other car at any angle. FACT!",
                "***Did you know...***\nContrary to popular belief Redeyes does not actually have red eyes!",
                "***Did you know...***\nSome say that Chef was born wearing a chefs hat, others say it’s just his hair.",
                "***Did you know...***\nFor ages, no-one knew what the LTX in LTXSam stood for. Now we know it's Lieutennant X Sam from his Xbox days!",
                "***Did you know...***\nDave Forehead, Daithi and Tully all share the honour of being the first ever Rocket League LAN winners in Ireland!",
                "***Did you know...***\nThat Lovelycans doesn’t just drink cans, in fact he rarely drinks cans!",
                "***Did you know...***\nAfter seeing him at Q-con, some believe that Dormer was born on the dancefloor.",
                "***Did you know...***\nJoseph once took up so much boost that it caused a drought in the pitch itself, this pitch is now called wasteland!",
                "***Did you know...***\nSome say that Mayday is so defensive that he’s never even been in the opponents half!",
                "***Did you know...***\nLegend has it Enwrong’s nickname used to be solar panel head….. Can’t imagine why",
                "***Did you know...***\nLawlurr was the first ever console player to win an RLI event.",
                "***Did you know...***\nNo-one knows if Mugg is a typo or if he meant to type it like that. What do you think?",
                "***Did you know...***\nNo-one knows how to pronounce Fusure. Even Fusure couldn’t tell you!",
                "***Did you know...***\nDaithi, Mugg and Fusure all have 2 LAN wins each. Who's gonna be the first to get to 3???",
                "***Did you know...***\nThese facts haven't been updated in years!!! :sweat_smile:",
                "***Did you know...***\nSome say Ghosts favourite move is the left, right, goodnight. Others think it's the whiff! :joy:",
                "***Did you know...***\nDave Forehead has written the history of RLI, go check it out in the pinned messages in announcements if you haven't seen it!",
                "***Did you know...***\nSome say that Pandaa lives off a diet of just bamboo... who's to say he doesn't?",
                "***Did you know...***\nRedeyes was our first and second ever Seasonal Elite champion!",
                "***Did you know...***\nRLI had it's first ever LAN event on the 21/04/19 in Cork",
                "***Did you know...***\nDemoqz was our first ever 6mans league champion!",
                "***Did you know...***\nJkee is by far and away the loudest player in RLI :joy:",
                "***Did you know...***\nDave Forehead can't make a bot to save his life! :sweat_smile:",
                "***Did you know...***\nAfter seeing his performance at RLI's first ever LAN, some believe that Crossy has never hit a bowling pin in his life!",
                "***Did you know...***\nDid you know Mugg, Fusure and ItsPureLogic were the winners of RLIs first ever LAN",
                "***Did you know...***\nAdzer was the MVP of RLIs first ever LAN",
                '***Did you know...***\nPat. won the "Redeyes Redemption" award at RLIs first ever LAN, a reward for the player who performed above expectations the most. It got its name from JtoPrey who funded the award after winning money from a Redeyes giveaway',
                "***Did you know...***\nWe have a twitter page!!! :open_mouth:\nhttps://twitter.com/RL_Ireland",
                "***Did you know...***\nWe have a twitch!!!\nhttps://www.twitch.tv/rlireland",
                "***Did you know...***\nWe have a Youtube account!!!\nhttps://www.youtube.com/channel/UC1pwAipHTesV55OYY7r8FMg",
                "***Did you know...***\nWe have a Facebook page!!!\nhttps://www.facebook.com/groups/RLIreland/?ref=bookmarks",
                ]

facts = [       
                    "***Did you know...***\nDFH stadium stands for Dave Forehead stadium!",
                    "***Did you know...***\nDave Forehead actually lives in a shed!",
                    "***Did you know...***\nRL Ireland was founded by Joseph and Darcy.",
                    "***Did you know...***\nRL Ireland was first set up as a facebook page on the 28th December 2015.",
                    "***Did you know...***\nBarzey shares the same birthday as Rocket League!",
                    "***Did you know...***\nFor ages, no-one knew what the LTX in LTXSam stood for. Now we know it's Lieutennant X Sam from his Xbox days!",
                    "***Did you know...***\nDave Forehead, Daithi and Tully all share the honour of being the first ever Rocket League LAN winners in Ireland!",
                    "***Did you know...***\nLawlurr was the first ever console player to win an RLI event.",
                    "***Did you know...***\nSolo once took up so much boost that it caused a drought in the pitch itself, this pitch is now called wasteland!",
                    "***Did you know...***\nDave Forehead has written the history of RLI.\nYou can check it out here --> <https://docs.google.com/document/d/1oW8iqr8yDmqB2GQdnPGQaZ48TGfP0UFd122TOVHryPg/edit?usp=sharing>",
                    "***Did you know...***\nRLI hosted it's first ever LAN event on the 21/04/19 in Cork",
                    "***Did you know...***\nWe have a twitter page!!! :open_mouth:\nhttps://twitter.com/RL_Ireland",
                    "***Did you know...***\nWe have a twitch!!!\nhttps://www.twitch.tv/rlireland",
                    "***Did you know...***\nWe have a Youtube account!!!\nhttps://www.youtube.com/channel/UC1pwAipHTesV55OYY7r8FMg",
                    "***Did you know...***\nWe have a Facebook page!!!\nhttps://www.facebook.com/groups/RLIreland/?ref=bookmarks",

                    "***Did you know...***\nSamsara took a game off LTXSam at LAN despite only playing the game for the first time a week prior",
                    "***Did you know...***\nWe run a league called RLIS, which incorporates 1s, 2s and 3s, with divisions for all skill tiers.",
                    "***Did you know...***\nRL Ireland has only opened mod applications 3 times ever",
                    "***Did you know...***\nColin and Waz AREN’T actually the same person",
                    "***Did you know...***\nThe Rai Boi aka Ryan has been dubbed “Tier 2 Redeyes” for his domination of tier 2 seasonal cups",
                    "***Did you know...***\nWe had a record-setting 4 LANs in 2019, all with Liquipedia pages viewable here:\n\n**RLI LAN Cork:** <https://liquipedia.net/rocketleague/RL_Ireland/LAN_Cork/2019>\n**Q-con 2019:** <https://liquipedia.net/rocketleague/RL_Ireland/Q-CON/2019>\n**Giga-Bite Cafe LAN:** <https://liquipedia.net/rocketleague/RL_Ireland/Giga-Bite_Cafe_LAN>\n**Insomnia Dublin:** <https://liquipedia.net/rocketleague/Insomnia_Dublin>",
                    "***Did you know...***\nRLI has an IEL team, and has made 3 out of 6 grand finals in 2 seasons, with a masters championship too",
                    "***Did you know...***\nAs of writing this, There are 23 people on the RLI ban list, including “Stop banning me#0527” ",
                    "***Did you know...***\nRes is the first person to bypass moderator on his way to operator!",
                    "***Did you know...***\nWe only update these once in a blue moon",
                    "***Did you know...***\nMul is the only person to simultaneously be a part of 3 different RLIS teams",
                    "***Did you know...***\nRes’ first name is actually Reginald!",
                    "***Did you know...***\nRLI Weekly by carrickdan ran for 20 consecutive weeks!",
                    "***Did you know...***\nJHZER once hosted an RLI stream for 700 viewers… as it was finishing :(",
                    "***Did you know...***\nLovelyCans has said “xD” over 1000 times in the RLI discord, officially making him the XD God",
                    "***Did you know...***\nForeheads chair fell over while on stream at Ballymena Lan\n<https://www.twitch.tv/rlireland/clip/PlacidRockyPterodactylAMPEnergy?filter=clips&range=all&sort=time>",
                    "***Did you know...***\nLovelyCans is the quizmaster for RLI",
                    "***Did you know...***\nDomhnaill has the record for the longest time being muted in RLI",
                    "***Did you know...***\nDespite most people in the server being Irish, Redport is known for his particular love of green",
                    "***Did you know...***\nThere’s a concerning amount of people from Tipperary in the server",
                    "***Did you know...***\nLTXSam never wakes up for tournaments",
                    "***Did you know...***\nLovelycans has no idea how to spell",
                    "***Did you know...***\nWe have a Community Games Night! You can use <#653606944371638281> to give yourself the Community Ping role and get notified of the next Community game night.",
                    "***Did you know...***\nLuachra’s spirit animal is a giraffe",
                    "***Did you know...***\nThere are many *alleged* stories about Dave Forehead, such as:\n\n- He lives in a shed\n- He verbally abuses his RLIS teammates\n- He has previously attacked homeless people\n- His name isn't actually Dave!",
                    ]

welcome_channel = 000000000000000000
role_channel = 000000000000000000
playground = 000000000000000000
comment_channel = 000000000000000000
comment_inbox = 000000000000000000
exit_door = 000000000000000000

class Helper(commands.Cog):

    @commands.command()
    async def links(self, ctx):
        if ctx.channel.id == playground:
            msg = "**Our Facebook**: <https://www.facebook.com/groups/RLIreland/?ref=bookmarks>\n**Our Twitter**: <https://twitter.com/RL_Ireland>\n**Our Twitch**: <https://www.twitch.tv/rlireland>\n**Our Youtube**: <http://www.youtube.com/c/RLIreland>\n**Our Steamgroup**: <https://steamcommunity.com/groups/RLIreland>"
            await ctx.send(msg)

    @commands.command()
    async def invite(self, ctx):
        if ctx.channel.id == playground:
            invite = await ctx.channel.create_invite(max_age=86400)
            await ctx.send(f"**RLI Invite Link:**\n{invite}")

    @commands.command()
    async def dyk(self, ctx):
        if ctx.channel.id == playground:
            await ctx.send(facts[random.randint(0,len(facts)-1)])

    @commands.command()
    async def vintage_dyk(self, ctx):
        if ctx.channel.id == playground:
            await ctx.send(vintage_facts[random.randint(0,len(vintage_facts)-1)])

    @commands.command()
    async def me(self, ctx):
        if ctx.message.channel.id == playground:
            roles = [role for role in ctx.message.author.roles]
            bots = [000000000000000000, 000000000000000000, 000000000000000000, 000000000000000000, 000000000000000000, 000000000000000000, 000000000000000000, 000000000000000000, 000000000000000000, 000000000000000000]
            #       "Enwrong",          "LovelyCans",       "Pandaa",           "Res",              "Crossy",           "Gilzo",            "Art3mis",          "Aaron",            "Redport",          "Paradox"

            embed = discord.Embed(colour=ctx.message.author.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"{ctx.message.author.display_name}'s info:")
            embed.set_thumbnail(url=ctx.message.author.avatar_url)

            embed.add_field(name='Account ID:', value=ctx.message.author.id)
            embed.add_field(name='Account Name:', value=ctx.message.author)
            embed.add_field(name='Nickname:', value=ctx.message.author.display_name)

            embed.add_field(name='Account Created on:', value=ctx.message.author.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
            embed.add_field(name='Joined Server:', value=ctx.message.author.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
            embed.add_field(name='Right now:', value=ctx.message.author.activity)

            embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))
            embed.add_field(name='Top role:', value=ctx.message.author.top_role.mention)


            if ctx.message.author.id == 00000000000000000000000:
                embed.add_field(name='Is User a Bot?', value="Well... D is for Deranking!") #ID is Dormer

            elif ctx.message.author.id in bots:
                embed.add_field(name='Is User a Bot?', value="True")

            else:
                embed.add_field(name='Is User a Bot?', value="False")

            await ctx.send(embed=embed)

    @commands.command()
    async def comment (self, ctx, *args):
        if ctx.channel.id == comment_channel:
            comment = " ".join(args)
            await ctx.message.delete()
            community_comments = get(ctx.guild.channels, id=comment_inbox)
            await community_comments.send("```{} said:\n\n{}```".format(ctx.author.name, comment))


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        exit = get(member.guild.channels, id = exit_door)
        await exit.send("{} has left the server".format(member.name))


def setup(bot):
    print("setup")
    bot.add_cog(Helper(bot))
    bot.remove_command("help")