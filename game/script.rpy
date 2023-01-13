"""
現在考えている少女の差分
* 普通の表情(girl)
* 笑顔(girl smile)
* 驚いた顔(girl surprise)
* 目をそらす(girl look away)
"""
define g = Character('girl', color="#c8ffc8")

default global_data = Const()

label main_menu:
    python:
        # update_user_dir()
        global_data.lazy()
        if auto_load:
            fn = renpy.newest_slot()
            if fn != None:
                renpy.load(fn)
    return

label start:
    jump pr
    
    return

#ロールバックの無効化
init:
    $ config.keymap["rollback"] = []
    