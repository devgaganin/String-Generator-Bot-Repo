import pickledb
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import OWNER_ID

# Initialize the database
db = pickledb.load("user_db.db", True)  # The second argument "True" creates the file if it doesn't exist

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

GAGAN = 6964148334

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    user_id = msg.from_user.id
    if not db.exists(str(user_id)):
        db.set(str(user_id), True)
        db.dump()  # Save changes to the database file
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

@Client.on_message(filter("broadcast") & filters.private)
async def broadcast_command(client, message):
    if message.from_user.id == GAGAN:  # Real Owner
        await message.reply_text("Enter the message you want to broadcast:")
        broadcast_text = message.text.split(" ", 1)[1]
        delivered_count = 0
        for user_id in db.getall():
            try:
                user_id = int(user_id)
                await client.send_message(
                    user_id, f"Broadcast message By @dev_gagan: {broadcast_text}"
                )
                delivered_count += 1
            except ValueError:
                pass

        await client.send_message(
            message.chat.id, f"Broadcast sent successfully to {delivered_count} users!"
        )
    else:
        await message.reply_text("You are not authorized to use this command.")
