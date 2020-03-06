#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 
import gspread
import time

class open_google_spreadsheet:
    """
    Google Spreadsheetのトークンやワークブック、ログインリセット関数などを保持する

    Attributes
    ----------
    gc : gspread.Client
        認証を受けログインしたクライアント情報
    workbook : Spreadsheet
        キーで指定したスプレッドシート
    SPREADSHEET_KEY : String
        使いたいスプレッドシートのキー
    set_token_time : int
        トークンを生成してからの時間
    """

    gc = []
    workbook = []
    SPREADSHEET_KEY = '1ThG04nz4l-ISa504UNcF97gKlkMx75YtggMGSJR2Eic'
    set_token_time = 0
    
    def gs_login(self):
        """
        oauth2を用いてGoogleからClientを取得する
        """

        # *** Google SpreadSheetへのアクセス
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        #認証情報設定
        #ダウンロードしたjsonファイル名を設定
        credentials = ServiceAccountCredentials.from_json_keyfile_name('gaba-cocbot-readspreadsheet-22b6a04f8d0a.json', scope)

        #OAuth2の資格情報を使用してGoogle APIにログインします。
        self.gc = gspread.authorize(credentials)

    def open_workbook(self):
        """
        Client情報とSPREADSHEET_KEYを使ってスプレッドシートを開く
        """

        self.workbook = self.gc.open_by_key(self.SPREADSHEET_KEY)

    def set_token(self):
        """
        スプレッドシートへのアクセスとアクセストークンを発行した時刻を記録
        """

        self.gs_login()
        self.open_workbook()
        self.set_token_time = time.time()

    def give_workbook(self):
        """
        取得しているスプレッドシートを与える。
        与える時に、トークンを発行してから一定時間立っている場合再発行
        """

        print(time.time() - self.set_token_time)
        if (time.time() - self.set_token_time)> 3500:
            print("refresh token")
            self.set_token()

        return self.workbook

def read_skill_point(workbook, player_name, action):
    """
    技能値の取得

    Parameters
    ----------
    workbook : spreadsheet
        取得したいspreadsheet
    player_name : string
        /actコマンドの第1引数。プレイヤーの名称(検索するシート名)
    action : string
        /actコマンドの第2引数。技能名(検索する文字)

    Returns
    -------
    act_skill_point : int
        技能値

    """
    
    action_cmd = action
    multipl_point = 1
        
    worksheet = workbook.worksheet(player_name)
    act_cell = worksheet.find(action_cmd)

    act_skill_point = int(worksheet.cell(act_cell.row, act_cell.col + 4).value)

    return act_skill_point