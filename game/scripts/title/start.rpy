image bg title = "bg room"

label title:
    python:
        move_room("title")
        init_room("title")
    scene bg title
    show screen title_screen(read_room())
    with Fade(0.0, 1.0, 2.0)

label .scloop:
    window hide
    show screen pr_screen(read_room())

    pause
    jump .scloop