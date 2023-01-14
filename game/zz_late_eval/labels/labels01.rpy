# 渡された文字列を改行区切りでgirlにしゃべらせる
label say_simple(msg, jumplabel=None):
    show girl at right with dissolve
    python:
        for s in msg.splitlines():
            g(s)
    hide girl with dissolve
    if jumplabel != None:
        jump expression jumplabel
    
    return
