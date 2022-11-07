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


