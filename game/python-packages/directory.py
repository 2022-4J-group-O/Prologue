import os
import pathlib
from typing import Dict, Set, Any

class Directory:
    def __init__(self, dirs: Dict[str, Any], files: Dict[str, bytes]):
        self.dirs = dirs
        self.files = files
    
    def read(fp: str):
        return Directory.read_rec(pathlib.Path(fp))

    def read_rec(fp: pathlib.Path):
        files = {item.name: item.read_bytes() for item in fp.iterdir() if item.is_file()}
        dirs = {item.name: Directory.read_rec(item) for item in fp.iterdir() if item.is_dir()}
        return Directory(dirs, files)
    
    def make(self, fp: str, relpath: str = ''):
        if relpath == '':
            path = pathlib.Path(fp)
            if path.is_file():
                path.unlink()
                path.mkdir()
            elif not path.exists():
                path.mkdir(parents=True)
            for item in self.files:
                ip = path / item
                with ip.open(mode='wb') as f:
                    f.write(self.files[item])
            for d in self.dirs:
                self.dirs[d].make(path / d)
        else:
            d = self
            rp = pathlib.Path(relpath)
            for part in rp.parts:
                d = d.dirs[part]
            d.make(fp)
    
    # fpは生成先、relpathは生成元の相対パス
    def make_file(self, fp: str, relpath: str):
        d, n = os.path.split(relpath)
        dat = self
        for part in pathlib.Path(d).parts:
            dat = dat.dirs[part]
        with open(os.path.join(fp, n), mode="wb") as f:
            f.write(dat.files[n])

    def __repr__(self):
        return f"Directory({self.dirs.__repr__()}, {self.files.__repr__()})"


def __main__():
    dire = Directory.read('../game_data/loadfile1')
    s = dire.__repr__()
    print(s)
    back: Directory = eval(s)
    print(back.__repr__())
    #back.make('./loadfile1/room1', 'room1')
    os.makedirs("./loadfile1/room1")
    back.make_file("./loadfile1/room1", 'room1/Door')

if __name__ == "__main__":
    __main__()