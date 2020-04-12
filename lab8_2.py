import pygame

pygame.init()
displayw = 640
displayh = 480
clock = pygame.time.Clock()
screen = pygame.display.set_mode((displayw,displayh))
class MainRun():
    def __init__(self,displayw,displayh):
        self.dw = displayw
        self.dh = displayh
        self.Main()

    def Main(self):
        mainloop = True
        screenrect = screen.get_rect()
        background = pygame.Surface(screen.get_size())
        background.fill((255,255,255)) 
        background = background.convert()    
        ballsurface = pygame.Surface((50,50))
        ballsurface.set_colorkey((0,0,0)) 
        pygame.draw.circle(ballsurface, (0,0,255), (25,25),25)
        ballrect = ballsurface.get_rect()
        ballsurface = ballsurface.convert_alpha() 
        ballx, bally = 550,240 
        dx,dy  = 60, 50 
        screen.blit(background, (0,0))
        screen.blit(ballsurface, (ballx, bally)) 
        FPS = 30
        while mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False
    
            milliseconds = clock.tick(FPS)
            seconds = milliseconds/1000.0
 
            ballx += dx * seconds 
            bally += dy * seconds 
 
            if ballx < 0:
                ballx = 0
                dx *= -1 
            elif ballx + ballrect.width > screenrect.width:
                ballx = screenrect.width - ballrect.width
                dx *= -1
            if bally < 0:
                bally = 0
                dy *= -1
            elif bally + ballrect.height > screenrect.height:
                bally = screenrect.height - ballrect.height
                dy *= -1
    
            screen.blit(background,(0,0))    
            screen.blit(ballsurface, (round(ballx,0), round(bally,0)))
            pygame.display.flip()          

MainRun(displayw,displayh)

pygame.quit()