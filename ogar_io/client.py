import pygame
import requests

s = requests.Session()
pygame.init()
pygame.display.set_caption("OgarIO")
screen = pygame.display.set_mode((300, 300))
url = 'http://localhost:5000/'

while True:
    event = pygame.event.poll()
    # quit if the quit button was pressed
    if event.type == pygame.QUIT:
        exit()
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_UP]:
            s.get(url + 'up')
        if keys[pygame.K_DOWN]:
            s.get(url + 'down')
        if keys[pygame.K_RIGHT]:
            s.get(url + 'right')
        if keys[pygame.K_LEFT]:
            s.get(url + 'left')
