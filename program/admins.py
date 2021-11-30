from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Gᴇʀi", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 Kᴀᴘᴀᴛ", callback_data="cls")]]
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ Bᴏᴛ **Yᴇɴɪᴅᴇɴ Bᴀşʟᴀᴛıʟᴅı !**\n✅ **Aᴅᴍɪɴ Liꜱᴛᴇꜱi** **Güɴᴄᴇʟʟᴇɴᴅɪ !**"
    )


@Client.on_message(command(["atla", f"atla@{BOT_USERNAME}", "vatla"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• Mᴇɴᴜ", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="• Kᴀᴘᴀᴛ", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ Şᴜ Aɴᴅᴀ Hiç Biʀ Şᴇʏ Oʏɴᴀᴛıʟᴍıʏᴏʀ")
        elif op == 1:
            await m.reply("✅ Liꜱᴛᴇ Bᴏş.\n\n• Bᴏᴛ Sᴇꜱʟi Sᴏʜʙᴇᴛᴛᴇɴ Aʏʀıʟıʏᴏʀ**")
        elif op == 2:
            await m.reply("🗑️ **Sıʀᴀᴅᴀᴋi Pᴀʀçᴀʟᴀʀı Tᴇᴍiᴢʟᴇᴍᴇ**\n\n**• Bᴏᴛ Sᴇꜱʟi Sᴏʜʙᴇᴛᴛᴇɴ Aʏʀıʟıʏᴏʀ**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **Biʀ Sᴏɴʀᴀᴋi Pᴀʀçᴀʏᴀ Aᴛʟᴀɴᴅı.**\n\n🔘 **İꜱiᴍ:** [{op[0]}]({op[1]})\n💬 **Sᴏʜʙᴇᴛ:** `{chat_id}`\n👁‍🗨 **Dᴜʀᴜᴍ:** `Çᴀʟıʏᴏʀ`\n👉 **Tᴀʟᴇᴘ Eᴅᴇɴ:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **Sıʀᴀᴅᴀɴ Şᴀʀᴋı Kᴀʟᴅıʀıʟᴅı:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["son", f"son@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vson"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **Aᴋış Sᴏɴᴀ Eʀᴅi.**")
        except Exception as e:
            await m.reply(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Aᴋışᴛᴀ Hiç Biʀ Şᴇʏ Yᴏᴋ**")


@Client.on_message(
    command(["durdur", f"durdur@{BOT_USERNAME}", "vdurdur"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **Pᴀʀçᴀ Dᴜʀᴀᴋʟᴀᴛıʟᴅı.**\n\n• **Aᴋışı Süʀᴅüʀᴍᴇᴋ İçɪɴ,**\n» /devam Kᴏᴍᴜᴛᴜ Kᴜʟʟᴀɴıɴ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Aᴋışᴛᴀ Hiç Biʀ Şᴇʏ Yᴏᴋ**")


@Client.on_message(
    command(["devam", f"devam@{BOT_USERNAME}", "vdevam"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **Pᴀʀçᴀ Dᴇᴠᴀᴍ Eᴛᴛiʀiʟᴅi.**\n\n• **Aᴋışı Dᴜʀᴀᴋʟᴀᴛᴍᴀᴋ İçɪɴ**\n» /durdur Kᴏᴍᴜᴛᴜ Kᴜʟʟᴀɴıɴ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Aᴋışᴛᴀ Hiç Biʀ Şᴇʏ Yᴏᴋ**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **Kᴜʟʟᴀɴıᴄı Bᴏᴛᴜɴᴜɴ Sᴇꜱi Kᴀᴘᴀᴛıʟᴅı.**\n\n• **Uꜱᴇʀʙᴏᴛ'ᴜɴ Sᴇꜱiɴi Açᴍᴀᴋ İçiɴ Şᴜɴᴜ Kᴜʟʟᴀɴıɴ**\n» /unmute Kᴏᴍᴜᴛᴜ Kᴜʟʟᴀɴıɴ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Aᴋışᴛᴀ Hiçʙɪʀ Şᴇʏ**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **Kᴜʟʟᴀɴıᴄı Bᴏᴛᴜɴᴜɴ Sᴇꜱi Açıʟᴅı.**\n\n• **Uꜱᴇʀʙᴏᴛ'ᴜɴ Sᴇꜱɪɴɪ Kᴀᴘᴀᴛᴍᴀᴋ İçiɴ**\n» /mute Kᴏᴍᴜᴛᴜ Kᴜʟʟᴀɴıɴ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Aᴋışᴛᴀ Hiçʙɪʀ Şᴇʏ**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sᴇɴ Biʀ Aɴᴏɴɪᴍ Yöɴᴇᴛiᴄiꜱiɴ !\n\n» Yöɴᴇᴛɪᴄɪ Hᴀᴋʟᴀʀıɴᴅᴀɴ Kᴜʟʟᴀɴıᴄı Hᴇꜱᴀʙıɴᴀ Gᴇʀi Döɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yᴀʟɴıᴢᴄᴀ Bᴜ Düɢᴍᴇʏᴇ Dᴏᴋᴜɴᴀʙɪʟᴇɴ Sᴇꜱʟi Sᴏʜʙᴇᴛʟᴇʀi Yöɴᴇᴛᴍᴇ İᴢɴiɴᴇ Sᴀʜiᴘ Yöɴᴇᴛiᴄi !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ Aᴋış Dᴜʀᴀᴋʟᴀᴛıʟᴅı", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Şᴜ Aɴᴅᴀ Hiçʙiʀ Şᴇʏ Yᴀʏıɴʟᴀɴᴍıʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sᴇɴ Biʀ Aɴᴏɴɪᴍ Yöɴᴇᴛiᴄiꜱiɴ !\n\n» Yöɴᴇᴛiᴄi Hᴀᴋʟᴀʀıɴᴅᴀɴ Kᴜʟʟᴀɴıᴄı Hᴇꜱᴀʙıɴᴀ Gᴇʀi Döɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yᴀʟɴıᴢᴄᴀ Bᴜ Düɢᴍᴇʏᴇ Dᴏᴋᴜɴᴀʙiʟᴇɴ Sᴇꜱʟi Sᴏʜʙᴇᴛʟᴇʀi Yöɴᴇᴛᴍᴇ İᴢɴɪɴᴇ Sᴀʜiᴘ Yöɴᴇᴛiᴄi !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ Aᴋış Yᴇɴiᴅᴇɴ Bᴀşʟᴀᴅı", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Şᴜ Aɴᴅᴀ Hiçʙiʀ Şᴇʏ Yᴀʏıɴʟᴀɴᴍıʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sᴇɴ Biʀ Aɴᴏɴɪᴍ Yöɴᴇᴛiᴄiꜱiɴ !\n\n» Yöɴᴇᴛiᴄi Hᴀᴋʟᴀʀıɴᴅᴀɴ Kᴜʟʟᴀɴıᴄı Hᴇꜱᴀʙıɴᴀ Gᴇʀi Döɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yᴀʟɴıᴢᴄᴀ Bᴜ Düɢᴍᴇʏᴇ Dᴏᴋᴜɴᴀʙiʟᴇɴ Sᴇꜱʟi Sᴏʜʙᴇᴛʟᴇʀi Yöɴᴇᴛᴍᴇ İᴢɴiɴᴇ Sᴀʜiᴘ Yöɴᴇᴛiᴄi !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **Bᴜ Aᴋış Sᴏɴᴀ Eʀᴅi**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Şᴜ Aɴᴅᴀ Hiçʙiʀ Şᴇʏ Yᴀʏıɴʟᴀɴᴍıʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sᴇɴ Biʀ Aɴᴏɴɪᴍ Yöɴᴇᴛiᴄiꜱiɴ !\n\n» Yöɴᴇᴛiᴄi Hᴀᴋʟᴀʀıɴᴅᴀɴ Kᴜʟʟᴀɴıᴄı Hᴇꜱᴀʙıɴᴀ Gᴇʀi Döɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yᴀʟɴıᴢᴄᴀ Bᴜ Düɢᴍᴇʏᴇ Dᴏᴋᴜɴᴀʙiʟᴇɴ Sᴇꜱʟi Sᴏʜʙᴇᴛʟᴇʀi Yöɴᴇᴛᴍᴇ İᴢɴiɴᴇ Sᴀʜiᴘ Yöɴᴇᴛiᴄi !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 Uꜱᴇʀʙᴏᴛ Bᴀşᴀʀıʏʟᴀ Kᴀᴘᴀᴛıʟᴅı", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Şᴜ Aɴᴅᴀ Hiçʙiʀ Şᴇʏ Yᴀʏıɴʟᴀɴᴍıʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Sᴇɴ Biʀ Aɴᴏɴɪᴍ Yöɴᴇᴛiᴄiꜱiɴ !\n\n» Yöɴᴇᴛiᴄi Hᴀᴋʟᴀʀıɴᴅᴀɴ Kᴜʟʟᴀɴıᴄı Hᴇꜱᴀʙıɴᴀ Gᴇʀi Döɴ.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yᴀʟɴıᴢᴄᴀ Bᴜ Düɢᴍᴇʏᴇ Dᴏᴋᴜɴᴀʙiʟᴇɴ Sᴇꜱʟi Sᴏʜʙᴇᴛʟᴇʀi Yöɴᴇᴛᴍᴇ İᴢɴiɴᴇ Sᴀʜiᴘ Yöɴᴇᴛiᴄi !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 Uꜱᴇʀʙᴏᴛ Bᴀşᴀʀıʏʟᴀ Açıʟᴅı", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Şᴜ Aɴᴅᴀ Hiçʙiʀ Şᴇʏ Yᴀʏıɴʟᴀɴᴍıʏᴏʀ", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **Sᴇꜱ Sᴇᴠiʏᴇꜱi** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **Hᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Aᴋışᴛᴀ Hiçʙiʀ Şᴇʏ**")
