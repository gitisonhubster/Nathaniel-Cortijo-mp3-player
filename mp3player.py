import pygame
pygame.mixer.init()
pygame.display.init()
pygame.display.set_mode(size=(400, 800))
if pygame.mixer.get_init is None:
    print("none")
pygame.mixer.music
pygame.mixer.music.load('Union_Dixie_Trap_Remix.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(1)
if pygame.mixer.music.get_busy() == True:
    print("huh")

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False