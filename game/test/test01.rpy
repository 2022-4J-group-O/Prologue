label test01_1:
    call screen front(["sample/test2.jpg", "sample/test1.png", "bg room.png", "sample/P.png"], 0)

label test01_2:
    $ xp = float(renpy.input("input position x.", length=10))
    $ yp = float(renpy.input("input position y.", length=10))
    $ poss[0] = (xp, yp)
    call screen fortest()
    jump test01_2

label test01_3:
    python:
        if exists("red"):
            renpy.jump("test01_4")
        else:
            renpy.jump("test01_5")

label test01_4:
    python:
        ims.append("sample/red.png")
        poss.append((0.5, 0.5))
    jump test01_5

label test01_5:
    call screen fortest()
    jump d01