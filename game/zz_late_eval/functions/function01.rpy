define user_dir_path = os.path.join(config.basedir, user_directory)

init python :
    import hashlib

    def cps(sp):
        preferences.text_cps = sp
    
    def dot(amount, cps=preferences.slow_cps):
        return f"{{cps={cps}}}" + "." * amount + "{/cps}"
    
    def cps_str(s, cps):
        return f"{{cps={cps}}}" + str(s) + "{/cps}"
    
    def slow(s):
        return f"{{cps={preferences.slow_cps}}}" + str(s) + "{/cps}"
    
    # fpは相対パス
    def exists(fp):
        return os.path.exists(os.path.join(user_dir_path, fp))
    
    # ファイルのハッシュ値をチェック
    def check_hash(objname):
        with open(objname, mode="rb") as f:
            cond = f.read() == hashlib.sha256(os.path.basename(objname).encode("utf-8")).digest()
        return cond

    # バイナリファイル(pngやzip)のハッシュ値をチェック
    def check_hash_binary(filename):
        fp = os.path.join(config.basedir, "game/data/hash_list", os.path.basename(filename))
        if os.path.isfile(fp):
            with open(fp, "rb") as hf:
                hf_hash = hf.read()
        else:
            return False
        if os.path.isfile(filename):  # 多分必要ないけど一応
            with open(filename, "rb") as f:
                f_hash = hashlib.sha256(f.read()).digest()
            return hf_hash == f_hash
        else:
            return False

    def read_room_raw(roomdir=None):
        path = ""
        if roomdir == None:
            path = os.path.join(user_dir_path, current_room)
        else:
            path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            os.chdir(path)
            return [p for p in objects if os.path.isfile(p) and (check_hash(p) or check_hash_binary(p))]
        else:
            return list()
    
    # roomのパスを指定してオブジェクトを読み込む
    # 読み込み可能なオブジェクトはoption.rpyのobjects定数で指定する
    # roomを指定しない場合現在いるroomのオブジェクトを読み込む
    # オブジェクト名の前に.が付いたファイルも読み込む
    def read_room(roomdir=None):
        cwd = os.getcwd()
        l = read_room_raw(roomdir)
        os.chdir(cwd)
        return l

    def check_obj(objname, roomdir=None):
        if roomdir == None:
            path = os.path.join(user_dir_path, current_room, objname)
        else:
            path = os.path.join(user_dir_path, roomdir, objname)
        return os.path.isfile(path) and (check_hash(path) or check_hash_binary(path))

    def make_obj_room_raw(roomdir, objname):
        path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            os.chdir(path)
            with open(objname, "wb") as f:
                f.write(hashlib.sha256(objname.encode("utf-8")).digest())
            return True
        else:
            return False
    
    # roomのパスとオブジェクト名を指定してオブジェクトを作成する
    # 読み込み可能でなくてもOK
    # 成功時にTrue、失敗時にFalseを返す(すでにオブジェクトが存在していても成功)
    def make_obj_room(roomdir, objname):
        cwd = os.getcwd()
        cond = make_obj_room_raw(roomdir, objname)
        os.chdir(cwd)
        return cond

    # 現在いるルームにオブジェクトを作成
    # 対象room以外はmake_obj_room関数と同じ動作
    def make_obj(objname):
        return make_obj_room(current_room, objname)
    
    def give_hidden_raw(roomdir, objname):
        path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            os.chdir(path)
            if os.path.isfile(objname):
                if renpy.windows:
                    info = subprocess.STARTUPINFO()
                    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    info.wShowWindow = subprocess.SW_HIDE
                    result = subprocess.run(["attrib", "+H", objname], startupinfo=info)
                    return result.returncode == 0
                elif renpy.macintosh:
                    os.rename(objname, "." + objname)
                    return True
        return False
    
    # roomdirで指定したフォルダにobjnameのファイルが存在するとき、
    # そのファイルに隠しファイルの属性を付与する
    # 成功: True, 失敗時False
    def give_hidden(roomdir, objname):
        cwd = os.getcwd()
        cond = give_hidden_raw(roomdir, objname)
        os.chdir(cwd)
        return cond

    def give_nothidden_raw(roomdir, objname):
        path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            os.chdir(path)
            if renpy.windows:
                if os.path.isfile(objname):
                    info = subprocess.STARTUPINFO()
                    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    info.wShowWindow = subprocess.SW_HIDE
                    result = subprocess.run(["attrib", "-H", objname], startupinfo=info)
                    return result.returncode == 0
                    return True
            elif renpy.macintosh:
                if os.path.isfile("." + objname):
                    os.rename("." + objname, objname)
                    return True
        return False
    
    # roomdirで指定したフォルダにobjnameのファイルが存在するとき、
    # そのファイルから隠しファイルの属性を取り除く
    # 成功: True, 失敗時False
    # macの場合はobjnameは、'.'無しの名前で指定
    def give_nothidden(roomdir, objname):
        cwd = os.getcwd()
        cond = give_nothidden_raw(roomdir, objname)
        os.chdir(cwd)
        return cond

    def delete_obj_room_raw(roomdir, objname):
        path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            os.chdir(path)
            if os.path.isfile(objname):
                os.remove(objname)
                return 'Ok'
            else:
                return 'NF'
        else:
            return 'NR'
    
    # roomのパスとオブジェクト名を指定してオブジェクトを削除する
    # 成功時は'OK'、オブジェクトが存在しない場合は'NF'、roomが存在しない場合は'NR'が返される
    def delete_obj_room(roomdir, objname):
        cwd = os.getcwd()
        re = delete_obj_room_raw(roomdir, objname)
        os.chdir(cwd)
        return re

    # 現在いるroomのオブジェクトを削除
    # その他はdelete_obj_room関数と同じ
    def delete_obj(objname):
        return delete_obj_room(current_room, objname)
    
    # 内部的に部屋を移動
    def move_room(roomdir):
        global current_room
        global room_prefix
        current_room = roomdir
        if roomdir == "simple room":
            room_prefix = "pr"
        else:
            room_prefix = roomdir
    
    from pathlib import Path

    # フォルダの存在を確認し、存在しない場合は新しく作る
    # baseが指すフォルダは存在していなければならない
    def check_folder_new(base, rel):
        cwd = os.getcwd()
        os.chdir(base)
        relpath = Path(os.path.normpath(rel))
        for part in relpath.parts:
            if os.path.isfile(part):
                os.remove(part)
                os.mkdir(part)
            elif not os.path.isdir(part):
                os.mkdir(part)
            os.chdir(part)

    # 現在の部屋に対応する無限ループ用のラベルの名前を返す
    def loop_label():
        return room_prefix + ".scloop"

    def check_main():
        return not os.path.isfile(os.path.join(config.basedir, main_built_flg_path))