# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hᴏşɢᴇʟᴅɪɴ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ʏᴇɴɪ ᴛᴇʟᴇɢʀᴀᴍ'ıɴ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛʟᴇʀɪ ᴀʀᴀᴄıʟıɢıʏʟᴀ Gʀᴜᴘʟᴀʀᴅᴀ Müᴢiᴋ Vᴇ Viᴅᴇᴏ Oʏɴᴀᴛᴍᴀɴıᴢᴀ Oʟᴀɴᴀᴋ Tᴀɴıʀ!**

💡 **Kᴏᴍᴜᴛʟᴀʀ ᴅüɢᴍᴇꜱɪɴɪ ᴛıᴋʟᴀʏᴀʀᴀᴋ ʙᴏᴛ'ᴜɴ ᴛüᴍ ᴋᴏᴍᴜᴛʟᴀʀıɴı ᴠᴇ ɴᴀꜱıʟ çᴀʟışᴛıᴋʟᴀʀıɴı öɢʀᴇɴɪɴ » 📚 Kᴏᴍᴜᴛʟᴀʀ Düɢᴍᴇꜱɪ!**

🔖 **Bᴜ Bᴏᴛᴜɴ Nᴀꜱıʟ Kᴜʟʟᴀɴıʟᴀᴄᴀɢıɴı Öɢʀᴇɴᴍᴇᴋ İçɪɴ Lüᴛꜰᴇɴ Tıᴋʟᴀʏıɴ » ❓ Bᴀꜱɪᴛ Kᴏᴍᴜᴛʟᴀʀ!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Bᴇɴɪ Gʀᴜʙᴜɴᴀ Eᴋʟᴇ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Bᴀꜱɪᴛ Kᴏᴍᴜᴛʟᴀʀ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Kᴏᴍᴜᴛʟᴀʀ", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Sᴀʜiʙi", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Rᴇꜱᴍi Gʀᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Rᴇꜱᴍɪ Kᴀɴᴀʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Bᴜ Bᴏᴛᴜ Kᴜʟʟᴀɴᴍᴀᴋ İçɪɴ Tᴇᴍᴇʟ Aɴʟᴀᴛıᴍ:**

1.) ***Öɴᴄᴇ ʙᴇɴɪ ɢʀᴜʙᴜɴᴜᴢᴀ ᴇᴋʟᴇʏɪɴ.**
2.) **Bᴇɴɪ ʏöɴᴇᴛɪᴄɪ ᴏʟᴀʀᴀᴋ ʏüᴋꜱᴇʟᴛ ᴠᴇ ᴀɴᴏɴɪᴍ ʏöɴᴇᴛɪᴄɪ ʜᴀʀɪç ᴛüᴍ ɪᴢɪɴʟᴇʀɪ ᴠᴇʀ.**
3.) **Bᴇɴɪ ʏöɴᴇᴛɪᴄɪ ᴇᴛᴛɪʀᴅɪᴋᴛᴇɴ ꜱᴏɴʀᴀ, ʏöɴᴇᴛɪᴄɪ ᴠᴇʀɪʟᴇʀɪɴɪ ʏᴇɴɪʟᴇᴍᴇᴋ ɪçɪɴ /reload ɢʀᴜᴘᴛᴀ ʏᴀᴢıɴ.**
3.) **Gʀᴜʙᴜɴᴜᴢᴀ @{ASSISTANT_NAME}ᴇᴋʟᴇʏɪɴ ᴠᴇʏᴀ ᴏɴᴜ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇᴋ ɪçɪɴ /gel ʏᴀᴢıɴ.**
4.) **Viᴅᴇᴏ/Müᴢɪᴋ ᴏʏɴᴀᴛᴍᴀʏᴀ ʙᴀşʟᴀᴍᴀᴅᴀɴ öɴᴄᴇ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛɪ ᴀçıɴ.**
5.) **Bᴀᴢᴇɴ /reload ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴᴀʀᴀᴋ ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴛᴍᴀᴋ ᴠᴇ ʙᴀᴢı ꜱᴏʀᴜɴʟᴀʀı çöᴢᴍᴇɴɪᴢᴇ ʏᴀʀᴅıᴍᴄı ᴏʟᴀʙɪʟɪʀ.**

📌 **Aꜱɪꜱᴛᴀɴ ʙᴏᴛᴜ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛᴇ ᴋᴀᴛıʟᴍᴀᴅıʏꜱᴀ, ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛɪɴ ᴀçıᴋ ᴏʟᴅᴜğᴜɴᴅᴀɴ ᴇᴍɪɴ ᴏʟᴜɴ ᴠᴇʏᴀ şᴜɴᴜ ʏᴀᴢıɴ /git ᴠᴇ ꜱᴏɴʀᴀꜱıɴᴅᴀ /gel ʏᴀᴢıɴ ʏᴇɴɪᴅᴇɴ.**

