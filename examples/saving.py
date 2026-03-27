# Hello students! This is a tutorial that I learned from Clear Code at https://www.youtube.com/watch?v=__mZO-53PPM. I commented on it to help some of the code make more sense!
import pygame, sys # This is simply to use pygame and the system for closing the game and starting pygame
import json # This allows you to read and write json (JavaScript Object Notation) files using python!

pygame.init() #The GOAT at starting games

# Set up the display
WIDTH = 600 
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # We need to see the screen
clock = pygame.time.Clock() # Gotta get that fps
game_font = pygame.font.Font(None, 24) # I'm not picky about what font, but how big it is
pygame.display.set_caption("Saving") # Such a creative game name

#Data
data = {
    'red_score': 0,
    'blue_score': 0
} # This is essentially creating a "dictionary" for us that can be altered, as they are "mutable (changeable)"
try: #Python lets us do something really cool in attempting to do things that have a "back-up plan" called "except"
    with open('save.json','r') as read_file: #The open() function lets us open a json file and define it as a variable
        data = json.load(read_file) # This does a few things: it redefines our dictionary, parses the json, and lets us "read" written data
except FileNotFoundError: # This is the "back-up plan"
    print("No save file found, starting with default data.") #Simple console log, allows us to continue the script

#Rectangles
red_rurf = pygame.Surface((100, 100)) # What does the rectangle look like?
red_rurf.fill((255, 0, 0)) # What color is it?
red_rect = red_rurf.get_rect(center=(200, 180)) # What actual structure is the red, 100 x 100 pixel rectangle going on?

blue_surf = pygame.Surface((100, 100))
blue_surf.fill((0, 0, 255))
blue_rect = blue_surf.get_rect(center=(400, 180))

red_score_surf = game_font.render(f'red: {data["red_score"]}', True, 'black') # We make a spot for the text
red_score_rect = red_score_surf.get_rect(center=(200, 300)) # We put that text on a rectangle in that space
blue_score_surf = game_font.render(f'blue: {data["blue_score"]}', True, 'black')
blue_score_rect = blue_score_surf.get_rect(center=(400, 300))

# Main game loop
running = True
while running: # Normal pygame quit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('save.json', 'w') as write_file: # This is the change: this allows us to "dump" dictionary infomation into a json file
                json.dump(data, write_file)
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # Like keydown, this allows us to click things
            if red_rect.collidepoint(event.pos): # collidepoint() as a function allows us to see if something collides with the rectangle or object we made, in this case we check if the event of us clicking makes contact with the rectangle
                print("red") # Leftover testing code
                data["red_score"] += 1 # Adds 1 to the integer value in our dictionary for "red score"
                red_score_surf = game_font.render(f'red: {data["red_score"]}', True, 'black') # We have to re-render the font or our change won't be visibly seen

            elif blue_rect.collidepoint(event.pos):
                print("blue")
                data["blue_score"] += 1
                blue_score_surf = game_font.render(f'blue: {data["blue_score"]}', True, 'black')

    # Fill the background with white
    screen.fill((255, 255, 255)) # Fill the screen first

    # Draw the rectangles
    screen.blit(red_rurf, red_rect) # Put the rectangles and scores on structural rectangles
    screen.blit(blue_surf, blue_rect)
    screen.blit(red_score_surf, red_score_rect)
    screen.blit(blue_score_surf, blue_score_rect)

    # Update the display
    pygame.display.flip() # We can use either .update() or .flip()
    clock.tick(60) # Clocking at 60fps
# Quit Pygame
pygame.quit() # Pygame exits
sys.exit() # The system closes the program