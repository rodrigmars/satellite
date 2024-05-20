
import os

from discord import Client, Intents, Guild, Game
from discord.message import Message

from dotenv import load_dotenv
from land_mining import message_mining, InvalidMessageError
from operator_discord import get_total_occurrences, kill_message, send_blacklist, notify_message
load_dotenv()

intents = Intents.default()
# intents.messages = True
intents.message_content = True
intents.members = True

client = Client(intents=intents)

guild = Guild


@client.event
async def on_ready():
    print(f'Serviço em operação por {client.user}')
    await client.change_presence(activity=Game('Magias com algoritmos computacionais'))


@client.event
async def on_message(message: Message):

    message_author = message.author
    message_content = message.content

    print(f'New message -> {message_author} said: {message_content}')

    # message = "[steamcommunity.com/gift/summer](https://u.to/ZwKuIA)"
    # message = "Lorem ipsum dolor sit https://u.to/ZwKuIA amet. Cum reprehenderit mollitia sit reprehenderit repudiandae cum ratione harum et nulla dignissimos et temporibus quaerat. Ad impedit quis cum sint exercitationem ad ducimus iure ut veritatis corrupti. Et magni omnis aut nesciunt aperiam et minus illo et beatae officiis et doloremque maiores et veniam facilis."

    try:

        check_message = await message_mining(message_content)

        await check_message()

    except InvalidMessageError as ex:

        await kill_message(message)

        if await get_total_occurrences(message_author) >= 5:
            await send_blacklist(message)
            return

        await notify_message(message, ex.message)

# if message_content not in (domains):
#     print(f'New message -> {message_author} said: {message_content}')

# print(f'New message -> {message_author} said: {message_content}')

# await message.channel.send('Messagem recebida com sucesso!!!')

# if message.author == client.user:
#     return

# if message.content.startswith('$hello'):
#     await message.channel.send('Hello!')

if __name__ == "__main__":

    client.run(os.environ['TOKEN'])
