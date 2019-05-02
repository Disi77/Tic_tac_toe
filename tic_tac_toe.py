def print_game_field(game_state):
    '''
    Print game field.
    Example:
                 1   2   3
                --- --- ---
            1  |   |   |   |
                --- --- ---
            2  |   |   |   |
                --- --- ---
            3  |   |   |   |
                --- --- ---
    '''
    rows = len(game_state)
    columns = len(game_state[0])
    first_row = ' '*3 + columns * '  {} '
    print(first_row.format(*range(1, columns+1)))
    for x in range(rows):
        print(' '*2, ' ---' * columns)
        print(x+1, ' ', end='')
        for y in range(columns):
            print('| {} '.format(game_state[x][y]), end='')
        print('|')
    print(' '*2, ' ---' * columns)


def intro():
    print('''
==================================================
|  Welcome to Tic Tac Toe                        |
==================================================
|  Each player can place one mark (or stone)     |
|  per turn on the 3x3 grid                      |
|  The WINNER is who succeeds in placing three   |
|  of their marks in a                           |
|     --> horizontal,                            |
|     --> vertical or                            |
|     --> diagonal row                           |
|                                                |
|  Enter your move like number of row and column.|
|  Example Row 2 + Column 5 = enter 25           |
|                                                |
|                  Press ENTER to start the game |
==================================================
    ''')


def create_game_state_table(rows, columns):
    table = []
    for row in range(rows):
        row = ' ' * columns
        row = list(row)
        table.append(row)
    return table


def players_move(game_state, symbol):
    rows = len(game_state)
    columns = len(game_state)
    while True:
        players_move = input('Enter your move like number of row and column.-->  ')
        print()
        players_move = players_move.replace(' ', '').replace(',', '').strip()
        if len(players_move) == 2 and players_move.isdigit() and '0' not in players_move:
            move_r, move_c = int(players_move[0]), int(players_move[1])
            if move_r > rows or move_c > columns:
                print('Coordinates not in game field, try again.')
            elif game_state[move_r - 1][move_c - 1] == ' ':
                return move_r, move_c, symbol
            else:
                print('Coordinates not empty, try again.')
        else:
            print('Try it again')


def change_game_field(game_state, move):
    for index_r, row in enumerate(game_state):
        for index_c, column in enumerate(row):
            if index_r == (move[0] - 1) and index_c == (move[1] - 1):
                game_state[index_r][index_c] = move[2]
    return game_state


def print_separator(round, symbols):
    if round % 2 == 0:
        symbol = symbols[0]
        player = '#2'
    else:
        symbol = symbols[1]
        player = '#1'
    print('''
==================================================
|  Player {} with symbol \'{}\'                     |
==================================================
    '''.format(player, symbol))


def evaluation(game_state, symbols):
    s1_3x = symbols[0] * 3
    s2_3x = symbols[1] * 3
    transpose = list(zip(*game_state))

    # Search 'xxx' or 'ooo' in rows and columns
    for table in (game_state, transpose):
        for row in table:
            tested_row = ''
            for column in row:
                tested_row += column
            if s1_3x in tested_row:
                return symbols[0]
            elif s2_3x in tested_row:
                return symbols[1]

    # DIAG
    for row in range(len(game_state) - 3 + 1):
        for col in range(len(game_state[0]) - 3 + 1):
            tested_row = str(game_state[row][col]) + str(game_state[row+1][col+1]) + str(game_state[row+2][col+2])
            if s1_3x in tested_row:
                return symbols[0]
            elif s2_3x in tested_row:
                return symbols[1]
    for row in range(len(game_state) - 3 + 1):
        for col in range(len(game_state[0]) - 3 + 1):
            tested_row = str(game_state[row][-(1+col)]) + str(game_state[row+1][-(2+col)]) + str(game_state[row+2][-(3+col)])
            if s1_3x in tested_row:
                return symbols[0]
            elif s2_3x in tested_row:
                return symbols[1]

    # Is finding out, if is free space in game field
    for row in game_state:
        for column in row:
            if column == ' ':
                return 'game'
    else:
        return 'full field'


def field_size():
    print('Set the field size.')
    while True:
        rows = input('How many rows? From 3 to 9.  ').strip()
        if rows.isdigit() and rows != '0':
            if int(rows) in range(3, 10):
                break
    while True:
        columns = input('How many columns? From 3 to 9.  ').strip()
        if columns.isdigit() and columns != '0':
            if int(columns) in range(3, 10):
                break
    return int(rows), int(columns)


def congratulation(player, symbol):
    print('''
=======================================================
|  Congratulations, the player {} with symbol {} WON!  |
=======================================================
    '''.format(player, symbol))


def main():
    intro()
    input()
    rows, columns = field_size()
    game_state = create_game_state_table(rows, columns)
    symbols = ['O', 'X']
    round = 1
    print_game_field(game_state)

    while True:
        print_separator(round, symbols)
        # User choose
        if round % 2 == 0:
            move = players_move(game_state, symbols[0])
        else:
            move = players_move(game_state, symbols[1])

        # Write user move in game field
        game_state = change_game_field(game_state, move)
        print_game_field(game_state)

        # Evaluation
        result = evaluation(game_state, symbols)
        if result == symbols[0]:
            congratulation('#1', symbols[0])
            break
        elif result == symbols[1]:
            congratulation('#2', symbols[1])
            break
        elif result == 'full field':
            print('Nobody won.')
            break
        round += 1


main()
