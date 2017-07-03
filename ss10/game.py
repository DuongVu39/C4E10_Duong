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
        pixel = 64
        w = (pixel - object.image.get_width()) / 2 + object.x * pixel
        h = (pixel - object.image.get_height())/ 2 + object.y * pixel
        screen.blit(object.image, (w, h))

    def draw(self, screen, ground_image):
        #draw in pygame:
        pixel = 64
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(ground_image, (x * pixel, y * pixel))

        self.draw_image_center(self.box, screen)
        self.draw_image_center(self.dest, screen)
        self.draw_image_center(self.pusher, screen)

    def in_map(self, object, dx, dy):
        if 0 <= object.x + dx < self.map.width and 0 <= object.y + dy < self.map.height:
            return True
        else:
            return False

    def reset_level(saved_pusher, saved_boxes):
        global pusher, boxes
        pusher = saved_pusher
        boxes = saved_boxes

    def handle_input(self, event):
        dx = 0
        dy = 0
        # saved_pusher = self.pusher.copy()
        # saved_boxes = self.box.copy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy -= 1
            elif event.key == pygame.K_DOWN:
                dy += 1
            elif event.key == pygame.K_RIGHT:
                dx += 1
            elif event.key == pygame.K_LEFT:
                dx -= 1
            elif event.key == pygame.K_ESCAPE:
                quit()
            # elif event.key == pygame.K_F5:
            #     self.reset_level(saved_pusher, saved_boxes)
            #     self.draw(screen,ground_image)
            #  #level saved

        if self.pusher.collide(self.box, dx, dy):
            if self.in_map(self.box, dx, dy):
                self.box.move(dx, dy)
                self.pusher.move(dx, dy)
        elif self.in_map(self.pusher, dx, dy):
            self.pusher.move(dx, dy)
        elif self.box.check_win(self.dest):
            self.draw_image_center(screen, win_image)
            time.sleep(10)
            quit()

