import pygame 
import random
import math

# instalasi
pygame.init()

# menentukan ukuran screen
height = 300
width  = 550

screen = pygame.display.set_mode([height,width])

# mengubah title
pygame.display.set_caption("Spaceship Game")
# mengubah logo
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# player
def player(x,y):
    img_player = pygame.image.load("spaceship.png")
    screen.blit(img_player,(x,y))

x_player = 140
y_player = 510
x_player_point = 0

# enemy 
def enemy(x,y):
    img_enemy = pygame.image.load("enemy.png")
    screen.blit(img_enemy,(x,y))

x_enemy = random.randint(50,200)
y_enemy = random.randint(5,10)
y_enemy_point = 6

# collision
def collision(x_player,y_player,x_enemy,y_enemy):
    distance = math.sqrt(math.pow(x_player-x_enemy,2)) + (math.pow(y_player-y_enemy,2))
    if distance < 10:
        return True
    else:
        return False

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 16)

def show_score(x,y):
    score_number = font.render("score:" + str(score), True, (255,255,255))
    screen.blit(score_number,(x,y))

x_score = 10
y_score = 10

clock = pygame.time.Clock()

running = True
while running:
    # mengubah warna Screen
    screen.fill((0,0,0))
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player_point -= 5
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player_point += 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player_point = 0

    # movement player
    x_player += x_player_point
    if x_player >= 270:
        x_player = 260
    if x_player <= 10:
        x_player = 35

    # movement enemy
    y_enemy += y_enemy_point
    if y_enemy >= 540:
        x_enemy = random.randint(50,200)
        y_enemy = random.randint(5,10)
        score += 1

    if score == 6:
        break
    
    # collision
    tabrakan = collision(x_player,y_player,x_enemy,y_enemy)
    if tabrakan:
        break

    clock.tick(60)
    # show player
    player(x_player, y_player)
    # show enemy
    enemy(x_enemy,y_enemy)
    # show score
    show_score(x_score,y_score)

    pygame.display.update()

pygame.quit()

print("score anda :", score)