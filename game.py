import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
gameWindow = pygame.display.set_mode((600, 600))
bgimg = pygame.image.load("bgimg.jpg")
bgimg = pygame.transform.scale(bgimg, (600, 600)).convert_alpha()
gameover_img = pygame.image.load("gameover.jpg")
gameover_img = pygame.transform.scale(gameover_img, (600, 600)).convert_alpha()
intro_img = pygame.image.load("untitled.jpg")
intro_img = pygame.transform.scale(intro_img, (600, 600)).convert_alpha()

# Game Title
pygame.display.set_caption("Snakes@Ev|L")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


def score_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill((239, 106, 128))
        gameWindow.blit(intro_img, (0, 0))
        # score_text("Welcome to SNAKES", black, 175, 235)
        # score_text("by @Ev|L", black, 245, 280)
        # score_text("press 'space' to play", black, 185, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('ingamebg.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(120)


# Game Loop
def gameloop():
    exit_game = False
    game_over = False

    snake_x = 300
    snake_y = 300

    velocity_x = 0
    velocity_y = 0

    snk_list = []
    snk_len = 1

    food_x = random.randint(20, 300)
    food_y = random.randint(20, 300)

    score = 0
    init_velocity = 2
    snake_size = 15
    fps = 120

    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill((239, 106, 128))
            gameWindow.blit(gameover_img, (0, 0))
            score_text("Game Over :-( ", (27, 12, 128), 250, 320)
            score_text("Press ENTER to continue", (27, 12, 128), 190, 360)
            score_text("Made By @VishaL PatiL", (27, 12, 128), 300, 570)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 17 and abs(snake_y - food_y) < 17:
                pygame.mixer.music.load('eat.mp3')
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(75, 525)
                food_y = random.randint(75, 525)
                snk_len += 6
                init_velocity += 0.15
                if score > int(highscore):
                    highscore = score

            gameWindow.fill((119, 249, 63))
            gameWindow.blit(bgimg, (0, 0))
            score_text("Score: " + str(score) + "  Highscore: " + str(highscore), (17, 7, 126), 8, 8)
            pygame.draw.circle(gameWindow, red, [food_x, food_y], 10)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_len:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > 600 or snake_y < 0 or snake_y > 600:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, (8, 8, 8), snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
