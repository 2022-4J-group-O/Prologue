"""
探索パート: 牢獄の鍵を探す
"""
label e02:
    scene bg room with fade
    show screen e02

    show girl at right

    g "まずはこの部屋から脱出しよう"

    hide girl

# screenをshowしたうえでpauseすると
# screenを表示したまま画面を固定できる
# クリックによるイベントを起こす度にこのラベルへジャンプする
label e02_pause:

    $ renpy.pause(hard=True)

    # 以下はdroppedでTrueが返されたときに実行される
    # drag and dropのイベントでTrueが返されるとscreenが強制終了する
    # droppedでdropされたDragの名前がKeyなら、鍵を消してドアを開く
    show screen e02

    if store.draggable == "Key":

        $ flg_key_visible = False
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

    jump e02_pause


# 本をクリックしたとき
label e02_book_clicked:

    show girl at right

    if (not flg_key_visible) and (not flg_door_opened):

        g "この本、違和感があるね"

        $ flg_key_visible = True # 鍵を表示

        show girl surprise at right

        g "わ、中に鍵がはいってた"

        show girl at right

        g "この鍵、使えそうだね"

    else:

        g "この本、偽物だったんだね"

    hide girl

    jump e02_pause


# ドアをクリックしたとき
label e02_door_clicked:

    show girl at right

    g "鍵がかかってるね"

    hide girl

    jump e02_pause


# 開かれたドアをクリックしたとき
label e02_door_opened_clicked:

    hide screen e02

    jump d03  # d03へ