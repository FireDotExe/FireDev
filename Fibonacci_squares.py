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
background = (13, 59, 102)
foreground = (250, 240, 202)

x = 0
y = arr[0]

cx = 0
cy = 0


# SCREEN
screen = pygame.display.set_mode((width, height))
screen.fill(background)


for j in range(13):
    if j % 4 == 0:  # 0, 4, 8
        y -= arr[j]
        cx = x + arr[j]
        cy = y + arr[j]

    elif (j - 1) % 4 == 0:  # 1, 5, 9
        x += arr[j - 1]

        cx = x
        cy = y + arr[j]

    elif (j + 2) % 4 == 0:  # 2, 6, 10
        x += arr[j + 1]
        y += arr[j - 1]

        cx = x
        cy = y

    else:  # 3, 7, 11
        x -= arr[j]
        y += arr[j + 1]

        cx = x + arr[j]
        cy = y

    pygame.draw.rect(screen, foreground, pygame.Rect(x, y, arr[j], arr[j]), 2)
    #pygame.draw.circle(screen, foreground, (cx, cy), arr[j], 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
