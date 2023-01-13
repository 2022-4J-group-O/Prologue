init python:

    # このスクリーンで使用するフラグ
    pr_door_opened = False  # ドアが開錠されたか
    jumped_pr_door_opened_clicked = False  # pr_door_opened_clickedラベルを訪問済みか
    pr_door_showing = False
    pr_reset_times = 0 # simple roomでリセットした回数

    # ドアにものがドロップされたときに呼び出される関数
    # drop : ドロップ先Dragオブジェクト
    # drags: ドロップ元のDragオブジェクトのリスト
    def pr_dropped_to_door(drop, drags):
        # ドロップ元が鍵ならJump
        global key_dropped
        if drags[0].drag_name == "Key":
            key_dropped = True
        return True
