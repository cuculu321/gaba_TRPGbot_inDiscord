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

1. botを動かす

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

コピーしたIDを*trpg_bot.py*の17行目の********と置き換えます。
```
channel_id = [********]
            ↓
channel_id = [コピーしたID]
```

## 4. SPREADSHEET_KEYの入力
---
使いたいスプレッドシートを開いた時際、URLの/d/と/edit~~の部分を*read_spreadsheet.py*の24行目の
```
SPREADSHEET_KEY = '使いたいスプレッドシートのキー'
```
と置き換えます。

## 5. サービスアカウントキー取得
---
ここ(https://tanuhack.com/operate-spreadsheet/)の
**1. Google Cloud Platformの設定**
を実行し、jsonファイルを取得してください。

## 6. json_keyfileの入力
取得したjsonファイルを、このフォルダに入れてください。

その後、ファイル名をコピーし*read_spreadsheet.py*の
```
json_keyfile = "jsonファイルのファイル名"
```
と置き換えます。

## 7. Discordのトークンの入力
---
まず、https://discordapp.com/developers/applications/ にアクセスして、New Applicationをクリックします。

![コメント 2020-03-07 014558](https://user-images.githubusercontent.com/25599717/76103726-8595fb00-6015-11ea-952c-b4c984773c90.png)

クリックすると、CREATE AN APPLICATIONという画面が出るので、NAMEに適当にアプリ名を付け、Createボタンを押します。

![コメント 2020-03-07 014900](https://user-images.githubusercontent.com/25599717/76103906-d4dc2b80-6015-11ea-931c-d46fcb1cfa72.png)

すると、このような画面になります。この画面では、CoC_botというアプリ名になっています。

![キャプチャ1](https://user-images.githubusercontent.com/25599717/76104154-2edcf100-6016-11ea-90ed-a9253b8bc478.PNG)

左端の中段にある**Bot**から、**Add Bot**をクリックします。

![コメント 2020-03-07 015346](https://user-images.githubusercontent.com/25599717/76104363-91ce8800-6016-11ea-8044-bce7cf8e490d.png)

クリックすると、このような画面が開かれます。

この画面ではbotのアイコンや名称の変更などが出来ます。いつでも変えることが出来るので、変更したい場合は変更を加えてください。

今は、Tokenの下にあるCopyをクリックします。

![コメント 2020-03-07 015609](https://user-images.githubusercontent.com/25599717/76104571-f558b580-6016-11ea-9441-822f34e4dcbb.png)

*TRPGbot_inDiscord*フォルダの中に、*token.txt*を作成し、*token.txt*に先ほどコピーしたTokenを貼り付けます。

## 8. Discord botの作成
---
Tokenを貼り付け保存したら、先ほどのDiscordに戻り、左端の欄にある**OAuth2**をクリックします。
その画面で**scopes**内の**bot**に☑を入れます。

するとURLが生成されるのでCopyボタンをクリックしコピーします。

![コメント 2020-03-07 021226](https://user-images.githubusercontent.com/25599717/76106420-2686b500-601a-11ea-8c7b-52acaea7e099.png)

そのURLに接続するとこのような画面が表示されます。

その後、サーバーを選択から、botを入れたいサーバーを選択します。

※サーバーの管理者権限がなければサーバーを入れることは出来ません。

![コメント 2020-03-07 022342](https://user-images.githubusercontent.com/25599717/76107343-ce50b280-601b-11ea-8783-83a46cbbc8d6.png)

サーバーを選ぶとこのような画面になるので、ロボットではないと宣言します。

![キャプチャ3](https://user-images.githubusercontent.com/25599717/76107348-cf81df80-601b-11ea-874b-9502afb14504.PNG)

そうすると、対象のサーバーにbotが追加されます。

![キャプチャ4](https://user-images.githubusercontent.com/25599717/76107463-0a841300-601c-11ea-8283-0b33ce9a1eaf.PNG)

## 9. botを動かす
---
* pythonで動かす
* herokuで動かす

### 9.1 pythonで動かす
---
```
python trpg_bot.py
```

### 9.2 herokuで動かす
---
```
git add .
git commit -m "run"
git push heroku master
```