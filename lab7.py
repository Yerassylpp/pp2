import pygame
import math

pygame.init()

screen = pygame.display.set_mode((480,480))

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()
PI = math.pi
pygame.draw.circle(background,(255,192,203),(240,240),240) # giant pink circle in the middle
pygame.draw.polygon(background, (0,180,0), ((316,88),(384,276),(199,160),(427,160),(241,274),(316,88)),5) # pentagram
pygame.draw.arc(background, (0,0,0),(0,0,960,960), PI/4,5*PI/4) # arc from top right to bottom left 
for point in range(0,480,20):
    pygame.draw.line(background, (255,0,255), (0,0),(480,point),1)
for point in range(0,480,20):
    pygame.draw.line(background,(255,0,255), (480,0),(0,point),1)
for point in range(0,480,20):
    pygame.draw.line(background,(255,0,255), (0,480),(480,point),1)
for point in range(0,480,20):
    pygame.draw.line(background, (255,0,255),(480,480),(0,point),1)            
screen.blit(background,(0,0))

ballsurface = pygame.Surface((50, 50))
pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25)

ballsurface = ballsurface.convert()
screen.blit(background, (0, 0))
# screen.blit(ballsurface, (50, 50)) out-commented to remove black square and blue ball



clock = pygame.time.Clock()

running = True
FPS = 30
while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
    pygame.display.update()
    pygame.display.flip()

pygame.quit()