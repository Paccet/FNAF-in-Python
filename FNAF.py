import pygame, random, time

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background = pygame.image.load("Images/Background.png")
    backgroundrect = background.get_rect()

    screen.fill("purple")
    screen.blit(background, backgroundrect)
    pygame.display.flip()

Animatronics = ['Freddy', 'Chica', 'Bonnie', 'Foxy']
Aimatronics = ['Freddy', 'Chica', 'Bonnie', 'Foxy']
Locations = {'Main Stage', 'Back Stage', 'Main Hall', 'Left Hall', 'Right Hall', 'Office', 'Kitchen', 'Restrooms',
             'Arcade', 'Party Room', 'Closet'}

def Roll():
    Aimatronics[0] = random.randint(1, 20)
    Aimatronics[1] = random.randint(1, 20)
    Aimatronics[2] = random.randint(1, 20)
    Aimatronics[3] = random.randint(1, 20)

# [0] = Freddy, [1] = Chica, [2] = Bonnie, [3] = foxy.

if Animatronics == ['Freddy', 'Chica', 'Bonnie', 'Foxy']:
    Roll()
    print('Freddies AI is ' + str(Aimatronics[0]))
    print('Chicas AI is ' + str(Aimatronics[1]))
    print('Bonnies AI is ' + str(Aimatronics[2]))
    print('Foxies AI is ' + str(Aimatronics[3]))
    if Aimatronics == ['Freddy', 'Chica', 'Bonnie', 'Foxy']:
        print('An Error has Occurred!')

