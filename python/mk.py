import hashlib
import os
import sys

def make_obj(room: str, name: str):
    cwd = os.getcwd()
    os.chdir(room)
    with open(name, mode="wb") as f:
        f.write(hashlib.sha256(name.encode("utf-8")).digest())
    os.chdir(cwd)

def check_hash(objname: str) -> bool:
    with open(objname, mode="rb") as f:
        cond = f.read() == hashlib.sha256(objname.encode("utf-8")).digest()
    return cond

def __main__():
    make_obj(".", sys.argv[1])

if __name__ == "__main__":
    __main__()