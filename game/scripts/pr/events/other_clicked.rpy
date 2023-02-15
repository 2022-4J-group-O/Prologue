label pr_key_clicked:

    call say_simple("古い鍵だね")

    $ event_end(loop_label())

label pr_door_clicked:

    play sound se_door_locked

    call say_simple("鍵がかかってるみたい")

    $ event_end(loop_label())