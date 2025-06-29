import pygame
class Venom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.stand_image = pygame.transform.scale(
            pygame.image.load("images/Sprites/venom_stand.png"), (100, 100)
        )
        # Load original (right-facing) walk images
        self.original_walk_images = [
            pygame.transform.scale(pygame.image.load(f"images/Sprites/venom_walk{i}.png"), (100, 100))
            for i in [1, 2, 3, 4, 4, 6]
        ] + [pygame.transform.scale(pygame.image.load("images/Sprites/venom__walk7.png"), (100, 100))]

        self.original_punch_images = [
            pygame.transform.scale(pygame.image.load(f"images/Sprites/venom_punch{i}.png" if i else "images/Sprites/venom_punch.png"), (100, 100))
            for i in ["", 2, 3, 4]
        ]
        self.hammer_image = pygame.transform.scale(
            pygame.image.load("images/Sprites/venom_hammer.png"), (100, 100)
        )

        self.image = self.stand_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.walk_index = 0
        self.punch_index = 0
        self.speed = 1.1
        self.direction = "right"
        self.attacking = False
        self.attack_range = 80
        self.anim_timer = 0
        self.anim_delay = 100

    def update(self, player_rect):
        dx = player_rect.centerx - self.rect.centerx

        if abs(dx) > self.attack_range:
            self.attacking = False
            self.direction = "right" if dx > 0 else "left"
            if self.direction == "right" :
                 self.rect.x += self.speed 
            else:
                 self.rect.x -= 1
            self._animate_walk()
        else:
            self.attacking = True
            self._animate_attack()

    def _animate_walk(self):
        now = pygame.time.get_ticks()
        if now - self.anim_timer > self.anim_delay:
            self.walk_index = (self.walk_index + 1) % len(self.original_walk_images)
            img = self.original_walk_images[self.walk_index]
            if self.direction == "left":
                img = pygame.transform.flip(img, True, False)
            self.image = img
            self.anim_timer = now

    def _animate_attack(self):
        now = pygame.time.get_ticks()
        if now - self.anim_timer > self.anim_delay:
            self.punch_index = (self.punch_index + 1) % len(self.original_punch_images)
            img = self.original_punch_images[self.punch_index]
            if self.direction == "left":
                img = pygame.transform.flip(img, True, False)
            self.image = img
            self.anim_timer = now

    def hurt(self):
        print("Venom hurt!")
