define default_user_dir_abs = os.path.join(config.basedir, default_user_dir)

init python:
    import shutil
    import glob
    def delete_dir_file(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            os.mkdir(path)
    
    def delete_savefile():
        delete_dir_file(os.path.join(config.basedir, "game/saves"))
    
    # バイナリデータの全単射写像を定義するためのテーブルを作成
    # shiftは0~8のどれか
    def maketable(shift):
        num = 0
        for i in range(0, 256):
            num <<= 8
            num |= ((i << shift) | (i >> (8 - shift))) & 0x00FF
        return num.to_bytes(256, byteorder="big")
    
    # pathで指定されるファイルの中身を返す
    def dumpbfile(path):
        s = bytes()
        with open(path, "rb") as f:
            s = f.read()
        return s
    
    # デフォルトのユーザー用ディレクトリ構造をバイナリデータで暗号化してpathで指定されるファイルに保存
    def update_user_dir(path=default_user_dir_abs):
        direc = Directory()
        direc.load(path)
        by = direc.__repr__().encode("utf-8").translate(global_data.crypttable)
        with open(default_user_dirdata_path_abs, "wb") as f:
            f.write(by)
    
    # デフォルトのユーザー用ディレクトリ構造を読み込んで返す
    # 戻り値はDirectoryクラス
    def load_user_dirdata():
        by = dumpbfile(default_user_dirdata_path_abs).translate(global_data.decrypttable)
        return Directory(eval(by.decode("utf-8")))
    
    # 部屋をリセット(相対パスで)
    # PE -> PermissionError
    def reset_room(room_path: str):
        cwd = os.getcwd()
        os.chdir(user_dir_path)
        if os.path.isdir(room_path):
            try:
                shutil.rmtree(room_path)
            except PermissionError:
                return "PE"
        # os.makedirs(room_path)
        for p in global_data.default_dir_data.dirlist[0]:
            tmp = os.path.commonpath([p, room_path])
            # print(tmp)
            if tmp != "" and os.path.relpath(tmp, room_path) == ".":
                os.mkdir(p)
        for (i, p) in enumerate(global_data.default_dir_data.dirlist[1]):
            tmp = os.path.commonpath([p, room_path])
            if tmp != "" and os.path.relpath(tmp, room_path) == ".":
                with open(p, "wb") as f:
                    f.write(global_data.default_dir_data.dirlist[2][i])
        os.chdir(cwd)
        return None