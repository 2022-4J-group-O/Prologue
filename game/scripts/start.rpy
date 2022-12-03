"""
プロローグ
"""

# 各種変数の初期化
# イベントフラグ
define pr_evflg_opening = True  # 初回起動時のイベント
define pr_evflg_door_clicked = False  # ドアクリック時に発生するイベント
define pr_evflg_main_activated = False  # Mainのプログラムが起動されたときTrueになる(未実装)

label pr_start:

    # 背景をゆっくり表示
    scene bg room
    with fade

    if pr_evflg_opening:  # 初回起動時 
        $ pr_evflg_opening = False  # 初回起動のイベントを無効化
        jump pr_ev_opening  # 初回起動時のイベントへジャンプ
    
    if pr_evflg_door_clicked:  # ドアクリック時
        $ pr_evflg_door_clicked = False  # イベント無効化
        jump pr_door_clicked

    if pr_evflg_main_activated:  # Mainのプログラム起動時
        pass  # 何か書くかも？

    jump pr_show_screen  # 部屋の表示
