import pygame

pygame.init()

win=pygame.display.set_mode((500,480))

pygame.display.set_caption("The Goblin Game")

walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png') ]

walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]

bg=pygame.image.load('bg.jpg')

char=pygame.image.load('standing.png')

clock=pygame.time.Clock()
bulletSound=pygame.mixer.Sound('bullet.wav')
hitSoung=pygame.mixer.Sound('bullet.wav')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

score=0

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.left=False
        self.right=False
        self.walkCount=0
        self.jumpCount=10
        self.standing=True
        self.hitbox=(self.x+17,self.y+11,29,52)
        
    def draw(self,win):
        if self.walkCount+1>=27:
            self.walkCount=0
            
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
                
            else:
                if self.right:
                    win.blit(walkRight[0],(self.x,self.y))
                else :
                    win.blit(walkLeft[0],(self.x,self.y))
                self.hitbox=(self.x+17,self.y+11,29,52)
                
    def hit(self):
        self.isJump=False
        self.jumpCount=10
        self.x=100
        self.y=410
        self.walkCount=0
        font1=pygame.font.SysFont('comicsans',100)
        text=font1.render('-5',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))
        pygame.display.update()
        i=0
        while i<200:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT():
                    i=201
                    pygame.quit
        