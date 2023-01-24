import os


def dir(directory):
    if directory:
        files = os.listdir(directory)
        out = ''

        for file in files:
            out += file + ' '

        print(out)
    else:
        print('Directory not found')
