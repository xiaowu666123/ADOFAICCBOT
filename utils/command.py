import re


from khl.card import Card,CardMessage,Types,Module,Element
from datetime import *
from .kookapi import *
from .files import *
from khl import *




user_data_file = 'user_data.json'
levels_data_file = 'levels_data.json'
msg_log = 'msg_log.json'

# 如果用户数据文件不存在，则创建一个空的用户数据文件
if not os.path.exists(user_data_file):
    with open(user_data_file, 'w') as f:
        json.dump({}, f)

if not os.path.exists(msg_log):
    with open(msg_log, 'w') as f:
        json.dump({}, f)



def get_msg_log():
    with open(msg_log, 'r') as f:
        return json.load(f)

# 生成临时用户名的函数
def generate_temp_username(new_id):
    return f'ADOFAICC_{new_id}'

def get_user_data():
    with open(user_data_file, 'r') as f:
        return json.load(f)

def save_user_data(user_data):
    with open(user_data_file, 'w') as f:
        json.dump(user_data, f)

current_time_is = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_next_user_id():
    with open(user_data_file, 'r') as f:
        user_data = json.load(f)
    if not user_data:
        return 1
    else:
        return user_data[-1]['id'] + 1

if not os.path.exists(levels_data_file):
    with open(levels_data_file, 'w') as f:
        json.dump([], f)

# 获取关卡数据
def get_levels_data():
    with open(levels_data_file, 'r') as f:
        return json.load(f)

# 保存关卡数据
def save_levels_data(levels_data):
    with open(levels_data_file, 'w') as f:
        json.dump(levels_data, f)

def create_user(bot:Bot):
    @bot.command(name='create_user')
    async def create_user(msg: Message):
        try:
            user_id = msg.author.id  # 获取用户 ID
            with open(user_data_file, 'r') as f:
                user_data = json.load(f)

            # 检查用户是否已经创建过用户名
            for user in user_data:
                if user['kook_id'] == user_id:
                    await msg.reply('您已经创建过用户名了。')
                    return

            # 生成下一个可用的用户ID
            new_id = get_next_user_id()

            # 生成随机的临时用户名
            temp_username = generate_temp_username(new_id)

            # 保存用户数据
            user_data.append({'id': new_id, 'username': temp_username, 'kook_id': user_id, 'pp':0})
            with open(user_data_file, 'w') as f:
                json.dump(user_data, f)

            await msg.reply(f'用户创建成功！您的临时用户名为：{temp_username}')

        except Exception as e:
            await msg.reply(f'创建用户时出现错误：{e}')

def set_username(bot:Bot):
    @bot.command(name='set_username')
    async def set_username(msg:Message,username: str):
        try:
            user_id = msg.author.id  # 获取用户 ID
            user_data = get_user_data()

        # 查找用户并更新用户名
            for user in user_data:
                if user['kook_id'] == user_id:
                    user['username'] = username
                    save_user_data(user_data)
                    await msg.reply(f'用户名已更新为：{username}')
                    return

            await msg.reply('未找到相应用户。')

        except Exception as e:
            await msg.reply(f'设置用户名时出现错误：{e}')


