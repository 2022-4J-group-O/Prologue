define default_user_dirdata_path_abs = os.path.join(config.basedir, default_user_dirdata_path)

init python:
    from directory import Directory

    # 常に保持しておくデータ
    class Const:
        def __init__(self):
            # 暗号化用テーブル
            self.crypttable = maketable(2)
            # 復号用テーブル
            self.decrypttable = maketable(6)
            self.default_dir_data = Directory({}, {})
        
        # ファイルの中身が空である可能性あり
        def lazy(self):
            self.default_dir_data = eval(dumpbfile(default_user_dirdata_path_abs).translate(self.decrypttable).decode("utf-8"))
