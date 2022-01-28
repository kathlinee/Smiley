import hikari
import lightbulb
import random
import requests
import json
import os

intents = hikari.Intents.ALL

bot = lightbulb.BotApp(token = "NO TOKEN STEAL FOR U >:) ", prefix=".", intents=intents, default_enabled_guilds=([]), help_class=None)

help_message = hikari.Embed(title = "You need help?"
).add_field(
    name="**Fun**", value="`ping`, `8ball`, `hottie`, `catFact`, `deez`, `animeQuote`", inline = False
    ).add_field(
        name = "**Roleplay**", value = "`hug`, `pat`, `slap`", inline = False
        ).add_field(
            name="**Moderation**", value="`clear`, `kick`, `ban`", inline = False
             ).add_field(name = "**Other**", value = "`about`, `userinfo`"
                 ).add_field(name = "Something isn't working! I need you to help me personally!", value = "You can join my discord (https://discord.gg/nw7VMPTzZy) and I'll help you!!", inline = False)

#########################################################
# HELP COMMAND                                          #
#########################################################

@bot.command
@lightbulb.command("help", "help message")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx : lightbulb.Context) -> None:
    await ctx.respond(help_message)

#########################################################
#                 PING COMMAND                          #
#########################################################
@bot.command
@lightbulb.command("ping", "checks if the bot is alive and shows its latency")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
      await ctx.respond(f"Pong! {bot.heartbeat_latency * 1000:.0f}ms")  

#########################################################
#                 LYRICS COMMAND                        #
#########################################################


@bot.command
@lightbulb.option("artist", "artist of the song")
@lightbulb.option("song","name of the song")
@lightbulb.command("lyrics", "fetch lyrics of a song youd wish")
@lightbulb.implements(lightbulb.SlashCommand)
async def lyrics(ctx):
    ly = requests.get(f"https://api.lyrics.ovh/v1/{ctx.options.artist}/{ctx.options.song}")
    lyjson = ly.json()
    lyrics = lyjson["lyrics"]
    embed = hikari.Embed(title = f"{ctx.options.song} by {ctx.options.artist}", description = f"{lyrics}")
    await ctx.respond(embed=embed)

###################################################################################################################################

for filename in os.listdir("./extensions"):
    if filename.endswith(".py"):
        bot.load_extensions(f"extensions.{filename[:-3]}")

bot.run(activity = hikari.Activity(name = "/help", type = 3))