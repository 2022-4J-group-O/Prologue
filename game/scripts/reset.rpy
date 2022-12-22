init python:
    def pr_reset():
        global pr_reset_times
        global pr_book_opened
        if reset_room("simple room") == "PE": # 例外が発生
            return
        pr_reset_times += 1
        pr_book_opened = False
