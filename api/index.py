# ServerlessTelegram - a telegram bot which can be hosted on Vercel.
# Copyright (c) 2022 dakshy/ServerlessTelegram
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import logging
import telegram

from flask import Flask, jsonify, request
app = Flask(__name__)
bot_token = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=bot_token)

@app.route('/api', methods=['POST'])
def api():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    # Reply with the same message
    bot.sendMessage(chat_id=chat_id, text="Hello")
        
    return jsonify({"status": "ok"})
