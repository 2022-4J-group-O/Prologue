﻿"""
現在考えている少女の差分
* 普通の表情(girl)
* 笑顔(girl smile)
* 驚いた顔(girl surprise)
* 目をそらす(girl look away)
"""
define g = Character('girl', color="#c8ffc8")

label main_menu:
    python:
        fn = renpy.newest_slot()
        if fn != None:
            renpy.load(fn)
    return

label start:
    jump d01
    
    return

#ロールバックの無効化
init:
    $ config.keymap["rollback"] = []
    