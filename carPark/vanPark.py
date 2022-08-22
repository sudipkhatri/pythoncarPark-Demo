import pygame

#initialize pygame
pygame.init()

#screen
width = 700
height = 700
screen = pygame.display.set_mode((width, height))

#boolean
boolean = True

#images
bg = pygame.image.load("photos/carPaark.jpg")
bg = pygame.transform.scale(bg, (width, height))
car = pygame.image.load("photos/car.jpg")
car = pygame.transform.scale(car, (100, 100))
van = pygame.image.load("photos/van.jpg")
van = pygame.transform.scale(van, (100, 100))
truck = pygame.image.load("photos/truck.jpg")
truck = pygame.transform.scale(truck, (100, 100))


#method for movement
def carMove(x, y, wid, hei):
    screen.blit(car, (x, y, wid, hei))
def truckMove(x, y, wid, hei):
    screen.blit(truck, (x, y, wid, hei))
def vanMove(x, y):
    screen.blit(van, (x, y, wid, hei))
x = 100
y = 100
wid = width - 200
hei = height - 300
move = 2

#arrays
vehicle = [car, van, truck]
#while loop/ game loop
while(boolean):
    #event in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boolean = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 50:
        x -= move
    if keys[pygame.K_RIGHT] and x <wid - move:
        x += move
    if keys[pygame.K_UP] and y > 150:
        y -= move
    if keys[pygame.K_DOWN] and y < hei - move:
        y += move

    #screen background
    screen.blit(bg, [0, 0])

    screen.blit(van, (x, y, wid, hei))


    #screen draw
   # pygame.draw.rect(screen, 5, 10, 50, 50)

    #flip display

    pygame.display.flip()
    pygame.display.update()

pygame.quit()