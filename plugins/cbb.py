#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🚥 Creator : <a href='https://t.me/Bruce_Lee_2X2'>This Person</a>\n🚥 Language : <code>Python3</code>\n🚥 Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n🚥 GROUP : <a href='https://t.me/joinchat/jyp_-d874eQzMmZl'>Click here</a>\n🚥 Series Channel : @series_drawer\n🚥 Pdisk channel : <a href='https://t.me/joinchat/SuBbc27an7A4NmFl'>Click here</a> </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
