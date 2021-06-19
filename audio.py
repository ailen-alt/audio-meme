from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
from pyrogram.types import ChatPermissions

from time import sleep
from random import randint, choice

app = Client("my_account")

@app.on_message(filters.command("audio", prefixes=".") & filters.me)
def audio(_, msg):
    p = 0
    while(p != 1):
        try:
            text = "Прослушивание сообщения"
            msg.edit(text)
            sleep(1.0)

            text = text + "."
            msg.edit(text)
            sleep(1.0)

            text = text + "."
            msg.edit(text)
            sleep(1.0)

            text = text + "."
            msg.edit(text)
            sleep(1.0)

            text = "Прослушивание сообщения"
            msg.edit(text)
            sleep(1.0)

            text = text + "."
            msg.edit(text)
            sleep(1.0)

            text = text + "."
            msg.edit(text)
            sleep(1.0)

            text = "Пользователь установил ограничения на получение аудио сообщений." + "\n" + "\n" + "<b>Сообщение не доставлено.</b>"
            msg.edit(text)
            p = 1
            sleep(3.0)



        except FloodWait as e:
            sleep(e.x)

app.run()
