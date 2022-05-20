import pygame



def create_game_window(width,height):
    pygame.init()
    game_window=pygame.display.set_mode((width,height))
    pygame.display.set_caption("PONG")
    pygame.draw.line(game_window,(255,255,255),(0,718),(1024,718))
    return game_window

def draw_scoreboard(points_p1,points_p2,window):
    pygame.draw.rect(window,(0,0,0),(340,720,300,100))
    font = pygame.font.SysFont(None, 48)
    board = font.render(('SCORE :    '+str(points_p1)+'   :   '+str(points_p2)), True, (0,22,111))
    window.blit(board,(350,725))
    pygame.display.flip()
    return board
    

class Ball:
    def __init__(self,xpos,ypos,r,window,velocity):
        self.xvel=velocity
        self.yvel=velocity
        self.x=xpos
        self.y=ypos
        self.r=r
        pygame.draw.circle(window,(0,0,255),(xpos,ypos),r)
        pygame.display.update()
    def move_ball(self,r,window):
        pygame.draw.circle(window,(0,0,0),(self.x,self.y),r)
        self.x+=self.xvel
        self.y+=self.yvel
        pygame.draw.circle(window,(0,0,255),(self.x,self.y),r)
        pygame.display.update()
    def hit_border(self):
        if (self.y==0 or self.y==718):
            return -self.yvel
        else:
            return self.yvel
    def ball_reset(self,window,r):
        pygame.draw.circle(window,(0,0,0),(self.x,self.y),r)
        pygame.display.update()
        self.x=512
        self.y=384

class Paddle:
    def __init__(self,xpos,ypos,width,height,window):
        self.x=xpos
        self.y=ypos
        self.width=width
        self.height=height
        self.points=0
        pygame.draw.rect(window,(255,255,255),(xpos,ypos,width,height))
        pygame.display.update()
    def move_paddle(self,x_move,y_move,window):
        pygame.draw.rect(window,(0,0,0),(self.x,self.y,self.width,self.height))
        self.y-=y_move
        pygame.draw.rect(window,(255,255,255),(self.x,self.y,self.width,self.height))
        pygame.draw.rect(window,(0,0,0),(0,719,40,60))
        pygame.draw.rect(window,(0,0,0),(984,719,40,60))
        pygame.display.update()

    def hit_paddle(self,ball : Ball,paddle_number):
        if paddle_number==1:
            r=-ball.r
        elif paddle_number==2:
            r=ball.r
        if(ball.x+r==(self.x+self.width))and(ball.y<=self.y+self.height and ball.y>=self.y)and paddle_number==1:
            return -ball.xvel
        elif(ball.x+r==self.x)and(ball.y<=self.y+self.height and ball.y>=self.y)and paddle_number==2:
            return -ball.xvel
        else:
            return ball.xvel
    def get_points(self):
        return self.points
    def give_point(self):
        self.points+=1

game_window=create_game_window(1024,768)
run=True
paddle1=Paddle(10,344,20,120,game_window)
paddle2=Paddle(994,344,20,120,game_window)
ball=Ball(512,384,10,game_window,-2)
scoreboard=draw_scoreboard(paddle1.get_points(),paddle2.get_points(),game_window)



while(run==True):
    pygame.time.delay(7)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    ball.move_ball(10,game_window)
    ball.yvel=ball.hit_border()
    ball.xvel=paddle1.hit_paddle(ball,1)
    ball.xvel=paddle2.hit_paddle(ball,2)
    if(ball.x==0):
        paddle1.move_paddle(0,0,game_window)
        paddle1.give_point()
        ball.ball_reset(game_window,10)
    if(ball.x==1024):
        paddle2.move_paddle(0,0,game_window)
        paddle2.give_point()
        ball.ball_reset(game_window,10)
    scoreboard=draw_scoreboard(paddle1.get_points(),paddle2.get_points(),game_window)
    pygame.draw.line(game_window,(255,255,255),(0,718),(1024,718))



    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and paddle1.y>0:
        paddle1.move_paddle(0,10,game_window)
    if keys[pygame.K_s] and paddle1.y<688:
        paddle1.move_paddle(0,-10,game_window)
    if keys[pygame.K_UP] and paddle2.y>0:
        paddle2.move_paddle(0,10,game_window)
    if keys[pygame.K_DOWN] and paddle2.y<688:
        paddle2.move_paddle(0,-10,game_window)
    