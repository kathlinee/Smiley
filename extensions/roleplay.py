

#################################
# RP COMMANDS                   #
#################################


import hikari
import lightbulb
import requests
import json

RPl = lightbulb.Plugin("RPl")


def get_hug():
     resp = requests.get("https://some-random-api.ml/animu/hug")
     if 300 > resp.status_code >= 200:
        content = resp.json()
        contentFinal = content["link"]
     else:
        contentFinal = f"Uh oh! I recieved a bad status code of {resp.status_code}."
     return(contentFinal)

@RPl.command
@lightbulb.option("user", "choose who you want to hug", type = hikari.Member, required = True)
@lightbulb.command("hug", "hug someone!")
@lightbulb.implements(lightbulb.SlashCommand)
async def hug(ctx: lightbulb.Context, *, hugGif = get_hug()):
    embed = hikari.Embed(title = f"You hugged {ctx.options.user}!")
    embed.set_image(hugGif)
    await ctx.respond(embed=embed)



def get_pat():
     resp = requests.get("https://some-random-api.ml/animu/pat")
     if 300 > resp.status_code >= 200:
        content = resp.json()
        contentFinal = content["link"]

@RPl.command
@lightbulb.option("user", "choose who you want to pat", type = hikari.Member, required = True)
@lightbulb.command("pat", "pat someone!")
@lightbulb.implements(lightbulb.SlashCommand)
async def pat(ctx: lightbulb.Context, *, patGif = get_pat()):
    embed = hikari.Embed(title = f"You patted {ctx.options.user}!")
    embed.set_image(patGif)
    await ctx.respond(embed=embed)



def get_cry():
     responseC = requests.get("https://nekos.best/api/v1/cry")
     if 300 > responseC.status_code >= 200:
        content = responseC.json()
        contentFinal = content["url"]
     else:
        contentFinal = f"Uh oh! I recieved a bad status code of {responseC.status_code}."
     return(contentFinal)

@RPl.command
@lightbulb.command("cry", "you need to cry?")
@lightbulb.implements(lightbulb.SlashCommand)
async def cry(ctx: lightbulb.Context, *, cryGif = get_cry()):
    embed = hikari.Embed(title = f"uh oh! Someone started crying!")
    embed.set_image(cryGif)
    await ctx.respond(embed=embed)


def get_kiss():
     responseK = requests.get("https://nekos.best/api/v1/kiss")
     if 300 > responseK.status_code >= 200:
        content = responseK.json()
        contentFinal = content["url"]
     else:
        contentFinal = f"Uh oh! I recieved a bad status code of {responseK.status_code}."
     return(contentFinal)

@RPl.command
@lightbulb.option("user", "choose who you want to kiss", type = hikari.Member, required = True)
@lightbulb.command("kiss", "kiss someone!")
@lightbulb.implements(lightbulb.SlashCommand)
async def kiss(ctx: lightbulb.Context, *, kissGif = get_kiss()):
    embed = hikari.Embed(title = f"You kissed {ctx.options.user}!")
    embed.set_image(kissGif)
    await ctx.respond(embed=embed)


def get_slap():
     responseS = requests.get("https://nekos.best/api/v1/slap")
     if 300 > responseS.status_code >= 200:
        content = responseS.json()
        contentFinal = content["url"]
     else:
        contentFinal = f"Uh oh! I recieved a bad status code of {responseS.status_code}."
     return(contentFinal)

@RPl.command
@lightbulb.option("user", "choose who you want to slap", type = hikari.Member, required = True)
@lightbulb.command("slap", "slap someone!")
@lightbulb.implements(lightbulb.SlashCommand)
async def slap(ctx: lightbulb.Context, *, slapGif = get_slap()):
    embed = hikari.Embed(title = f"You slapped {ctx.options.user}!")
    embed.set_image(slapGif)
    await ctx.respond(embed=embed)



def get_poke():
     responseP = requests.get("https://nekos.best/api/v1/poke")
     if 300 > responseP.status_code >= 200:
        content = responseP.json()
        contentFinal = content["url"]
     else:
        contentFinal = f"Uh oh! I recieved a bad status code of {responseP.status_code}."
     return(contentFinal)

@RPl.command
@lightbulb.option("user", "choose who you want to poke", type = hikari.Member, required = True)
@lightbulb.command("poke", "poke someone!")
@lightbulb.implements(lightbulb.SlashCommand)
async def poke(ctx: lightbulb.Context, *, pokeGif = get_poke()):
    embed = hikari.Embed(title = f"You poked {ctx.options.user}!")
    embed.set_image(pokeGif)
    await ctx.respond(embed=embed)


def get_cuddle():
     responseCU = requests.get("https://nekos.best/api/v1/cuddle")
     if 300 > responseCU.status_code >= 200:
        content = responseCU.json()
        contentFinal = content["url"]
     else:
        contentFinal = f"Uh oh! I recieved a bad status code of {responseCU.status_code}."
     return(contentFinal)


@RPl.command
@lightbulb.option("user", "choose who you want to cuddle", type = hikari.Member, required = True)
@lightbulb.command("cuddle", "cuddle someone!")
@lightbulb.implements(lightbulb.SlashCommand)
async def cuddle(ctx: lightbulb.Context, *, cudGif = get_cuddle()):
    embed = hikari.Embed(title = f"You cuddled {ctx.options.user}!")
    embed.set_image(cudGif)
    await ctx.respond(embed=embed)






def load(bot):
   bot.add_plugin(RPl)