from utils.command import *
from khl import *

from utils.files import *
from datetime import *


bot = Bot(token=f'{bot_token}')


current_time_is = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@bot.on_startup
async def create_user_cmd(bot:Bot):
    create_user(bot)

@bot.on_startup
async def set_username_cmd(bot:Bot):
    set_username(bot)

@bot.on_startup
async def upload_levels_cmd(bot:Bot):
    upload_levels(bot)

@bot.on_startup
async def button_event_onstartup_event(bot:Bot):
    button_event(bot)

@bot.on_startup
async def ticket_cardmessage_cmd(bot:Bot):
    ticket_cardmessage(bot)

@bot.on_startup
async def search_levels_cmd(bot:Bot):
    search_levels(bot)

@bot.on_startup
async def download_levels_cmd(bot:Bot):
    download_levels(bot)

@bot.on_startup
async def role_card_cmd(bot:Bot):
    role_card(bot)

@bot.on_startup
async def reply_cmd(bot:Bot):
    reply(bot)

@bot.on_message()
async def message(msg:Message):
    if msg.channel_type == ChannelPrivacyTypes.PERSON:
        ch = await bot.client.fetch_public_channel(f'{Receive_messages_channel_id}')
        await ch.send(CardMessage(Card(Module.Section(f'用户(met){msg.author_id}(met)发送了一条消息: {msg.content}\nmsg id: {msg.id}\n您可以使用`/reply {msg.author_id} {msg.id} (content)`回复消息'),Module.Divider(),Module.Context(f'{current_time_is}'))))
        return


import logging
logging.basicConfig(level='INFO')
if __name__ == '__main__':

    bot.run()