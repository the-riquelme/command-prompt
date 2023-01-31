# commands
from commands import *

# prompt
command = ''
while command != 'exit':
    commands = input('/> ').split(' ')
    command = commands[0]

    if command == 'exit':
        break

    if (len(commands) >= 2):
        param = commands[1]

        if param == '':
            print('Command Invalid!')
            continue

        if len(commands) >= 3:
            param2 = commands[2]

            if command == 'rm':
                rm(param2, param)
            else:
                print('Command Invalid!')

            continue

        if command == 'dir' or command == 'ls':
            dir(param)
        if command == 'cat':
            cat(param)
        if command == 'cd':
            cd(param)
        if command == 'mkdir':
            mkdir(param)
        else:
            print('Command Invalid!')
    else:
        print('Command Invalid!')
