"""
STATUS: Code is working. β
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import time
from Shikimori.modules.helper_funcs.readable_time import get_readable_time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.utils.helpers import escape_markdown
from telegram.ext import CallbackContext, CallbackQueryHandler
from Shikimori.vars import ANIME_NAME, BOT_USERNAME, NETWORK, NETWORK_USERNAME, OWNER_USERNAME, START_MEDIA, SUPPORT_CHAT, UPDATE_CHANNEL
from Shikimori import StartTime, dispatcher

bot_name = f"{dispatcher.bot.first_name}"


PM_START_TEXT = """
\nβHey There! [π©βπΌ](https://telegra.ph/file/839f01a0dd2063dd52722.jpg) 
I aα΄ Power
β I am Advanced Group Management Bot with some fun features
ββββββββββββββββββββββββ
Γ Uα΄α΄Ιͺα΄α΄: {}
ββββββββββββββββββββββββ
βͺ HΙͺα΄ /help Tα΄ Sα΄α΄ MΚ Aα΄ α΄ΙͺΚα΄ΚΚα΄ Cα΄α΄α΄α΄Ι΄α΄s.
"""

HELP_STRINGS = """
Hey there... Im Power 
I have lots of features like AI Chatbot, Anime, Music, Notes, Filters, Fun and many others useful commands!
Click on the buttons below to get documentation about specific modules.."""

buttons = [
     [
        InlineKeyboardButton(text="β ADD Power TO YOUR GROUP β", url="t.me/Power_Superbot?startgroup=true"),   
    ],
    [
        InlineKeyboardButton(text=" About Me  ", url=f"https://t.me/tpx_bots"),
    ],
   
    [
        InlineKeyboardButton(text=" Commands/Help π ", callback_data="help_back"),
        InlineKeyboardButton(text="Updates π‘", url=f"https://t.me/{UPDATE_CHANNEL}"),
    ],
]
try:
    if network_name == "uchihaxnetwork":
        HMMM = InlineKeyboardButton(text="βββ ππππππ βββ πππ©π¬π€π§π ", callback_data="sern_")
    elif NETWORK:
        HMMM = InlineKeyboardButton(text=f"{NETWORK}", url=f"https://t.me/{NETWORK_USERNAME}")
    else:
        HMMM = None
except:
    HMMM = None

def Shikimori_about_callback(update, context):
    query = update.callback_query
    if query.data == "Shikimori_":
        query.message.edit_text(
            text=f"ΰΉ I'm *{bot_name}*, a powerful group management bot built to help you manage your group easily."
            "\nβ’ I can restrict users."
            "\nβ’ I can greet users with customizable welcome messages and even set a group's rules."
            "\nβ’ I have an advanced anti-flood system."
            "\nβ’ I can warn users until they reach max warns, with each predefined actions such as ban, mute, kick, etc."
            "\nβ’ I have a note keeping system, blacklists, and even predetermined replies on certain keywords."
            "\nβ’ I check for admins' permissions before executing any command and more stuffs",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Github", callback_data="github_"),
                    InlineKeyboardButton(text="License", callback_data="license_"),
                    ],
                    [
                    HMMM,
                    InlineKeyboardButton(text="Documentation", url="https://some1hing.gitbook.io/shikimori-bot/"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_back"),
                    ],
                ]
            ),
        )

    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "β Hα΄ΚΚα΄ *{}*!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT.format(uptime)
     
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def git_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "github_":
        query.message.edit_text(
            text=f"Orginal Repositiory created by [SOME1HING](https://github.com/SOME-1HING) on [github](https://github.com/SOME-1HING/ShikimoriBot) for [Shikimori Bot](https://t.me/micchon_shikimori_bot)",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="Repo", url="https://github.com/SOME-1HING/ShikimoriBot"),
                    InlineKeyboardButton(text="Creator", url="https://github.com/SOME-1HING"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_"),
                    ],
                ]
            ),
        )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "β Hα΄ΚΚα΄ *{}*!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT.format(uptime)
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def sern_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "sern_":
        query.message.edit_text(
            text=f"""
join @shinobu_support.
""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="Shinobu ", url="https://t.me/shinobu_support")],
                    
                ]
            ),
        )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "β Hα΄ΚΚα΄ *{}*!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT.format(uptime)
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

def license_call_back(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "license_":
        query.message.edit_text(
            text=f"\n\n_{bot_name}'s licensed under the GNU General Public License v3.0_",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton(text="License", url="https://github.com/SOME-1HING/ShikimoriBot/blob/master/LICENSE"),
                    ],
                    [
                    InlineKeyboardButton(text="Back", callback_data="Shikimori_"),
                    ],
                ]
            ),
        )
    elif query.data == "Shikimori_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        hmm = "β Hα΄ΚΚα΄ *{}*!".format(escape_markdown(first_name))
        HMM = hmm + PM_START_TEXT.format(uptime)
    
        query.message.edit_text(
                HMM,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )
about_callback_handler = CallbackQueryHandler(
        Shikimori_about_callback, pattern=r"Shikimori_", run_async=True
    )
license_call_back_handler = CallbackQueryHandler(
    license_call_back, pattern=r"license_", run_async=True
)
git_call_back_handler = CallbackQueryHandler(
    git_call_back, pattern=r"github_", run_async=True
)
sern_call_back_handler = CallbackQueryHandler(
    sern_call_back, pattern=r"sern_", run_async=True
)

dispatcher.add_handler(sern_call_back_handler)
dispatcher.add_handler(git_call_back_handler)
dispatcher.add_handler(about_callback_handler)
dispatcher.add_handler(license_call_back_handler)
