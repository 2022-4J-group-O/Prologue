image title logo big:
    "title_logo"
    zoom 1.5

screen title_screen(current):
    layer "master"
    add "title logo big" pos (0.5, 0.3) anchor (0.5, 0.5)

    use obj_screen(current)

screen trash():
    $ row = 25
    $ column = 50
    $ tile_size = 120
    $ space = -70
    fixed:
        grid column row:
            spacing space
            for i in range(0, row):
                for j in range(0, column):
                    if renpy.random.random() > 0.5:
                        add SampleImage("", tile_size, tile_size, "#5050ff20")
                    else:
                        add SampleImage("", tile_size, tile_size, "#e0e0e050")
        xminimum column * tile_size + space * (column - 1)
        yminimum row * tile_size + space * (row - 1)
        xcenter 0.5
        ycenter 0.5
