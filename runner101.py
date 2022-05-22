import pygame
from sys import exit
import time
from pickle import TRUE
from tkinter import CENTER

#functie pentru scor
def display_score():
  current_time = int(pygame.time.get_ticks() / 150 ) - start_time
  score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
  score_rect = score_surf.get_rect(center = (400, 50))
  screen.blit(score_surf, score_rect)
  return current_time
 
pygame.init()
screen = pygame.display.set_mode((800, 400))
icon = pygame.image.load('stand.png').convert_alpha()
pygame.display.set_icon(icon)

pygame.display.set_caption("Runner") 
icon = pygame.image.load('jump.png').convert_alpha()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True 
start_time = 0
score = 0

#importare imagini pentru sky, ground, snail si player
sky_surf = pygame.image.load("Sky.png").convert()
ground_surf = pygame.image.load('ground.png').convert()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom =(80, 300))
player_gravity = 0

player_stand = pygame.image.load('stand.png'). convert_alpha()
player_stand = pygame.transform.scale(player_stand, (77, 100))
player_stand_rect = player_stand.get_rect( center = (400, 200))

game_message =  test_font.render("Press space to play", False,(111,196,169))
game_message_rect = game_message.get_rect( center = (400, 350))

game_name = test_font.render("Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 50))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer

#while-ul principal, jocul efectiv
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

      if game_active:
        if event.type == pygame.MOUSEBUTTONUP:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
              player_gravity = -20

        if event.type == pygame.KEYDOWN:
          if event.key ==pygame.K_SPACE and player_rect.bottom >= 300:
            player_gravity = -20
      else :
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
          game_active = True
          snail_rect.left = 800 
          start_time = int(pygame.time.get_ticks() / 150 )

    if game_active:   
      screen.blit(sky_surf, (0,0))
      screen.blit(ground_surf, (0, 300))
      score = display_score()  

      snail_rect.x -= 10
      if snail_rect.right <= 0: snail_rect.left = 800
      screen.blit(snail_surf, snail_rect)
        
      #gravitatie pentru caracter
      player_gravity += 1
      player_rect.y += player_gravity
      if player_rect.bottom >= 300:player_rect.bottom = 300
      screen.blit(player_surf,player_rect)
#daca exista colisiune, jocul devine inactiv

      if snail_rect.colliderect(player_rect):
        game_active = False 


    else:
       screen.fill((90, 100, 162))
       screen.blit(player_stand, player_stand_rect)

       score_message = test_font.render(f'Your score: {score}', False,(111, 196, 169) )
       score_message_rect = score_message.get_rect( center = (400, 350))
       screen.blit(game_name, game_name_rect)

       if score == 0: screen.blit(game_message, game_message_rect)
       else:screen.blit(score_message, score_message_rect)
      
    pygame.display.update()   
    clock.tick(60) 