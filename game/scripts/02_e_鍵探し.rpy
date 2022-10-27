"""
探索パート: 牢獄の鍵を探す
"""
image background = "Background Room.png"
label e01:
    scene background
    with fade


    "ここから鍵を探す探索パート"
    # TODO: 鍵を探す
    call screen book
label key:
    call screen key
    call screen opened

label end:
    "you're in \"label end\""
    return
