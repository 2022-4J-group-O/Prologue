"""
プロローグ
"""

# 各種変数の初期化
# イベントフラグ
default pr_evflg_opening = True  # 初回起動時のイベントフラグ
# 状態フラグ
default pr_main_activated = False  # Mainのプログラムが起動されたときTrueになる(未実装)

default key_dropped = False # KeyがドロップされるとTrue

default jumped_pr_door_clicked = False  # 閉じたドアが一回以上クリックされたかどうか

label pr_start:
    if pr_evflg_opening:
        $ init_room("simple room")
    $ move_room("simple room")  # 部屋移動
    scene bg room
    show screen pr_screen(read_room())
    with Fade(2.0, 1.0, 2.0)
    jump pr.scloop

label pr:
    if pr_evflg_opening:
        $ init_room("simple room")
    $ move_room("simple room")  # 部屋移動
    scene bg room

# スクリーンを表示する無限ループ
label .scloop:
    window hide
    show screen pr_screen(read_room())  # スクリーン表示
    with dissolve

    if pr_evflg_opening:  # 初回起動時 
        python:
            pr_evflg_opening = False  # 初回起動のイベントを無効化
            Event("pr_ev_opening")()

    if pr_main_activated:  # Mainのプログラム起動時
        pass  # 何か書くかも？

    # KeyがDoorにドロップされたときのイベント
    if key_dropped:
        python:
            key_dropped = False
            if not pr_door_opened:
                pr_door_opened = True
                Event("pr_door_opened")()

    pause

    jump .scloop 