💡 **Bᴜ ʙᴏᴛ ʜᴀᴋᴋıɴᴅᴀ ꜱᴏʀᴜʟᴀʀıɴıᴢ ᴠᴀʀꜱᴀ, @jackdanielssx ʙᴏᴛ ꜱᴀʜɪʙɪɴᴇ ᴠᴇʏᴀᴅᴀ ᴅᴇꜱᴛᴇᴋ ꜱᴏʜʙᴇᴛɪɴᴇ ɪʟᴇᴛᴇʙɪʟɪʀꜱɪɴɪᴢ.: @{GROUP_SUPPORT}**

⚡ __Cʀᴇᴀᴛᴏʀ{BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Mᴇʀʜᴀʙᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **Açıᴋʟᴀᴍᴀʏı Oᴋᴜᴍᴀᴋ Vᴇ Mᴇᴠᴄᴜᴛ Kᴏᴍᴜᴛʟᴀʀıɴ Lɪꜱᴛᴇꜱɪɴɪ Göʀᴍᴇᴋ İçɪɴ Aşᴀɢıᴅᴀᴋɪ Düɢᴍᴇʏᴇ Bᴀꜱıɴ !**

⚡ __Cʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Aᴅᴍɪɴ Kᴏᴍᴜᴛ", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Cʀᴇᴀᴛᴏʀ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Bᴀꜱɪᴄ Kᴏᴍᴜᴛ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Tᴇᴍᴇʟ Kᴏᴍᴜᴛʟᴀʀ:

» /oynat (Şᴀʀᴋı Aᴅı / Lɪɴᴋ) - Göʀüɴᴛüʟü ꜱᴏʜʙᴇᴛᴛᴇ ᴍüᴢɪᴋ çᴀʟ
» /stream (İꜱɪᴍ / Lɪɴᴋ) - Yᴛ Cᴀɴʟı/ʀᴀᴅʏᴏ ᴄᴀɴʟı ᴍüᴢɪɢɪɴɪ ʏᴀʏıɴʟᴀʏıɴ
» /vplay (Viᴅᴇᴏ Aᴅı / Lɪɴᴋ) - Göʀüɴᴛüʟü ꜱᴏʜʙᴇᴛᴛᴇ ᴠɪᴅᴇᴏ ᴏʏɴᴀᴛ
» /vstream - ʏᴛ ʟɪᴠᴇ/ᴍ3ᴜ8'ᴅᴇɴ ᴄᴀɴʟı ᴠɪᴅᴇᴏ ᴏʏɴᴀᴛıɴ
» /playlist - Çᴀʟᴍᴀ ʟɪꜱᴛᴇꜱɪɴɪ ɢöꜱᴛᴇʀ
» /bul (query) - Yᴏᴜᴛᴜʙᴇ'ᴅᴀɴ şᴀʀᴋı ɪɴᴅɪʀᴍᴇ
» /ara (query) - Yᴏᴜᴛᴜʙᴇ'ᴅᴀɴ ᴠɪᴅᴇᴏ ɪɴᴅɪʀᴍᴇ
» /lyric (query) - Şᴀʀᴋı ꜱöᴢü ᴀʀᴀᴍᴀ
» /search (query) - ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʙᴀɢʟᴀɴᴛıꜱı ᴀʀᴀᴍᴀ

» /ping - Bᴏᴛ ᴘɪɴɢ ᴅᴜʀᴜᴍᴜɴᴜ ɢöꜱᴛᴇʀ
» /uptime - Bᴏᴛ çᴀʟışᴍᴀ ꜱüʀᴇꜱɪ ᴅᴜʀᴜᴍᴜɴᴜ ɢöꜱᴛᴇʀ
» /alive - Bᴏᴛᴜɴ ʙɪʟɢɪꜱɪɴɪ ɢöꜱᴛᴇʀ (ɢʀᴜᴘᴛᴀ)

⚡️ __Cʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Aᴅᴍɪɴ Kᴏᴍᴜᴛʟᴀʀı:

» /pause - Aᴋışı Dᴜʀᴀᴋʟᴀᴛ
» /resume - Aᴋışı Dᴇᴠᴀᴍ Eᴛᴛɪʀ
» /skip - Sᴏɴʀᴀᴋɪ Aᴋışᴀ Gᴇç
» /stop - Aᴋışı Dᴜʀᴅᴜʀ
» /vmute - Sᴇꜱʟɪ Sᴏʜʙᴇᴛᴛᴇ Uꜱᴇʀʙᴏᴛ'ᴜ Sᴇꜱꜱɪᴢᴇ Aʟ
» /vunmute - Sᴇꜱʟɪ Sᴏʜʙᴇᴛᴛᴇ Uꜱᴇʀʙᴏᴛ'ᴜɴ Sᴇꜱɪɴɪ Aç
» /volume `1-200` - Müᴢɪɢɪɴ Sᴇꜱɪɴɪ Aʏᴀʀʟᴀʏıɴ (Uꜱᴇʀʙᴏᴛ Yöɴᴇᴛɪᴄɪ Oʟᴍᴀʟıᴅıʀ)
» /reload - Bᴏᴛᴜ Yᴇɴɪᴅᴇɴ Yüᴋʟᴇʏɪɴ Vᴇ Yöɴᴇᴛɪᴄɪ Vᴇʀɪʟᴇʀɪɴɪ Yᴇɴɪʟᴇʏɪɴ
» /gel - Aꜱɪꜱᴛᴀɴ'ı Gʀᴜʙᴀ Kᴀᴛıʟᴍᴀʏᴀ Dᴀᴠᴇᴛ Eᴛ
» /git - Aꜱɪꜱᴛᴀɴ'ıɴ Gʀᴜᴘᴛᴀɴ Aʏʀıʟᴍᴀꜱıɴı Eᴍʀᴇᴛ

⚡️ __Cʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Sᴜᴅᴏ Kᴏᴍᴜᴛʟᴀʀı:

» /rmw - Tüᴍ Dᴏꜱʏᴀʟᴀʀı Tᴇᴍɪᴢʟᴇ
» /rmd - İɴᴅɪʀɪʟᴇɴ Tüᴍ Dᴏꜱʏᴀʟᴀʀı Tᴇᴍɪᴢʟᴇ
» /sysinfo - Sɪꜱᴛᴇᴍ Bɪʟɢɪʟᴇʀɪɴɪ Göꜱᴛᴇʀ
» /update - Bᴏᴛᴜɴᴜᴢᴜ Eɴ Sᴏɴ Süʀüᴍᴇ Güɴᴄᴇʟʟᴇʏɪɴ
» /restart - Bᴏᴛᴜɴᴜ Yᴇɴɪᴅᴇɴ Bᴀşʟᴀᴛ
» /leaveall - Uꜱᴇʀʙᴏᴛ'ᴜɴ Tüᴍ Gʀᴜᴘᴛᴀɴ Aʏʀıʟᴍᴀꜱıɴı Eᴍʀᴇᴛ

⚡ __Cʀᴇᴀᴛᴏʀ {BOT_NAME} @jackdanielssx""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴇʀɪ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sᴇɴ ʙɪʀ ᴀɴᴏɴɪᴍ ʏöɴᴇᴛɪᴄɪꜱɪɴ !\n\n» Yöɴᴇᴛɪᴄɪ ʜᴀᴋʟᴀʀıɴᴅᴀɴ ᴋᴜʟʟᴀɴıᴄı ʜᴇꜱᴀʙıɴᴀ ɢᴇʀɪ ᴅöɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yᴀʟɴıᴢᴄᴀ ʙᴜ ᴅüɢᴍᴇʏᴇ ᴅᴏᴋᴜɴᴀʙɪʟᴇɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪ ʏöɴᴇᴛᴍᴇ ɪᴢɴɪɴᴇ ꜱᴀʜɪᴘ ʏöɴᴇᴛɪᴄɪn !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **Aʏᴀʀʟᴀʀ** {query.message.chat.title}\n\n⏸ : 🔇 : ᴋᴜʟʟᴀɴıᴄı ʙᴏᴛᴜɴᴜ ꜱᴇꜱꜱɪᴢᴇ ᴀʟ\n🔊 : ᴋᴜʟʟᴀɴıᴄı ʙᴏᴛᴜɴᴜɴ ꜱᴇꜱɪɴɪ ᴀç",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Kᴀᴘᴀᴛ", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ Şᴜ Aɴᴅᴀ Hɪçʙɪʀ Şᴇʏ Yᴀʏıɴʟᴀɴᴍıʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yᴀʟɴıᴢᴄᴀ ʙᴜ ᴅüɢᴍᴇʏᴇ ᴅᴏᴋᴜɴᴀʙɪʟᴇɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪ ʏöɴᴇᴛᴍᴇ ɪᴢɴɪɴᴇ ꜱᴀʜɪᴘ ʏöɴᴇᴛɪᴄɪ !", show_alert=True)
    await query.message.delete()
