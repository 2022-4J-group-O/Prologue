"""
本をクリックしたときのイベント
"""

label pr_book_clicked:

    show girl at right with dissolve
    g "この本、違和感があるね"
    
    $ delete_obj("Book")
    $ make_obj("Book Opened")
    $ make_obj('Key') # 鍵オブジェクトを生成

    show girl surprise at right with dissolve

    show screen pr_screen(read_room()) # 鍵を表示させるためにスクリーン更新する

    g "わ、中に鍵がはいってた"

    show girl at right with dissolve

    g "この鍵、使えそうだね"

    hide girl with dissolve

    $ event_end(loop_label())


label pr_book_opened_clicked:

    show girl at right with dissolve

    g "この本、偽物だったんだね"

    hide girl with dissolve

    $ event_end(loop_label())