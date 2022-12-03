"""
探索パート: 牢獄の鍵を探す
"""

# ジャンプフラグ
default jumped_pr_show_screen = False  # pr_show_screenラベルを一度以上訪れたか

label pr_show_screen:
    $ move_room('simple room')

    if not jumped_pr_show_screen:
        $ jumped_pr_show_screen = True  # pr_show_screenを訪問済みに
        
        show girl at right

        g "まずはこの部屋から脱出しよう"

        g "何か使えそうなものはないかな"

    show screen pr_screen(read_room())


# screenをshowしたうえでpauseすると
# screenを表示したまま画面を固定できる
# クリックによるイベントを起こす度にこのラベルへジャンプする
label pr_scloop:

    $ renpy.pause()

    show screen pr_screen(read_room())

    # 以下はdroppedでTrueが返されたときに実行される
    # drag and dropのイベントでTrueが返されるとscreenが強制終了する
    # droppedでdropされたDragの名前がKeyなら、鍵を消してドアを開く
    if store.draggable == "Key" and (not pr_door_opened):

        $ pr_door_opened = True

        show girl at right

        g "ドアが開いたね"

        hide girl

    jump pr_scloop 
