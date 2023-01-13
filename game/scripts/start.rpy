"""
プロローグ
"""

# 各種変数の初期化
# イベントフラグ
default pr_evflg_opening = True  # 初回起動時のイベントフラグ
# 状態フラグ
default pr_main_activated = False  # Mainのプログラムが起動されたときTrueになる(未実装)

default key_dropped = False # KeyがドロップされるとTrue

label pr:
    $ move_room("simple room")  # 部屋移動
    $ init_room("simple room")
    scene bg room
    show screen pr_screen(read_room())
    with Fade(0.0, 1.0, 2.0)


# スクリーンを表示する無限ループ
label .scloop:
    window hide
    show screen pr_screen(read_room())  # スクリーン表示

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
