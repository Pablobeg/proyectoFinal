import asyncio
from telegram import Bot

# Tu token de acceso del bot de Telegram
bot_token = '6756397759:AAHeS0nEY71RUljHPBCZDVnTMQoZ0-teb8A'

async def enviar_mensaje(msj):
    bot = Bot(token=bot_token)
    chat_id = 1509393039  # ID del chat al que deseas enviar el mensaje
    mensaje = msj
    await bot.send_message(chat_id=chat_id, text=mensaje)

async def inicio(mensaje):
    # Tu otro método que llamará a enviar_mensaje con el mensaje proporcionado
    await enviar_mensaje(mensaje)