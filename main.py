from random import randint, shuffle
import numpy as np, pygame, sys

BLOCK_SIZE = 72
board3 = []
NUM_OF_SQUARES = 9
WIDTH = NUM_OF_SQUARES * BLOCK_SIZE
HEIGHT = NUM_OF_SQUARES * BLOCK_SIZE
BORDER_SIZE = 3
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
selected_x = 10
selected_y = 10
size = 9
wrong = 0
ingame = False
startscreen = True
endscreen = False
game_done = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

board2 = [[3, 1, 0, 5, 0, 0, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 5, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]


fontname = pygame.font.match_font("times")

def write_text(surf, text, size, x, y, color):
    font = pygame.font.Font(fontname, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def render_board(board, NUM_OF_SQUARES):
    if NUM_OF_SQUARES == 9:
        SQUARE_SIZE = 72
        for c in range(NUM_OF_SQUARES):
            for r in range(NUM_OF_SQUARES):
                if c % 3 == 2 and r % 3 == 2:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 8, r * SQUARE_SIZE, BORDER_SIZE + 5, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 8, SQUARE_SIZE, BORDER_SIZE + 5))
                elif c % 3 == 2:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 8, r * SQUARE_SIZE, BORDER_SIZE + 5, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 3, SQUARE_SIZE, BORDER_SIZE))
                elif r % 3 == 2:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 3, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 8, SQUARE_SIZE, BORDER_SIZE + 5))

                else:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 3, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 3, SQUARE_SIZE, BORDER_SIZE))
                if board[r][c] != 0:
                    write_text(screen, str(board[r][c]), 30, c * SQUARE_SIZE + 35, r * SQUARE_SIZE + 23, BLACK)
    elif NUM_OF_SQUARES == 4:
        SQUARE_SIZE = 162
        for c in range(NUM_OF_SQUARES):
            for r in range(NUM_OF_SQUARES):
                if c % 2 == 1 and r % 2 == 1:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 8, r * SQUARE_SIZE, BORDER_SIZE + 5, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 8, SQUARE_SIZE, BORDER_SIZE + 5))
                elif c % 2 == 1:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 8, r * SQUARE_SIZE, BORDER_SIZE + 5, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 3, SQUARE_SIZE, BORDER_SIZE))
                elif r % 2 == 1:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 3, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 8, SQUARE_SIZE, BORDER_SIZE + 5))

                else:
                    pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                    pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE + SQUARE_SIZE - 3, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 3, SQUARE_SIZE, BORDER_SIZE))
                if board[r][c] != 0:
                    write_text(screen, str(board[r][c]), 50, c * SQUARE_SIZE + 75, r * SQUARE_SIZE + 50, BLACK)


    pygame.display.update()



def process_event(board, size):
    global selected_x, selected_y, wrong
    temp_board = board.copy()

    if size == 9:
        box_size = 72
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_x, selected_y = pygame.mouse.get_pos()
                selected_x = selected_x // box_size
                selected_y = selected_y // box_size
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    backtrack(board, size)
                if event.key == pygame.K_7 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 \
                        or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 \
                        or event.key == pygame.K_8 or event.key == pygame.K_9:
                    if selected_y == 10:
                        selected_y = int(pygame.key.name(event.key))-1
                    elif selected_x == 10:
                        selected_x = int(pygame.key.name(event.key))-1
                    elif board[selected_y][selected_x] != 0:
                        selected_x = 10
                        selected_y = 10
                    elif valid_board(board, int(pygame.key.name(event.key)), selected_y, selected_x, len(board)):
                        temp_board[selected_y][selected_x] = int(pygame.key.name(event.key))
                        if backtrack(temp_board, size) == True:
                            board[selected_y][selected_x] = int(pygame.key.name(event.key))
                            selected_x = 10
                            selected_y = 10
                        else:
                            wrong += 1
                            temp_board[selected_y][selected_x] = 0
                    else:
                        wrong += 1



            render_board(board, size)
            if event.type == pygame.QUIT:
                sys.exit()

    elif size == 4:
        box_size = 162
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_x, selected_y = pygame.mouse.get_pos()
                selected_x = selected_x // box_size
                selected_y = selected_y // box_size
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    backtrack(board, size)
                if event.key == pygame.K_4 or event.key == pygame.K_1 or event.key == pygame.K_2 or \
                        event.key == pygame.K_3:
                    if selected_y == 10:
                        selected_y = int(pygame.key.name(event.key)) - 1
                    elif selected_x == 10:
                        selected_x = int(pygame.key.name(event.key)) - 1
                    elif board[selected_y][selected_x] != 0:
                        selected_x = 10
                        selected_y = 10
                    elif valid_board(board, int(pygame.key.name(event.key)), selected_y, selected_x, len(board)):
                        temp_board[selected_y][selected_x] = int(pygame.key.name(event.key))
                        if backtrack(temp_board, size) == True:
                            board[selected_y][selected_x] = int(pygame.key.name(event.key))
                            selected_x = 10
                            selected_y = 10
                        else:
                            wrong += 1
                            temp_board[selected_y][selected_x] = 0
                    else:
                        wrong += 1

            render_board(board, 4)
            if event.type == pygame.QUIT:
                sys.exit()


