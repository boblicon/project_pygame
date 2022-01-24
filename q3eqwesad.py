import random
import pygame
import sys

clock = pygame.time.Clock()
FPS = 60
pygame.init()
WIDTH = 1920
HEIGHT = 1080
player_width = 192
player_height = 128
tile_width = tile_height = 64
main_fon = pygame.transform.scale(pygame.image.load('fon.png'), (WIDTH, HEIGHT))
town_fon = pygame.transform.scale(pygame.image.load('middleground.png'), (WIDTH, HEIGHT))
sky = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
death = pygame.transform.scale(pygame.image.load('game_over.jpg'), (WIDTH, HEIGHT))
heaven = pygame.transform.scale(pygame.image.load('heaven.jpg'), (WIDTH, HEIGHT))
jungle_back = pygame.transform.scale(pygame.image.load('forest_back.png'), (WIDTH, HEIGHT))
jungle_middle = pygame.transform.scale(pygame.image.load('forest_middle.png'), (WIDTH, HEIGHT))
graveyard_back = pygame.transform.scale(pygame.image.load('graeveyardback.png'), (WIDTH, HEIGHT))
graveyard = pygame.transform.scale(pygame.image.load('graveyard.png'), (WIDTH, HEIGHT))
middle = pygame.transform.scale(pygame.image.load('middle.png'), (WIDTH, HEIGHT))
back = pygame.transform.scale(pygame.image.load('back.png'), (WIDTH, HEIGHT))
near = pygame.transform.scale(pygame.image.load('near.png'), (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))


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
combat_idle_left, combat_idle_right = create_frames('HeavyBandit_CombatIdle_{i}.png', 4, tile_width, tile_height)
heavy_hurt_left, heavy_hurt_right = create_frames('HeavyBandit_Hurt_{i}.png', 2, tile_width, tile_height)
heavy_attack_right, heavy_attack_left = create_frames('HeavyBandit_Attack_{i}.png', 8, tile_width, tile_height)
hurt_left, hurt_right = create_frames('LightBandit_Hurt_{i}.png', 4, tile_width, tile_height)
hard_attack_right_animations, hard_attack_left_animations = create_frames('sprite_hard_attack{i}.png', 6)
walkLeft, walkRight = create_frames('LightBandit_Run_{i}.png', 16, tile_width, tile_height)
death_right, death_left = create_frames('LightBandit_Death_{i}.png', 3, tile_width, tile_height)
attack_left, attack_right = create_frames('LightBandit_Attack_{i}.png', 7, tile_width, tile_height)
player_death_right, player_death_left = create_frames('death_0{i}.png', 10)
hit_right, hit_left = create_frames('_Hit.png', 1)
heavy_death_right, heavy_death_left = create_frames('HeavyBandit_Death_{i}.png', 1, tile_width, tile_height)
hat_man_right, hat_man_left = create_frames('hat-man-walk-{i}.png', 6, tile_width, tile_height)
old_man_walk_right, old_man_walk_left = create_frames('oldman-walk-{i}.png', 12, tile_width, tile_height)
beard_idle_right, beard_idle_left = create_frames('bearded-idle-{i}.png', 5, tile_width, tile_height)
woman_right, woman_left = create_frames('woman-idle-{i}.png', 7, tile_width, tile_height)

bandit_right = {'walk': walkRight,
                'hurt': hurt_right,
                'death': death_right,
                'attack': attack_right
                }
bandit_left = {'walk': walkLeft,
               'hurt': hurt_left,
               'death': death_left,
               'attack': attack_left
               }

heavy_right = {'idle': combat_idle_right,
               'hurt': heavy_hurt_right,
               'attack': heavy_attack_right,
               'death': heavy_death_right
               }
heavy_left = {'idle': combat_idle_left,
              'hurt': heavy_hurt_left,
              'attack': heavy_attack_left,
              'death': heavy_death_left
              }

animations_right = {'walk': walk_right_animation,
                    'jump': jump_animation_right,
                    'idle': idle_right_animation,
                    'attack': attack_right_animation,
                    'hard_attack': hard_attack_right_animations,
                    'hurt': hit_right,
                    'death': player_death_right
                    }

