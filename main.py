import asyncio
from enviomsj import enviar_mensaje

async def main():
    usuario = "Mensaje a enviar"  # Define el mensaje que deseas enviar
    await enviar_mensaje(usuario)

# Ejecutar el bucle de eventos asíncronos
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

