# CoCサポートDiscord bot

## 目次
----
1. [キャラクターシートのスプシの紹介](https://github.com/cuculu321/gaba_TRPGbot_inDiscord/tree/make_readme#1-%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC%E3%82%B7%E3%83%BC%E3%83%88%E3%81%AE%E3%82%B9%E3%83%97%E3%82%B7%E3%81%AE%E7%B4%B9%E4%BB%8B)

1. [インストールするもの](https://github.com/cuculu321/gaba_TRPGbot_inDiscord/tree/make_readme#2%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E3%82%82%E3%81%AE)

1. [chennel idの入力](https://github.com/cuculu321/gaba_TRPGbot_inDiscord/tree/make_readme#3chennel-id%E3%81%AE%E5%85%A5%E5%8A%9B)

1. SPREADSHEET_KEYの入力

1. サービスアカウントキー取得

1. json_keyfileの入力

1. Discordのトークンの入力

1. Discord botの作成

## 1. キャラクターシートのスプシの紹介
---
キャラクターシートのスプシはCoC第6版となっています。

以下のリンクのスプシをコピーして利用してください。

[キャラクターシートのスプシ](
https://docs.google.com/spreadsheets/d/1ByjbgapG7UmpT6AoQwB32EUCJaULlCT5-kUGZBQ1-dI/edit?usp=sharing)

## 2.インストールするもの
---
動作環境として以下のものが必要となります。
* python3系
* discord.py 1.3
* oauth2client
* gspread

or 

* heroku

## 3.chennel idの入力
---
Discordのユーザー設定からテーマを開き、開発者モードをONにします。
![Discord_開発者モード](https://user-images.githubusercontent.com/25599717/76095944-870cf680-6008-11ea-9fc2-9b762373b19b.PNG)

ONにしたら、botを導入したいチャンネルを右クリックするとIDをコピーできます。
![コメント 2020-03-07 001459](https://user-images.githubusercontent.com/25599717/76096384-5d080400-6009-11ea-9082-9b32d51a1467.png)

コピーしたIDをtrpg_bot.pyの17行目の********と置き換えます。
```
channel_id = [********]
            ↓
channel_id = [コピーしたID]
```
