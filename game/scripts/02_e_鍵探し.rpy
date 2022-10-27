"""
探索パート: 牢獄の鍵を探す
"""
image background = "Background Room.png"
label e01:
    scene background
    with fade


    "ここから鍵を探す探索パート"
    jump book
    # TODO: 鍵を探す
label book:
    call screen key(g)

label key:
    call screen key
    

    




label end:
    "you're in \"label end\""
    return
