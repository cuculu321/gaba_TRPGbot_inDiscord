# coding: utf-8
import random
import json
import re

import discord

from read_spreadsheet import *
from madness_list import *

# *** Discordのボットの設定
# 自分のBotのアクセストークンに置き換えてください
token_file = open('token.txt')
tokens = token_file.read().split()
TOKEN = tokens[0]

channel_id = [681676739310780436, 497063980385435681, 683269397095514166]

# 接続に必要なオブジェクトを生成
client = discord.Client()

#*** スプレッドシートを使用するためのクラスと、トークンのセット
acccess_spreadsheet = open_google_spreadsheet()
acccess_spreadsheet.set_token()   


def parse_space(message_content):
    """
    スペースをもとに分割

    Parameters
    ----------
    message_content : string
        Discord内で発言された文章

    Returns
    -------
    return : list[string]
        スペースをもとに分割されたリスト

    """

    return message_content.split()

def parse_d(diceroll_cmd):
    """
    「d」をもとに分割

    Parameters
    ----------
    diceroll_cmd : string
        /diceコマンドの引数

    Returns
    -------
    return : list[string]
        「d」をもとに分割されたリスト
    """

    return diceroll_cmd.split("d")

def dice_roll(num_dice, dice_faces):
    """
    ダイスを振る

    Parameters
    ----------
    num_dice : int
        振るサイコロの数
    dice_faces : int
        サイコロの面の数

    Returns
    -------
    return : int
        ダイス結果
    """

    return random.randint(num_dice, num_dice * dice_faces)

def action_check(skill_point, dice):
    """
    技能の成否判定を行う

    Parameters
    ----------
    skill_point : int
        技能値
    dice : int
        ダイス結果

    Returns
    -------
    return : string
        成否判定

    """

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

def search_operational_symbol(action):
    """
    文字列から四則演算記号の位置を取得する

    Parameters
    ----------
    action : string
        /actコマンドの第2引数。技能名(検索する文字)

    Returns
    -------
    return : int
        四則演算記号の位置。見つからなかった場合は0

    """
    
    search_result_obj = re.search(r'\+|-|\*|/', action)
    if search_result_obj is None:
        return 0
    else:
        return search_result_obj.start()

def splitting_action(action, index):
    """
    四則演算記号を元に分割を行う

    Parameters
    ----------
    action : string
        /actコマンドの第2引数。技能名(検索する文字)
    index : int
        四則演算記号のあるindex

    Returns
    -------
    splited_action : string
        技能名
    operational_symbol : string
        四則演算記号
    arithmetic_num : int
        修正値
    """
    
    splited_action = action[0 : index]
    operational_symbol = action[index]
    arithmetic_num = action[index + 1 : len(action)]

    return splited_action, operational_symbol, int(arithmetic_num)

def four_arithmetic_operations(skill_point, symbol, num):
    """
    四則演算

    Parameters
    ----------
    skill_point : int
        技能値
    symbol : string
        演算記号
    num : int
        修正値

    Returns
    -------
    return : int
        四則演算後の値

    """
    
    if symbol == "+":
        return skill_point + num
    elif symbol == "*":
        return skill_point * num
    elif symbol == "-":
        return skill_point - num
    elif symbol == "/":
        return skill_point / num

def bot_switch(message):
    """

    Parameters
    ----------
    message : string
        Discord内で発言された文章メソッド

    Returns
    -------
    return : string
        Discordに表示する文字列

    """
    
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

        #四則演算記号の検索
        operational_index = search_operational_symbol(action)

        if operational_index == 0: #四則演算がない場合はすぐに返す
            try:
                act_skill_point = read_skill_point(workbook, player_name, action)
            except gspread.exceptions.WorksheetNotFound:
                return "err : プレイヤー名が存在しないか、間違っています。"
            except gspread.exceptions.CellNotFound:
                return "err : 技能名が存在しないか、間違っています。"

            dice = dice_roll(1, 100)
            act_result = action_check(act_skill_point, dice)

            return (player_name + " の " + action + "(" + str(act_skill_point) + ") → **"
                        + str(dice) +" "+ act_result + "**")

        action, operational_symbol, arithmetic_num = splitting_action(action, operational_index)
        act_skill_point = read_skill_point(workbook, player_name, action)
        act_skill_point = four_arithmetic_operations(act_skill_point, operational_symbol, arithmetic_num)
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