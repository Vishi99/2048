import pygame
import random

x_end = 290
y_end = 290
x = x_st = 20
y = y_st = 20
width = 80
height = 80

light = (240, 230, 140)
yellow = (255, 255, 0)
maroon = (128, 0, 0)
red = (255, 0, 0)

green = (45, 167, 98)
black = (0, 0, 0)

coord = []
tileclr = []
number = []
dirty = []

def flush():
    for i in range(len(dirty)):
        dirty[i] = 0

def init():
    for i in range (20, 300, 90):
        for j in range(20, 300, 90):
            coord.append((j, i))
            tileclr.append(green)
            number.append(0)
            dirty.append(0)

def numtocol(num):
    if num == 0:
        return green
    if num <= 4:
        return light
    elif num <= 64:
        return yellow
    elif num <= 512:
        return red
    elif num >= 1024:
        return maroon

def func(dir, win):

    flag = 0

    if dir == 'l':
        for i in range(0, 16):
            if tileclr[i] == green:
                continue

            j = i - 1
            while j % 4 != 3 and number[j] == 0:
                j = j - 1
            if j % 4 != 3 and number[j] == number[i] and dirty[j] != 1:
                number[j] = 2*number[i]
                dirty[j] = 1
                number[i] = 0
                tileclr[j] = numtocol(number[j])
                tileclr[i] = green
                flag = 1
            elif j != i - 1:
                tileclr[j + 1] = tileclr[i]
                number[j + 1] = number[i]
                tileclr[i] = green
                number[i] = 0
                flag = 1

    elif dir == 'r':
        for i in range(15, -1, -1):
            if tileclr[i] == green:
                continue

            j = i + 1

            while j % 4 != 0 and number[j] == 0:
                j = j + 1
            if j % 4 != 0 and number[j] == number[i] and dirty[j] != 1:
                dirty[j] = 1
                number[j] = 2*number[i]
                number[i] = 0
                tileclr[j] = numtocol(number[j])
                tileclr[i] = green
                flag = 1
            elif j != i + 1:
                tileclr[j - 1] = tileclr[i]
                number[j - 1] = number[i]
                tileclr[i] = green
                number[i] = 0
                flag = 1

    elif dir == 'd':
        for i in range(15, -1, -1):
            if tileclr[i] == green:
                continue

            j = i + 4

            while j < 16 and number[j] == 0:
                j = j + 4
            if j < 16 and number[j] == number[i] and dirty[j] != 1:
                dirty[j] = 1
                number[j] = 2*number[i]
                number[i] = 0
                tileclr[j] = numtocol(number[j])
                tileclr[i] = green
                flag = 1
            elif j != i + 4:
                tileclr[j - 4] = tileclr[i]
                number[j - 4] = number[i]
                tileclr[i] = green
                number[i] = 0
                flag = 1

    elif dir == 'u':
        for i in range(0, 16):
            if tileclr[i] == green:
                continue

            j = i - 4
            while j >= 0 and number[j] == 0:
                j = j - 4
            if j >= 0 and number[j] == number[i] and dirty[j] != 1:
                dirty[j] = 1
                number[j] = 2*number[i]
                number[i] = 0
                tileclr[j] = numtocol(number[j])
                tileclr[i] = green
                flag = 1
            elif j != i - 4:
                tileclr[j + 4] = tileclr[i]
                number[j + 4] = number[i]
                tileclr[i] = green
                number[i] = 0
                flag = 1

    flush()
    while flag:
        x = random.choice([20, 110, 200, 290])
        y = random.choice([20, 110, 200, 290])
        if(tileclr[coord.index((x, y))] == green):
            rand = random.randrange(1, 9, 1)
            if rand == 8:
                tileclr[coord.index((x, y))] = light
                number[coord.index((x, y))] = 4
            else:
                tileclr[coord.index((x, y))] = light
                number[coord.index((x, y))] = 2
            break
        flag = flag + 1
        if(flag == 16):
            break

def gridDisp(win):
    win.fill((225, 255, 225))
    pygame.draw.rect(win, (0, 0, 0), (x_st, y_st, 350, 350))
    font = pygame.font.Font('freesansbold.ttf', 26)
    x = x_st
    while(x <= x_end):
        y = y_st
        while(y <= y_end):
            pygame.draw.rect(win, (45,167,98), (x, y, 80, 80))
            y+=90
        x+=90
    for i in range(0, 16):
        pygame.draw.rect(win, tileclr[i], (coord[i][0], coord[i][1], width, height))
        if number[i] != 0:
            text = font.render(str(number[i]), True, black)
            win.blit(text, (coord[i][0] + 30, coord[i][1] + 30))

def main():
    pygame.init()
    win = pygame.display.set_mode((390, 390))
    pygame.display.set_caption("2048")
    run = True
    color = light
    init()

    tileclr[1] = light
    number[1] = 2

    while run:

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    func('l', win)
                if event.key == pygame.K_RIGHT:
                    func('r', win)
                if event.key == pygame.K_UP:
                    func('u', win)
                if event.key == pygame.K_DOWN:
                    func('d', win)

        gridDisp(win)
        pygame.display.update()

        if 0 not in number or run == False:
            run = True
            score = 0
            for ele in number:
                while ele >= 2:
                    score+=ele
                    ele = ele//2
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                win.fill((225, 255, 225))
                font = pygame.font.Font('freesansbold.ttf', 40)
                text = font.render("Score: "+str(score), True, black)
                win.blit(text, (100, 100))
                pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
