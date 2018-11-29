import math
import random
from itertools import combinations
from multiprocessing import Queue
import queue

import pygame

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 255)
GREEN = (0, 255, 0)
VIOLET = (255, 0, 255)
SMALL_CIRCLE_SIZE = 5
INITIAL_MASS = 12


class Player:
    def __init__(self, id, x, y):
        self.id = id
        self.mass = INITIAL_MASS
        self.color = (random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))
        self.posx = x
        self.posy = y
        self.command = ''


class OgarIOGame:
    def __init__(self, queue: Queue):
        self.players = {}
        self.queue = queue
        pygame.init()
        self.width, self.height = 1800, 900
        self.offset = 20
        self.max_x, self.max_y = self.width - self.offset, self.height - self.offset

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ogar.io server")
        self.clock = pygame.time.Clock()

        self.food = [(random.randint(self.offset, self.max_x), random.randint(self.offset, self.max_y))
                     for i in range(20)]

    def update(self, frame):
        # sleep to make the game 60 fps
        self.clock.tick(60)
        self.screen.fill(0)

        if frame % 5 == 0:
            self.add_food()

        if frame % 60 * 5 == 0:
            self.loose_mass()

        self.eat_food()
        self.eat_players()
        self.process_events()
        self.receive_player_commands()
        self.update_players()

        # update the screen
        pygame.display.flip()

    def update_players(self):
        for player in self.players.values():
            self.move_player(player)
            pygame.draw.circle(self.screen, player.color, (player.posx, player.posy), round(player.mass), 2)

    def receive_player_commands(self):
        try:
            command, user = self.queue.get_nowait()
            if user not in self.players:
                self.create_player(user)
                print('player added')
            self.players[user].command = command
        except queue.Empty:
            pass

    def process_events(self):
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

    def eat_food(self):
        for food_piece in self.food:
            pygame.draw.circle(self.screen, VIOLET, food_piece, SMALL_CIRCLE_SIZE, 3)
            x1, y1 = food_piece
            for player in self.players.values():
                dist = math.hypot(x1 - player.posx, y1 - player.posy)
                if dist < abs(SMALL_CIRCLE_SIZE - player.mass) and food_piece in self.food:
                    self.food.remove(food_piece)
                    player.mass += 0.5
        #             TODO: bug!

    def eat_players(self):
        for player1, player2 in combinations(self.players.values(), 2):
            dist = math.hypot(player1.posx - player2.posx, player1.posy - player2.posy)
            if dist < abs(SMALL_CIRCLE_SIZE - player1.mass):
                if player1.mass > player2.mass:
                    player1.mass += player2.mass / 2
                    del self.players[player2.id]
                    break
                elif player2.mass > player1.mass:
                    player2.mass += player1.mass / 2
                    del self.players[player1.id]
                    break

    def start(self):
        frame = 0
        while True:
            self.update(frame)
            frame += 1

    def add_food(self):
        self.food.append((random.randint(self.offset, self.max_x), random.randint(self.offset, self.max_y)))

    def move_player(self, player):
        x = player.posx
        y = player.posy
        command = player.command
        speed = round(10 * INITIAL_MASS / player.mass) + 1
        if command == 'up' and y > self.offset:
            y -= speed
        elif command == 'down' and y < self.max_y:
            y += speed
        elif command == 'right' and x < self.max_x:
            x += speed
        elif command == 'left' and x > self.offset:
            x -= speed

        player.posy = y
        player.posx = x

    def create_player(self, id):
        self.players[id] = Player(id, random.randint(self.offset, self.max_x), random.randint(self.offset, self.max_y))

    def loose_mass(self):
        for player in self.players.values():
            player.mass -= 2
            player.mass = max(player.mass, INITIAL_MASS)
