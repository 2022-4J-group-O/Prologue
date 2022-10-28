init python:
    # _x: ドロップ先Dragオブジェクト
    # _y: ドロップ元のDragオブジェクトのリスト
    def key_interacted(_x, _y):
        return True
        
# Book
screen book:
    imagebutton:
        xanchor 0
        yanchor 0
        xpos 0.2
        ypos 0
        idle "book_idle.png"
        hover "book_hover.png"
        action Jump("key")
    imagebutton:
        xanchor 0
        yanchor 0
        xpos 0.2
        ypos 0.8
        yoffset 15
        idle "door_idle.png"
        hover "door_hover.png"
        # action Jump("end")

#key
screen key:
    draggroup:
        drag:
            drag_name "Key"
            idle_child "key_idle.png"
            hover_child "key_hover.png"
            xpos 0
            ypos 0
            draggable True
            droppable False
                
        drag:
            drag_name "Book"
            idle_child "book_idle.png"
            hover_child "book_hover.png"
            xpos 0.2
            ypos 0
            draggable False
            droppable False

        drag:
            drag_name "Door"
            idle_child "door_idle.png"
            hover_child "door_hover.png"
            xpos 0.2
            ypos 0.8
            yoffset 15
            draggable False
            droppable True
            dropped key_interacted

screen opened:
    imagebutton:
        xpos 0.2
        ypos 0
        idle "book_idle.png"
        hover "book_hover.png"

    imagebutton:
        idle "door_idle.png"
        hover "door_hover.png"
        xpos 0.2
        ypos 0.8
        yoffset 15
        action Jump("end")
        