import pygame
import tkinter as tk
pygame.mixer.init()
pygame.display.init()
pygame.display.set_mode(size=(400, 800))
if pygame.mixer.get_init is None:
    print("none")
pygame.mixer.music.load('Union_Dixie_Trap_Remix.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(1)
Paused = False

running = True


while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if Paused == False:
                    pygame.mixer.music.pause()
                    Paused = True
                elif Paused == True:
                    pygame.mixer.music.unpause()    
                    Paused = False
