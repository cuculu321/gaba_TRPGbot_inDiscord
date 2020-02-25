# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
token_file = open('token.txt')
TOKEN = token_file.read()

channel_id = 681676739310780436

# 接続に必要なオブジェクトを生成
client = discord.Client()

def parse_space(message_content):
    return message_content.split()

def bot_switch(message):
    #botのモードをコマンドによってスイッチ
    print(message.content)
    if message.content.startswith('/neko'):
        return('にゃーん')
    
    elif message.content.startswith('/dice'):
    #サイコロを振るコマンド
        message_splitd_space = print(parse_space(message.content))
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