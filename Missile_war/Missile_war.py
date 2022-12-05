import pygame, os, random
from pygame.locals import KEYDOWN, K_SPACE, K_UP, K_DOWN
from os.path import exists

#미사일 클래스
class C_missile(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image  #회전시 원본
        self.rect = image.get_rect(center = position) 
        self.offset = pygame.math.Vector2(0,0)  #x, y로 이동
        self.position = position
        self.direction =  LEFT      #왼,오 방향 판별  
        self.angle_speed = 2.5  
        self.angle = 45   #최초 각도
        
    def update(self, event, to_y): 
        if event.type == KEYDOWN:
            if miss.direction != stop:
                  
                if event.key == K_DOWN:
                    self.direction = LEFT
                    if self.direction == LEFT:
                        self.angle += self.angle_speed
                        if self.angle > 90:
                            self.angle = 90
                elif event.key == K_UP:
                    self.direction = RIGHT
                    if self.direction == RIGHT:
                        self.angle -= self.angle_speed
                        if self.angle < 0:
                            self.angle = 0

        self.offset.y -= to_y  
        self.rotate()

    def rotate(self):   #미사일 이미지가 각도조절되며 회전할때의 회전처리
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1) #이미지 회전및 크기조절
        offset_rotated = self.offset.rotate(self.angle) #집게 각도에 따라 회전한 값을 저장      
        self.rect = self.image.get_rect(center = self.position + offset_rotated)    #회전된 변경한 값 저장
        
    def set_direction(self, direction): 
        self.direction = direction
    
    def draw(self, screen):  #update시 바뀐 이미지로 그림
        screen.blit(self.image, self.rect)
        
    def set_init_state(self):
        self.offset.y = 0  #miss원위치  0,0 
        self.direction = LEFT   #줄 이동방향 
        
#유닛 클래스
class c_unit(pygame.sprite.Sprite): 
    def __init__(self, image, position, speed):  
        super().__init__()
        self.image = image  
        self.rect = image.get_rect(center = position)   #움직일때마다 위치
        self.speed = speed 
           
    def set_position(self, position):   #중심
       self.rect.width // 2 
       self.rect.height // 2
       self.rect.center = (position[0] , position[1]) 
  
##################  아이템   1, 2
def item_1_new():  
    x__1 = random.randint(300,700)
    item_1_group.add(c_unit(item_1_images[0], (x__1,0), item_1_speed)) 

def item_2_new():
    x__2 = random.randint(700,1260)
    item_2_group.add(c_unit(item_2_images[0], (x__2,0), item_2_speed))
    
##################### 유닛생성
def Unit_12():
    rect = pygame.Rect(unit_image.get_rect())
    rect.right = 1280
    rect.top = random.randint(0, 300)
    dy = random.randint(3, 9)
    unit_list.append({'rect': rect, 'dy': dy}) 
    
#####################  item_1의 벽
def wall_new():
    global wall_rect
    wall_rect = pygame.Rect(walls.get_rect())
    wall_rect.left = 0
    wall_rect.top = -100
    
    
pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("missile_war")   
sysfont = pygame.font.SysFont(None, 36)
fail_font = pygame.font.SysFont("Maplestory Bold.ttf", 450)
clock = pygame.time.Clock()
game_over = False

#게임 관련변수 
caught_item_1 = None #줄 뻗었을때 잡히는 아이템 정보 
caught_item_2 = None
to_y = 0    #미사일 이미지를 이동시킬 값 저장                     

#방향
LEFT, RIGHT = -1, 1  #왼/오
stop = 0 # 이동방향 고정

#속도 
move_speed = 35     #발사할때 이동 스피드 
item_1_speed = 35   #가져올때 스피드
item_2_speed = 35

#색깔 
#RED = (255,0,0)  #빨강
BLACK = (0,0,0)  #검정

load_path = os.path.dirname(__file__)  #현재 파일 위치반환

##############◆◆◆◆◆음악◆◆◆◆◆##############

pygame.mixer.music.load(os.path.join(load_path, "bgm.mp3"))
pygame.mixer.music.set_volume(0.5) # 무한 반복
pygame.mixer.music.play(-1) # 무한 반복

boom_wav = pygame.mixer.Sound(os.path.join(load_path, "bbboom_1.wav"))
boom_wav.set_volume(0.5)
boom_wav.fadeout(1000)

clear = pygame.mixer.Sound(os.path.join(load_path, "clear.wav"))
ending = pygame.mixer.Sound(os.path.join(load_path, "ending.wav"))
fail = pygame.mixer.Sound(os.path.join(load_path, "fail.wav"))

shot = pygame.mixer.Sound(os.path.join(load_path, "shot.wav"))
shot.set_volume(0.4)

new_wall = pygame.mixer.Sound(os.path.join(load_path, "new_wall.wav"))
back_wall = pygame.mixer.Sound(os.path.join(load_path, "back_wall.wav"))
marin = pygame.mixer.Sound(os.path.join(load_path, "marin.wav"))
heal = pygame.mixer.Sound(os.path.join(load_path, "heal.wav"))
rope = pygame.mixer.Sound(os.path.join(load_path, "rope.wav"))