def upload_levels(bot:Bot):
    @bot.command(name='upload')
    async def upload_levels(msg:Message,song: str, artist: str, creator: str, dllink: str, vidlink: str,dlc: str,*args):
        try:
            levels_data = get_levels_data()
            describe = ' '.join(args)
            next_id = len(levels_data) + 1
            name = str(next_id)
            guild_id = Guild_id
            parent_id = Levels_category_id
            success = create_channel(guild_id,name,parent_id)
            ch = await bot.client.fetch_public_channel(f"{success['data']['id']}")
            level_data = {
                'id': next_id,
                'song': song,
                'artist': artist,
                'creator': creator,
                'difficulty': 0,
                'dllink': dllink,
                'vidlink': vidlink,
                'dlc': dlc,
                'describe': describe
            }


            levels_data.append(level_data)

        # 保存关卡数据
            save_levels_data(levels_data)

            await msg.reply('关卡上传成功！')
            await ch.send(CardMessage(Card(Module.Section(f'ID：{next_id}\nSong: {song}\nartist: {artist}\ncreator: {creator}\ndlc: {dlc}\ndescribe: {describe}'),Module.ActionGroup(Element.Button("下载关卡",value=dllink,theme=Types.Theme.INFO),Element.Button("视频链接",value=vidlink,theme=Types.Theme.INFO)))))
            await ch.send(CardMessage(Card(Module.ActionGroup(Element.Button("1",value='1',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("2",value='2',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                           Module.ActionGroup(Element.Button("3",value='3',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("4",value='4',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                           Module.ActionGroup(Element.Button("5",value='5',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("6",value='6',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                              Module.ActionGroup(Element.Button("7",value='7',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("8",value='8',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                              Module.ActionGroup(Element.Button("9",value='9',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("10",value='10',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                              Module.ActionGroup(Element.Button("11",value='11',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("12",value='12',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                              Module.ActionGroup(Element.Button("13",value='13',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("14",value='14',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                              Module.ActionGroup(Element.Button("15",value='15',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("16",value='16',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                              Module.ActionGroup(Element.Button("17",value='17',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                                                 Module.ActionGroup(Element.Button("18",value='18',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("18+",value='18+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                                                 Module.ActionGroup(Element.Button("19",value='19',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("19+",value='19+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                             Module.ActionGroup(Element.Button("20.0",value='20.0',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("20.0+",value='20.0+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                                Module.ActionGroup(Element.Button("20.1",value='20.1',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("20.1+",value='20.1+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                                Module.ActionGroup(Element.Button("20.2",value='20.2',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                              Element.Button("20.2+",value='20.2+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                                                Module.ActionGroup(Element.Button("20.3",value='20.3',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                           Element.Button("20.3+",value='20.3+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                          Module.ActionGroup(Element.Button("20.4",value='20.4',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                           Element.Button("20.4+",value='20.4+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                          Module.ActionGroup(Element.Button("20.5",value="20.5",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                            Element.Button("20.5+",value='20.5+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                          Module.ActionGroup(Element.Button("20.6",value='20.6',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                        Element.Button("20.6+",value='20.6+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("20.7",value="20.7",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                            Element.Button("20.7+",value='20.7+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("20.8",value="20.8",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                                Element.Button("20.8+",value='20.8+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("20.9",value="20.9",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                                Element.Button("20.9+",value='20.9+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("21",value="21",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                                Element.Button("21+",value='21+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("21.1",value="21.1",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                                Element.Button("21.1+",value='21.1+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("21.2",value="21.2",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                                Element.Button("21.2+",value='21.2+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("21.3",value="21.2",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                                Element.Button("21.3+",value='21.3+',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)),
                                             Module.ActionGroup(Element.Button("-21",value="-21",click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
                                                                Element.Button("Censored",value='Censored',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)))))
        except Exception as e:
            await msg.reply(f'上传关卡时出现错误：{e}')

"""按钮事件"""
def button_event(bot:Bot):
    @bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
    async def button_event(b:Bot,e:EventTypes):
        user_name = e.body['user_info']['username']
        user_id = e.body['user_id']

        levels = e.body['value']
        print(e.target_id)
        print(e.body,"\n")
        ch = await bot.client.fetch_public_channel(f"{e.body['target_id']}")
        if e.body['value'] == 'openticket':
            guild_id = Guild_id
            name = f'{user_name}'
            parent_id = Ticket_category_id
            success1 = create_channel(guild_id,name,parent_id)
            value = e.body['user_info']['id']
            channel_id = success1['data']['id']
            success2 = create_channel_role_permissions(channel_id,"user_id",value)
            success3 = update_channel_role_permissions(channel_id,"user_id", value,2048)
            await asyncio.sleep(0.2)  # 休息一会 避免超速
            ch2 = await bot.client.fetch_public_channel(f'{channel_id}')
            ch3 = await bot.client.fetch_user(f'{user_id}')
            await ch3.send('工单已开启')
            await ch2.send(CardMessage(Card(Module.Section(f'请发送您的疑问\n如果解决完请按下方的`关闭工单`按钮\n(met){user_id}(met)'),Module.ActionGroup(Element.Button("关闭工单",value='closeticket',click=Types.Click.RETURN_VAL,theme=Types.Theme.PRIMARY)))))
            return

        if e.body['value'] == 'closeticket':
            channel_id = e.body['target_id']
            await asyncio.sleep(0.2)  # 休息一会 避免超速
            success = delete_channel(channel_id)
            ch = await bot.client.fetch_user(f'{user_id}')
            await ch.send('工单已关闭')
            return
        if e.body['value'] == 'getrole':
            role_id = Role_id
            guild_id = Guild_id
            success = add_role_to_user(guild_id,user_id,role_id)
            ch = await bot.client.fetch_user(f'{user_id}')
            await ch.send('已成功获取身份组')
            return

        if e.body['value'] == 'revokerole':
            role_id = Role_id
            guild_id = Guild_id
            success = revoke_role_to_user(guild_id,user_id,role_id)
            ch = await bot.client.fetch_user(f'{user_id}')
            await ch.send('已删除身份组')
            return




        await ch.send(f'{user_id}给这个谱子评了{levels}')

"""发送工单卡片"""
def ticket_cardmessage(bot:Bot):
    @bot.command(name='send_ticket_cardmessage')
    async def ticket_cardmessage(ctx:Message):
        user_id = ctx.author_id
        ch = await bot.client.fetch_public_channel('9100820697226550')
        await ch.send(CardMessage(Card(Module.Header('Open a Ticket'),Module.Divider(),Module.Section('点击下方按钮，开启工单'),Module.ActionGroup(Element.Button("Click me to open a ticket",value="openticket",click=Types.Click.RETURN_VAL,theme=Types.Theme.PRIMARY)))))




"""禁言功能"""
def mute(bot:Bot):
    @bot.command(name='mute')
    async def mute(ctx:Message,target_id :str,*args):
        reason = ' '.join(args)
        user_id = re.search(r'\d+', target_id).group()
        use_user_id = ctx.author_id
        ch = bot.client.fetch_public_channel(f'{Mute_channel_id}')

        await ch.send(CardMessage(Card(Module.Header('禁言公示'),
                                       Module.Divider(),
                                       Module.Section(f'(met){user_id}(met)被禁言，原因：{reason}\n执行者：(met){use_user_id}(met)'),
                                       Module.Divider(),
                                       Module.Context(f'{current_time_is}'))))
"""get role card"""
def role_card(bot:Bot):
    @bot.command(name='get_role_cardmessage')
    async def role_card(ctx:Message):
        await ctx.reply(CardMessage(Card(Module.Header('点击领取身份组'),
                                   Module.Divider(),
                                   Module.Section('点击下方按钮获得身份组'),
                                   Module.ActionGroup(Element.Button("get role!",value="getrole",click=Types.Click.RETURN_VAL,theme=Types.Theme.PRIMARY),
                                                      Element.Button('remoke role!',value="revokerole",click=Types.Click.RETURN_VAL,theme=Types.Theme.PRIMARY)))))

"""reply"""
def reply(bot:Bot):
    @bot.command(name='reply')
    async def reply(ctx:Message,user_id: str,msg_id: str,*args):
        send_id = ctx.author_id
        msg_id = msg_id
        user_id = user_id
        content =' '.join(args)
        ch = await bot.client.fetch_user(f'{user_id}')
        await ch.send(CardMessage(Card(Module.Header('您收到一条回复！'),Module.Divider(),Module.Section(f'管理员(met){send_id}(met)给你回复了一条消息\n消息：{content}'),Module.Divider(),Module.Context(f'{current_time_is}'))),quote=msg_id)


sharky_get_api = 'http://server.sharkmc.cn:8086/getLevels'
sharky_search_api = 'http://server.sharkmc.cn:8086/searchLevel'
sharky_download_api = 'http://server.sharkmc.cn:8086/requestDownload'


def search_levels(bot:Bot):
    @bot.command(name='search')
    async def search_levels(msg: Message,*args):

        search_value = ' '.join(args)
    # 构建 API 请求参数
        api_params = {
        'input': search_value,
        'amount': 30
        }

        try:
        # 发送 API 请求
            response = requests.post(sharky_get_api, data=api_params)
            response.raise_for_status()
            levels_data = response.json()

            # 构建消息
            if levels_data:
                message = '\n'.join([f'ID: {level["id"]}, Name: {level["name"]}, Artist: {level["artist"]}, Creator: {level["creator"]}, Diff: {level["diff"]}' for level in levels_data])
                await msg.reply(CardMessage(Card(Module.Section("搜索结果"),Module.Divider(),Module.Section(f'{message}'))))
            else:
                await msg.reply('No results found.')
        except requests.exceptions.RequestException as e:
            await msg.reply(f'Error occurred while searching levels: {e}')

def download_levels(bot:Bot):
    @bot.command(name='download')
    async def download_levels(msg:Message, value:str):
        api_parms = {
            'level_id': value
        }
        try:
            response = requests.post(sharky_download_api, data=api_parms)
            response.raise_for_status()
            download_data = response.json()

            if download_data:
                await msg.reply(CardMessage(Card(Module.ActionGroup(Element.Button("点击下载",value=download_data["text"],click=Types.Click.LINK)))))
            else: msg.reply('该论坛为提供下载链接')
        except requests.exceptions.RequestException as e:
            await msg.reply(f'Error occurred while searching levels: {e}')
