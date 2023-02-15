label pr_clock_clicked:
    if check_main():
        $ event_end()
    show girl at right with dissolve
    
    g "時計があるね"
    
    g "止まってるように見えるけど実際は動いてるよ"
    
    hide girl
    
    window hide
    
    with dissolve
    
    $ event_end(loop_label())