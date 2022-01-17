import random
import pygame
import sys

FPS = 50
pygame.init()
WIDTH = 1920
HEIGHT = 1080
player_width = 192
player_height = 128
tile_width = tile_height = 64


def create_frames(image_name, number, width=player_width, height=player_height):
    left_animation = []
    right_animation = []
    for i in range(number):
        file_name = image_name.format(i=i)
        right_image = pygame.image.load(file_name)
        right_image = pygame.transform.scale(right_image, (width, height))
        left_image = pygame.transform.flip(right_image, True, False)
        right_animation += [right_image]
        left_animation += [left_image]
    return right_animation, left_animation


attack_right_animation, attack_left_animation = create_frames('sprite_attack{i}.png', 4)
walk_right_animation, walk_left_animation = create_frames('sprite_run0{i}.png', 9)
idle_right_animation, idle_left_animation = create_frames('sprite_idle0{i}.png', 10)
jump_animation_right, jump_animation_left = create_frames('sprite_jump{i}.png', 3)

stealth_trans_right = pygame.image.load('stealth_transition.png')
stealth_trans_left = pygame.transform.flip(pygame.image.load('stealth_transition.png'), True, False)

hurt_left, hurt_right = create_frames('LightBandit_Hurt_{i}.png', 4, tile_width, tile_height)
hard_attack_right_animations, hard_attack_left_animations = create_frames('sprite_hard_attack{i}.png', 6)
walkLeft, walkRight = create_frames('LightBandit_Run_{i}.png', 16, tile_width, tile_height)
death_right, death_left = create_frames('LightBandit_Death_{i}.png', 3, tile_width, tile_height)
bandit_right = {'walk': walkRight,
                'hurt': hurt_right,
                'death': death_right
                }
bandit_left = {'walk': walkLeft,
               'hurt': hurt_left,
               'death': death_left
               }
animations_right = {'walk': walk_right_animation,
                    'jump': jump_animation_right,
                    'idle': idle_right_animation,
                    'attack': attack_right_animation,
                    'hard_attack': hard_attack_right_animations
                    }

animations_left = {'walk': walk_left_animation,
                   'jump': jump_animation_left,
                   'idle': idle_left_animation,
                   'attack': attack_left_animation,
                   'hard_attack': hard_attack_left_animations
                   }

