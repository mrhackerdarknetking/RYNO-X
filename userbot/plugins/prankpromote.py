#Made by @helloji123bot. Keep credits cause it hurts...#editedforall. Original credits to @Kraken_The_BadASS


import random, re
from uniborg.util import admin_cmd
from userbot.events import register 

from userbot import bot, CMD_HELP
import asyncio
from telethon import events

@register(outgoing=True, pattern="^.rpromote(?: |$)(.*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`RYNO-X`:**PROMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**PROMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**PROMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**PROMOTED USER SUCCESSFULLY**")
        
        
@register(outgoing=True, pattern="^.npromote(?: |$)(.*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`RYNO-X`:**PROMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**PROMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**PROMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**Not Enough Rights To Promote user to Admin**")
        
        
        
@register(outgoing=True, pattern="^.ndemote(?: |$)(.*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`RYNO-X`:**DEMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**DEMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**DEMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**Not Enough Rights To Demote user **")
        
        
@register(outgoing=True, pattern="^.rdemote(?: |$)(.*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`RYNO-X`:**DEMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**DEMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**DEMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`RYNO-X`:**DEMOTED USER SUCCESSFULLY**")

CMD_HELP.update({

        
     "prankpromote":

        "`.rpromote`\

\nUsage:PRANK PROMOTION OF USER.\

            \n\n`.npromote`\

            \nUsage:NOT PROMOTING USER\

            \n\n`.ndemote`>\

            \nUsage:NOT DEMOTING.\

            \n\n`.rdemote`\

            \nUsage: PRANK PROMOTING USER.\"



      



})
