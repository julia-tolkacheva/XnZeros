def print_field(matrix):
    # x_header:
    print('  * * *  \t  Key pos:')
    print('*',matrix[0], matrix[1], matrix[2], '*\t - 1 2 3 -')
    print('*',matrix[3], matrix[4], matrix[5], '*\t - 4 5 6 -')
    print('*',matrix[6], matrix[7], matrix[8], '*\t - 7 8 9 -')
    print('  * * *  ')

def print_win(matrix, win):
    # x_header:
    print('  * * * ')
    print('* ', end='')
    for item in range(9):
        if item in win:
            print('\033[9;31m' + matrix[item] + '\033[0m ', end='')
        else:
            print(matrix[item], '', end='')

        if not ((item + 1) % 3):
            print('*')
            if item < 8:
                print('* ', end='')
    print('  * * * ')

def input_step(char):
    while True:
        in_str = input("Please, input position for " + char + ":")
        if not in_str.isnumeric():
            print('Input value is not numeric! Try once more!')
            continue

        pos = int(in_str) - 1
        if not (0 <= pos <= 8):
            print('Position must be between 1 and 9! Try once more!')
            continue

        y = pos // 3
        x = pos % 3
        if matrix[pos] == '.':
            return pos  # X,Y
        else:
            print('This position is busy. Try other')


def check_win_cond(matrix, char):
    #list with win coordinates
    glob = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]

    for line in glob:
        winline = ''
        for coord in line:
            winline += matrix[coord]
        #check win condition
        if winline == char*len(winline):
            return line

    #if no win condition:
    return None


matrix = list('.' * 9)

char = 'X'
step = 0
while True:
    print_field(matrix)
    p = input_step(char)
    step += 1
    matrix[p] = char
    win = check_win_cond(''.join(matrix), char)
    if win:
        print_win(matrix, win)
        print('ViCtOrY!!! \033[5;31m' + char + '\033[0m win!!')
        break
    if step >= 9:
        print('No one wins... ')
        break

    char = 'X' if char != 'X' else '0'
