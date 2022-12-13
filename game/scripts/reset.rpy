init python:
    def pr_reset():
        global pr_reset_times
        global pr_book_opened
        pr_reset_times += 1
        reset_room("simple room")
        pr_book_opened = False
