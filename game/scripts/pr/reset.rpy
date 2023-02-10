init python:
    def pr_reset():
        global pr_reset_times
        if init_room("simple room") == "PE": # 例外が発生
            return
        pr_reset_times += 1
