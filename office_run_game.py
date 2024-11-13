import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score:{current_time}',False,'Black')
    score_rect = score_surf.get_rect(center = (400,350))
    screen.blit(score_surf,score_rect)

    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Office jump')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True

sky_surface = pygame.image.load('Graphics/cityback.png')
ground_surface = pygame.image.load('Graphics/pathroadn.png')
text_surface = test_font.render('Office Jump', False, 'White')

hydrant_surface = pygame.image.load('Graphics/hydrant1.png')
hydrant_rect = hydrant_surface.get_rect(midbottom = (600,320))
hydrant_rect.x = 600

man_surface = pygame.image.load('Graphics/dbk.png')
man_rect = man_surface.get_rect(midbottom = (80,320))
gravity = 0
start_time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_active:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and man_rect.bottom == 320:
                    gravity = -17
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                hydrant_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
                
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,320))
        screen.blit(text_surface,(300,50))
        display_score()
        hydrant_rect.x -= 4
        
        if hydrant_rect.right <= 0: hydrant_rect.left = 800
        screen.blit(hydrant_surface,hydrant_rect)
        
        gravity += 1
        man_rect.y += gravity
        if man_rect.bottom >= 320: man_rect.bottom = 320
        screen.blit(man_surface,man_rect)
    
        if hydrant_rect.colliderect(man_rect):
            game_active = False

    
    pygame.display.update()
    clock.tick(60)