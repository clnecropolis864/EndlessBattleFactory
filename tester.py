"""
import calc
import trainer
import pokedex as dex
modifier = [1, 1, 1, 1.5, 2, 1, 1]

#print calc.damageCalc(30, 150, 71, 45, modifier)

party = [dex.charizard(), dex.venusaur(), dex.blastoise()]
you = trainer.Trainer("Chuck", party)
print(type(you))
"""
import textbox
import pygame
pygame.init()

# Create TextInput-object
textinput = textbox.TextInput()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)

