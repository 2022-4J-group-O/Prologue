"""
会話パート:
真っ黒なドアが表示され、クリックした直後に発生する会話
"""
label d03:
    # ドアを開けると真っ黒だった

    scene bg room

    show girl surprise
    
    g "......ドアは開いたけど、真っ暗だね"

    show girl look away

    g "こういう、向こう側が見えない真っ黒なドア、ゲームにはよくあるけど......"

    show girl smile

    g "これは本当に向こう側がつながってない感じだね"

    show girl

    g "私が移動できないってことはそういうことだと思う"

    "......"

    g "......ねえ、君さ、このゲームどうやって起動したの？"

    g "君が起動したゲームの周辺に、もう一つ実行できそうなファイルってなかった？"

    g "このドア、別のプログラムにつながってるんじゃないかな......"

    g "そのプログラムを起動すれば、このドアがそこへつながるかもしれない"

    show girl smile

    g "ちょっと探してきてもらえる？"

    # 実行ファイル起動待ちの探索パートへ
    jump e04
    
    return