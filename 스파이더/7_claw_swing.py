#집게 ()좌우로 이동시키기.  나는 위아래로
import pygame, os

#집게클래스 (줄)
class line(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image  #회전시 이미지
        self.rect = image.get_rect(center = position)  #1

        self.offset = pygame.math.Vector2(default_x_claw,default_y_claw)  #x, y로 이동
        self.position = position

        self.direction =  LEFT      #왼쪽,오른쪽 방향 판별  // #집게 이동방향
        self.angle_speed = 2.5 #각도로 커진다. (좌,우 이동속도)  클수록 빨리움직임
        self.angle = 0 #최초 각도 정의 (오른쪽 끝)

    def update(self):  #가만히 숨쉬는것처럼. 혼자이동   ◆이미지 당기기  중심점
        #rect_center = self.position + self.offset #__init position으로부터 offset을 더하는거 계산.
        #self.rect = self.image.get_rect(center = rect_center)  #get_rect할때 center위치를 rect_center로 업데이트
        
        if self.direction == LEFT:     #오른쪽 방향으로 이동하고있다면
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
 
        #if 허용각도 범위 벗어나면? \
        if self.angle > 90:
            self.angle = 90
            self.direction = RIGHT
        if self.angle < 0:
            self.angle = 0
            self.direction = LEFT
        
        self.rotate() #회전처리

        print(self.angle, self.direction)

    def rotate(self):  #회전   #새로회전해서 나온 이미지▼▼▼▼
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1) #rotozoom 이미지 회전및 크기조절  #각도에 따라 회전 1.회전시킬 이미지, 각도, 이미지크가(1) 
        
        #offset데이터를 angle에 맞춰서 회전시킨 새롭게 만들어진 offset을 받아옴
        offset_rotated = self.offset.rotate(self.angle)#집게 각도에 따라 회전한 값을 전달받음
        #print(offset_rotated)  

        #회전된 변경한 값을 self.rect에 넣음
        self.rect = self.image.get_rect(center = self.position + offset_rotated) #새로운 이미지로부터 get_rect한다. 그때 이미지의 center정보 업데이트
        #print(self.rect) #x,y좌표 위치와 높이넓잌 크기
        pygame.draw.rect(screen, RED, self.rect, 1)

    
    def draw(self, screen):  #update시 바뀐 이미지로 그림
        screen.blit(self.image, self.rect) #클래스 객체가 가지는 #1 image와 rect(x랑y) 정보를 통해 그림
        pygame.draw.circle(screen, RED, self.position, 3) #위치 = self.position 처음으로 // 중심점
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)  #어디까지= claw의 rect의 중심점까지
        # ↑ 직선그리기

# 보석클래스  (구름)
class gem(pygame.sprite.Sprite):  #Sprite상속. (부모)  클래스 정의
    def __init__(self, image, position):  #객체마다 어떤 image쓰고 위치.힐건지
        super().__init__()
        self.image = image  #캐릭터가 가지는 이미지 파일  
        self.rect = image.get_rect(center = position)  #캐릭터가 가지는 정보 (가로,세로) / 움직일때마다 위치 
         
def setup_gem():
    #작은금(구름)
    cloud = gem(cloud_images[0], (650,150)) #[0]번째 이미지를 200*380 위치에 둠
    spider_group.add(cloud) #그룹에 추가

    #큰 금 (비구름)
    spider_group.add(gem(cloud_images[1], (1000,150)))


pygame.init()
screen_width, screen_height = 1280, 720

screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("Spider_man")     #게임제목
clock = pygame.time.Clock()

#게임 줄 관련변수
default_x_claw = 0  #중심점에서 줄까지의 x간격 90
default_y_claw = -200                          

LEFT = -1  #왼쪽 방향으로
RIGHT = 1  #오른쪽 방향으로


#색깔 변수
RED = (255,0,0)  #빨강
BLACK = (0,0,0)  #검정


#배경 불러오기
current_path = os.path.dirname(__file__)  #현재 파일 위치반환
back = pygame.image.load(os.path.join(current_path, "back.png"))

#이미지 불러오기. (구름, 벽? , 먹구름)
cloud_images = [
    pygame.image.load(os.path.join(current_path, "cloud.png")), #os.경로설정 후 현재위치 current_path에 사진. 
    pygame.image.load(os.path.join(current_path, "rain_cloud.png")) #먹구름
]

#보석 그룹
spider_group = pygame.sprite.Group()  #보석(구름) 객체들을 하나씩 추가.
setup_gem() #게임에 원하는 만큼의 보석을 정의

# 집게 (줄)
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = line(claw_image, (150,500))


running = True
while running:
    clock.tick(30)  #FPS 30고정  게임속도 일정.
    for event in pygame.event.get():       #이벤트 반복 확인. 이벤트 받아오기
        if event.type == pygame.QUIT:
            running = False

    screen.blit(back, (0,0) ) #배경, 위치(x,y)

    spider_group.draw(screen) #screen에다 spider그룹엔의 모든 sprite를 다 그린다.

    claw.update() #update함수 통해서 rect정보 업데이트 됨
    claw.draw(screen)   # 그다음 화면에 그려짐 

    pygame.display.update()

pygame.quit() #진짜종료