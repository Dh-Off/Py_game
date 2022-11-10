import sys, random, pygame
from pygame.locals import QUIT, KEYDOWN,\
    K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

pygame.init()
SURFACE = pygame.display.set_mode((900, 600))
FPSCLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)

FOODS, SNAKE = [], []
SP_y,SP_b = [], []
(W, H) = (20, 20)
score, speed = 0, 5

##############################  파랑
def sp_b_food():
    while True:
        pos_b = (random.randint(0, W-1), random.randint(0, H-1))
        if pos_b in SP_b:
            continue
        SP_b.append(pos_b)
        break

def sp_b_move(pos_b):
    j = SP_b.index(pos_b)
    del SP_b[j]

    sp_b_food()
##############################  노랑
def sp_y_food():
    while True:
        pos_y = (random.randint(0, W-1), random.randint(0, H-1))
        if pos_y in SP_b:
            continue
        SP_y.append(pos_y)
        break

def sp_y_move(pos_y):
    j = SP_y.index(pos_y)
    del SP_y[j]

    sp_y_food()
##############################
def add_food():
    """ 임의의 장소에 먹이를 배치 """
    while True:
        pos = (random.randint(0, W-1), random.randint(0, H-1))
        if pos in FOODS or pos in SNAKE: 
            continue
        FOODS.append(pos)
        break

def move_food(pos):
    """ 먹이를 다른 장소로 이동 """
    i = FOODS.index(pos)
    del FOODS[i]
    
    add_food()
##############################
def paint(message):
    """ 화면 전체 그리기 """
    SURFACE.fill((0, 0, 0))
    for food in FOODS:
        pygame.draw.ellipse(SURFACE, (0, 255, 0), Rect(food[0]*30, food[1]*30, 30, 30))  #ellipse( 스크린, 색상, 좌표(x,y,w,h))
    for spfood in SP_b:  #파랑  
        pygame.draw.ellipse(SURFACE, (0, 0, 255), Rect(spfood[0]*30, spfood[1]*30, 30, 30))  #ellipse( 스크린, 색상, 좌표(x,y,w,h))
    for sp_y_food in SP_y: #노랑
        pygame.draw.ellipse(SURFACE, (255, 255, 0), Rect(sp_y_food[0]*30, sp_y_food[1]*30, 30, 30))  #ellipse( 스크린, 색상, 좌표(x,y,w,h))

    for body in SNAKE:
        pygame.draw.rect(SURFACE, (0, 255, 255),
                         Rect(body[0]*30, body[1]*30, 30, 30))
    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64), ((index+1)*30, 0),     #세로줄
                         ((index+1)*30, 600))
        pygame.draw.line(SURFACE, (64, 64, 64), (0, (index+1)*30),     #가로줄
                         (600, (index+1)*30))
    if message != None:
        SURFACE.blit(message, (150, 300))

    score_image = sysfont.render("score is {}".format(score), True, (255, 255, 225))
    speed_image = sysfont.render("speed is {}".format(speed), True, (255, 255, 255))
    info_y = sysfont.render("Yellow -  Body init", True, (255, 255, 0))
    info_b = sysfont.render("Blue    -  Speed init", True, (0, 0, 255))
    SURFACE.blit(score_image, (640, 150)) 
    SURFACE.blit(speed_image, (640, 200)) 
    SURFACE.blit(info_y, (640, 400)) 
    SURFACE.blit(info_b, (640, 450)) 

    pygame.display.update()  

def main():
    """ 메인 루틴 """
    global score,speed
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    SNAKE.append((int(W/2), int(H/2)))
    for _ in range(10):
        add_food()
    for k in range(1):
        sp_b_food()
        sp_y_food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key       

        if not game_over:
            if key == K_LEFT:
                head = (SNAKE[0][0] - 1, SNAKE[0][1])
            elif key == K_RIGHT:
                head = (SNAKE[0][0] + 1, SNAKE[0][1])
            elif key == K_UP:
                head = (SNAKE[0][0], SNAKE[0][1] - 1)
            elif key == K_DOWN:
                head = (SNAKE[0][0], SNAKE[0][1] + 1)

            #벽에 닿을때    
            if head[0] < 0 or head[0] >= W or \
               head[1] < 0 or head[1] >= H:
               head = (SNAKE[0][0], SNAKE[0][1] + 19) #위>아래
               
            if head[0] < 0 or head[0] >= W or \
               head[1] < 0 or head[1] >= H:
               head = (SNAKE[0][0] - 19, SNAKE[0][1]) #우측>우측  

            if head[0] < 0 or head[0] >= W or \
               head[1] < 0 or head[1] >= H:
               head = (SNAKE[0][0] + 19, SNAKE[0][1]) #좌측>좌측 

            if head[0] < 0 or head[0] >= W or \
               head[1] < 0 or head[1] >= H:
                head = (SNAKE[0][0], SNAKE[0][1] - 19) #아래>위

            #뱀머리가 몸에 포함된경우
            if head in SNAKE:
                message = myfont.render("Game Over!",True, (255, 255, 0))
                game_over = True

            ############################## #스페셜 먹으면  
            if head in SP_y:        #  y = 노랑
                del SNAKE[1:]
                sp_y_move(head)

            elif head in SP_b:      #  b = 파랑
                speed = 5
                sp_b_move(head)
            ##############################    
            
            SNAKE.insert(0, head)

            if head in FOODS: #먹이먹을때    
                score += 100
                if score % 500 == 0:
                    speed += 5
                move_food(head) 

            else:
                SNAKE.pop()

        paint(message)
        FPSCLOCK.tick(speed)

if __name__ == '__main__':
    main()