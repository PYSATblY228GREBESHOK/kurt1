import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_board(board):
    size = len(board)
    print("\n   " + " | ".join(str(i) for i in range(size)))
    print("  " + "---+" * (size - 1) + "---")
    for i in range(size):
        print(f"{i}  " + " | ".join(board[i]))
        if i < size - 1:
            print("  " + "---+" * (size - 1) + "---")

def check_win(board, symbol):
    size = len(board)

    # Проверка строк
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Проверка столбцов
    for col in range(size):
        if all(board[row][col] == symbol for row in range(size)):
            return True

    # Проверка диагоналей
    if all(board[i][i] == symbol for i in range(size)):
        return True
    if all(board[i][size - 1 - i] == symbol for i in range(size)):
        return True

    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board, symbol):
    size = len(board)
    while True:
        try:
            x = int(input("Введите номер строки: "))
            y = int(input("Введите номер столбца: "))
            if 0 <= x < size and 0 <= y < size:
                if board[x][y] == ' ':
                    board[x][y] = symbol
                    return
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Координаты вне диапазона!")
        except ValueError:
            print("Введите числа!")

def bot_move(board, symbol):
    size = len(board)
    empty_cells = [(x, y) for x in range(size) for y in range(size) if board[x][y] == ' ']
    if empty_cells:
        x, y = random.choice(empty_cells)
        board[x][y] = symbol
        print(f"\nБот сделал ход в ({x}, {y})")

def play_game():
    clear_screen()
    print("=== КРЕСТИКИ-НОЛИКИ ===")

    # Ввод размера поля
    while True:
        try:
            size = int(input("Введите размер поля (например, 3 для 3x3): "))
            if size >= 3:
                break
            else:
                print("Минимальный размер поля — 3!")
        except ValueError:
            print("Введите число!")

    # Выбор режима игры
    print("\nВыберите режим игры:")
    print("1 - Игрок против Игрока")
    print("2 - Игрок против Бота")
    mode = input("Ваш выбор (1/2): ").strip()

    # Создаём пустое поле
    board = create_board(size)

    # Определяем, кто ходит первым
    current_symbol = random.choice(['X', 'O'])
    print(f"\nПервым ходит: {current_symbol}")

    # Основной цикл игры
    game_over = False
    while not game_over:
        clear_screen()
        print_board(board)
        print(f"\nХод игрока '{current_symbol}'")

        if mode == '2' and current_symbol == 'O':
            bot_move(board, current_symbol)
        else:
            player_move(board, current_symbol)

        if check_win(board, current_symbol):
            clear_screen()
            print_board(board)
            print(f"\nПобедил игрок '{current_symbol}'! 🎉")
            game_over = True
        elif check_draw(board):
            clear_screen()
            print_board(board)
            print("\nНичья! 🤝")
            game_over = True
        else:
            current_symbol = 'O' if current_symbol == 'X' else 'X'

def main():
    while True:
        play_game()
        again = input("\nХотите сыграть ещё раз? (y/n): ").strip().lower()
        if again != 'y':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
