import pygame
from pygame.locals import *  #to access keyboard and mouse events
from time import *  #everything 


pygame.init() 
screen=pygame.display.set_mode((600, 600)) 
#initial position of rocket/player
player_x = 200 
player_y = 200


keys = [False, False, False, False]   
# up , left, down, right


player = pygame.image.load("character.png") 
background = pygame.image.load("background.png")


while player_y < 600: 
  screen.blit(background, (0,0)) 
  screen.blit(player, (player_x, player_y)) 
  pygame.display.flip()


  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
    # if it is quit the game
      pygame.quit() 
      exit(0)


    #check if any keyboard button is pressed 
    if event.type == pygame.KEYDOWN: 
      #check which button is pressed 
      if event.key==K_UP: 
        keys[0]=True 
      elif event.key==K_LEFT: 
        keys[1]=True
      elif event.key==K_DOWN: 
        keys[2]=True 
      elif event.key==K_RIGHT:
        keys[3]=True


    #check if any keyboard button is released 
    if event.type == pygame.KEYUP:  
      #check which button is released 
      if event.key==pygame.K_UP: 
        keys[0]=False 
      elif event.key==pygame.K_LEFT: 
        keys[1]=False 
      elif event.key==pygame.K_DOWN: 
        keys[2]=False 
      elif event.key==pygame.K_RIGHT:
        keys[3]=False


  # If the up button is pressed 
  if keys [0]: 
    if player_y>0: 
    # If the coordinate is greater than 0 (not outside the playing field) 
      player_y -= 2 
      # Change the y position by pixels. The player moves upwards


  # If the down button is pressed 
  elif keys [2]: 
    if player_y<536: 
      # If the coordinate is greater than 0 (not outside the playing field) 
      player_y += 2 
      # Change the y position by pixels. The player moves upwards


  # If the left button is pressed 
  if keys [1]: 
    if player_x>0: 
      # If the player is inside the playing field
      player_x -= 2 
      # Decrease X position. The player goes left


  # If the right button is pressed 
  elif keys [3]: 
    if player_x<536: 
      # If the player is inside the playing field
      player_x += 2 
      # Increase X position. The player goes right


    #assume the gravity is applying on the rocket so the rocket will move down continuosly
  player_y+=5
  sleep(0.05)
    #to update the screen
print("Game Over")
    


  