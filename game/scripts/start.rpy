"""
プロローグ
"""

# 各種変数の初期化
# イベントフラグ
default pr_evflg_opening = True  # 初回起動時のイベントフラグ
# 状態フラグ
default pr_main_activated = False  # Mainのプログラムが起動されたときTrueになる(未実装)

label pr_start:
    $ move_room('simple room')  # 部屋移動
    scene bg room
    show screen pr_screen(read_room())
    with Fade(0.0, 1.0, 2.0)


# スクリーンを表示する無限ループ
label .scloop:
    window hide
    show screen pr_screen(read_room())  # スクリーン表示

    if pr_evflg_opening:  # 初回起動時 
        $ pr_evflg_opening = False  # 初回起動のイベントを無効化
        call say_about("pr_ev_opening", "pr_start.scloop")

    if pr_main_activated:  # Mainのプログラム起動時
        pass  # 何か書くかも？

    # KeyがDoorにドロップされたときのイベント
    if store.draggable == "Key" and (not pr_door_opened):
        $ pr_door_opened = True
        call say_about("pr_ev_door_opened", "pr_start.scloop")

    $ renpy.pause()

    jump .scloop 
