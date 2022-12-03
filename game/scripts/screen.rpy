init python:
    # dragに用いる変数
    store.droppable = ""
    store.draggable = ""

    # このスクリーンで使用するフラグ
    pr_door_opened = False  # ドアが開錠されたか
    pr_book_opened = False # bookのメッセージ既読フラグ
    jumped_pr_door_opened_clicked = False  # pr_door_opened_clickedラベルを訪問済みか

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
    draggroup:
        for item in current:
            # 鍵の表示
            if item == 'Key':
                drag:
                    drag_name "Key"
                    child "key_idle.png"
                    xpos 0
                    ypos 0
                    draggable True
                    droppable False
                    clicked Call("say_about", calllabel="say_simple", jumplabel="pr_start.scloop", msg='古い鍵だね')
            # 本の表示
            elif item == 'Book':
                drag:
                    drag_name "Book"
                    child "book_idle.png"
                    xpos 0.2
                    ypos 0
                    draggable False
                    droppable False
                    clicked Call("say_about", calllabel="pr_ev_book_clicked", jumplabel="pr_start.scloop")

            elif item == 'Door':
                # ドア(閉)の表示
                if not pr_door_opened:
                    drag:
                        drag_name "Door"
                        child "door_idle.png"
                        xpos 0.2
                        ypos 0.8
                        yoffset 15
                        draggable False
                        droppable True
                        dropped pr_dropped_to_door
                        clicked Call("say_about", calllabel="say_simple", jumplabel="pr_start.scloop", msg='鍵がかかってるみたい')

                # ドア(開)の表示
                if pr_door_opened:
                    drag:
                        drag_name "Door Opened"
                        child "door_opened.png"
                        xpos 0.2
                        ypos 0.8
                        yoffset 15
                        draggable False
                        droppable False
                        clicked Call("say_about", calllabel="pr_ev_door_opened_clicked", jumplabel="pr_start.scloop")
            else:
                drag:
                    drag_name item
                    child item
                    pos objpos[item]
                    draggable True
                    droppable False