animations_left = {'walk': walk_left_animation,
                   'jump': jump_animation_left,
                   'idle': idle_left_animation,
                   'attack': attack_left_animation,
                   'hard_attack': hard_attack_left_animations,
                   'hurt': hit_left,
                   'death': player_death_left
                   }

tile_images = {
    'grass_1': pygame.image.load('grass_block_side.png'),
    'block': pygame.image.load('dirt_1.png'),
    'tree': pygame.image.load('tree.png'),
    'brevno': pygame.image.load('brevno.png'),
    'cloud': pygame.image.load('cloud (2).png'),
    'point': pygame.image.load('point.png'),
    'house_middle': pygame.image.load('house-a.png'),
    'house': pygame.image.load('house-b.png'),
    'house_c': pygame.image.load('house-c.png'),
    'road': pygame.image.load('country_road.png'),
    'crate': pygame.image.load('crate.png'),
    'crates_stack': pygame.image.load('crate-stack.png'),
    'lantern': pygame.image.load('street-lamp.png'),
    'well': pygame.image.load('well.png'),
    'wagon': pygame.image.load('wagon.png'),
    'barrel': pygame.image.load('barrel.png'),
    'sign': pygame.image.load('sign.png'),
    'flower': pygame.image.load('flower.png'),
    'grass': pygame.image.load('grass.png'),
    'stone': pygame.image.load('stone_1.png'),
    'bush': pygame.image.load('bush_1.png'),
    'ladder': pygame.image.load('ladder.png'),
    'tree_2': pygame.image.load('another_tree.png'),
    'yolka': pygame.image.load('yolka.png'),
    'ground_jungle': pygame.image.load('ground_jungle.png'),
    'jungle_block': pygame.image.load('jungle_asd.png'),
    'jungle_wall': pygame.image.load('sprite_as3.png'),
    'jungle_left': pygame.image.load('jungle_left.png'),
    'jungle_right': pygame.image.load('jungle_right.png'),
    'jungle_under': pygame.image.load('under.png'),
    'jungle_tree': pygame.image.load('tree_jungle.png'),
    'jungle_plant': pygame.image.load('plant.png'),
    'jungle_house': pygame.image.load('house.png'),
    'jungle_rock': pygame.image.load('jungle_rock.png'),
    'jungle_mushroom': pygame.image.load('mushroom-red.png'),
    'jungle_vine': pygame.image.load('vine.png'),
    'graveyard_ground': pygame.image.load('graveyard_floor.png'),
    'graveyard_block': pygame.image.load('graveyard_block.png'),
    'graveyard_tree_1': pygame.image.load('tree-1.png'),
    'graveyard_tree_2': pygame.image.load('tree-2.png'),
    'graveyard_tree_3': pygame.image.load('tree-3.png'),
    'graveyard_statue': pygame.image.load('statue.png'),
    'graveyard_bush': pygame.image.load('bush-large.png'),
    'graveyard_grave': pygame.image.load('stone-3.png'),
    'graveyard_cross': pygame.image.load('stone-2.png'),
    'rocky_ground': pygame.image.load('загружено.png'),
    'rocky_right': pygame.image.load('rocky_right.png'),
    'rocky_left': pygame.image.load('rocky_left.png'),
    'blessrng': pygame.image.load('blessrng.png'),
    'rocky_crystal': pygame.image.load('crystal-1.png'),
    'rocky_plant': pygame.image.load('plant-2.png'),
    'rocky_top': pygame.image.load('rocky_top.png'),
}
for key in tile_images.keys():
    width = tile_images[key].get_width()
    height = tile_images[key].get_height()
    if key in ['tree', 'house_middle', 'house', 'house_c', 'tree_2', 'jungle_tree', 'graveyard_statue',
               'graveyard_tree_1', 'graveyard_tree_2', 'graveyard_tree_3']:
        width = height = 400
    if key in ['lantern']:
        width = 60
        height = 170
    if key in ['yolka']:
        width = 150
        height = 350
    if key in ['jungle_house']:
        width = 600
        height = 400
    if key in ['well', 'wagon', 'graveyard_cross']:
        width = height = 100
    if key in ['barrel']:
        width = 35
        height = 50
    if key in ['crate']:
        width = 40
        height = 40
    if key in ['ladder', 'ground_jungle', 'jungle_block', 'jungle_wall',
               'jungle_right', 'jungle_left', 'jungle_under', 'jungle_vine'
               'graveyard_ground', 'graveyard_block', 'graveyard_grave',
               'rocky_ground', 'rocky_right', 'rocky_left', 'blessrng'
               'rocky_plant', 'rocky_crystal']:
        width = 64
        height = 64
    tile_images[key] = pygame.transform.scale(tile_images[key], (width, height))
