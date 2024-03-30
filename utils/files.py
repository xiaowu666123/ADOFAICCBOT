import json
import os
import sys
import asyncio




def open_file(path:str):
    """打开文件"""
    assert(isinstance(path,str)) # 如果路径不是str，报错
    with open(path, 'r', encoding='utf-8') as f:
        tmp = json.load(f)
    return tmp


def write_file(path: str, value):
    """写入文件,仅支持json格式的dict或者list"""
    assert(isinstance(path,str)) # 如果路径不是str，报错
    with open(path, 'w+', encoding='utf-8') as fw2:
        json.dump(value, fw2, indent=2, sort_keys=True, ensure_ascii=False)




current_file_path = os.path.abspath(__file__)

current_dir = os.path.dirname(current_file_path)

Bot_config_file_path = os.path.join(current_dir, '..', 'config', 'config.json')

Bot_conf = open_file(Bot_config_file_path)
bot_token = Bot_conf[0]["token"]
Guild_id = Bot_conf[0]["Guild_id"]
Ticket_category_id = Bot_conf[0]["Ticket_category_id"]
Role_id = Bot_conf[0]["Role_id"]
Levels_category_id = Bot_conf[0]["Levels_category_id"]
Mute_channel_id = Bot_conf[0]["Mute_channel_id"]
Receive_messages_channel_id = Bot_conf[0]["Receive_messages_channel_id"]

