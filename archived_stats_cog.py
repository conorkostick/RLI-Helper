from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import random
import discord
import csv
import json

tiers = ["premier", "championship"]

class Archived_stats(commands.Cog):

    @commands.command()
    async def stats_to_csv(self, ctx):

        for t in tiers:

            all_players = []

            with open(f"{t}_games_played.txt", "r") as gp:
                games_played = json.load(gp)
            with open(f"{t}_wins.txt", "r") as w:
                wins = json.load(w)

            for id in games_played:
                player = ctx.guild.get_member(int(id))
                if player == None:
                    continue
                try:
                    player_stats = [player.name, games_played[id], wins[id]]
                except:
                    player_stats = [player.name, games_played[id], "0"]
                all_players.append(player_stats)

            with open(f"{t}_stats_april.csv", "w") as stats_file:
                writer = csv.writer(stats_file)
                for player in all_players:
                    writer.writerow(player)

        await ctx.send("csv files made")


def setup(bot):
    print("setup")
    bot.add_cog(Archived_stats(bot))
    bot.remove_command("help")