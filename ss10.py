import pygame

class Game:
    def __init__(self):
        pass

    def console_draw(self):
        #draw in console
        for y in range(self.map.height):
            for x in range(self.map.width):
                if y == self.dest.y and x == self.dest.x:
                    print(" D ", end = "")
                elif y == self.box.y and x == self.box.x:
                    print(" B ", end = "")
                elif y == self.pusher.y and x == self.pusher.x:
                    print(" P ", end = "")
                else:
                    print (" - ", end = "")
            print()
    def draw_image_center(self, object, screen):
        w = (pixel - object.image.get_width()) / 2 + object.x * pixel
        h = (pixel - object.image.get_height())/ 2 + object.y * pixel
        screen.blit(object.image, (w, h))

    def draw(self):
        #draw in pygame:
        pixel = 64
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(ground_image, (x * pixel, y * pixel))


        self.draw_image_center(self.pusher, screen)
        self.draw_image_center(self.box, screen)
        self.draw_image_center(self.dest, screen)

    def in_map(self, object, dx, dy):
        if 0 <= object.x + dx < self.map.width and 0 <= object.y + dy < self.map.height:
            return True
        else:
            return False


    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy -= 1
            elif event.key == pygame.K_DOWN:
                dy += 1
            elif event.key == pygame.K_RIGHT:
                dx += 1
            elif event.key == pygame.K_LEFT:
                dx -= 1
        if self.pusher.collide(self.box, dx, dy):
            if self.in_map(self.box, dx, dy):
                self.box.move(dx, dy)
                self.pusher.move(dx, dy)
        elif self.in_map(self.pusher, dx, dy):
            self.pusher.move(dx, dy)

class Map:
    def __init__(self, w, h):
        self.width = w
        self.height = h

class Pusher:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def collide(self, object, dx, dy):
        if self.x + dx == object.x and self.y + dy == object.y:
            return True
        else:
            return False
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Dest:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#object = Class()
sokoban = Game()
sokoban.map = Map(5, 5)
sokoban.pusher = Pusher(1, 1)
sokoban.box = Box (2, 2)
sokoban.dest = Dest(3, 3)
sokoban.console_draw()

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False
box_image = pygame.image.load("images/Crate_Red.png")
pusher_image = pygame.image.load("images/pusher.png")
ground_image = pygame.image.load("images/Wall.png")
dest_image =  pygame.image.load("images/EndPoint_Red.png")
sokoban.box.image = box_image
sokoban.dest.image = dest_image
sokoban.pusher.image = pusher_image

pixel = 64

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        sokoban.handle_input(event)
    sokoban.draw()
    pygame.display.flip()



