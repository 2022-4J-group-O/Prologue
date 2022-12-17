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
            cond = f.read() == hashlib.sha256(objname.encode("utf-8")).digest()
        return cond

    def read_room_raw(roomdir=None):
        path = ""
        if roomdir == None:
            path = os.path.join(user_dir_path, current_room)
        else:
            path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            os.chdir(path)
            return [p for p in objects if os.path.isfile(p) and check_hash(p)]
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

    def make_obj_room_raw(roomdir, objname):
        path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            os.chdir(path)
            with open(objname, 'wb') as f:
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
        current_room = roomdir