tile_images = {
    'grass_1': pygame.image.load('grass_block_side.png'),
    'block': pygame.image.load('dirt_1.png'),
    'tree': pygame.image.load('tree.png'),
    'rock': pygame.image.load('rock_1.png'),
    'tree_dead': pygame.image.load('tree_dead.png'),
}
player_image = pygame.image.load('knight.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        d_x = 0
        d_y = 0
        if tile_type in ['tree', 'tree_dead']:
            width = height = 400
            self.image = pygame.transform.scale(self.image, (width, height))
            d_x = (width - tile_width) // 2
            d_y = height - tile_height
        self.rect = self.image.get_rect().move(
            tile_width * pos_x - d_x, tile_height * pos_y - d_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.cur_frame = 0
        self.level = []
        self.d_x = 0
        self.d_y = 0
        self.enemies = []
        self.left = False
        self.right = False
        self.right_side = True
        self.moving = False
        self.status = 'idle'

        self.velocity = 0
        self.max_velocity = 3
        self.jump_k = 1

        self.x_walk_speed = 1
        self.x_jump_speed = 1
        self.x_speed = self.x_walk_speed

        self.x = pos_x
        self.y = pos_y
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + (tile_width - player_width) // 2, tile_height * pos_y + (tile_height - player_height))

    def add_level(self, level):
        self.level = level

    def add_enemies(self, enemies):
        self.enemies = enemies

    def move(self):
        if self.moving:
            if self.right_side:
                d_x = self.x_speed
            else:
                d_x = -self.x_speed
            self.d_x += d_x
            if self.check():
                self.d_x -= d_x

    def base_jump(self):
        one_jump = self.velocity // abs(self.velocity)
        self.d_y -= one_jump*self.jump_k
        if self.check():
            self.d_y += one_jump*self.jump_k
            return False
        else:
            return True

    def check_fall(self):
        return self.level[self.y + 1][self.x] not in ["^", "-"]

    def jump(self, start=False):
        if not self.check_fall():
            if start:
                self.status = 'jump'
                self.velocity = self.max_velocity
        else:
            self.velocity -= 1
            self.status = 'jump'

        if self.status == "jump":
            self.x_speed = self.x_jump_speed

        success = False
        for i in range(abs(self.velocity)):
            success = self.base_jump()
        if not success:
            self.velocity = 0

        if not self.check_fall() and self.status == "jump":
            if self.moving:
                self.status = 'walk'
            else:
                self.status = 'idle'
            self.x_speed = self.x_walk_speed

    def attack(self, start=False):
        if self.status == 'attack':
            if start:
                self.cur_frame = 0
                for enemy in self.enemies:
                    enemy.hit(self.x, self.y)
            elif self.cur_frame >= len(attack_right_animation):
                if self.moving:
                    self.status = 'walk'
                else:
                    self.status = 'idle'

    def hard_attack(self, start=False):
        if self.status == 'hard_attack':
            if start:
                self.cur_frame = 0
            elif self.cur_frame >= len(hard_attack_right_animations):
                if self.moving:
                    self.status = 'walk'
                else:
                    self.status = 'idle'

    def check(self):
        y = self.y + int(self.d_y)
        x = self.x + int(self.d_x)
        if (x >= len(self.level[0]) or y >= len(self.level)
                or x < 0 or y < 0
                or self.level[y][x] == '-' or self.level[y][x] == '^'):
            return True
        else:
            return False

    def change_status(self, key, button_down, mouse_button=False):
        if button_down:
            if mouse_button and key == 1 and self.status in ['walk', 'idle']:
                self.status = 'attack'
                self.attack(start=True)
            if mouse_button and key == 3 and self.status in ['walk', 'idle']:
                self.status = 'hard_attack'
                self.hard_attack(start=True)
            if key == 100:
                self.right = True
                self.right_side = True
            if key == 97:
                self.left = True
                self.right_side = False
            if key == 32 and (self.status == 'walk' or self.status == 'idle'):
                self.jump(start=True)

        else:
            if key == 100:
                if self.left:
                    self.right_side = False
                self.right = False
            if key == 97:
                if self.right:
                    self.right_side = True
                self.left = False
        if self.right != self.left:
            self.moving = True
        else:
            self.moving = False
        if self.moving and self.status == 'idle':
            self.status = 'walk'
        if not self.moving and self.status == 'walk':
            self.status = 'idle'

    def update(self):
        if self.right_side:
            animations = animations_right
        else:
            animations = animations_left
        animation = animations[self.status]
        self.cur_frame %= len(animation)
        self.image = animation[self.cur_frame]
        self.cur_frame += 1

        self.move()

        d_x, d_y = int(self.d_x), int(self.d_y)
        self.rect.y += tile_height * d_y
        self.y += d_y
        self.d_y -= d_y
        self.rect.x += tile_width * d_x
        self.x += d_x
        self.d_x -= d_x

        self.jump()
        self.attack()
        self.hard_attack()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, end):
        super().__init__(all_sprites)
        self.image = walkLeft[0]
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.x = x
        self.y = y
        self.hp = 5
        self.status = 'walk'
        self.slow = 0
        if random.randint(0, 1):
            self.right_side = True
        else:
            self.right_side = False
        self.end = end
        self.start = self.x
        self.velocity_of_enemy = 0
        self.count_of_steps = 0
        self.cur_frame = 0

    def hit(self, x, y):
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= 2 ** 0.5:
            self.hp -= 1
            self.hurt(True)

    def hurt(self, start=False):
        if start:
            self.cur_frame = 0
            self.status = 'hurt'
        if self.cur_frame >= len(bandit_right['hurt']):
            self.status = 'walk'
        if self.hp <= 0:
            self.death()

    def death(self):
        self.status = 'death'

    def update(self):
        if self.status == 'death':
            self.image = pygame.transform.scale(pygame.image.load('LightBandit_Death_2.png'), (64, 64))
        else:
            if self.x >= self.end:
                self.right_side = False
            elif self.x < self.start:
                self.right_side = True
            if self.right_side:
                d_x = 1
                animations = bandit_right
            else:
                d_x = -1
                animations = bandit_left
            animation = animations[self.status]
            if self.status != 'walk' or self.slow % 5 != 0:
                d_x = 0
            self.slow += 1
            self.cur_frame %= len(animation)
            self.image = animation[self.cur_frame]
            self.cur_frame += 1
            self.hurt()
            self.rect.x += tile_width * d_x
            self.x += d_x


def load_level(filename='game_map.txt'):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]

    max_width = max(map(len, level_map))

    level_list = list(map(lambda x: x.ljust(max_width, ' '), level_map))
    return level_list


player = None

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    enemies = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '-':
                tile = Tile('block', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '5':
                tile = Tile('tree', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '^':
                tile = Tile('grass_1', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '@':
                new_player = Player(x, y)
                all_sprites.add(new_player)
                player_group.add(new_player)
            elif level[y][x] == '=':
                enemy = Enemy(x, y, x + 15)
                enemies.append(enemy)
                all_sprites.add(enemy)
                enemy_group.add(enemy)
    return new_player, x, y, enemies


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


def terminate():
    pygame.quit()
    sys.exit()


def main(screen, fon):
    camera = Camera()
    clock = pygame.time.Clock()
    level = load_level()
    new_player, x, y, enemies = generate_level(level)
    new_player.add_enemies(enemies)
    new_player.add_level(level)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                new_player.change_status(event.key, True)
            elif event.type == pygame.KEYUP:
                new_player.change_status(event.key, False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_player.change_status(event.button, True, True)
        screen.blit(fon, (0, 0))
        all_sprites.update()
        camera.update(new_player)
        for sprite in all_sprites:
            camera.apply(sprite)
        tiles_group.draw(screen)
        enemy_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(pygame.image.load('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                main(screen, fon)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    start_screen()
