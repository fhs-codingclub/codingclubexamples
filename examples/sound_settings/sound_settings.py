import pygame, sys
import pygame_menu

# Full disclosure students, this is certainly not the best way to manage menus in pygame_menu. You should use menu linking instead. This was simply to show how to set up a very simple menu interaction for sound. Enjoy!
pygame.init()
pygame.mixer.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Volume Test')
pygame.mixer.music.load('testsong.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def set_volume(value):
    pygame.mixer.music.set_volume(float(value) / 100)
    print(f'Volume set to {value}%')
def volume_menu():
    volume = pygame_menu.Menu('Volume', 600, 400, theme=pygame_menu.themes.THEME_DARK)
    volume.add.range_slider('Volume', default=50, range_values=(0, 100), increment=1, value_format=lambda x: str(int(x)), onchange=set_volume)
    volume.add.button('Back', pygame_menu.events.BACK)
    volume.mainloop(surface)
def settings_menu():
    settings = pygame_menu.Menu('Settings', 600, 400, theme=pygame_menu.themes.THEME_DARK)
    settings.add.button('Volume', volume_menu)
    settings.add.button('Back', main_menu)
    settings.mainloop(surface)
def main_menu():
    main_menu = pygame_menu.Menu('Volume Test', 600, 400, theme=pygame_menu.themes.THEME_DARK)
    main_menu.add.button('Settings', settings_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.mainloop(surface)
main_menu()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()