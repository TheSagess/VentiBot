import discord

OWNER_IDS = [1028698287999553556]

def is_owner(ctx):
    return ctx.message.author.id in OWNER_IDS