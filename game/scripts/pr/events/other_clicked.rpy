label pr_key_clicked:
    if check_main():
        $ event_end()
    show girl at right with dissolve

    g "古い鍵だね"

    show girl look away at right with dissolve

    g "浮いているように見えるかもしれないけど、それはご愛敬ということで......よろしく......"

    show girl at right with dissolve

    $ event_end(loop_label())

label pr_door_clicked:
    if check_main():
        $ event_end()
    $ jumped_pr_door_clicked = True

    show girl at right with dissolve

    g "鍵がかかってるみたい"

    g "どこかに鍵はないかな"

    show girl smile at right with dissolve

    g "探してきてもらえる？"
    
    hide girl with dissolve

    $ event_end(loop_label())
