import os
import errno
import fcntl
import shutil
import platform


def dir(directory):
    if directory:
        files = os.listdir(directory)
        out = ''

        for file in files:
            out += file + ' '

        print(out)
    else:
        print('Directory not found')


def cat(path):
    try:
        if os.path.isfile(path):
            with open(path, "r") as file:
                fcntl.flock(file, fcntl.LOCK_EX)
                conteudo = file.read()
                print(conteudo)
        else:
            print('File not found')
    except FileNotFoundError:
        print(f'File "{path}" not found')
    except PermissionError:
        print(f'File "{path}" is blocked by another program')
    except OSError as e:
        if e.errno == errno.EAGAIN or e.errno == errno.EACCES:
            print(f'File "{path}" is blocked by another program')
        else:
            raise


def cd(path):
    try:
        if os.path.isdir(path):
            os.chdir(path)
        else:
            print('Directory not found')
    except FileNotFoundError:
        print(f'Directory "{path}" not found')
    except PermissionError:
        print(f'No permission to access "{path}"')


def mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f'Directory "{path}" already exists')
    except PermissionError:
        print(f'No permission to create "{path}"')
    except Exception:
        print('Command Invalid!')


def rm(path, param):
    path = os.path.abspath(path)

    if os.path.isfile(path) and (param == '-a'):
        try:
            os.remove(path)
        except PermissionError:
            print(f'Sem permissão para apagar "{path}"')
    elif os.path.isdir(path) and param == '-d':
        try:
            shutil.rmtree(path)
        except PermissionError:
            print(f'Sem permissão para apagar "{path}"')
    else:
        print(f'{path} not a file or directory')


def cp(src, dst):
    abs_src = os.path.abspath(src)
    abs_dst = os.path.abspath(dst)
    abs_dst_verification = os.path.join(abs_dst, os.path.basename(abs_src))

    if os.path.exists(abs_dst_verification):
        print(f'{abs_dst_verification} already exists')

    try:
        if os.path.isfile(abs_src):
            shutil.copy2(abs_src, abs_dst)
        else:
            print(f'{abs_src} not a file')
    except FileExistsError:
        print('File already exists in the destination')


def mv(src, dst):
    abs_src = os.path.abspath(src)
    abs_dst = os.path.abspath(dst)

    if os.path.isfile(abs_src):
        os.rename(abs_src, abs_dst)
    elif os.path.isdir(abs_src):
        os.rename(abs_src, abs_dst)
    else:
        print(f'{abs_src} not a file or directory')


def seeOS():
    print(platform.system())
    print(platform.release())


def touch(path):
    if os.path.exists(path):
        print(f"File {path} already exists.")
    else:
        with open(path, "w"):
            pass
