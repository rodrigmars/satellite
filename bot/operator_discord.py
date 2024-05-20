from discord.message import Message
from discord import User, Member, HTTPException


async def send_blacklist(message: Message) -> None:
    print(f"Conta {message.author} bloqueada")


async def kill_message(message: Message) -> None:

    try:

        await message.delete()

    except HTTPException as ex:
        print(ex)
        print(f"Unable to delete message {message.id}")


async def get_total_occurrences(author: User | Member) -> int:
    return 5


async def check_author(author: str):
    print("Verificar")


async def notify_message(message: Message, notify: str) -> None:
    # print(
    #     "Banimento realizado para conta [ AGENTE-ESPERTALHAO ] - Motivo: Número de tentativas excedido.")
    await message.channel.send(f"{message.author.mention} **Aviso**, este canal não permite o envio de conteúdo classificado como spam. Risco de bloqueio após três tentativas.")