##############◆◆◆◆◆음악◆◆◆◆◆##############

##############◆◆◆◆◆사진◆◆◆◆◆##############
back = pygame.image.load(os.path.join(load_path, "background.png"))
rok = pygame.image.load(os.path.join(load_path, "rok.png"))
rok = pygame.transform.scale(rok, (200, 133))
warning = pygame.image.load(os.path.join(load_path, "warning.png"))
castle = pygame.image.load(os.path.join(load_path, "castle.png"))
castle = pygame.transform.scale(castle, (550, 550))

castle_crack = pygame.image.load(os.path.join(load_path, "castle_crack.png"))
castle_crack = pygame.transform.scale(castle_crack, (550, 550))
castle_boom = pygame.image.load(os.path.join(load_path, "castle_boom.png"))

walls = pygame.image.load(os.path.join(load_path, "walls.png"))

unit_image = pygame.image.load(os.path.join(load_path, "unit.png"))
unit_image = pygame.transform.scale(unit_image, (100, 140))

boom = pygame.image.load(os.path.join(load_path, "boom.png"))
boom = pygame.transform.scale(boom, (100, 100))

##############◆◆◆◆◆사진◆◆◆◆◆##############

unit_list = []

#이미지 불러오기. (아이템, 벽? , 먹아이템)
item_1 = pygame.image.load(os.path.join(load_path, "item_1.png"))
item_1 = pygame.transform.scale(item_1, (120, 120))

item_2 = pygame.image.load(os.path.join(load_path, "item_2.png"))
item_2 = pygame.transform.scale(item_2, (120, 120))

item_1_images = [item_1]
item_2_images = [item_2]

 #아이템 1
wall_new()

castle_rect = pygame.Rect(castle.get_rect()) # 성
castle_rect.left = -360
castle_rect.top = 214

#보석 그룹
item_1_group = pygame.sprite.Group()  #보석(아이템) 객체들을 하나씩 추가.
item_2_group = pygame.sprite.Group()

# 미사일
miss_image = pygame.image.load(os.path.join(load_path, "miss.png"))
miss_image = pygame.transform.scale(miss_image, (50, 80))  # 100 312
miss = C_missile(miss_image, (100,691))

running = True
a = random.randint(1,2) # 유닛 낙하속도
ch, new, nak = 0, 0, 0     #ch = 미사일이 아이템을 잡았을 경우   nak = 아이템1,2 선택판별
castle_hp, p = 100, 10  #castle_hp = 성벽 체력  /  p = 아이템벽 충돌 제한
score, unit_count = 0, 0 # score = 점수    //   unit_count = 증가되는 유닛 수
#=============================================================
file_exists = exists("score.txt")
if file_exists == True :
    scoreFile = open("score.txt", "r")
    best_score = int(scoreFile.readline())
    scoreFile.close()
else :
    best_score = 0
#=============================================================
for j in range(7):
    Unit_12()
    
