import hikari
import lightbulb
from datetime import datetime
import time

from lightbulb.commands.slash import SlashCommand


info = lightbulb.Plugin("info")

@info.command
@lightbulb.option("user", "user you want to get info on", hikari.User, required = False)
@lightbulb.command("userinfo", "get info on a server member")
@lightbulb.implements(SlashCommand)
async def userinfo(ctx : lightbulb.Context) -> None:
    user = ctx.get_guild().get_member(ctx.options.user or ctx.user)

    if not user:
        await ctx.respond("Uh oh! User not found :(", flags=hikari.MessageFlag.EPHEMERAL)
        return

    created_at = int(user.created_at.timestamp())
    joined_at = int(user.joined_at.timestamp())

    roles = (await user.fetch_roles())[1:]

    embed = hikari.Embed(title = f"Info about {user.display_name}", description = f"`ID: {user.id}`", timestamp = datetime.now().astimezone())
    embed.set_footer(text = f"Requested by: {ctx.member.display_name}", icon = ctx.member.avatar_url or ctx.member.default_avatar_url)
    embed.set_thumbnail(user.avatar_url or user.default_avatar_url)
    embed.add_field(name ="Bot?", value = str(user.is_bot), inline = True)
    embed.add_field(name = "Created account on", value = f"<t:{created_at}:d>\n(<t:{created_at}:R>)", inline = True)
    embed.add_field(name = "Joined on", value = f"<t:{joined_at}:d>\n(<t:{joined_at}:R>)", inline=True)
    embed.add_field(name = "Roles", value = ", ".join(r.mention for r in roles), inline=False)
    await ctx.respond(embed=embed)



@info.command
@lightbulb.command("about", "about the bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def about(ctx : lightbulb.Context) -> None:
    embed = hikari.Embed(title = "You wanna know more about the bot?")
    embed.add_field(name = "Language and library", value = "Smiley was originally built in python with discord.py but because the library is dead and discord wants bots to implement slash commands by <t:1648764000:D> , I decided to rewrite the bot with Hikari-lightbulb.")
    embed.add_field(name = "How long did it take you to code the bot?", value = "Honestly, I don't really know. I'd say it was late November 2021, when I started to actually code it more consistantly. The rewrite took me like 3 days to figure out hikari and to rewrite it.")
    embed.add_field(name = "Why did you decide code a bot?", value = "Because coding is something that I've always wanted to try. And I did try it a lot of times, but I got distracted from it. I remember that the first thing I actually coded was a very simple game with JavaScript following a book. Now here I am, learning python and coding something completely different with a completely different language.")
    embed.add_field(name = "How do you host the bot?", value = "i dont :smiley:")
    embed.add_field(name = "Something isn't working. Where can I get help?", value = "You can join my server (https://discord.gg/nw7VMPTzZy) and ping the owner there (that's me lololol). I will help you!")
    await ctx.respond(embed=embed)


@info.command
@lightbulb.command("date", "shows the date")
@lightbulb.implements(lightbulb.SlashCommand)
async def time(ctx : lightbulb.Context, t = datetime.now()) -> None:
    embed = hikari.Embed(title = f"{t}")
    await ctx.respond(embed=embed)


def load(bot):
    bot.add_plugin(info)