player_image = pygame.image.load('knight.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__()
        self.image = tile_images[tile_type]
        image_width = self.image.get_width()
        image_height = self.image.get_height()
        if tile_type in ['stone', 'well', 'barrel', 'crates-stack',
                         'crate', 'lantern', 'flower', 'yolka', 'bush', 'brevno',
                         'plant']:
            d_y = tile_height // 6
        elif tile_type in ['jungle_tree']:
            d_y = tile_height // 2
        else:
            d_y = 0
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + (tile_width - image_width) // 2,
            tile_height * pos_y + (tile_height - image_height) + d_y)


class HpClass(pygame.sprite.Sprite):
    def __init__(self, player, i, group):
        super().__init__(group)
        self.player = player
        self.i = i
        self.image = pygame.transform.scale(pygame.image.load('hp.png'), (40, 40))
        self.rect = self.image.get_rect().move(
            40 * (i - 1), 0)

    def update(self):
        if self.i > self.player.hp:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
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
        self.hp = 10

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
        self.d_y -= one_jump * self.jump_k
        if self.check():
            self.d_y += one_jump * self.jump_k
            return False
        else:
            return True

    def check_fall(self):
        return self.level[self.y + 1][self.x] not in ["^", "-", "%", "*", 'y', 'j', '[', ']',
                                                      'i', '(', ')', '~', '"', 'm', ':']

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
                for enemy in self.enemies:
                    enemy.hit(self.x, self.y)
            elif self.cur_frame >= len(hard_attack_right_animations):
                if self.moving:
                    self.status = 'walk'
                else:
                    self.status = 'idle'

    def hit(self, x, y):
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= 2 ** 0.5 and self.status in ['walk', 'idle', 'jump']:
            self.hp -= 1
            self.hurt(True)
            return True
        else:
            return False

    def hurt(self, start=False):
        if start:
            self.cur_frame = 0
            self.status = 'hurt'
        if self.cur_frame >= len(animations_right['hurt']) and self.status == 'hurt':
            if self.moving:
                self.status = 'walk'
            else:
                self.status = 'idle'
        if self.hp <= 0:
            self.death()

    def death(self):
        self.status = 'death'
        if self.right_side:
            animations = animations_right
        else:
            animations = animations_left
        animation = animations[self.status]
        self.cur_frame %= len(animation)
        self.image = animation[self.cur_frame]

    def check(self):
        y = self.y + int(self.d_y)
        x = self.x + int(self.d_x)
        if (x >= len(self.level[0]) or y >= len(self.level)
                or x < 0 or y < 0
                or self.level[y][x] == '-' or self.level[y][x] == '^'
                or self.level[y][x] == '%' or self.level[y][x] == '*'
                or self.level[y][x] == 'j' or self.level[y][x] == 'y'
                or self.level[y][x] == 'i' or self.level[y][x] == ')'
                or self.level[y][x] == '(' or self.level[y][x] == '~'
                or self.level[y][x] == '"' or self.level[y][x] == 'm'
                or self.level[y][x] == ':' or self.level[y][x] == ']'
                or self.level[y][x] == '['):
            return True
        else:
            return False

    def change_status(self, key, button_down, mouse_button=False):
        if button_down:
            if mouse_button and key == 1 and self.status in ['walk', 'idle', 'hurt']:
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
        if self.status == 'death':
            self.cur_frame += 1
            if self.cur_frame >= 10:
                pass
            else:
                self.death()
        else:
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
            self.hurt()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, end):
        super().__init__()
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
        self.player = 0
        self.start = self.x
        self.velocity_of_enemy = 0
        self.count_of_steps = 0
        self.cur_frame = 0

    def hit(self, x, y):
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= 2 ** 0.5:
            if self.player.status == 'hard_attack':
                self.hp -= 2
            if self.player.status == 'attack':
                self.hp -= 1
            self.hurt(True)

    def add_player(self, player):
        self.player = player

    def hurt(self, start=False):
        if start:
            self.cur_frame = 0
            self.status = 'hurt'
        if self.cur_frame >= len(bandit_right['hurt']) and self.status == 'hurt':
            self.status = 'walk'
        if self.hp <= 0:
            self.death()

    def attack(self):
        if self.cur_frame >= len(bandit_right['attack']) and self.status == 'attack':
            self.status = 'walk'
        if self.status != 'attack' and self.cur_frame == 7:
            success = self.player.hit(self.x, self.y)
        else:
            success = False
        if success:
            self.status = 'attack'
            self.cur_frame = 0

    def death(self):
        self.status = 'death'

    def update(self):
        if self.status == 'death':
            self.image = bandit_right['death'][-1]
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
            if self.status == 'attack':
                if self.x < self.player.x:
                    animations = bandit_right
                else:
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
            self.attack()


