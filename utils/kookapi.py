import requests
import json
from .files import *



def create_invite_link(guild_id ,duration, setting_times):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'guild_id': guild_id,
            'duration': duration,
            'setting_times': setting_times,
        }
        response = requests.post(
            'https://www.kookapp.cn/api/v3/invite/create',
            json=data,
            headers=headers,
        )
        response.raise_for_status()  # 检查请求是否成功
        # 解析 API 响应
        data = response.json()
        if data['code'] == 0:
            return data['data']['url']
        else:
            print(f"API Error: {data['message']}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def add_role_to_user(guild_id, user_id, role_id):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'guild_id': guild_id,
            'user_id': user_id,
            'role_id': role_id,
        }
        response = requests.post(
            'https://www.kookapp.cn/api/v3/guild-role/grant',
            json=data,
            headers=headers,
        )
        response.raise_for_status()  # 检查请求是否成功
        # 解析 API 响应
        data = response.json()
        if data['code'] == 0:
            return True
        else:
            print(f"API Error: {data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def revoke_role_to_user(guild_id, user_id, role_id):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'guild_id': guild_id,
            'user_id': user_id,
            'role_id': role_id,
        }
        response = requests.post(
            'https://www.kookapp.cn/api/v3/guild-role/revoke',
            json=data,
            headers=headers,
        )
        response.raise_for_status()  # 检查请求是否成功
        # 解析 API 响应
        data = response.json()
        if data['code'] == 0:
            return True
        else:
            print(f"API Error: {data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def get_guild_user_list(guild_id):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'guild_id': guild_id,
        }
        response = requests.post(
            'https://www.kookapp.cn/api/v3/guild/user-list',
            json=data,
            headers=headers,
        )
        response.raise_for_status()  # 检查请求是否成功
        # 解析 API 响应
        data = response.json()
        if data['code'] == 0:
            return True
        else:
            print(f"API Error: {data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def whisper_to_target_id(target_id, content):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'type': 9,
            'target_id': target_id,
            'content': f'{content}',
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/direct-message/create',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return True
        else:
            print(f"Error:{data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def ban_target(guild_id,target_id,remark):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'guild_id': guild_id,
            'target_id': target_id,
            'remark': remark,
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/blacklist/create',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return True
        else:
            print(f"Error:{data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def music_game(software,singer,music_name):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'data_type': 2,
            'software': software,
            'singer': singer,
            'music_name': music_name,
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/game/activity',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return True
        else:
            print(f"Error:{data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def create_channel(guild_id, name, parent_id):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'guild_id': guild_id,
            'name': name,
            'parent_id': parent_id,
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/channel/create',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return data
        else:
            print(f"Error:{data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_channel_role_permissions(channel_id,type,value):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'channel_id': channel_id,
            'type': type,
            'value': value,
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/channel-role/create',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return data
        else:
            print(f"Error:{data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def update_channel_role_permissions(channel_id,type,value,allow):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'channel_id': channel_id,
            'type': type,
            'value': value,
            'allow': allow,
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/channel-role/update',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return data
        else:
            print(f"Error:{data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def delete_channel(channel_id):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'channel_id': channel_id,
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/channel/delete',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return data
        else:
            print(f"Error:{data['message']}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def Send_private_message_chat_message(target_id,content,quote):
    try:
        headers = {
            'Authorization': f'Bot {bot_token}',
            'Content-Type': 'application/json',
        }
        data = {
            'type': 10,
            'target_id' : target_id,
            'content': content,
            'quote': quote
        }
        response =requests.post(
            'https://www.kookapp.cn/api/v3/direct-message/create',
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] == 0:
            return data
        else:
            print(f"Error:{data}")
            return data
    except Exception as e:
        print(f"Error: {e} {data}")
        return False