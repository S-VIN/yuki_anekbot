import asyncio
from telethon import TelegramClient, events, Button, types
from db import db
import os


API_ID = int(os.environ.get("TG_API_ID", 111111111))
API_HASH = os.environ.get("TG_API_HASH", "add TG_API_HASH, TG_API_ID, TG_BOT_TOKEN to the environment variables")
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "default_bot_token")

print(API_HASH)

bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    buttons = [
        [Button.text('/get_random_anek')]
    ]
    await event.respond('Push the button.', buttons=buttons)


@bot.on(events.NewMessage(pattern='/get_random_anek'))
async def random_anek_handler(event):
    anek = db.get_random_anek_sync()
    if anek:
        await send_anek_with_buttons(event, anek)
    else:
        await event.respond('Error. Do not use internet, please')


@bot.on(events.NewMessage())
async def number_handler(event):
    # Если это сообщение отправил сам бот — игнорируем
    if event.out:
        return

    text = event.raw_text.strip()
    if text.startswith('/'):
        # Команды мы обрабатываем в других хендлерах
        return

    # Проверяем, является ли сообщение числом
    if text.isdigit():
        anek_id = int(text)
        anek = db.get_anek_by_id(anek_id)
        if anek:
            await send_anek_with_buttons(event, anek)
        else:
            await event.respond(f'I do not have anek by number: {anek_id}. Bye')
    else:
        await event.respond('Use numbers for anek by number, kiddo')


async def send_anek_with_buttons(event, anek):
    message = str(anek['id']) + '\n'
    message += anek['anek']
    await event.respond(message)


async def main():
    await bot.start(bot_token=BOT_TOKEN)
    await bot.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