class HatMan(pygame.sprite.Sprite):
    def __init__(self, x, y, end):
        super().__init__()
        self.image = walkLeft[0]
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.x = x
        self.y = y
        self.slow = 0
        self.right_side = True
        self.end = end
        self.start = self.x
        self.cur_frame = 0

    def add_player(self, player):
        self.player = player

    def update(self):
        if self.x >= self.end:
            self.right_side = False
        elif self.x < self.start:
            self.right_side = True
        if self.right_side:
            d_x = 1
            animations = hat_man_right
        else:
            d_x = -1
            animations = hat_man_left
        animation = animations
        if self.slow % 5 != 0:
            d_x = 0
        self.slow += 1
        self.cur_frame %= len(animation)
        self.image = animation[self.cur_frame]
        if self.slow % 3 >= 1:
            self.cur_frame += 1
        self.rect.x += tile_width * d_x
        self.x += d_x

    def hit(self, x, y):
        pass


class OldMan(pygame.sprite.Sprite):
    def __init__(self, x, y, end):
        super().__init__()
        self.image = walkLeft[0]
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.x = x
        self.y = y
        self.slow = 0
        self.right_side = False
        self.end = end
        self.start = self.x
        self.cur_frame = 0

    def add_player(self, player):
        self.player = player

    def update(self):
        if self.x >= self.end:
            self.right_side = False
        elif self.x < self.start:
            self.right_side = True
        if self.right_side:
            d_x = 1
            animations = old_man_walk_right
        else:
            d_x = -1
            animations = old_man_walk_left
        animation = animations
        if self.slow % 5 != 0:
            d_x = 0
        self.cur_frame %= len(animation)
        self.image = animation[self.cur_frame]
        if self.slow % 3 >= 1:
            self.cur_frame += 1
        self.slow += 1
        self.rect.x += tile_width * d_x
        self.x += d_x

    def hit(self, x, y):
        pass


