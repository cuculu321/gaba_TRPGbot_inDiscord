# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
token_file = open('token.txt')
TOKEN = token_file.read()

channel_id = 681676739310780436

# 接続に必要なオブジェクトを生成
client = discord.Client()

def parse_space(message_content):
    return message_content.split()

def parse_d(diceroll_cmd):
    return diceroll_cmd.split("d")

def dice_roll(num_dice, dice_faces):
    return random.randint(num_dice, num_dice * dice_faces)

def bot_switch(message):
    #botのモードをコマンドによってスイッチ
    print(message.content)
    if message.content.startswith('/neko'):
        return('にゃーん')
    
    elif message.content.startswith('/dice'):
    #サイコロを振るコマンド
        message_splitd_space = parse_space(message.content)
        num_dice, dice_faces = parse_d(message_splitd_space[1])
        return ("roll")

    else:
        return None

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.channel.id == channel_id:
        return_message = bot_switch(message)

        await message.channel.send(return_message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)