while running:
    screen.fill(BLACK)
    clock.tick(25) 
    screen.blit(back, (0,0) ) 
     
    if castle_hp > 40:  #성체력 판별 
        cas = castle
        screen.blit(cas, castle_rect)
    elif castle_hp <= 40:
        tle = castle_crack
        screen.blit(tle, castle_rect)
    ####
    item_2_group.draw(screen)
    item_1_group.draw(screen) 
    ####
         
    for event in pygame.event.get():       
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if not game_over:
                if miss.direction != stop:  
                    if event.key == K_SPACE:  
                        shot.play()
                        miss.set_direction(stop)  
                        to_y = move_speed #move_speed만큼 빠르게 뻗음 
                                    
    if not game_over:          
        if  miss.rect.right > 1280 or miss.rect.top < 0: 
            to_y = 0
            miss.set_init_state()   #처음상태

    #================================ 아이템이 바닥 닿으면 지워짐    
        for item_1 in item_1_group:  
            if item_1.rect.top > 650:
                item_1_group.remove(item_1)
        for item_2 in item_2_group:
            if item_2.rect.top > 650:
                item_2_group.remove(item_2)
    
    #================================유닛
        for unit in unit_list:
            unit['rect'].right -= unit['dy']
            unit['rect'].top += a
        
            if unit['rect'].right < 50 or unit['rect'].top > 600:
                marin.play()
                screen.blit(boom,unit['rect'])
                unit_list.remove(unit)   
    #================================
        if miss.offset.y > 0:   #반대방향 이상으로 갈때. 다시 돌아옴 
            to_y = 0
            miss.set_init_state()   
            if caught_item_1: 
                new_wall.play()
                item_1_group.draw(screen) 
                p = 10
                wall_rect.left = random.randint(250,1000)
                wall_rect.top = random.randint(100,600)
                item_1_group.remove(caught_item_1)  #그룹에서 잡힌 아이템 제외
                caught_item_1 = None 
                    
            if caught_item_2:  
                castle_hp = 100
                item_2_group.draw(screen)
                item_2_group.remove(caught_item_2)
                caught_item_2 = None
                heal.play()  
        ####
        if not caught_item_1: 
            ch = 0
            for item_1 in item_1_group:  
                if miss.rect.colliderect(item_1.rect):  
                    item_1.rect.top += 0
                    caught_item_1 = item_1   
                    to_y = -item_1.speed    
                    break  
                item_1.rect.top += random.randint(1,6)  
                   
        if not caught_item_2:    
            ch = 0
            for item_2 in item_2_group:
                if miss.rect.colliderect(item_2.rect):
                    item_2.rect.top += 0
                    caught_item_2 = item_2
                    to_y = -item_2.speed
                    break
                item_2.rect.top += random.randint(1,6)
       
        if caught_item_1 or caught_item_2: 
            ch = 1    
            if caught_item_1:
                rope.play()
                caught_item_1.set_position(miss.rect.center)

            elif caught_item_2:
                rope.play()
                caught_item_2.set_position(miss.rect.center)
    #print(ch)            
    ###########################미사일
        for unit in unit_list:
            screen.blit(unit_image, unit['rect'])
            
            if ch == 1:
                if unit['rect'].colliderect(castle_rect):
                    boom_wav.play()
                    screen.blit(boom,unit['rect'])
                    unit_list.remove(unit)
       
            if ch == 0:
                if unit['rect'].colliderect(miss.rect):
                    boom_wav.play()
                    screen.blit(boom,unit['rect'])
                    score += 10
                    to_y = 0
                    miss.set_init_state()   
                    unit_list.remove(unit)
            
                    if caught_item_1 or caught_item_2:
                        if caught_item_1:
                            item_1_group.remove(caught_item_1)  
                            caught_item_1 = None 
                        
                        elif caught_item_2:
                            item_2_group.remove(item_2)
                            item_2 = None
                ####
                elif unit['rect'].colliderect(wall_rect) or unit['rect'].colliderect(castle_rect):
                    screen.blit(boom, unit['rect'])
                    unit_list.remove(unit) 
                    if unit['rect'].colliderect(wall_rect):  
                        boom_wav.play()
                        p -= 1
                        if p == 0:
                            back_wall.play()
                            wall_new() 
                            p = 10
                             
                    elif unit['rect'].colliderect(castle_rect):  
                        marin.play()
                        castle_hp -= 10
                        if castle_hp == 0:
                            fail.play()
                            game_over = True

    ########################### 
        if len(unit_list) == 0:        #유닛 모두 제거
            clear.play()
            new += 1
            for j in range(7+unit_count): 
                Unit_12()

            if new % 4 == 0:  
                if (nak == 0 and len(item_1_group) == 0):
                    item_1_new()
                    nak =1
        
                elif nak == 1 and len(item_2_group) == 0:
                    item_2_new() 
                    nak = 0
                unit_count += 2    ######### 해당 부대 스테이지 다 깬 후에 인원 증가 == unit_count 
                
    ###########################
    #print("남은 사람 : ",len(unit_list)," 성 체력 : ",castle_hp," wall 체력 : ",p," 부대 : ",new, "그룹",nak, "item_1_group",len(item_1_group), "item_2_group",len(item_2_group))  

    screen.blit(rok, (10,600))
    screen.blit(walls, wall_rect)
    screen.blit(warning, (wall_rect.left+55,wall_rect.top-60))
    
    miss.update(event,to_y) 
    miss.draw(screen)  
    
    enemy_image = sysfont.render("Enemy : {}".format(len(unit_list)),True, (255, 255, 255)) 
    kill_group = sysfont.render("Kill Group : {}".format(new),True, (255, 255, 255))  
    score_image = sysfont.render("Score {}  |  Best Score {}".format(score, best_score),True, (255, 255, 255)) 
    wall_image = sysfont.render("{}".format(p),True, (255, 0, 0))   # p = 아이템 벽의 충돌제한 횟수
    hp_image = sysfont.render("HP : {}".format(castle_hp), True, (0, 255, 0))   
    
    fail_rogo = fail_font.render("FAIL",True, (255, 0, 0))  
    
    screen.blit(score_image, (screen_width/2, 10)) 
    screen.blit(kill_group, (5, 10))
    screen.blit(enemy_image, (5, 50))
    screen.blit(wall_image, (wall_rect.left+130,wall_rect.top-25)) 
    screen.blit(hp_image, (50,150))

    pygame.draw.rect(screen,(255,0,0),(0, 180, castle_hp*2, 20)) 
    pygame.draw.rect(screen,(255,255,255),(0, 180, 200, 20), 3)
    
    if game_over == True:
        screen.blit(castle_boom,(0,0))
        pygame.mixer.music.stop() #배경음악 STOP
        screen.blit(fail_rogo, (320,225))

        if best_score < score :
            best_score = score
            scoreFile = open("score.txt", "w")
            scoreFile.writelines(str(best_score))
            scoreFile.close() 
    
    pygame.display.update()  
pygame.quit()
