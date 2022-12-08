"""
prologue初回起動時にのみ発生させるイベント
少女とプレイヤーが出会うシーン

イベント終了後、pr_startラベルへ戻る

# ラベル
* pr_opening
    * .pr_q
    * .pr_yes
    * .pr_no
"""

define jumped_pr_no = False  # pr_noラベルは訪問済みか

label pr_ev_opening:
    show girl at right
    # cpsを変更
    $ cps(10)
    "......"

    $ cps(30)
    g "この場所が読み込まれるなんて、ずいぶん久しぶりだね"

    g "君は......どうやら私の知り合いではないみたい"

    show girl smile at right

    g "君が誰なのかはよくわからないけど、人と話せてうれしい"

    "......"

    show girl look away at right

    g "......ところでさ、どうして君がこのプログラムを起動したのか私にはわからないんだけど......"

    show girl at right
    
    g "ゲームを遊びに来た......ってことでいいんだよね？"

    "......"

    show girl smile at right

    g "なんにせよ、私との遊びに付き合ってほしいんだけど、どうかな？"

    show girl look away at right

    g "とにかく暇なんだよ......私ここにずっと一人だからさ......"

    "......"

    show girl at right

    g "このゲームは、脱出ゲームだよ"

    g "特に理由もなく狭い部屋に閉じ込められて、どういう仕組みなのかよくわからない珍妙な機械にパスワードを入力して......"

    g "とにかくそこから出ることだけを目指して進んでいく、あの、脱出ゲーム"

    "......"

    g "つまらなそう？"

    show girl look away at right

    g "そりゃあ、大手の企業が開発したソシャゲみたいなやつと比べると、見劣りするかもしれないし......"
    
    g "それどころか、一部バグってるかもしれないけど......"

    show girl at right
    
    g "そんな状態のゲームをプレイさせるなって？"

    g "ほら、個人製作のゲームなわけだし、多少のほころびは許してよ"

    show girl smile at right

    g "とにかく、私の暇を紛らわせてほしい"

    g "きっと、君の暇つぶしにもなるよ"

    g "君だってこんな時間からこんなゲーム起動して、時間持て余してたんでしょ？"

    show girl look away at right

    g "ま、私には、今君がどういう状況でこのゲームをプレイしてるのか、さっぱりわかんないけど"
    
    show girl at right
    
    g "きっと、退屈させないからさ、どう？"



label .question:  # 遊びに付き合うか尋ねる
    menu:
        "遊びに付き合う":
            jump .yes
        "断る":
            jump .no


# 遊びに付き合うと答えた場合
label .yes:
    show girl at right
    
    g "ありがとう！"

    g "それじゃさっそく、脱出ゲームスタートだよ"

    g "......まずは、この部屋から脱出しないとね"

    g "この部屋の探索から始めてみたら？"

    hide girl

    return  # イベント終了


# 遊びに付き合うことを断った場合
label .no:
    if not jumped_pr_no:  # 初訪問時

        $ jumped_pr_no = True

        show girl

        "......"
        
        show girl smile

        g "だよねー、まずは断って、キャラのリアクション見てみないといけないよね"

        g "了承してしまったら、断った時にどういう反応するのか見れないもんね"

        g "拒否権のない質問であることは分かったうえで、拒否せざるを得ない......"

        g "ゲームプレイヤーっていうのは、そういう生き物だもんね"

        g "というわけで、断ってもどうせまたループさせるわけなんだけど、改めてもう一回聞くね？"

        g "儀式みたいなもんだからさ"

        g "ゲームに付き合ってくれるよね？"
    
    else:  # 訪問二回目以降
        show girl at right

        "......"

        show girl smile at right

        g "なかなか慎重派なプレイヤーさんだね"

        g "これ以上違うイベントは起こさないよ。安心して"

        hide girl

    jump .question  # もう一度質問する