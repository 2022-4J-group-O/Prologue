label pr_door_opened:

    show girl at right with dissolve

    $ delete_obj("Door")
    $ make_obj("Door Opened")

    play sound se_door_open

    show screen pr_screen(read_room())

    g "やった！ドアが開いたね"

    g "君には少し簡単すぎたかな？"

    hide girl with dissolve

    $ event_end(loop_label())
