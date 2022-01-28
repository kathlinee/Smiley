import hikari
import lightbulb
import datetime
from datetime import timedelta, timezone
from datetime import datetime

Mod = lightbulb.Plugin("Mod")

@Mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES)
)
@lightbulb.option("amount", "the number of messages that you want to delete", type = int, required = True)
@lightbulb.command("clear", "deletes messages")
@lightbulb.implements(lightbulb.SlashCommand)
async def clear(ctx: lightbulb.Context) -> None:
    amount = ctx.options.amount
    channel = ctx.channel_id
    msgs = await ctx.bot.rest.fetch_messages(channel).limit(amount)
    await ctx.bot.rest.delete_messages(channel, msgs)



@Mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.KICK_MEMBERS)
)
@lightbulb.option("user", "user you wish to kick", type = hikari.Member, required = True)
@lightbulb.option("reason", "reason for the kick", type = str, required = False)
@lightbulb.command("kick", "kicks the user")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title = "Success!")
    embed.add_field(name = f"You kicked {ctx.options.user}", value = f"Reason: {ctx.options.reason}")
    gid = ctx.guild_id
    await ctx.bot.rest.kick_member(user = ctx.options.user, guild = gid)
    await ctx.respond(embed=embed)


@Mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.BAN_MEMBERS)
)
@lightbulb.option("user", "user you wish to ban", type = hikari.Member, required = True)
@lightbulb.option("reason", "reason for the ban", type = str, required = False)
@lightbulb.command("ban", "bans the user")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title = "Success!")
    embed.add_field(name = f"You banned {ctx.options.user}", value = f"Reason: {ctx.options.reason}")
    embed.set_footer(text = f"Requested by: {ctx.author}", icon = ctx.author.avatar_url or ctx.author.default_avatar_url)
    gid = ctx.guild.id
    await ctx.bot.rest.ban_member(user = ctx.options.user, guild = gid)
    await ctx.respond(embed=embed)

@Mod.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.MODERATE_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.MODERATE_MEMBERS)
)
@lightbulb.option("days", "The duration of the timeout in days", type=int, default=0)
@lightbulb.option("hours", "The duration of the timeout in hours", type=int, default=0)
@lightbulb.option("minutes", "The duration of the timeout in minutes", type=int, default=0)
@lightbulb.option("seconds", "The duration of the timeout in seconds", type=int, default=0)
@lightbulb.option("member", "The member to timeout", type=hikari.Member, required=True)
@lightbulb.command("timeout", "Timeout a member")
@lightbulb.implements(lightbulb.SlashCommand)
async def timeout(ctx: lightbulb.Context):
    member = ctx.options.member
    now = datetime.now(timezone.utc)
    then = now + timedelta(days=ctx.options.days, hours=ctx.options.hours, minutes=ctx.options.minutes, seconds=ctx.options.seconds)
    if (then - now).days > 28:
        await ctx.respond("You can't time someone out for more than 28 days", flags=hikari.MessageFlag.EPHEMERAL)
        return
    await ctx.bot.rest.edit_member(user=member, guild=ctx.guild_id, communication_disabled_until=then)
    await ctx.respond(f"{ctx.options.member} is now muted for {ctx.options.days} days, {ctx.options.minutes} minutes, {ctx.options.seconds} seconds", flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
    bot.add_plugin(Mod)