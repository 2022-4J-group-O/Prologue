"""
探索パート: 牢獄の鍵を探す
"""

label e02:
    scene bg room with fade

    $ move_room('simple room')


    show screen e02(read_room())

    show girl at right

    g "まずはこの部屋から脱出しよう"
    
    window hide #前の場面の台詞ウィンドウをとじる

    hide girl

# screenをshowしたうえでpauseすると
# screenを表示したまま画面を固定できる
# クリックによるイベントを起こす度にこのラベルへジャンプする
label e02_pause:

    $ renpy.pause()

    # 以下はdroppedでTrueが返されたときに実行される
    # drag and dropのイベントでTrueが返されるとscreenが強制終了する
    # droppedでdropされたDragの名前がKeyなら、鍵を消してドアを開く
    show screen e02(read_room())

    hide window

    if store.draggable == "Key" and (not flg_door_opened):

        $ flg_door_opened = True

        show girl at right

        g "ドアが開いたね"

        hide girl

    jump e02_pause


# 以下は各種クリックによるイベント

# 鍵をクリックしたとき
label e02_key_clicked:

    show girl at right

    g "古い鍵だね"

    hide girl

    return


# 本をクリックしたとき
label e02_book_clicked:

    show girl at right

    if not e02_flag_book:

        g "この本、違和感があるね"

        $ e02_flag_book = True # 既読フラグ
        $ make_obj('Key') # 鍵オブジェクトを生成

        show girl surprise at right

        g "わ、中に鍵がはいってた"

        show girl at right

        g "この鍵、使えそうだね"

    else:

        g "この本、偽物だったんだね"

    hide girl

    return


# ドアをクリックしたとき
label e02_door_clicked:

    show girl at right

    g "鍵がかかってるね"

    hide girl

    jump e02_pause


# 開かれたドアをクリックしたとき
label e02_door_opened_clicked:

    hide screen e02

    return  # d03へ