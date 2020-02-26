# coding: utf-8

import discord
import random

import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

# *** Discordのボットの設定
# 自分のBotのアクセストークンに置き換えてください
token_file = open('token.txt')
tokens = token_file.read().split()
TOKEN = tokens[0]

channel_id = 681676739310780436

# 接続に必要なオブジェクトを生成
client = discord.Client()


# *** Google SpreadSheetへのアクセス
#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('gaba-cocbot-readspreadsheet-22b6a04f8d0a.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '1ThG04nz4l-ISa504UNcF97gKlkMx75YtggMGSJR2Eic'

workbook = gc.open_by_key(SPREADSHEET_KEY)
worksheet_list = workbook.worksheets()

print(worksheet_list)

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
        rolled = dice_roll(int(num_dice), int(dice_faces))
        return (message_splitd_space[1] + " => **" + str(rolled) +"**")

    elif message.content.startswith('/act'):
        cmd, player_name,  action = parse_space(message.content)
        

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