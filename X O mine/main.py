import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Futuristic Tic-Tac-Toe AI")

black = (10, 10, 10)
neon_blue = (0, 255, 255)
neon_red = (255, 50, 50)
neon_green = (50, 255, 50)
white = (200, 200, 200)

mediumFont = pygame.font.Font(None, 36)
largeFont = pygame.font.Font(None, 48)
moveFont = pygame.font.Font(None, 72)

user = None
board = ttt.initial_state()
ai_turn = False

def draw_board():
    screen.fill(black)
    for i in range(1, 3):
        pygame.draw.line(screen, neon_blue, (0, i * height / 3), (width, i * height / 3), 5)
        pygame.draw.line(screen, neon_blue, (i * width / 3, 0), (i * width / 3, height), 5)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ttt.X:
                text = moveFont.render("X", True, neon_red)
            elif board[i][j] == ttt.O:
                text = moveFont.render("O", True, neon_green)
            else:
                continue
            rect = text.get_rect(center=((j + 0.5) * width / 3, (i + 0.5) * height / 3))
            screen.blit(text, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_board()
    game_over = ttt.terminal(board)
    player_turn = ttt.player(board)

    if user is None:
        x_button = pygame.Rect(width / 4, height / 2, width / 4, 50)
        o_button = pygame.Rect(2 * width / 4, height / 2, width / 4, 50)

        pygame.draw.rect(screen, neon_red, x_button)
        pygame.draw.rect(screen, neon_green, o_button)

        x_text = mediumFont.render("Play X", True, black)
        o_text = mediumFont.render("Play O", True, black)
        screen.blit(x_text, x_button.topleft)
        screen.blit(o_text, o_button.topleft)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if x_button.collidepoint(mouse):
                user = ttt.X
                time.sleep(0.2)
            elif o_button.collidepoint(mouse):
                user = ttt.O
                time.sleep(0.2)

    else:
        if user != player_turn and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                if move:
                    board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player_turn and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == ttt.EMPTY and
                        (j * width / 3 < mouse[0] < (j + 1) * width / 3) and
                        (i * height / 3 < mouse[1] < (i + 1) * height / 3)):
                        board = ttt.result(board, (i, j))

    pygame.display.flip()
    pygame.time.delay(10)  # Prevents freezing by slowing down loop slightly
