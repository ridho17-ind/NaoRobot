import os
from pyrogram import Client, filters
from pyrogram.types import *

from NaoRobot.conf import get_str_key
from NaoRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/e1ff8620519d6378ac1f0.jpg) To Make Your Groups Secured And Organized !** \n\n**『 Owner 』 : 『 [Skyzo](t.me/xflskyzo) 』**\n**╭──────────────**\n**┣─ » Python ~ 3.8.6**\n**┣─ » Update ~ Recently**\n**╰──────────────**\n\n**»» 『 @SadRoomsInfo 』 ««**"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ɢɪᴛʜᴜʙ​", url=f"https://github.com/ridho17-ind"),
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ​", url=f"https://t.me/FlicksSupport"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ ʙᴏᴛ ꜰʟɪᴄᴋs​", url="https://t.me/XFLSkyzo"),
      ],[
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/SadRoomsInfo"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/devoloperflicks/32"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
