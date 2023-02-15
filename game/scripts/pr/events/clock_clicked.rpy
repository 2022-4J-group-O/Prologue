init python:
    import datetime

label pr_clock_clicked:
    if check_main():
        $ event_end()
    show girl at right with dissolve

    $ now = datetime.datetime.now().strftime("%H時%M分%S秒")
    
    g "時計があるね"
    
    g "今の時刻は......"

    g "[now]だって"

    g "まあ、この端末に設定されている時間を読んだだけで、あの時計はただの絵に過ぎないんだけど......"

    show girl smile at right with dissolve

    g "こうすると、私が時計を読み取ったかのように見えるでしょう？"
    
    hide girl
    
    window hide
    
    with dissolve
    
    $ event_end(loop_label())