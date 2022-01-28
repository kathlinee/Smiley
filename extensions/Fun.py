

####################################
#          FUN COMMANDS            #
####################################


from re import L
import hikari
from hikari.files import URL
import lightbulb
import json
from lightbulb import context
import requests
import random

Fun = lightbulb.Plugin("Fun")


@Fun.command
@lightbulb.command("hottie", "shows how hot is the user")
@lightbulb.implements(lightbulb.SlashCommand)
async def hottie(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title= "How hot are you?")
    embed.add_field(name="Drum roll please..", value= f"You are {random.randrange(100)}% hot! :weary:")
    await ctx.respond(embed=embed)

@Fun.command
@lightbulb.option("question", "this is an 8ball, ask a question", required = True)
@lightbulb.command("8ball", "just an 8ball", aliases = ["8ball"])
@lightbulb.implements(lightbulb.SlashCommand)
async def _8ball(ctx: lightbulb.Context) -> None:
    responsesB = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
    embed = hikari.Embed(title = "You asked 8ball a question..")
    embed.add_field(name = "Here is your answer:", value = f"Your question was: {ctx.options.question}\nAnswer: {random.choice(responsesB)}")
    await ctx.respond(embed=embed)


##########################################################################################


def get_cFact():
    responseC = requests.get("https://catfact.ninja/fact").text
    json_dat = json.loads(responseC)
    CatFact = json_dat["fact"]
    return(CatFact)

@Fun.command
@lightbulb.command("cat-fact", "a fact about cats")
@lightbulb.implements(lightbulb.SlashCommand)
async def catFact(ctx: lightbulb.Context, *, cFact = get_cFact()) -> None:
    embed = hikari.Embed(title = "You wanted a fact about cats?")
    embed.add_field(name = "Here you go!", value = cFact)
    await ctx.respond(embed=embed)


def get_quote():
        responseQ = requests.get("https://some-random-api.ml/animu/quote")
        if 300 > responseQ.status_code >= 200:
         content = responseQ.json()
         contentFinal = content ["sentence"] + " - " + content ["character"] + ", " + content ["anime"]
        else:
         contentFinal = f"Uh oh! I recieved a bad status code of {responseQ.status_code}."
        return(contentFinal)


@Fun.command
@lightbulb.command("animequote", "a random quote from an anime")
@lightbulb.implements(lightbulb.SlashCommand)
async def animeQuote(ctx: lightbulb.Context, *, quote = get_quote()) -> None:
    embed = hikari.Embed(title = quote)
    await ctx.respond(embed=embed)


#################################################################################################################################


@Fun.command
@lightbulb.command("mrk", "dovolte abych na vás mrknul")
@lightbulb.implements(lightbulb.SlashCommand)
async def mrk(ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title= "Dovolte abych na vás mrknul")
        embed.set_image("https://c.tenor.com/diLpgcuL_zkAAAAC/mrk-zeman.gif")
        await ctx.respond(embed=embed)


@Fun.command
@lightbulb.command("rawr", "aligator")
@lightbulb.implements(lightbulb.SlashCommand)
async def rawr(ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title= "Aligator..rawr")
        embed.set_image("https://c.tenor.com/n60VqdzgWroAAAAd/milos-zeman.gif")
        await ctx.respond(embed=embed)


@Fun.command
@lightbulb.command("deez", "zeed")
@lightbulb.implements(lightbulb.SlashCommand)
async def catFact(ctx: lightbulb.Context) -> None:
    embed =  hikari.Embed(title = "nuts :peanuts:")
    await ctx.respond(embed=embed)


########################################################################################


def get_meme():
    responseM = requests.get("https://meme-api.herokuapp.com/gimme")
    if 300 > responseM.status_code >= 200:
         content = responseM.json()
         contentFinal = content["url"]
    else:
         contentFinal = f"Uh oh! I recieved a bad status code of {responseM.status_code}."
    return(contentFinal)

@Fun.command
@lightbulb.command("meme", "get a meme")
@lightbulb.implements(lightbulb.SlashCommand)
async def meme(ctx : lightbulb.Context, meme = get_meme()) -> None:
    embed = hikari.Embed(title = "Here is a meme for you!")
    embed.set_image(meme)
    await ctx.respond(embed=embed)


@Fun.command
@lightbulb.command("lol", "lol")
@lightbulb.implements(lightbulb.SlashCommand)
async def lol(ctx):
    await ctx.respond("lol")


def load(bot):
    bot.add_plugin(Fun)