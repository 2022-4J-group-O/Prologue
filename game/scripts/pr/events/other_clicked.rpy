label pr_key_clicked:

    call say_simple("古い鍵だね")

    $ event_end(loop_label())

label pr_door_clicked:

    call say_simple("鍵がかかってるみたい")

    $ event_end(loop_label())

label pr_cushion_clicked:

    call say_simple("なんの変哲もないクッションだね")

    $ event_end(loop_label())