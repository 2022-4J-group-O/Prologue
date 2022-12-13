init python:
    # dragに用いる変数
    store.droppable = ""
    store.draggable = ""

    # このスクリーンで使用するフラグ
    pr_door_opened = False  # ドアが開錠されたか
    pr_book_opened = False # bookのメッセージ既読フラグ
    jumped_pr_door_opened_clicked = False  # pr_door_opened_clickedラベルを訪問済みか
    pr_reset_times = 0 # simple roomでリセットした回数

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
            # 鍵の表示
            if item == 'Key':
                drag:
                    drag_name "Key"
                    child "key.png"
                    xpos 0.5
                    xoffset 55
                    ypos 0.8
                    yoffset 50
                    draggable True
                    droppable False
                    clicked FromSc("say_simple", "pr_start.scloop", msg="古い鍵だね")
            elif item == 'Clock':
                drag:
                    drag_name "Clock"
                    child "clock.png"
                    xpos 0.65
                    ypos 0
                    yoffset 30
                    draggable False
                    droppable False
            elif item == 'Cushion':
                drag:
                    drag_name "Cushion"
                    child "cushion.png"
                    xanchor 0.5
                    xpos 0.7
                    yanchor 0.5
                    ypos 0.8
                    yoffset 50
                    draggable False
                    droppable False
            # 本の表示
            elif item == 'Book':
                if not pr_book_opened:
                    drag:
                        drag_name "Book"
                        child "book.png"
                        xpos 0.5
                        ypos 0.8
                        yoffset 60
                        draggable False
                        droppable False
                        clicked FromSc("pr_ev_book_clicked", "pr_start.scloop")
                if pr_book_opened:
                    drag:
                        drag_name "Book"
                        child "book_opened.png"
                        xpos 0.4
                        ypos 0.7
                        yoffset 10
                        draggable False
                        droppable False
                        clicked FromSc("pr_ev_book_clicked", "pr_start.scloop")
            elif item == 'Door':
                if not door_show and not pr_door_opened:
                    drag:
                        drag_name "Door"
                        child "door_hidden.png"
                        xpos 0.1
                        yanchor 0.5
                        ypos 0.5
                        draggable False
                        droppable False
                        clicked FromSc("door_show", "pr_start.scloop")
                # ドア(閉)の表示
                if door_show and not pr_door_opened:
                    drag:
                        drag_name "Door"
                        child "door.png"
                        xpos 0.1
                        yanchor 0.5
                        ypos 0.5
                        yoffset 30
                        draggable False
                        droppable True
                        dropped pr_dropped_to_door
                        clicked FromSc("say_simple", "pr_start.scloop", msg="鍵がかかってるみたい")
                # ドア(開)の表示
                if pr_door_opened:
                    drag:
                        drag_name "Door Opened"
                        child "door_frame.png"
                        xpos 0.1
                        yanchor 0.5
                        ypos 0.5
                        yoffset 15
                        draggable False
                        droppable False
                        clicked FromSc("pr_ev_door_opened_clicked", "pr_start.scloop")
            else:
                drag:
                    drag_name item
                    child item
                    pos objpos[item]
                    draggable True
                    droppable False
