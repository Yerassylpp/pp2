import pygame
import random

pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('BattleCity')
pygame.draw.rect(screen, (107, 201, 179), (0, 0, screen_width, 20))
clock=pygame.time.Clock()

shoot_sound=pygame.mixer.Sound('sounds/shoot.wav')
hit_sound=pygame.mixer.Sound('sounds/hit.wav')
class Direction:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tank:
    def  __init__(self, x, y, speed, color,direction, fire=pygame.K_RETURN, d_right=pygame.K_RIGHT, 
                    d_left=pygame.K_LEFT, d_up=pygame.K_UP, 
                    d_down=pygame.K_DOWN,to_left=pygame.image.load("pleft.png"),to_right=pygame.image.load("pright.png"),
                    to_up=pygame.image.load("pup.png"),to_down=pygame.image.load("pdown.png")):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 65
        self.speed = speed
        self.color = color
        self.direction = Direction
        self.to_left = to_left
        self.to_right = to_right
        self.to_up = to_up
        self.to_down = to_down
        self.life=3
        self.fire=fire

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self): 
        if self.direction == Direction.RIGHT:
            screen.blit(self.to_right,(self.x,self.y))
            self.width = 65
            self.height = 50
        elif self.direction == Direction.LEFT:
            screen.blit(self.to_left,(self.x,self.y))
            self.width = 65
            self.height = 50
        elif self.direction == Direction.UP:
            screen.blit(self.to_up,(self.x,self.y))
            self.width = 50
            self.height = 65
        elif self.direction == Direction.DOWN:
            screen.blit(self.to_down,(self.x,self.y))
            self.width = 50
            self.height = 65
        else:
            screen.blit(self.to_up,(self.x,self.y))   

    def change_direction(self, direction):
        self.direction = direction

    def move(self):                 
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        self.draw()

        if self.x < 0-self.width:               
            self.x=screen_width
        if self.x>800:
            self.x=0-self.width
        if self.y<0-self.height:
            self.y=screen_height
        if self.y>screen_height:
            self.y=0-self.height            
    
class Bullet:
    def __init__(self, x=0, y=0, color=(255,255,255), direction=Direction.UP):
        self.x=x
        self.y=y
        self.color=color
        self.radius=7
        self.speed=30
        self.screen=screen
        self.direction=direction
        self.ready=True             

    def move(self): 
        if self.direction==Direction.RIGHT:
            self.x+=self.speed
        if self.direction==Direction.LEFT:
            self.x-=self.speed
        if self.direction==Direction.UP:
            self.y-=self.speed
        if self.direction==Direction.DOWN:
            self.y+=self.speed 
        
        if self.ready:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)  
            
def bullet_position(tank): 
    if tank.direction==Direction.RIGHT:
        x=tank.x+tank.width
        y=tank.y+int(tank.height/2)
    elif tank.direction==Direction.LEFT:
        x=tank.x-int(int(tank.width/2)/2)
        y=tank.y+int(tank.height/2)
    elif tank.direction==Direction.UP:
        x=tank.x+int(tank.width/2)
        y=tank.y-int(tank.height/2)
    elif tank.direction==Direction.DOWN:
        x=tank.x+int(tank.width/2)
        y=tank.y+tank.height

    bullet=Bullet(x,y,tank.color, tank.direction)  
    bullets.append(bullet)
                
def get_hit():
    for bullet in bullets:        
        for tank in tanks:
            if bullet.x>tank.x and bullet.x<tank.x+tank.width and bullet.y>tank.y and bullet.y<tank.height+tank.y:
                bullet.ready=False 
                hit_sound.play()  
                tank.life-=0.5
                    
def tank_life():
    health1=int(tank1.life)
    health2=int(tank2.life)
    font = pygame.font.Font("fonts/2p.ttf", 18)
    text1 = font.render("BLUE HP {}".format(health1), 1, (0, 0, 0))        
    place1 = [10, 10]
    text2 = font.render('RED HP {}'.format(health2), 1, (0, 0, 0))
    place2 = [650, 10]
    screen.blit(text1, place1)
    screen.blit(text2, place2)

def game_over():
    if int(tank1.life<=0):
            game_over=pygame.image.load('gameover2.jpg')
            gameover = True 
            for tank in tanks:
                tank.speed = 0
                tank1.x = 0
                tank1.y = 0
                tank2.x = 800
                tank2.y = 600                   
            screen.blit(game_over, (0,0)) 
    if int(tank2.life<=0):
            game_over=pygame.image.load('gameover1.jpg')
            gameover = True 
            for tank in tanks:
                tank.speed = 0
                tank1.x = 0
                tank1.y = 0
                tank2.x = 800
                tank2.y = 600                   
            screen.blit(game_over, (0,0))     
    pygame.display.flip()       

eleft = pygame.image.load("eleft.png")
eright = pygame.image.load("eright.png")
eup = pygame.image.load("eup.png")
edown = pygame.image.load("edown.png")

tank1 = Tank(random.randint(50, 350), random.randint(50, 300), 3, (0, 0, 255),Direction.UP,pygame.K_RETURN,pygame.K_RIGHT,pygame.K_LEFT,pygame.K_UP,pygame.K_DOWN)
tank2 = Tank(random.randint(450, 750), random.randint(300, 550), 3, (255, 0, 0),Direction.DOWN, pygame.K_SPACE, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s,eleft,eright,eup,edown)

bullet1=Bullet()      
bullet2=Bullet()

tanks = [tank1, tank2]
bullets = [bullet1, bullet2]

FPS = 50
gameover = False
mainloop = True
while mainloop:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            key = pygame.key.get_pressed()
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])      
                if key[tank.fire] and gameover == False:
                    shoot_sound.play()
                    bullet_position(tank)

    screen.fill((107, 201, 179))
    tank_life()
    get_hit()
    
    for s in bullets:
        s.move()
    for tank in tanks:
        tank.draw()
        tank.move()
    
    game_over()
    pygame.display.flip()  
pygame.quit()