# commands
from commands import *

# prompt
command = ''
while command != 'exit':
    commands = input('/> ').split(' ')
    command = commands[0]

    if command == 'exit':
        break

    if (len(commands) == 2):
        param = commands[1]

        if param == '':
            print('Command Invalid!')
            continue

        if command == 'dir':
            dir(param)
        if command == 'cat':
            cat(param)
        if command == 'cd':
            cd(param)
        else:
            print('Command Invalid!')
    else:
        print('Command Invalid!')
