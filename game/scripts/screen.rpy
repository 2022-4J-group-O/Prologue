init python:
    # dragに用いる変数
    store.droppable = ""
    store.draggable = ""

    # このスクリーンで使用するフラグ
    pr_door_opened = False  # ドアが開錠されたか
    pr_book_opened = False # bookのメッセージ既読フラグ
    jumped_pr_door_opened_clicked = False  # pr_door_opened_clickedラベルを訪問済みか
    pr_door_showing = False

    # ドアにものがドロップされたときに呼び出される関数
    # drop : ドロップ先Dragオブジェクト
    # drags: ドロップ元のDragオブジェクトのリスト
    def pr_dropped_to_door(drop, drags):
        # ドロップ元が鍵ならJump
        store.droppable = drop.drag_name
        store.draggable = drags[0].drag_name
        return True
        
screen pr_screen(current):
    $ objpos = {'red': (0.25, 0.3), 'blue': (0.6, 0.2), 'green': (0.3, 0.45)}
    layer "master"
    draggroup:
        for item in current:
            drag:
                drag_name item
                if renpy.can_show(item.lower()):
                    child item.lower()
                else:
                    child Text(item + "not found")
                if item == "Door":
                    dropped pr_dropped_to_door
                properties default_obj_prop[item]