class BeardMan(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = walkLeft[0]
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.x = x
        self.y = y
        self.right_side = True
        self.cur_frame = 0
        self.slow = 0

    def add_player(self, player):
        self.player = player

    def update(self):
        if self.x < self.player.x:
            animation = beard_idle_right
        else:
            animation = beard_idle_left

        self.cur_frame %= len(animation)
        self.image = animation[self.cur_frame]
        if self.slow % 5 == 0:
            self.cur_frame += 1
        self.slow += 1

    def hit(self, x, y):
        pass
    

class Woman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = walkLeft[0]
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.x = x
        self.y = y
        self.right_side = True
        self.cur_frame = 0
        self.slow = 0

    def add_player(self, player):
        self.player = player

    def update(self):
        if self.x < self.player.x:
            animation = woman_right
        else:
            animation = woman_left

        self.cur_frame %= len(animation)
        self.image = animation[self.cur_frame]
        self.cur_frame += 1
        self.slow += 1

    def hit(self, x, y):
        pass


class EnemyHeavy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = heavy_hurt_right[0]
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.x = x
        self.y = y
        self.hp = 5
        self.status = 'idle'
        if random.randint(0, 1):
            self.right_side = True
        else:
            self.right_side = False
        self.player = 0
        self.start = self.x
        self.cur_frame = 0

    def hit(self, x, y):
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= 2 ** 0.5:
            if self.player.status == 'hard_attack':
                self.hp -= 2
            if self.player.status == 'attack':
                self.hp -= 1
            self.hurt(True)

    def add_player(self, player):
        self.player = player

    def hurt(self, start=False):
        if start:
            self.cur_frame = 0
            self.status = 'hurt'
        if self.cur_frame >= len(heavy_right['hurt']) and self.status == 'hurt':
            self.status = 'idle'
        if self.hp <= 0:
            self.death()

    def attack(self):
        if self.cur_frame >= len(heavy_right['attack']) and self.status == 'attack':
            self.status = 'idle'
        if self.status != 'attack':
            success = self.player.hit(self.x, self.y)
        else:
            success = False
        if success:
            self.status = 'attack'
            self.cur_frame = 0

    def death(self):
        self.status = 'death'

    def update(self):
        if self.status == 'death':
            self.image = heavy_right['death'][-1]
        else:
            if self.x < self.player.x:
                animations = heavy_right
            else:
                animations = heavy_left
            animation = animations[self.status]
            self.cur_frame %= len(animation)
            self.image = animation[self.cur_frame]
            self.cur_frame += 1
            self.hurt()
            self.attack()


def load_level(filename='game_map.txt'):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line for line in mapFile]

    max_width = max(map(len, level_map))

    level_list = list(map(lambda x: x.ljust(max_width, ' '), level_map))
    return level_list


