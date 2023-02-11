init python:
    import datetime

label pr_clock_clicked:

    show girl at right with dissolve

    $ now = datetime.datetime.now().strftime("%H時%M分")
    
    g "時計があるね"
    
    g "今の時刻は......"

    g "[now]だって"

    g "まあ、時間を取得する関数を呼び出しただけで、あの時計はただの絵に過ぎないんだけど......"

    show girl smile at right with dissolve

    g "こうすると、まるで、私が本当に時計を読み取ったみたいでしょう？"
    
    hide girl
    
    window hide
    
    with dissolve
    
    $ event_end(loop_label())