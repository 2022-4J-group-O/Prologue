label obj_clicked(objname):
    $ renpy.dynamic(lb=objname.lower().replace(" ", "_") + "_clicked")
    $ renpy.dynamic(pref_lb=room_prefix + "_" + lb)
    if renpy.has_label(pref_lb):
        jump expression pref_lb
    elif renpy.has_label(lb):
        jump expression lb
    $ event_end(loop_label())

label config_clicked:
    python:

        ShowMenu("preferences")() # 設定画面を呼び出す

        event_end(loop_label())
