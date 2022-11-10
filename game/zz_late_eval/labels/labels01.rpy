# 渡された文字列を改行区切りでgirlにしゃべらせる
label say_simple(msg, jumplabel=None):
    show girl at right
    python:
        for s in msg.splitlines():
            g(s)
    hide girl
    if jumplabel != None:
        jump expression jumplabel
    
    return

# インタラクション的なことをしながらラベルを呼ぶ(要検証)
# callするラベルは必ずreturnされなければならない
# screenからセリフを呼び出したいときは必ずこれを使う
label say_about(calllabel, jumplabel=None, **kwargs):
    if not say_interact:
        $ say_interact = True
        call expression calllabel pass (**kwargs) # must be returned
        $ say_interact = False
        if jumplabel != None:
            jump expression jumplabel
    return
