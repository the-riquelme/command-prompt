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
        directory = commands[1]

        if command == 'dir':
            dir(directory)
    else:
        print('Command Invalid!')
