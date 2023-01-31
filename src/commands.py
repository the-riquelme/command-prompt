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
