"""
開かれたドアをクリックしたときのイベント
"""

label pr_door_opened_clicked:
    # 初めてこのラベルにジャンプしたとき
    if not jumped_pr_door_opened_clicked:

        $ jumped_pr_door_opened_clicked = True  # このラベルを訪問済みに

        show girl surprise at right with dissolve
        
        g "......ドアは開いたけど、真っ暗だね"

        show girl look away at right with dissolve

        g "こういう、向こう側が見えない真っ黒なドア、ゲームにはよくあるけど......"

        show girl smile at right with dissolve

        g "これは本当に向こう側がつながってない感じだね"

        show girl with dissolve

        g "私が移動できないってことはそういうことだと思う"

        "......"

        g "......ねえ、君さ、このゲームどうやって起動したの？"

        g "君が起動したゲームの周辺に、もう一つ実行できそうなファイルってなかった？"

        g "このドア、別のプログラムにつながってるんじゃないかな......"

        g "そのプログラムを起動すれば、このドアがそこへつながるかもしれない"

        show girl smile at right with dissolve

        g "ちょっと探してきてもらえる？"

    else:  # 以前このラベルに訪問済みのとき

        show girl at right with dissolve

        g "別のプログラムを起動すれば、このドアが通れるようになるはずだよ"

        g "探してきて"

    hide girl
    with dissolve

    $ event_end(loop_label())
