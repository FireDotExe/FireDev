import sys, pygame
pygame.init()

#   FIBONACCI SEQUENCE
arr = [1, 1]
for i in range(14):
    n = arr[0] + arr[1]
    arr.insert(0, n)


# VARIABLES
width = arr[0] + arr[1]
height = arr[0]
background = (251, 86, 7)
foreground = (250, 240, 202)

x = 0
y = arr[0]

cx = 0
cy = 0

pi = 3.1415926
start = 0
stop = 0


# SCREEN
screen = pygame.display.set_mode((width, height))
screen.fill(background)

# DRAWING FIBONACCI SPIRAL
for j in range(13):
    if j % 4 == 0:  # 0, 4, 8
        y -= arr[j]

        cx = x
        cy = y

        start = pi/2
        stop = pi

    elif (j - 1) % 4 == 0:  # 1, 5, 9
        x += arr[j - 1]

        cx = x - arr[j]
        cy = y

        start = 0
        stop = pi/2

    elif (j + 2) % 4 == 0:  # 2, 6, 10
        x += arr[j + 1]
        y += arr[j - 1]

        cx = x - arr[j]
        cy = y - arr[j]

        start = 3 / 2 * pi
        stop = 2 * pi

    else:  # 3, 7, 11
        x -= arr[j]
        y += arr[j + 1]

        cx = x
        cy = y - arr[j]

        start = pi
        stop = 3 / 2 * pi

    pygame.draw.rect(screen, foreground, pygame.Rect(x, y, arr[j], arr[j]), 2)

    square = pygame.Rect(cx, cy, 2*arr[j], 2*arr[j])
    pygame.draw.arc(screen, foreground, square, start, stop, 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
