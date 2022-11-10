init python:
    store.droppable = ""
    store.draggable = ""
    # このスクリーンで使用するフラグ

    flg_door_opened = False  # ドアが開錠されたか
    e02_flag_book = False # bookのメッセージ既読フラグ

    # ドアにものがドロップされたときに呼び出される関数
    # drop : ドロップ先Dragオブジェクト
    # drags: ドロップ元のDragオブジェクトのリスト
    def dropped_to_door(drop, drags):
        # ドロップ元が鍵ならJump
        store.droppable = drop.drag_name
        store.draggable = drags[0].drag_name
        return True
        
screen e02(current):
    $ objpos = {'red': (0.25, 0.3), 'blue': (0.6, 0.2), 'green': (0.3, 0.45)}
    draggroup:
        for item in current:
            # 鍵の表示
            if item == 'Key':
                drag:
                    drag_name "Key"
                    idle_child "key_idle.png"
                    hover_child "key_hover.png"
                    xpos 0
                    ypos 0
                    draggable True
                    droppable False
                    clicked Call("say_about", calllabel="e02_key_clicked", jumplabel="e02_pause")
            # 本の表示
            elif item == 'Book':
                drag:
                    drag_name "Book"
                    idle_child "book_idle.png"
                    hover_child "book_hover.png"
                    xpos 0.2
                    ypos 0
                    draggable False
                    droppable False
                    clicked Call("say_about", calllabel="e02_book_clicked", jumplabel="e02_pause")

            elif item == 'Door':
                # ドア(閉)の表示
                if not flg_door_opened:
                    drag:
                        drag_name "Door"
                        idle_child "door_idle.png"
                        hover_child "door_hover.png"
                        xpos 0.2
                        ypos 0.8
                        yoffset 15
                        draggable False
                        droppable True
                        dropped dropped_to_door
                        clicked Call("say_about", calllabel="say_simple", jumplabel="e02_pause", msg='鍵がかかってるね')

                # ドア(開)の表示
                if flg_door_opened:
                    drag:
                        drag_name "Door Opened"
                        child "door_opened.png"
                        xpos 0.2
                        ypos 0.8
                        yoffset 15
                        draggable False
                        droppable True
                        dropped dropped_to_door
                        clicked Call("say_about", calllabel="e02_door_opened_clicked", jumplabel="d03")
            else:
                drag:
                    drag_name item
                    child item
                    pos objpos[item]
                    draggable True
                    droppable False
