import pygame
import random
from classes import Player, Collectable, Text, FadingText

clock = pygame.time.Clock()


def main():
    pygame.init()

    # screen
    screen_width = 1024
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Squareslinger')

    # vars
    has_winner = False

    # players
    player_red = Player(50, 500, 1, (255, 0, 0), 'left')
    player_blue = Player(974, 500, 1, (0, 0, 255), 'right')

    player_group = pygame.sprite.Group()
    player_group.add(player_red)  # ignore type issue
    player_group.add(player_blue)  # ignore type issue

    # bullets
    bullet_group = pygame.sprite.Group()
    shoot_red = False
    shoot_blue = False

    # collectables
    collectables_group = pygame.sprite.Group()
    last_collectable_spawn = pygame.time.get_ticks()
    collectable_spawn_interval = 5000

    red_collectables = [0, 0, 0]  # for speed, bullet speed and rate of fire
    blue_collectables = [0, 0, 0]  # for speed, bullet speed and rate of fire

    # text
    text_group = pygame.sprite.Group()

    player_red_stats = Text(
        f'Power-ups collected by RED: Speed: 0, Bullet speed: 0, Rate of fire: 0',
        None,
        24,
        20,
        20
    )
    player_blue_stats = Text(
        f'Power-ups collected by BLUE: Speed: 0, Bullet speed: 0, Rate of fire: 0',
        None,
        24,
        464,
        738
    )
    text_group.add(player_red_stats)  # ignore type error
    text_group.add(player_blue_stats)  # ignore type error

    # main game loop
    run = True
    while run:
        global clock
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    shoot_red = True
                if event.key == pygame.K_LEFT:
                    shoot_blue = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    shoot_red = False
                if event.key == pygame.K_LEFT:
                    shoot_blue = False

        screen.fill((0, 0, 0))

        # bullets
        bullet_group.update(screen_width)
        bullet_group.draw(screen)

        for bullet in bullet_group:
            if pygame.sprite.collide_rect(bullet, player_red):
                bullet.kill()
                player_red.kill_player()

            if pygame.sprite.collide_rect(bullet, player_blue):
                bullet.kill()
                player_blue.kill_player()

            for collectable in collectables_group:
                if pygame.sprite.collide_rect(bullet, collectable):
                    power = collectable.power
                    collectable.kill()

                    collector = 'blue' if bullet.direction == -1 else 'red'
                    collectable_index = 0

                    if collectable.power == "bullet_speed":
                        power_description_string = "GOT FASTER BULLETS"
                        collectable_index = 1
                    elif collectable.power == "player_speed":
                        power_description_string = "GOT FASTER"
                        collectable_index = 0
                    else:
                        power_description_string = "GOT FASTER RATE OF FIRE"
                        collectable_index = 2

                    if collector == 'blue':
                        player_blue.power_up(power)
                        blue_collectables[collectable_index] += 1
                        player_blue_stats.update_text(
                            f'Power-ups collected by BLUE: Speed: {blue_collectables[0]}, Bullet speed: {blue_collectables[1]}, Rate of fire: {blue_collectables[2]}'
                        )
                        string = "BLUE " + power_description_string
                    else:
                        player_red.power_up(power)
                        red_collectables[collectable_index] += 1
                        player_red_stats.update_text(
                            f'Power-ups collected by RED: Speed: {red_collectables[0]}, Bullet speed: {red_collectables[1]}, Rate of fire: {red_collectables[2]}'
                        )
                        string = "RED " + power_description_string

                    text = FadingText(string, None, 30, collectable.rect.centerx, collectable.rect.centery)
                    text_group.add(text)  # ignore type issue

        if shoot_red:
            bullet_red = player_red.shoot()
            if bullet_red:
                bullet_group.add(bullet_red)

        if shoot_blue:
            bullet_blue = player_blue.shoot()
            if bullet_blue:
                bullet_group.add(bullet_blue)

        # collectables
        current_time = pygame.time.get_ticks()
        if current_time - last_collectable_spawn >= collectable_spawn_interval:
            x = random.randint(200, 824)
            y = random.randint(100, 668)

            collectable_powers = {
                0: 'bullet_speed',
                1: 'player_speed',
                2: 'shoot_cooldown',
            }

            random_power = random.randint(0,2)
            collectable = Collectable(x, y, collectable_powers[random_power])
            collectables_group.add(collectable)  # ignore type issue
            last_collectable_spawn = current_time

        collectables_group.draw(screen)

        # player group
        player_group.update()
        player_group.draw(screen)

        # text and text group

        text_group.update()
        text_group.draw(screen)

        # win event
        if not has_winner:
            winner = ""
            if not player_red.alive:
                winner = "BLUE"
            elif not player_blue.alive:
                winner = "RED"

            if not player_red.alive or not player_blue.alive:
                winner_text = FadingText(f"{winner} WON", None, 128, 296, 384, 1)
                text_group.add(winner_text)  # ignore type issue
                has_winner = True

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
