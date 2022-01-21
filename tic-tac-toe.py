import random
import pygame
import os
WIDTH, HEIGHT = 1400, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tic tac toe")
Icon = pygame.image.load(
    os.path.join('pack/iconp.png'))
pygame.display.set_icon(Icon)
BORD_NOR = pygame.image.load(
    os.path.join('pack', 'bord.png'))
BORD_NOR = pygame.transform.scale(BORD_NOR, (700, 700))
X_NORMAL = pygame.image.load(
    os.path.join('pack/X_normal.png'))
X_NORMAL = pygame.transform.scale(X_NORMAL, (170, 170))
O_NORMAL = pygame.image.load(
    os.path.join('pack/O_normal.png'))
O_NORMAL = pygame.transform.scale(O_NORMAL, (170, 170))
X_TURN = pygame.image.load(
    os.path.join('pack/X_turn.png'))
X_TURN = pygame.transform.scale(X_TURN, (170, 170))
O_TURN = pygame.image.load(
    os.path.join('pack/O_turn.png'))
O_TURN = pygame.transform.scale(O_TURN, (170, 170))
LINE_WIN_HO = pygame.image.load(
    os.path.join('pack/line_norml.png'))
LINE_WIN_HO = pygame.transform.scale(LINE_WIN_HO, (570, 10))
LINE_WIN_VE = pygame.image.load(
    os.path.join('pack/line_norml.png'))
LINE_WIN_VE = pygame.transform.scale(LINE_WIN_VE, (10, 570))
LINE_WIN_BE = pygame.image.load(
    os.path.join('pack/line_norml.png'))
LINE_WIN_BE = pygame.transform.scale(LINE_WIN_BE, (700, 10))
LINE_WIN_BE = pygame.transform.rotate(LINE_WIN_BE, 45)
LINE_WIN_BV = pygame.image.load(
    os.path.join('pack/line_norml.png'))
LINE_WIN_BV = pygame.transform.scale(LINE_WIN_BV, (700, 10))
LINE_WIN_BV = pygame.transform.rotate(LINE_WIN_BV, 135)
RANDOM_NUMBER = 0
FPS = 60
BACKGROUND = (255, 255, 255)
WIN.fill(BACKGROUND)
WIN.blit(BORD_NOR, (1, 10))

first = pygame.draw.rect(WIN, (BACKGROUND), (1,10,233,231))
second = pygame.draw.rect(WIN, (BACKGROUND), (241,10,226,231))
third = pygame.draw.rect(WIN, (BACKGROUND), (474,10,227,231))
fourth = pygame.draw.rect(WIN, (BACKGROUND), (1,247,233,227))
fifth = pygame.draw.rect(WIN, (BACKGROUND), (241,247,226,227))
sixth = pygame.draw.rect(WIN, (BACKGROUND), (474,247,227,227))
seventh = pygame.draw.rect(WIN, (BACKGROUND), (1,480,233,231))
eighth = pygame.draw.rect(WIN, (BACKGROUND), (241,480,226,231))
ninth = pygame.draw.rect(WIN, (BACKGROUND), (474,480,227,231))

