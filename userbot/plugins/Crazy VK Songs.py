""" Spotify / Deezer downloader plugin by @anubisxx | Syntax: .vk link"""
import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd


@borg.on(admin_cmd("vk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("**Poddak idapn download wenawa...**")
    else:
        await event.edit("🎶**Initiating Download!**🎶")

    async with borg.conversation("@DeezerMusicBot") as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            try:
                await borg(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
            except UserAlreadyParticipantError:
                await asyncio.sleep(0.00000069420)
            await conv.send_message(d_link)
            details = await conv.get_response()
            songh = await conv.get_response()
            await borg.send_message(event.chat_id, details)
            await conv.get_response()
            songh = await conv.get_response()
            await borg.send_file(event.chat_id, songh, caption="🔆**Here's the requested song!**🔆")
            await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @DeezerMusicBot `and retry!`")
