from pyrogram import Client, filters

from TelegramBot.config import prefixes
from TelegramBot.database import MongoDb
from TelegramBot.helpers.decorators import ratelimiter, sudo_commands

commands = ["dbstats"]


@Client.on_message(filters.command(commands, **prefixes))
@sudo_commands
@ratelimiter
async def dbstats(_, message):
    TotalUsers = await MongoDb.users.total_documents()
    TotalChats = await MongoDb.chats.total_documents()
    stats_string = f"**Bot Database Statics.\n\n**Total Number of users = {TotalUsers}\nTotal number of chats  = {TotalChats}"
    return await message.reply_text(stats_string)
