# commands
from commands import *

# prompt
command = ''
while command != 'exit':
    commands = input('/> ').split(' ')
    command = commands[0]

    if command == 'exit':
        break

    if command == 'clear':
        clear()
    elif command == 'seeOS' or command == 'ver':
        seeOS()
    elif (len(commands) >= 2):
        param = commands[1]

        if param == '':
            print('Command Invalid!')
        elif len(commands) >= 3:
            param2 = commands[2]

            if command == 'rm':
                rm(param2, param)
            elif command == 'cp':
                cp(param, param2)
            elif command == 'mv':
                mv(param, param2)
            else:
                print('Command Invalid!')
        elif command == 'dir' or command == 'ls':
            dir(param)
        elif command == 'cat':
            cat(param)
        elif command == 'cd':
            cd(param)
        elif command == 'mkdir':
            mkdir(param)
        elif command == 'touch':
            touch(param)
        elif command == 'edit':
            edit(param)
        else:
            print('Command Invalid!')
    else:
        print('Command Invalid!')
