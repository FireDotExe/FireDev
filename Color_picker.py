import sys, pygame

pygame.init()

# VARIABLES
width = 255
height = 255

r = 255
g = 0
b = 0

done = False

timer = pygame.time.get_ticks()
milliseconds = 1

# SCREEN
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))

while True:
    if pygame.time.get_ticks() - timer > milliseconds:
        timer = pygame.time.get_ticks()

        screen.fill((r, g, b))
        picker = pygame.image.load("gradient.png")
        screen.blit(picker, (0, 0))

        if b < 255 and not done:
            b += 1

        if b == 255:
            if r > 0 and done:
                r -= 1

            elif g < 255 and done:
                g += 1
            done = True

        if g == 255 and done:
            if b > 0:
                b -= 1

        if b == 0 and done:
            if r < 255:
                r += 1

            if r == 255:
                if g > 0:
                    g -= 1
                if g == 0:
                    done = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
