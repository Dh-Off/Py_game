#보석이미지 불러오기. (구름)
import pygame, os

# 보석클래스
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
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("Spider_man")     #게임제목
clock = pygame.time.Clock()

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


running = True
while running:
    clock.tick(30)  #FPS 30고정  게임속도 일정.
    for event in pygame.event.get():       #이벤트 반복 확인. 이벤트 받아오기
        if event.type == pygame.QUIT:
            running = False

    screen.blit(back, (0,0) ) #배경, 위치(x,y)

    spider_group.draw(screen) #screen에다 spider그룹엔의 모든 sprite를 다 그린다.
    
    pygame.display.update()

pygame.quit() #진짜종료