import pygame

pygame.init()

#setting up the game window

window_witdh=800
window_height=600
window= pygame.display.set_mode((window_witdh,window_height))
pygame.display.set_caption("Snake Game")

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      game_over=True

#creating function
