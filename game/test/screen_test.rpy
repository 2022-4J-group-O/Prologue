default ims = ["blue.png", "green.png"]
default poss = [(0.0, 0.0), (0.0, 0.5)]

screen front(bglist, i):
    frame:
        background bglist[i]
        imagebutton:
            ypos 0.5
            idle "./sample/WhiteSquare.png"
            hover "./samplecolorful.png"
            action Show("front", bglist=bglist, i=(i + 1) % 4)
        imagebutton:
            pos (1.0, 0.5)
            idle "./sample/WhiteSquare.png"
            hover "./sample/colorful.png"
            action Show("front", bglist=bglist, i=(i - 1) % 4)
        drag:
            draggable True
            frame:
                align (.5, .5)
                padding (10, 10)
                has vbox
                text "abc"


screen fortest():
    frame:
        for img, po in zip(ims, poss):
            imagebutton:
                idle img
                hover "sample/lightblue.png"
                pos po
                action Return()


# オブジェクトの位置は部屋によって決まっている。

init python:
    # _x: ドロップ先Dragオブジェクト
    # _y: ドロップ元のDragオブジェクトのリスト
    def key_interacted(_x, _y):
        return True
        
# Book
screen book():
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
screen key():
    default show_key = False
    if not show_key:
        imagebutton:
            xanchor 0
            yanchor 0
            xpos 0.2
            ypos 0
            idle "book_idle.png"
            hover "book_hover.png"
            action SetLocalVariable("show_key", True)
    draggroup:
        if show_key:
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
        

screen room_e02f():
    frame:
        pos (0.0, 0.5)
        yanchor 0.5
        imagebutton:
            idle "leftarrow.png"
            hover "blue.png"
            action Jump("e02_left")
    frame:
        pos (1.0, 0.5)
        anchor (1.0, 0.5)
        imagebutton:
            idle "rightarrow.png"
            hover "blue.png"
            action Jump("e02_right")
    use key()

screen room_e02l():
    frame:
        pos (0.0, 0.5)
        yanchor 0.5
        imagebutton:
            idle "leftarrow.png"
            hover "blue.png"
            action Jump("e02_back")
    frame:
        pos (1.0, 0.5)
        anchor (1.0, 0.5)
        imagebutton:
            idle "rightarrow.png"
            hover "blue.png"
            action Jump("e02_front")

screen room_e02r():
    frame:
        pos (0.0, 0.5)
        yanchor 0.5
        imagebutton:
            idle "leftarrow.png"
            hover "blue.png"
            action Jump("e02_front")
    frame:
        pos (1.0, 0.5)
        anchor (1.0, 0.5)
        imagebutton:
            idle "rightarrow.png"
            hover "blue.png"
            action Jump("e02_back")

screen room_e02b():
    frame:
        pos (0.0, 0.5)
        yanchor 0.5
        imagebutton:
            idle "leftarrow.png"
            hover "blue.png"
            action Jump("e02_right")
    frame:
        pos (1.0, 0.5)
        anchor (1.0, 0.5)
        imagebutton:
            idle "rightarrow.png"
            hover "blue.png"
            action Jump("e02_left")