import os


path = input(f'Please put a path: ')
big_line = '├─────────── '
short_line_1 = '├─ '
short_line_2 = '────'


for root, dirs, files in os.walk(path):
    level = root.replace(path, '').count(os.sep)
    indent = str(level)
    if level >= 1:
        print("|" + short_line_2 * (level + 3) + f'{indent} {os.path.basename(root)}')
    else:
        print(big_line + f'{indent} {os.path.basename(root)}')
    subindent = ' ' * 10 * (level + 1)
    for f in files:
        if level >= 1:
            print('|' + ' ' * (16 + level * 2) + short_line_1 + f'{f}')
        else:
            print('|' + ' ' * 16 + short_line_1 + f'{f}')