def game_menu():
    global startscreen, ingame, size, board3
    board = [[3, 1, 0, 5, 0, 0, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 'S', 'U', 'D', 'O', 'K', 'U', 8, 0],
              [9, 0, 0, 0, 0, 0, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    SQUARE_SIZE = 72
    for c in range(NUM_OF_SQUARES):
        for r in range(NUM_OF_SQUARES):
            if c % 3 == 2 and r % 3 == 2:
                pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE + SQUARE_SIZE - 8, r * SQUARE_SIZE, BORDER_SIZE + 5, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 8, SQUARE_SIZE, BORDER_SIZE + 5))
            elif c % 3 == 2:
                pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE + SQUARE_SIZE - 8, r * SQUARE_SIZE, BORDER_SIZE + 5, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 3, SQUARE_SIZE, BORDER_SIZE))
            elif r % 3 == 2:
                pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE + SQUARE_SIZE - 3, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 8, SQUARE_SIZE, BORDER_SIZE + 5))

            else:
                pygame.draw.rect(screen, WHITE, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, BORDER_SIZE))
                pygame.draw.rect(screen, BLACK, (c * SQUARE_SIZE, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE + SQUARE_SIZE - 3, r * SQUARE_SIZE, BORDER_SIZE, SQUARE_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE - 3, SQUARE_SIZE, BORDER_SIZE))
            if board[r][c] != 0:
                write_text(screen, str(board[r][c]), 30, c * SQUARE_SIZE + 35, r * SQUARE_SIZE + 23, BLACK)
    pygame.draw.rect(screen, RED, (222, 400, 200, 75))
    pygame.draw.rect(screen, RED, (222, 525, 200, 75))
    write_text(screen, "Play 4X4", 30, 321, 420, WHITE)
    write_text(screen, "Play 9X9", 30, 321, 545, WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 222 and mouse_x < 422 and mouse_y > 400 and mouse_y < 475:
                size = 4
                make_board(size)
                make_valid_sudoku(board3, size)
                random_remove(board3, 9)
                ingame = True
                startscreen = False

            elif mouse_x > 222 and mouse_x < 422 and mouse_y > 525 and mouse_y < 600:
                size = 9
                make_board(size)
                make_valid_sudoku(board3, size)
                random_remove(board3, 40)
                ingame = True
                startscreen = False

    pygame.display.update()


def end_menu():
    global screen, startscreen, endscreen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (222, 525, 200, 75))
    write_text(screen, "Congratulations!", 50, 321, 120, WHITE)
    write_text(screen, "You finished", 30, 321, 220, WHITE)
    write_text(screen, " the sudoku with ", 30, 321, 320, WHITE)
    write_text(screen,"only " + str(wrong) + " errors", 30, 321, 420, WHITE)
    write_text(screen, "Play Again", 30, 321, 545, WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 222 and mouse_x < 422 and mouse_y > 525 and mouse_y < 600:
                startscreen = True
                endscreen = False

    pygame.display.update()


def find_open(board):
    for y_index, row in enumerate(board):
        for x_index, value in enumerate(row):
            if value == 0:
                return y_index, x_index

    return False


def valid_board(board, num, row, col, size):
    #check row
    for i in range(len(board[row])):
        if board[row][i] == num and col != i:
            return False

    #check col
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    if size == 9:
        y_big_box = row // 3
        x_big_box = col // 3

        begin_y_index = y_big_box*3
        begin_x_index = x_big_box*3
        for i in range(3):
            for j in range(3):
                if (board[begin_y_index + j][begin_x_index + i] == num and begin_y_index + j != row
                        and begin_x_index + i != col):
                    return False
    elif size == 4:
        y_big_box = row // 2
        x_big_box = col // 2

        begin_y_index = y_big_box*2
        begin_x_index = x_big_box*2
        for i in range(2):
            for j in range(2):
                if (board[begin_y_index + j][begin_x_index + i] == num and begin_y_index + j != row
                        and begin_x_index + i != col):
                    return False

    return True


def backtrack(board, size):

    open_spots = find_open(board)
    if open_spots == False:
        return True
    else:
        row, col = open_spots

    counter = 1
    while counter <= size:
        if valid_board(board, counter, row, col, size):
            board[row][col] = counter

            if backtrack(board, size) == True:
                return True

            board[row][col] = 0

        counter += 1
    return False


def make_board(size):
    global board3
    board3 = np.zeros((size, size), dtype=int)

def make_valid_sudoku(board, size):
    counter = 0
    numbers = []
    if size == 9:
        for i in range(1, 10):
            numbers.append(i)
        while counter < 81:
            row = counter//9
            col = counter % 9
            if board[row][col] == 0:
                shuffle(numbers)
                for value in numbers:
                    if valid_board(board, value, row, col, 9):
                        board[row][col] = value
                        open_spots = find_open(board)
                        if open_spots == False:
                            return True
                        else:
                            if make_valid_sudoku(board, 9):
                                return True
                break
            counter += 1
        board[row][col]=0
        return False
    elif size == 4:
        for i in range(1, 5):
            numbers.append(i)
        while counter < 16:
            row = counter // 4
            col = counter % 4
            if board[row][col] == 0:
                shuffle(numbers)
                for value in numbers:
                    if valid_board(board, value, row, col, 4):
                        board[row][col] = value
                        open_spots = find_open(board)
                        if open_spots == False:
                            return True
                        else:
                            if make_valid_sudoku(board, 4):
                                return True
                break
            counter += 1
        board[row][col] = 0

def remove_values(board, row, col):
    if board[row][col] != 0:
        board[row][col] = 0
        return True
    return False


def random_remove(board, count):
    counter = 0
    while counter < count:
        row = randint(0, len(board[0]) - 1)
        col = randint(0, len(board) - 1)
        if remove_values(board, row, col):
            counter += 1


def main():
    global ingame, startscreen, endscreen
    pygame.init()
    pygame.display.set_caption("SUDOKU")
    while not game_done:
        if startscreen:
            game_menu()
        if ingame:
            process_event(board3, size)
            open_spots = find_open(board3)
            if open_spots == False:
                pygame.time.wait(3000)
                ingame = False
                endscreen = True
        if endscreen:
            end_menu()

if __name__ == '__main__':
    main()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
