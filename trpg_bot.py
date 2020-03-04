# coding: utf-8

import discord
import random

import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

import time

# *** Discordのボットの設定
# 自分のBotのアクセストークンに置き換えてください
token_file = open('token.txt')
tokens = token_file.read().split()
TOKEN = tokens[0]

channel_id = [681676739310780436, 497063980385435681, 683269397095514166]

# 接続に必要なオブジェクトを生成
client = discord.Client()

#*** 一時的狂気リスト
temporary_madness = {}
temporary_madness[1] = '鸚鵡返し（誰かの動作・発言を真似することしか出来なくなる）'
temporary_madness[2] = '健忘症（1d6時間以内のことを忘れる）'
temporary_madness[3] = '多弁症（何があってもひたすら喋り続ける）'
temporary_madness[4] = '偏食症（奇妙なものを食べたくなる）'
temporary_madness[5] = '頭痛・嘔吐などの体調不良（技能値に-5）'
temporary_madness[6] = '暴力癖（誰彼構わず暴力を振るう）'
temporary_madness[7] = '幻聴或いは一時的難聴（聞き耳半減。この症状の探索者に精神分析や説得などを試みる場合は技能値に-10）'
temporary_madness[8] ='逃亡癖（その場から逃げようとする）'
temporary_madness[9] = '吃音や失声などの発語障害（交渉技能の技能値が半減する）'
temporary_madness[10] = '不信（単独行動をとりたがる。交渉技能不可。）'
temporary_madness[11] = '恐怖による行動不能'
temporary_madness[12] = '自傷癖（自傷行動を行う。ラウンドごと1d2のダメージ判定を行う）'
temporary_madness[13] = '感情の噴出（泣き続ける、笑い続けるなど。自発行動が出来なくなる）'
temporary_madness[14] = '気絶（精神分析・またはCON*5のロールに成功で目覚める）'
temporary_madness[15] = '幻覚あるいは妄想（目を使う技能は技能値に-30）'
temporary_madness[16] = '偏執症（特定のものや行動に強く執着する）'
temporary_madness[17] = 'フェティシズム（特定のものに性的魅惑を感じる）'
temporary_madness[18] = '退行（乳幼児のような行動をとってしまう）'
temporary_madness[19] = '自己愛（自分を守るために何でもしようとする）'
temporary_madness[20] = '過信（自分を全能と信じて、どんなことでもしてしまう）'

#*** 不定期の狂気リスト
indefinite_madness = {}
indefinite_madness[1] = '失語症（言葉を使う技能が使えなくなる）'
indefinite_madness[2] = '心因性難聴（聞き耳不可。精神分析を受ける際に技能値に-30）'
indefinite_madness[3] = '奇妙な性的嗜好（性的倒錯。特定のものに性的興奮を覚える）'
indefinite_madness[4] = '偏執症（特定のものや行動に異常に執着する）'
indefinite_madness[5] = '脱力・虚脱（自力での行動が出来なくなる）'
indefinite_madness[6] = '恐怖症（特定のものに強い恐怖を覚える。そのものが側に存在する場合、技能値に-20）'
indefinite_madness[7] = '自殺癖（ラウンドごとに1d4+1のダメージ判定を行う）'
indefinite_madness[8] = '不信（単独行動をとりたがる。交渉技能不可。）'
indefinite_madness[9] = '幻覚（目を使う技能は技能値に-30）'
indefinite_madness[10] = '殺人癖（誰彼構わず殺そうとする） '

class open_google_spreadsheet:
    gc = []
    workbook = []
    SPREADSHEET_KEY = '1ThG04nz4l-ISa504UNcF97gKlkMx75YtggMGSJR2Eic'
    set_token_time = 0
    
    def gs_login(self):
        # *** Google SpreadSheetへのアクセス
        #2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        #認証情報設定
        #ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
        credentials = ServiceAccountCredentials.from_json_keyfile_name('gaba-cocbot-readspreadsheet-22b6a04f8d0a.json', scope)

        #OAuth2の資格情報を使用してGoogle APIにログインします。
        self.gc = gspread.authorize(credentials)

    def open_workbook(self):
        self.workbook = self.gc.open_by_key(self.SPREADSHEET_KEY)

    def set_token(self):
        self.gs_login()
        self.open_workbook()
        self.set_token_time = time.time()

    def give_workbook(self):
        print(time.time() - self.set_token_time)
        if (time.time() - self.set_token_time)> 3500:
            print("refresh token")
            self.set_token()

        return self.workbook

#*** スプレッドシートを使用するためのクラスと、トークンのセット
acccess_spreadsheet = open_google_spreadsheet()
acccess_spreadsheet.set_token()   


def parse_space(message_content):
    return message_content.split()

def parse_d(diceroll_cmd):
    return diceroll_cmd.split("d")

def dice_roll(num_dice, dice_faces):
    return random.randint(num_dice, num_dice * dice_faces)

def action_check(skill_point, dice):
    if dice <= skill_point:
        if dice < 5:
            return "クリティカル"
        elif dice < 10:
            return "スペシャル"
        else:
            return "成功"

    else:
        if dice > 95:
            return "ファンブル"
        else:
            return "失敗"

def read_skill_point(workbook, player_name, action):
    action_cmd = action
    multipl_point = 1
        
    worksheet = workbook.worksheet(player_name)
    act_cell = worksheet.find(action_cmd)

    act_skill_point = int(worksheet.cell(act_cell.row, act_cell.col + 4).value)

    return act_skill_point

def bot_switch(message):
    #botのモードをコマンドによってスイッチ
    print(message.content)
    if message.content.startswith('/neko'):
        return('にゃーん')
    
    elif message.content.startswith('/help'):
        return (
            "** /dice [x]d[y] ** : x個のy面ダイスを振った結果を返します。\n" + 
            "** /act プレイヤー名 技能名 ** : 技能が成功したかどうかを返します。\n" + 
            "** /tmp_mad ** : 一時的狂気表からランダムに1つ返します。\n" +
            "** /ind_mad ** : 不逞の狂気表からランダムに1つを返します。\n"
        )

    elif message.content.startswith('/dice'):
    #サイコロを振るコマンド
        message_splitd_space = parse_space(message.content)
        num_dice, dice_faces = parse_d(message_splitd_space[1])
        rolled = dice_roll(int(num_dice), int(dice_faces))
        return (message_splitd_space[1] + " → **" + str(rolled) +"**")

    elif message.content.startswith('/act'):
    #プレイヤーが行動を行うときのコマンド        
        workbook = acccess_spreadsheet.give_workbook()

        cmd, player_name, action = parse_space(message.content)

        act_skill_point = read_skill_point(workbook, player_name, action)

        dice = dice_roll(1, 100)
        act_result = action_check(act_skill_point, dice)

        return (player_name + " の " + action + "(" + str(act_skill_point) + ") → **"
                    + str(dice) +" "+ act_result + "**")
    
    elif message.content.startswith('/tmp_mad'):
        return ("一時的狂気 : **" + temporary_madness[dice_roll(1, 20)] + "**")

    elif message.content.startswith('/ind_mad'):
        return ("不定な狂気 : **" + indefinite_madness[dice_roll(1, 10)] + "**")

    else:
        return


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

    if message.channel.id in channel_id:
        return_message = bot_switch(message)

        if return_message is None:
            return
        else:
            await message.channel.send(return_message)

    else:
        return

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)