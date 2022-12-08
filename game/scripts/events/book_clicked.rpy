"""
本をクリックしたときのイベント
"""

label pr_ev_book_clicked:

    if not pr_book_opened:
        
        g "この本、違和感があるね"
        
        $ pr_book_opened = True # 既読フラグ
        $ make_obj('Key') # 鍵オブジェクトを生成
   
        show girl surprise at right

        g "わ、中に鍵がはいってた"

        show girl at right

        g "この鍵、使えそうだね"

    else:

        g "この本、偽物だったんだね"

    hide girl

    return

