init python:
    import shutil
    def delete_dir_file(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            os.mkdir(path)
    
    def delete_savefile():
        delete_dir_file(os.path.join(config.basedir, "game/saves"))