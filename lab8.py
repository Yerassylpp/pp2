import pygame

pygame.init()

x = 100
y = 100
# cx = str(x)
# cy = str(y)
# title = 
screen = pygame.display.set_mode((500,500))

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()

# ballsurface = pygame.Surface((x,y))
# ballsurface.set_colorkey((0,0,0)) 
# pygame.draw.circle(background, (255, 0, 0), (x, y), 25)

screen.blit(background,(0,0))
# screen.blit(ballsurface, (50, 50))

speed = 15

clock = pygame.time.Clock()

running = True
FPS = 50
while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 25:
        x=x-speed
    if keys[pygame.K_RIGHT] and x < 500-29:
        x=x+speed
    if keys[pygame.K_UP] and y > 25:
        y=y-speed        
    if keys[pygame.K_DOWN] and y < 500 - 33: 
        y=y+speed
    pygame.draw.circle(background, (255, 0, 0), (x, y), 25)
    screen.blit(background,(0,0))
    background.fill((255,255,255))
    pygame.display.set_caption(pygame.ballsurface.get_rect(),icontitle = None)
    pygame.display.flip()
    pygame.display.update()
    

pygame.quit()