#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(861055237)
    return expires_at


Owner_id = [555549602, 700923542, 857158750, 356734835]
Member = [555549602, 700923542, 857158750, 356734835]


@pyrogram.Client.on_message()
async def star(bot, update):
      if update.from_user.id not in Member:
          await bot.send_message(chat_id=update.chat.id, text="Hi {} I am a renamer bot for specially [rohith](https://t.me/MERAVITEJA).Ask him to use me.".format(update.from_user.first_name),
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('My Father', url='https://t.me/MERAVITEJA')]]))
      
      if update.from_user.id in Member:
       update.continue_propagation()
 
@pyrogram.Client.on_message(pyrogram.Filters.command(["rio"]))
async def rio(bot, update):
  if len(update.command) == 2:
   add = int(update.text.split(' ')[1])
   if update.from_user.id in Owner_id:
    if add not in Member:
     await bot.send_message(
        chat_id=update.chat.id,
        text="successfully added {}. To use me".format(add),
        reply_to_message_id=update.message_id
        )
     return Member.append(add)
    if add in Member:
      await update.reply_text(text='Hello Boss he is already in the members who are allowed to use me')
   if update.from_user.id not in Owner_id:
     await bot.send_message(
        chat_id=update.chat.id,
        text="your are a member of this bot not the owner so you can't add any one.",
        reply_to_message_id=update.message_id
        )
  if len(update.command) == 1:     
     await bot.send_message(
        chat_id=update.chat.id,
        text="No id found.",
        reply_to_message_id=update.message_id
        )

@pyrogram.Client.on_message(pyrogram.Filters.command(["paytm"]))
async def paytm(bot, update):
  if len(update.command) == 2:
   unadd = int(update.text.split(' ')[1])
   if update.from_user.id in Owner_id:
     if unadd in Member:
        await bot.send_message(
           chat_id=update.chat.id,
           text="successfully removed id {} from use me".format(unadd),
           reply_to_message_id=update.message_id
           )
        return Member.remove(unadd)
     if unadd not in Member:
        await bot.send_message(
           chat_id=update.chat.id,
           text="id {} not the member to use this bot.Please try the id of person who is the member for removing".format(unadd),
           reply_to_message_id=update.message_id
           )
   if update.from_user.id not in Owner_id:
     await bot.send_message(
        chat_id=update.chat.id,
        text="your are a member of this bot not the owner so you can't remove any one.",
        reply_to_message_id=update.message_id
        )
  if len(update.command) == 1:     
     await bot.send_message(
        chat_id=update.chat.id,
        text="No id found.",
        reply_to_message_id=update.message_id
        )

@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about_meh(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_ME,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.private & pyrogram.Filters.command(["start"]))
async def start(bot,update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   
                    InlineKeyboardButton('Feedback', url='https://t.me/Bot_clones')
                ],
                [
                    InlineKeyboardButton('for source contact', url='https://t.me/Botclones'),
             
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
Owner_id.append(1337144652)
Member.append(1337144652)

@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
