label pr_ev_door_opened:
    show girl at right

    $ delete_obj("Door")
    $ make_obj("Door Opened")

    show screen pr_screen(read_room())
    
    g "やった！ドアが開いたね"

    g "君には少し簡単すぎたかな？"

    hide girl

    return
