"""
探索パート: 牢獄の鍵を探す
"""
<<<<<<< HEAD:game/scripts/02_e_鍵探し.rpy
image background = "Background Room.png"
label e01:
    scene background
=======
label e02:
    scene bg simple room 
>>>>>>> main:game/scripts/02_e_最初の部屋脱出.rpy
    with fade


    "ここから鍵を探す探索パート"
    # TODO: 鍵を探す
    call screen book
label key:
    call screen key
    call screen opened

<<<<<<< HEAD:game/scripts/02_e_鍵探し.rpy
label end:
    "you're in \"label end\""
    return
=======
    jump d03

    return
>>>>>>> main:game/scripts/02_e_最初の部屋脱出.rpy