def generate_level(level, all_sprites, tiles_group, front_tiles_group, player_group, enemy_group):
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
            elif level[y][x] == '_':
                tile = Tile('house_middle', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == ':':
                tile = Tile('blessrng', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == ')':
                tile = Tile('jungle_right', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '(':
                tile = Tile('jungle_left', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'w':
                tile = Tile('rocky_top', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'b':
                tile = Tile('barrel', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == '+':
                tile = Tile('house', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'j':
                tile = Tile('ground_jungle', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '!':
                tile = Tile('yolka', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '|':
                tile = Tile('lantern', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 's':
                tile = Tile('stone', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'o':
                tile = Tile('jungle_wall', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'u':
                tile = Tile('bush', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'g':
                tile = Tile('grass', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'n':
                tile = Tile('jungle_tree', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'z':
                tile = Tile('jungle_house', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'p':
                tile = Tile('jungle_mushroom', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'q':
                tile = Tile('graveyard_cross', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '9':
                tile = Tile('graveyard_grave', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '}':
                tile = Tile('graveyard_statue', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'x':
                tile = Tile('graveyard_tree_1', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '?':
                tile = Tile('graveyard_tree_3', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '6':
                tile = Tile('wagon', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == ';':
                tile = Tile('house_c', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'm':
                tile = Tile('rocky_ground', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == '[':
                tile = Tile('rocky_left', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == ']':
                tile = Tile('rocky_right', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == ',':
                tile = Tile('well', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 't':
                tile = Tile('brevno', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == '*':
                tile = Tile('road', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'f':
                tile = Tile('flower', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'c':
                tile = Tile('jungle_plant', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '%':
                tile = Tile('cloud', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'k':
                tile = Tile('jungle_rock', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '=':
                tile = Tile('water', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '>':
                tile = Tile('point', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'i':
                tile = Tile('jungle_under', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == 'v':
                tile = Tile('jungle_wall', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
                tile = Tile('jungle_vine', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'l':
                tile = Tile('jungle_vine', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '"':
                tile = Tile('graveyard_ground', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '~':
                tile = Tile('graveyard_block', x, y)
                all_sprites.add(tile)
                tiles_group.add(tile)
            elif level[y][x] == '.':
                tile = Tile('crate', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == '&':
                tile = Tile('crates_stack', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'y':
                tile = Tile('jungle_block', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == '/':
                tile = Tile('tree_2', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'r':
                tile = Tile('rocky_crystal', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'd':
                tile = Tile('rocky_plant', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == 'l':
                tile = Tile('ladder', x, y)
                all_sprites.add(tile)
                front_tiles_group.add(tile)
            elif level[y][x] == '@':
                new_player = Player(x, y)
                all_sprites.add(new_player)
                player_group.add(new_player)
            elif level[y][x] == '1':
                enemy = Enemy(x, y, x + 5)
                enemies.append(enemy)
                all_sprites.add(enemy)
                enemy_group.add(enemy)
            elif level[y][x] == '$':
                heavy = EnemyHeavy(x, y)
                enemies.append(heavy)
                all_sprites.add(heavy)
                enemy_group.add(heavy)
            elif level[y][x] == '2':
                hatman = HatMan(x, y, x + 30)
                enemies.append(hatman)
                all_sprites.add(hatman)
                enemy_group.add(hatman)
            elif level[y][x] == 'a':
                woman = Woman(x, y)
                enemies.append(woman)
                all_sprites.add(woman)
                enemy_group.add(woman)
            elif level[y][x] == '3':
                oldman = OldMan(x, y, x + 17)
                enemies.append(oldman)
                all_sprites.add(oldman)
                enemy_group.add(oldman)
            elif level[y][x] == '4':
                beardman = BeardMan(x, y)
                enemies.append(beardman)
                all_sprites.add(beardman)
                enemy_group.add(beardman)
    return new_player, x, y, enemies, all_sprites, tiles_group, front_tiles_group, player_group, enemy_group


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj, interface=False):
        if interface:
            obj.rect.x -= self.dx
            obj.rect.y -= self.dy
        else:
            obj.rect.x += self.dx
            obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2 - 150)


def terminate():
    pygame.quit()
    sys.exit()


def get_fon(level, player):
    x = player.x
    column = []
    for i in range(len(level)):
        column.append(level[i][x])
    if '*' in column:
        fons = [sky, town_fon]
    elif 'j' in column:
        fons = [jungle_back, jungle_middle]
    elif '"' in column:
        fons = [graveyard_back, graveyard]
    elif 'm' in column:
        fons = [back]
    else:
        fons = [main_fon]
    return fons


def main():
    camera = Camera()
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    front_tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    health_group = pygame.sprite.Group()

    level = load_level()
    new_player, x, y, enemies, all_sprites, tiles_group, front_tiles_group, player_group,\
        enemy_group = generate_level(level, all_sprites, tiles_group, front_tiles_group, player_group, enemy_group)
    new_player.add_enemies(enemies)
    for enemy in enemies:
        enemy.add_player(new_player)
    new_player.add_level(level)
    for i in range(new_player.hp):
        hp = HpClass(new_player, i + 1, health_group)
        health_group.add(hp)
    while True:
        if new_player.hp <= 0:
            death_screen()
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                new_player.change_status(event.key, True)
            elif event.type == pygame.KEYUP:
                new_player.change_status(event.key, False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_player.change_status(event.button, True, True)
        fons = get_fon(level, new_player)
        for fon in fons:
            screen.blit(fon, (0, 0))
        all_sprites.update()
        health_group.update()
        camera.update(new_player)
        for sprite in all_sprites:
            camera.apply(sprite)
        camera.update(new_player)
        for sprite in health_group:
            camera.apply(sprite, True)
        tiles_group.draw(screen)
        front_tiles_group.draw(screen)
        enemy_group.draw(screen)
        player_group.draw(screen)
        health_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "A - Движение назад",
                  "D - Движение вперёд",
                  "Mouse_buttin1 - Слабая атака",
                  "Mouse_button-2 - Сильная атака",
                  "Space - прыжок"]

    load_screen = pygame.transform.scale(pygame.image.load('aaaa.jpg'), (WIDTH, HEIGHT))
    screen.blit(load_screen, (0, 0))
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
                main()
                return
        pygame.display.flip()
        clock.tick(FPS)


def death_screen():
    load_screen = death
    screen.blit(death, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                start_screen()
                return
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    start_screen()
