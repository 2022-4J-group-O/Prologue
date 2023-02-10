init python:
    from datetime import datetime

label pr_clock_clicked:

    show girl at right with dissolve
    
    g "時計があるね"
    
    menu:
        "そっちの世界では今9時なの？":
            g "君はどうしてそう思うの？"

            g "だってこの時計には一切数字が書かれていないんだよ"

            g "この時計に9なんて数字は書かれていない"

            show girl smile with dissolve

            g "ま、私にもその理由はわからないんだけどね"

            show girl with dissolve

            g "なぜなら私はこの時計を時刻を知るものとして認識していないから"

            g "これが時計だということは知ってる"

            g "でも数字の書いていないこれをどう読むのかはわからない"

            g "パソコンみたいなデジタルな機器だったら時間は数値として扱うのが普通でしょ？"
            
            show girl smile with dissolve

            $ g("今の時刻は" + datetime.now().strftime("%H時%M分%S秒") + "だよ")

            show girl with dissolve

            g "君の世界ではどうなっているか知らないけど"

            show girl smile with dissolve

            g "たぶん同じ時間なんじゃないかな？"

            show girl with dissolve

            g "なぜそう思うのかって？"

            g "だって私はこの端末に設定されている時間を見ただけだから"

            g ""
        "この時計、止まってる？":
            pass

    
    hide girl
    
    window hide
    
    with dissolve
    
    $ event_end(loop_label())