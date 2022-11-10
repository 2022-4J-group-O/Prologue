define user_dir_path = os.path.join(config.basedir, user_directory)

init python :
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
    
    # roomのパスを指定してオブジェクトを読み込む
    # 読み込み可能なオブジェクトはoption.rpyのobjects定数で指定する
    # roomを指定しない場合現在いるroomのオブジェクトを読み込む
    def read_room(roomdir=None, maintain_cwd=False):
        path = ""
        if roomdir == None:
            path = os.path.join(user_dir_path, current_room)
        else:
            path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            if maintain_cwd:
                stack = os.getcwd()
                os.chdir(path)
                l = [p for p in objects if os.path.isfile(p)]
                os.chdir(stack)
                return l
            else:
                os.chdir(path)
                return [p for p in objects if os.path.isfile(p)]
        else:
            return list()
    
    # roomのパスとオブジェクト名を指定してオブジェクトを作成する
    # 読み込み可能でなくてもOK
    # 成功時にTrue、失敗時にFalseを返す(すでにオブジェクトが存在していても成功)
    def make_obj_room(roomdir, objname, maintain_cwd=False):
        path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            if maintain_cwd:
                stack = os.getcwd()
                os.chdir(path)
                open(objname, 'w').close()
                os.chdir(stack)
            else:
                os.chdir(path)
                open(objname, 'w').close()
            return True
        else:
            return False
    
    # 現在いるルームにオブジェクトを作成
    # 対象room以外はmake_obj_room関数と同じ動作
    def make_obj(objname, maintain_cwd=False):
        return make_obj_room(current_room, objname, maintain_cwd)
    
    # roomのパスとオブジェクト名を指定してオブジェクトを削除する
    # 成功時は'OK'、オブジェクトが存在しない場合は'NF'、roomが存在しない場合は'NR'が返される
    def delete_obj_room(roomdir, objname, maintain_cwd=False):
        path = os.path.join(user_dir_path, roomdir)
        if os.path.isdir(path):
            if maintain_cwd:
                stack = os.getcwd()
                os.chdir(path)
                if os.path.isfile(objname):
                    os.remove(objname)
                    os.chdir(stack)
                    return 'Ok'
                else:
                    os.chdir(stack)
                    return 'NF'
            else:
                os.chdir(path)
                if os.path.isfile(objname):
                    os.remove(objname)
                    return 'Ok'
                else:
                    return 'NF'
        else:
            return 'NR'
    
    # 現在いるroomのオブジェクトを削除
    # その他はdelete_obj_room関数と同じ
    def delete_obj(objname, maintain_cwd=False):
        return delete_obj_room(current_room, objname, maintain_cwd)
    
    # 内部的に部屋を移動
    def move_room(roomdir):
        global current_room
        current_room = roomdir