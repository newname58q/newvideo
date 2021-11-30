# Copyright (C) 2021 By Veez Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

import re
import asyncio

from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.veez import call_py, user
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["oynat", f"oynat@{BOT_USERNAME}"]) & other_filters)
async def play(c: Client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• Kᴀᴘᴀᴛ", callback_data="cls"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("Sᴇɴ Biʀ Aɴᴏɴiᴍ Yöɴᴇᴛiᴄi'ꜱiɴ!\n\n» Yöɴᴇᴛɪᴄɪ Hᴀᴋʟᴀʀıɴᴅᴀɴ Kᴜʟʟᴀɴıᴄı Hᴇꜱᴀʙıɴᴀ Gᴇʀi Döɴ.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 Bᴇɴi Kᴜʟʟᴀɴᴍᴀᴋ İçiɴ **Yöɴᴇᴛiᴄi** Aşᴀɢıᴅᴀᴋɪ **İᴢiɴʟᴇʀʟᴇ**:\n\n» ❌ __Mᴇꜱᴀᴊʟᴀʀı Siʟ__\n» ❌ __Kᴜʟʟᴀɴıᴄı Eᴋʟᴇ__\n» ❌ __Göʀüɴᴛüʟü Sᴏʜʙᴇᴛi Yöɴᴇᴛ__\n\nVᴇʀiʟᴇʀ **Güɴᴄᴇʟʟᴇɴᴅi** Bᴇɴi Yᴇᴛᴋiʟᴇɴᴅiʀᴅiᴋᴛᴇɴ Sᴏɴʀᴀ **Oᴛᴏᴍᴀᴛɪᴋ Oʟᴀʀᴀᴋ**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "Gᴇʀᴇᴋʟi İᴢiɴ Eᴋꜱiᴋ:" + "\n\n» ❌ __Göʀüɴᴛüʟü Sᴏʜʙᴇᴛi Yöɴᴇᴛ__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "Gᴇʀᴇᴋʟi İᴢiɴ Eᴋꜱiᴋ:" + "\n\n» ❌ __Mᴇꜱᴀᴊʟᴀʀı Siʟ__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("Gᴇʀᴇᴋʟi İᴢiɴ ᴇᴋꜱiᴋ:" + "\n\n» ❌ __Kᴜʟʟᴀɴıᴄı Eᴋʟᴇ__")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **Gʀᴜᴘᴛᴀ Yᴀꜱᴀᴋʟᴀɴᴅı** {m.chat.title}\n\n» **Bᴜ Bᴏᴛᴜ Kᴜʟʟᴀɴᴍᴀᴋ İꜱᴛiʏᴏʀꜱᴀɴıᴢ Öɴᴄᴇ Uꜱᴇʀʙᴏᴛᴜɴ Bᴀɴıɴı Kᴀʟᴅıʀıɴ.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **Uꜱᴇʀʙᴏᴛ Kᴀᴛıʟᴀᴍᴀᴅı**\n\n**Sᴇʙᴇᴘ**: `{e}`")
                return
        else:
            try:
                user_id = (await user.get_me()).id
                link = await c.export_chat_invite_link(chat_id)
                if "+" in link:
                    link_hash = (link.replace("+", "")).split("t.me/")[1]
                    await ubot.join_chat(link_hash)
                await c.promote_member(chat_id, user_id)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **Uꜱᴇʀʙᴏᴛ Kᴀᴛıʟᴀᴍᴀᴅı**\n\n**Sᴇʙᴇᴘ**: `{e}`"
                )
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **Şᴀʀᴋı İɴᴅiʀiʟiʏᴏʀ...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Pᴀʀçᴀ Sıʀᴀʏᴀ Eᴋʟᴇɴᴅɪ »** `{pos}`\n\n🔘 **İꜱiᴍ:** [{songname}]({link})\n💬 **Sᴏʜʙᴇᴛ:** `{chat_id}`\n👉 **Tᴀʟᴇᴘ Eᴅᴇɴ:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
            else:
             try:
                await suhu.edit("🔄 **Joining vc...**")
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"💡 **Mᴜꜱiᴄ Aᴋışı Bᴀşʟᴀᴛıʟᴅı.**\n\n🔘 **İꜱiᴍ:** [{songname}]({link})\n💬 **Sᴏʜʙᴇᴛ:** `{chat_id}`\n👁‍🗨 **Dᴜʀᴜᴍ:** `Çᴀʟıʏᴏʀ`\n👉 **Tᴀʟᴇᴘ Eᴅᴇɴ:** {requester}",
                    reply_markup=keyboard,
                )
             except Exception as e:
                await suhu.delete()
                await m.reply_text(f"🚫 Hᴀᴛᴀ:\n\n» {e}")
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» Bɪʀ ᴄᴇᴠᴀᴘ **ꜱᴇꜱ ᴅᴏꜱʏᴀꜱı** ᴠᴇʏᴀ **ᴀʀᴀᴍᴀᴋ ɪçɪɴ ʙɪʀ şᴇʏ ᴠᴇʀ.**"
                )
            else:
                suhu = await c.send_message(chat_id, "🔎 **Aʀᴀɴıʏᴏʀ...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **Sᴏɴᴜç Bᴜʟᴜɴᴀᴍᴀᴅı.**")
                else:
                    songname = search[0]
                    url = search[1]
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await suhu.edit(f"❌ yt-dl Sᴏʀᴜɴʟᴀʀı Aʟɢıʟᴀɴᴅı\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"💡 **Pᴀʀçᴀ Sıʀᴀʏᴀ Eᴋʟᴇɴᴅi »** `{pos}`\n\n🔘 **İꜱɪᴍ:** [{songname}]({url})\n💬 **Sᴏʜʙᴇᴛ:** `{chat_id}`\n👉 **Tᴀʟᴇᴘ Eᴅᴇɴ:** {requester}",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await suhu.edit("🔄 **Joining vc...**")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"💡 **Müᴢɪᴋ Aᴋışı Bᴀşʟᴀᴅı.**\n\n🔘 **İꜱɪᴍ:** [{songname}]({url})\n💬 **Sᴏʜʙᴇᴛ:** `{chat_id}`\n👁‍🗨 **Dᴜʀᴜᴍ:** `Çᴀʟıʏᴏʀ`\n👉 **Tᴀʟᴇᴘ Eᴅᴇɴ:** {requester}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await suhu.delete()
                                await m.reply_text(f"🚫 Hᴀᴛᴀ: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» Şᴜ ᴀɴ ᴄᴇᴠᴀᴘ ᴠᴇʀ **ꜱᴇꜱ ᴅᴏꜱʏᴀꜱı** ᴠᴇʏᴀ **ᴀʀᴀᴍᴀᴋ ɪçɪɴ ʙɪʀ şᴇʏ ᴠᴇʀ.**"
            )
        else:
            suhu = await c.send_message(chat_id, "🔎 **Aʀᴀɴıʏᴏʀ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **Sᴏɴᴜç ʙᴜʟᴜɴᴀᴍᴀᴅı.**")
            else:
                songname = search[0]
                url = search[1]
                veez, ytlink = await ytdl(url)
                if veez == 0:
                    await suhu.edit(f"❌ yt-dl ꜱᴏʀᴜɴʟᴀʀı ᴀʟɢıʟᴀɴᴅı\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"💡 **Pᴀʀçᴀ Sıʀᴀʏᴀ Eᴋʟᴇɴᴅi »** `{pos}`\n\n🔘 **İꜱɪᴍ:** [{songname}]({url})\n💬 **Sᴏʜʙᴇᴛ:** `{chat_id}`\n👉 **Tᴀʟᴇᴘ Eᴅᴇɴ:** {requester}",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await suhu.edit("🔄 **Joining vc...**")
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"💡 **Music streaming started.**\n\n🔘 **İꜱɪᴍ:** [{songname}]({url})\n💬 **Sᴏʜʙᴇᴛ:** `{chat_id}`\n👁‍🗨 **Dᴜʀᴜᴍ:** `Çᴀʟıʏᴏʀ`\n👉 **Tᴀʟᴇᴘ Eᴅᴇɴ:** {requester}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"🚫 Hᴀᴛᴀ: `{ep}`")


# stream is used for live streaming only


@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(c: Client, m: Message):
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data="cls"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("you're an __Anonymous Admin__ !\n\n» revert back to user account from admin rights.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 To use me, I need to be an **Administrator** with the following **permissions**:\n\n» ❌ __Delete messages__\n» ❌ __Add users__\n» ❌ __Manage video chat__\n\nData is **updated** automatically after you **promote me**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "missing required permission:" + "\n\n» ❌ __Manage video chat__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "missing required permission:" + "\n\n» ❌ __Delete messages__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("missing required permission:" + "\n\n» ❌ __Add users__")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **is banned in group** {m.chat.title}\n\n» **unban the userbot first if you want to use this bot.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **userbot failed to join**\n\n**reason**: `{e}`")
                return
        else:
            try:
                user_id = (await user.get_me()).id
                link = await c.export_chat_invite_link(chat_id)
                if "+" in link:
                    link_hash = (link.replace("+", "")).split("t.me/")[1]
                    await ubot.join_chat(link_hash)
                await c.promote_member(chat_id, user_id)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **userbot failed to join**\n\n**reason**: `{e}`"
                )

    if len(m.command) < 2:
        await m.reply("» give me a live-link/m3u8 url/youtube link to stream.")
    else:
        link = m.text.split(None, 1)[1]
        suhu = await c.send_message(chat_id, "🔄 **processing stream...**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            veez, livelink = await ytdl(link)
        else:
            livelink = link
            veez = 1

        if veez == 0:
            await suhu.edit(f"❌ yt-dl issues detected\n\n» `{livelink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Track added to queue »** `{pos}`\n\n💭 **Chat:** `{chat_id}`\n🎧 **Request by:** {requester}",
                    reply_markup=keyboard,
                )
            else:
                try:
                    await suhu.edit("🔄 **Joining vc...**")
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            livelink,
                        ),
                        stream_type=StreamType().live_stream,
                    )
                    add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                    await suhu.delete()
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"💡 **[Music live]({link}) stream started.**\n\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Request by:** {requester}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await suhu.delete()
                    await m.reply_text(f"🚫 error: `{ep}`")
