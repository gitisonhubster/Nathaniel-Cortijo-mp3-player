import pygame
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None,)
if pygame.mixer.get_init is None:
    print("none")
pygame.mixer.music
pygame.mixer.music.load("Union_Dixie_Trap_Remix.mp3")
Union_Dixie_Trap_Remix = pygame.mixer.Sound("Union_Dixie_Trap_Remix.mp3")
pygame.mixer.Sound.play(Union_Dixie_Trap_Remix.mp3)