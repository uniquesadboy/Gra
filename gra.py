def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Sprawdzanie ciągów
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Sprawdzanie kolumny
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    # Sprawdzanie przekątnych
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def tic_tac_toe():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = 'X'
        game_over = False

        print("Witaj w grze Kółko i Krzyżyk!")

        while not game_over:
            print_board(board)
            row = int(input(f"Gracz {player}, wybierz wiersz (0, 1, 2): "))
            col = int(input(f"Gracz {player}, wybierz kolumnę (0, 1, 2): "))

            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print(f"Gracz {player} wygrał!")
                    game_over = True
                else:
                    player = 'O' if player == 'X' else 'X'
            else:
                print("Ta komórka jest już zajęta. Spróbuj ponownie.")

            if all(row.count(' ') == 0 for row in board) and not check_winner(board):
                print_board(board)
                print("Remis!")
                game_over = True

        decision = input("Co chcesz zrobić? (W - Wejdź do gry, K - Zakończ): ").upper()
        if decision != 'W':
            break

if __name__ == "__main__":
    tic_tac_toe()
