define default_user_dirdata_path_abs = os.path.join(config.basedir, default_user_dirdata_path)

init python:
    # ディレクトリの構造を保持
    class Directory:
        # どこも指していないディレクトリ
        def __init__(self, direc=[[], [], []]):
            self.dirlist = direc
        
        # pathで指定されるディレクトリ内の構造を読み込み
        def load(self, path):
            if os.path.isdir(path):
                allf = glob.glob(os.path.join(path, "**"), recursive=True)
                fi = [p for p in allf if os.path.isfile(p)]
                self.dirlist = [
                    [os.path.relpath(s, path) for s in allf if os.path.isdir(s)], 
                    [os.path.relpath(s, path) for s in fi], 
                    [dumpbfile(p) for p in fi]
                ]
        
        # 保持しているディレクトリ構造をpathで指定されるディレクトリにコピー
        def make(self, path):
            cwd = os.getcwd()
            if os.path.exists(path):
                shutil.rmtree(path)
            os.mkdir(path)
            os.chdir(path)
            for s in self.dirlist[0][1:]:
                os.mkdir(s)
            for (s, b) in zip(self.dirlist[1], self.dirlist[2]):
                with open(s, "wb") as f:
                    f.write(b)
            os.chdir(cwd)

        def __str__(self):
            return str(self.dirlist)
        
        def __repr__(self):
            return self.dirlist.__repr__()

    # 常に保持しておくデータ
    class Const:
        def __init__(self):
            # 暗号化用テーブル
            self.crypttable = maketable(2)
            # 復号用テーブル
            self.decrypttable = maketable(6)
            self.default_dir_data = Directory()
        
        # ファイルの中身が空である可能性あり
        def lazy(self):
            self.default_dir_data = Directory(eval(dumpbfile(default_user_dirdata_path_abs).translate(self.decrypttable).decode("utf-8")))
