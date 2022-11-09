init python:
    store.droppable = ""
    store.draggable = ""
    # このスクリーンで使用するフラグ
    flg_key_visible = False  # 鍵が表示されるか
    flg_door_opened = False  # ドアが開錠されたか
    
    # ドアにものがドロップされたときに呼び出される関数
    # drop : ドロップ先Dragオブジェクト
    # drags: ドロップ元のDragオブジェクトのリスト
    def dropped_to_door(drop, drags):
        # ドロップ元が鍵ならJump
        store.droppable = drop.drag_name
        store.draggable = drags[0].drag_name
        return True
        
screen e02:
    draggroup:
        # 鍵の表示
        if flg_key_visible:
            drag:
                drag_name "Key"
                idle_child "key_idle.png"
                hover_child "key_hover.png"
                xpos 0
                ypos 0
                draggable True
                droppable False
                clicked Jump("e02_key_clicked")
                
        # 本の表示
        drag:
            drag_name "Book"
            idle_child "book_idle.png"
            hover_child "book_hover.png"
            xpos 0.2
            ypos 0
            draggable False
            droppable False
            clicked Call("e02_book_clicked")

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
                clicked Jump("e02_door_clicked")

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
                clicked Jump("e02_door_opened_clicked")