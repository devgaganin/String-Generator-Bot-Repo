from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_animation(
        chat_id=msg.chat.id,
        animation="start.mp4",  # Replace "start.mp4" with the path to your animation file
        caption=f"""Hey, {msg.from_user.mention}

👋 Welcome to the Pyrogram and Telethon Session Generator Bot! 
This handy tool allows you to effortlessly generate sessions for both Pyrogram and Telethon frameworks. 
Whether you're developing Telegram bots or automation scripts, our bot has got you covered. 
Dive in and start generating sessions with ease!

Made with ❤️ by [Team SPY](https://t.me/dev_gagan)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝖦𝖤𝖭𝖤𝖱𝖠𝖳𝖤 𝖲𝖳𝖱𝖨𝖭𝖦", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" Group", url="https://t.me/dev_gagan"),
                    InlineKeyboardButton("Channel", url="https://t.me/dev_gagan")
                ]
            ]
        )
    )
