import os
import py_compile

def compile_file(spath,sdir,tdir):
    if not spath.endswith(".py"):
        return
    dir_target = os.path.dirname(spath)
    if not os.path.exists(dir_target):
        os.mkdir(dir_target)
    tpath = str.replace(spath,sdir,tdir)
    tpath += "c"
    py_compile.compile(spath,tpath)
    pass

def compile_list(sdir,tdir):
    abs_sdir = os.path.abspath(sdir)
    abs_tdir = os.path.abspath(tdir)
    for r,ds,fs in os.walk(sdir):
        for f in fs:
            fpath = os.path.abspath(os.path.join(r,f))
            compile_file(fpath,abs_sdir,abs_tdir)
            print(r"compile file "+fpath)
    pass
    
if __name__ == "__main__":
    #compile_file(r"./1/ttt.py",r"./1",r"./2")
    compile_list(r"./1",r"./2")