import os
import errno
import fcntl


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