def main():
    point_X = 0
    point_O = 0
    END = 0
    TURN = 1
    ST1 = 1
    ST2 = 1
    ST3 = 1
    ST4 = 1
    ST5 = 1
    ST6 = 1
    ST7 = 1
    ST8 = 1
    ST9 = 1
    ST10 = 1
    ST11 = 1
    ST12 = 1
    ST13 = 1
    ST14 = 1
    ST15 = 1
    ST16 = 1
    PLACE_1 = 0
    PLACE_2 = 0
    PLACE_3 = 0
    PLACE_4 = 0
    PLACE_5 = 0
    PLACE_6 = 0
    PLACE_7 = 0
    PLACE_8 = 0
    PLACE_9 = 0
    AGAINS_COMPUTER = 0
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        RESET_BUTTON = pygame.image.load(
            os.path.join('pack/reset.png'))
        RESET_BUTTON = pygame.transform.scale(RESET_BUTTON, (75, 75))
        RESET_BUTTON = pygame.transform.rotate(RESET_BUTTON, 200)
        RESET_BUTTON = WIN.blit(RESET_BUTTON, (760, 10))
        pos = pygame.mouse.get_pos()
        KEY = pygame.key.get_pressed()

        if KEY[pygame.K_c] or AGAINS_COMPUTER == 1:
            AGAINS_COMPUTER = 1
            print("Against the computer mode")

        def line():
            if PLACE_1 == 1 and PLACE_2 == 1 and PLACE_3 == 1:
                WIN.blit(LINE_WIN_HO, (64, 120))
                pygame.display.update()
            if PLACE_4 == 1 and PLACE_5 == 1 and PLACE_6 == 1:
                WIN.blit(LINE_WIN_HO, (64, 360))
                pygame.display.update()
            if PLACE_7 == 1 and PLACE_8 == 1 and PLACE_9 == 1:
                WIN.blit(LINE_WIN_HO, (64, 580))
                pygame.display.update()

            if PLACE_1 == 1 and PLACE_4 == 1 and PLACE_7 == 1:
                WIN.blit(LINE_WIN_VE, (110, 70))
                pygame.display.update()
            if PLACE_2 == 1 and PLACE_5 == 1 and PLACE_8 == 1:
                WIN.blit(LINE_WIN_VE, (350, 70))
                pygame.display.update()
            if PLACE_3 == 1 and PLACE_6 == 1 and PLACE_9 == 1:
                WIN.blit(LINE_WIN_VE, (580, 70))
                pygame.display.update()
                
            if PLACE_1 == 1 and PLACE_5 == 1 and PLACE_9 == 1:
                WIN.blit(LINE_WIN_BV, (107, 113))
                pygame.display.update()
            if PLACE_3 == 1 and PLACE_5 == 1 and PLACE_7 == 1:
                WIN.blit(LINE_WIN_BE, (93, 120))
                pygame.display.update()

            if PLACE_1 == 2 and PLACE_2 == 2 and PLACE_3 == 2:
                WIN.blit(LINE_WIN_HO, (64, 120))
                pygame.display.update()
            if PLACE_4 == 2 and PLACE_5 == 2 and PLACE_6 == 2:
                WIN.blit(LINE_WIN_HO, (64, 360))
                pygame.display.update()
            if PLACE_7 == 2 and PLACE_8 == 2 and PLACE_9 == 2:
                WIN.blit(LINE_WIN_HO, (64, 580))
                pygame.display.update()

            if PLACE_1 == 2 and PLACE_4 == 2 and PLACE_7 == 2:
                WIN.blit(LINE_WIN_VE, (110, 70))
                pygame.display.update()
            if PLACE_2 == 2 and PLACE_5 == 2 and PLACE_8 == 2:
                WIN.blit(LINE_WIN_VE, (350, 70))
                pygame.display.update()
            if PLACE_3 == 2 and PLACE_6 == 2 and PLACE_9 == 2:
                WIN.blit(LINE_WIN_VE, (580, 70))
                pygame.display.update()

            if PLACE_1 == 2 and PLACE_5 == 2 and PLACE_9 == 2:
                WIN.blit(LINE_WIN_BV, (107, 113))
                pygame.display.update()
            if PLACE_3 == 2 and PLACE_5 == 2 and PLACE_7 == 2:
                WIN.blit(LINE_WIN_BE, (93, 120))
                pygame.display.update()

        if PLACE_1 == 1 and PLACE_2 == 1 and PLACE_3 == 1:
            END = 1
            line()
        if PLACE_4 == 1 and PLACE_5 == 1 and PLACE_6 == 1:
            END = 1
            line()
        if PLACE_7 == 1 and PLACE_8 == 1 and PLACE_9 == 1:
            END = 1
            line()
        if PLACE_1 == 1 and PLACE_4 == 1 and PLACE_7 == 1:
            END = 1
            line()
        if PLACE_2 == 1 and PLACE_5 == 1 and PLACE_8 == 1:
            END = 1
            line()
        if PLACE_3 == 1 and PLACE_6 == 1 and PLACE_9 == 1:
            END = 1
            line()
        if PLACE_1 == 1 and PLACE_5 == 1 and PLACE_9 == 1:
            END = 1
            line()
        if PLACE_3 == 1 and PLACE_5 == 1 and PLACE_7 == 1:
            END = 1
            line()
        if PLACE_1 == 2 and PLACE_2 == 2 and PLACE_3 == 2:
            END = 2
            line()
        if PLACE_4 == 2 and PLACE_5 == 2 and PLACE_6 == 2:
            END = 2
            line()
        if PLACE_7 == 2 and PLACE_8 == 2 and PLACE_9 == 2:
            END = 2
            line()
        if PLACE_1 == 2 and PLACE_4 == 2 and PLACE_7 == 2:
            END = 2
            line()
        if PLACE_2 == 2 and PLACE_5 == 2 and PLACE_8 == 2:
            END = 2
            line()
        if PLACE_3 == 2 and PLACE_6 == 2 and PLACE_9 == 2:
            END = 2
            line()
        if PLACE_1 == 2 and PLACE_5 == 2 and PLACE_9 == 2:
            END = 2
            line()
        if PLACE_3 == 2 and PLACE_5 == 2 and PLACE_7 == 2:
            END = 2
            line()

        if PLACE_1 == 1 and PLACE_2 == 1 and PLACE_3 == 1 and ST16 == 1:
            point_X += 1
            ST16 = 0
        if not PLACE_1 == 1 and PLACE_2 == 1 and PLACE_3 == 1:
            ST16 = 1
        if PLACE_4 == 1 and PLACE_5 == 1 and PLACE_6 == 1 and ST15 == 1:
            point_X += 1
            ST15 = 0
        if not PLACE_4 == 1 and PLACE_5 == 1 and PLACE_6 == 1:
            ST15 = 1
        if PLACE_7 == 1 and PLACE_8 == 1 and PLACE_9 == 1 and ST14 == 1:
            point_X += 1
            ST14 = 0
        if not PLACE_7 == 1 and PLACE_8 == 1 and PLACE_9 == 1:
            ST14 = 1
        if PLACE_1 == 1 and PLACE_4 == 1 and PLACE_7 == 1 and ST13 == 1:
            point_X += 1
            ST13 = 0
        if not PLACE_1 == 1 and PLACE_4 == 1 and PLACE_7 == 1:
            ST13 = 1
        if PLACE_2 == 1 and PLACE_5 == 1 and PLACE_8 == 1 and ST12 == 1:
            point_X += 1
            ST12 = 0
        if not PLACE_2 == 1 and PLACE_5 == 1 and PLACE_8 == 1:
            ST12 = 1
        if PLACE_3 == 1 and PLACE_6 == 1 and PLACE_9 == 1 and ST11 == 1:
            point_X += 1
            ST11 = 0
        if not PLACE_3 == 1 and PLACE_6 == 1 and PLACE_9 == 1:
            ST11 = 1
        if PLACE_1 == 1 and PLACE_5 == 1 and PLACE_9 == 1 and ST10 == 1:
            point_X += 1
            ST10 = 0
        if not PLACE_1 == 1 and PLACE_5 == 1 and PLACE_9 == 1:
            ST10 = 1
        if PLACE_3 == 1 and PLACE_5 == 1 and PLACE_7 == 1 and ST9 == 1:
            point_X += 1
            ST9 = 0
        if not PLACE_3 == 1 and PLACE_5 == 1 and PLACE_7 == 1:
            ST9 = 1

        if PLACE_1 == 2 and PLACE_2 == 2 and PLACE_3 == 2 and ST8 == 1:
            point_O += 1
            ST8 = 0
        if not PLACE_1 == 2 and PLACE_2 == 2 and PLACE_3 == 2:
            ST8 = 1
        if PLACE_4 == 2 and PLACE_5 == 2 and PLACE_6 == 2 and ST7 == 1:
            point_O += 1
            ST7 = 0
        if not PLACE_4 == 2 and PLACE_5 == 2 and PLACE_6 == 2:
            ST7 = 1
        if PLACE_7 == 2 and PLACE_8 == 2 and PLACE_9 == 2 and ST6 == 1:
            point_O += 1
            ST6 = 0
        if not PLACE_7 == 2 and PLACE_8 == 2 and PLACE_9 == 2:
            ST6 = 1
        if PLACE_1 == 2 and PLACE_4 == 2 and PLACE_7 == 2 and ST5 == 1:
            point_O += 1
            ST5 = 0
        if not PLACE_1 == 2 and PLACE_4 == 2 and PLACE_7 == 2:
            ST5 = 1
        if PLACE_2 == 2 and PLACE_5 == 2 and PLACE_8 == 2 and ST4 == 1:
            point_O += 1
            ST4 = 0
        if not PLACE_2 == 2 and PLACE_5 == 2 and PLACE_8 == 2:
            ST4 = 1
        if PLACE_3 == 2 and PLACE_6 == 2 and PLACE_9 == 2 and ST3 == 1:
            point_O += 1
            ST3 = 0
        if not PLACE_3 == 2 and PLACE_6 == 2 and PLACE_9 == 2:
            ST3 = 1
        if PLACE_1 == 2 and PLACE_5 == 2 and PLACE_9 == 2 and ST2 == 1:
            point_O += 1
            ST2 = 0
        if not PLACE_1 == 2 and PLACE_5 == 2 and PLACE_9 == 2:
            ST2 = 1
        if PLACE_3 == 2 and PLACE_5 == 2 and PLACE_7 == 2 and ST1 == 1:
            point_O += 1
            ST1 = 1
        if not PLACE_3 == 2 and PLACE_5 == 2 and PLACE_7 == 2:
            ST1 = 1
        if TURN == 1:
            WIN.blit(X_TURN, (1000, 100))
            pygame.display.update()
        if TURN == 0:
            WIN.blit(O_TURN, (1000, 100))
            pygame.display.update()

        if AGAINS_COMPUTER == 1 and END == 0 and TURN == 1:
            RANDOM_NUMBER1 = random.randrange(0, 100)
            RANDOM_NUMBER = random.randrange(0, 9)
            if RANDOM_NUMBER1 < 75:
                
                continue
            if RANDOM_NUMBER1 > 75 or A_END == 1:
                A_END = 0
                if RANDOM_NUMBER == 1:
                    if PLACE_1 == 0:
                        PLACE_1 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 2:
                    if PLACE_2 == 0:
                        PLACE_2 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 3:
                    if PLACE_3 == 0:
                        PLACE_3 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 4:
                    if PLACE_4 == 0:
                        PLACE_4 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 5:
                    if PLACE_5 == 0:
                        PLACE_5 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 6:
                    if PLACE_6 == 0:
                        PLACE_6 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 7:
                    if PLACE_7 == 0:
                        PLACE_7 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 8:
                    if PLACE_8 == 0:
                        PLACE_8 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue
                if RANDOM_NUMBER == 9:
                    if PLACE_9 == 0:
                        PLACE_9 = 1
                        TURN = 0
                    else:
                        RANDOM_NUMBER = random.randrange(0,9)
                        continue

        if KEY and END == 0:
            if KEY[pygame.K_KP_7] and PLACE_1 == 0:
                if TURN == 1:
                    PLACE_1 = 1
                    TURN = 0
                else:
                    PLACE_1 = 2
                    TURN = 1
            if KEY[pygame.K_KP_8] and PLACE_2 == 0:
                if TURN == 1:
                    PLACE_2 = 1
                    TURN = 0
                else:
                    PLACE_2 = 2
                    TURN = 1
            if KEY[pygame.K_KP_9] and PLACE_3 == 0:
                if TURN == 1:
                    PLACE_3 = 1
                    TURN = 0
                else:
                    PLACE_3 = 2
                    TURN = 1
            if KEY[pygame.K_KP_4] and PLACE_4 == 0:
                if TURN == 1:
                    PLACE_4 = 1
                    TURN = 0
                else:
                    PLACE_4 = 2
                    TURN = 1
            if KEY[pygame.K_KP_5] and PLACE_5 == 0:
                if TURN == 1:
                    PLACE_5 = 1
                    TURN = 0
                else:
                    PLACE_5 = 2
                    TURN = 1
            if KEY[pygame.K_KP_6] and PLACE_6 == 0:
                if TURN == 1:
                    PLACE_6 = 1
                    TURN = 0
                else:
                    PLACE_6 = 2
                    TURN = 1
            if KEY[pygame.K_KP_1] and PLACE_7 == 0:
                if TURN == 1:
                    PLACE_7 = 1
                    TURN = 0
                else:
                    PLACE_7 = 2
                    TURN = 1
            if KEY[pygame.K_KP_2] and PLACE_8 == 0:
                if TURN == 1:
                    PLACE_8 = 1
                    TURN = 0
                else:
                    PLACE_8 = 2
                    TURN = 1
            if KEY[pygame.K_KP_3] and PLACE_9 == 0:
                if TURN == 1:
                    PLACE_9 = 1
                    TURN = 0
                else:
                    PLACE_9 = 2
                    TURN = 1
        if KEY[pygame.K_q]:
            break

        if event.type == pygame.MOUSEBUTTONUP and END == 0:
            if first.collidepoint(pos) and PLACE_1 == 0:
                if TURN == 1:
                    PLACE_1 = 1
                    TURN = 0
                else:
                    PLACE_1 = 2
                    TURN = 1
            if second.collidepoint(pos) and PLACE_2 == 0:
                if TURN == 1:
                    PLACE_2 = 1
                    TURN = 0
                else:
                    PLACE_2 = 2
                    TURN = 1
            if third.collidepoint(pos) and PLACE_3 == 0:
                if TURN == 1:
                    PLACE_3 = 1
                    TURN = 0
                else:
                    PLACE_3 = 2
                    TURN = 1
            if fourth.collidepoint(pos) and PLACE_4 == 0:
                if TURN == 1:
                    PLACE_4 = 1
                    TURN = 0
                else:
                    PLACE_4 = 2
                    TURN = 1
            if fifth.collidepoint(pos) and PLACE_5 == 0:
                if TURN == 1:
                    PLACE_5 = 1
                    TURN = 0
                else:
                    PLACE_5 = 2
                    TURN = 1
            if sixth.collidepoint(pos) and PLACE_6 == 0:
                if TURN == 1:
                    PLACE_6 = 1
                    TURN = 0
                else:
                    PLACE_6 = 2
                    TURN = 1
            if seventh.collidepoint(pos) and PLACE_7 == 0:
                if TURN == 1:
                    PLACE_7 = 1
                    TURN = 0
                else:
                    PLACE_7 = 2
                    TURN = 1
            if eighth.collidepoint(pos) and PLACE_8 == 0:
                if TURN == 1:
                    PLACE_8 = 1
                    TURN = 0
                else:
                    PLACE_8 = 2
                    TURN = 1
            if ninth.collidepoint(pos) and PLACE_9 == 0:
                if TURN == 1:
                    PLACE_9 = 1
                    TURN = 0
                else:
                    PLACE_9 = 2
                    TURN = 1
        if event.type == pygame.MOUSEBUTTONUP and RESET_BUTTON.collidepoint(pos) and RESET_B == 1 or KEY[pygame.K_r] and RESET_B == 1:
            RESET_B = 0
            END = 0
            TURN = 1
            ST1 = 1
            ST2 = 1
            ST3 = 1
            ST4 = 1
            ST5 = 1
            ST6 = 1
            ST7 = 1
            ST8 = 1
            ST9 = 1
            ST10 = 1
            ST11 = 1
            ST12 = 1
            ST13 = 1
            ST14 = 1
            ST15 = 1
            ST16 = 1
            PLACE_1 = 0
            PLACE_2 = 0
            PLACE_3 = 0
            PLACE_4 = 0
            PLACE_5 = 0
            PLACE_6 = 0
            PLACE_7 = 0
            PLACE_8 = 0
            PLACE_9 = 0
            WIN.fill(BACKGROUND)
            WIN.blit(BORD_NOR, (1, 10))
            continue
        if not event.type == pygame.MOUSEBUTTONUP or KEY[pygame.K_r]:
            RESET_B = 1

        if PLACE_1 == 1:
            WIN.blit(X_NORMAL, (30, 40))
            line()
        if PLACE_1 == 2:
            WIN.blit(O_NORMAL, (30, 40))
            line()
        if PLACE_2 == 1:
            WIN.blit(X_NORMAL, (270, 40))
            line()
        if PLACE_2 == 2:
            WIN.blit(O_NORMAL, (270, 40))
            line()
        if PLACE_3 == 1:
            WIN.blit(X_NORMAL, (500, 40))
            line()
        if PLACE_3 == 2:
            WIN.blit(O_NORMAL, (500, 40))
            line()
        if PLACE_4 == 1:
            WIN.blit(X_NORMAL, (30, 280))
            line()
        if PLACE_4 == 2:
            WIN.blit(O_NORMAL, (30, 280))
            line()
        if PLACE_5 == 1:
            WIN.blit(X_NORMAL, (270, 280))
            line()
        if PLACE_5 == 2:
            WIN.blit(O_NORMAL, (270, 280))
            line()
        if PLACE_6 == 1:
            WIN.blit(X_NORMAL, (500, 280))
            line()
        if PLACE_6 == 2:
            WIN.blit(O_NORMAL, (500, 280))
            line()
        if PLACE_7 == 1:
            WIN.blit(X_NORMAL, (30, 500))
            line()
        if PLACE_7 == 2:
            WIN.blit(O_NORMAL, (30, 500))
            line()
        if PLACE_8 == 1:
            WIN.blit(X_NORMAL, (270, 500))
            line()
        if PLACE_8 == 2:
            WIN.blit(O_NORMAL, (270, 500))
            line()
        if PLACE_9 == 1:
            WIN.blit(X_NORMAL, (500, 500))
            line()
        if PLACE_9 == 2:
            WIN.blit(O_NORMAL, (500, 500))
            line()
        pygame.display.update()
        print("X =", point_X, ",  O =", point_O)

    pygame.quit()
if __name__ == "__main__":
    main()