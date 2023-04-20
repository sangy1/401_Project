# The title and difficulty screen are completed.
# The question screen is not completed yet need to add checks to see if you answer the question
# correctly

import pygame
# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Are You Smarter Than a Cyberesecurity Student?")
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (128,128,128)

# Define global variables
a = None
b = None
c = None
button_rect = None
current_question = 0
score = 0

# Load images and resize always
background_image = pygame.image.load("background.png")
logo_image = pygame.image.load("logo.png")
background_image = pygame.transform.scale(background_image, (800, 600))
logo_image = pygame.transform.scale(logo_image, (int(screen_width / 4), int(screen_width / 4)))

# Calculate position of images
logo_image_rect = logo_image.get_rect()
logo_image_x = (screen_width / 2) - (logo_image_rect.width / 2)
logo_image_y = screen_height * 0.1  # 10% of the screen height

# Set up fonts
title_font = pygame.font.SysFont("Arial", int(screen_height / 15))
subtitle_font = pygame.font.SysFont("Arial", int(screen_height / 20))
button_font = pygame.font.SysFont("Arial", int(screen_height / 20))

questions = [
    {
        "question": "How many times will this function run: for (int i = 1; i < 5; ++i) { ... }",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },

    # Add more questions here
]

# Draw the button
def draw_button():
    global button_rect
    button_text = button_font.render("Start Game", True, (255, 255, 255))
    button_rect = button_text.get_rect()
    button_rect.center = (screen_width // 2, int(screen_height * (2 / 3)))
    pygame.draw.ellipse(screen, (0, 128, 255), button_rect.inflate(20, 20))
    screen.blit(button_text, button_rect)
    
# Draw the title screen
def draw_title_screen():
    screen.blit(background_image, (0, 0))
    screen.blit(logo_image, (logo_image_x, logo_image_y))
    title_text = title_font.render("Are You Smarter Than a Cyberesecurity Student?", True, (255, 255, 255))
    title_rect = title_text.get_rect()
    title_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(title_text, title_rect)
    draw_button()

def draw_easy_button():
    global a
    button_text = button_font.render("Easy", True, (0, 255, 255))
    a = button_text.get_rect()
    a.center = (screen_width // 3, screen_height//2)
    pygame.draw.ellipse(screen, (0, 128, 255), a.inflate(20, 20))
    screen.blit(button_text, a)
    
def draw_medium_button():
    global b
    button_text = button_font.render("Medium", True, (0, 255, 255))
    b = button_text.get_rect()
    b.center = (screen_width // 2, screen_height//2)
    pygame.draw.ellipse(screen, (0, 128, 255), b.inflate(20, 20))
    screen.blit(button_text, b)

def draw_hard_button():
    global c
    button_text = button_font.render("Hard", True, (0, 255, 255))
    c = button_text.get_rect()
    c.center = (screen_width // 1.5, screen_height//2 )
    pygame.draw.ellipse(screen, (0, 128, 255), c.inflate(20, 20))
    screen.blit(button_text, c)

# Draw the difficulty screen
def draw_difficulty_screen():
    screen.blit(background_image, (0, 0))
    topic_text = title_font.render("Choose a difficulty", True, WHITE)
    topic_rect = topic_text.get_rect()
    topic_rect.center = (screen_width // 2, 50)
    screen.blit(topic_text, topic_rect)
    topic_button_font = pygame.font.SysFont("Arial", int(screen_height / 30))
    draw_easy_button()
    draw_medium_button()
    draw_hard_button()

#quizdraw
def draw_quiz():
    screen.blit(background_image, (0, 0))
    question_text = title_font.render(questions[current_question]["question"], True, WHITE)
    screen.blit(question_text, [50, 50])

    # Draw the answer options
    for i in range(4):
        option_text = title_font.render(questions[current_question]["options"][i], True, WHITE)
        x = 200
        y = 200 + i * 50
        pygame.draw.rect(screen, GRAY, [x, y, 400, 40])
        screen.blit(option_text, [x + 10, y + 2])

    # Draw the score
    score_text = title_font.render("Score: " + str(score) + " / " + str(len(questions)), True, WHITE)
    screen.blit(score_text, [50, 500])

    # Update the screen
    pygame.display.flip()


# Initial draw
draw_title_screen()
pygame.display.flip()
# Wait for the player to start the game or choose a topic
play_button_clicked = False # checks if play button is clicked
level_button_clicked = False # Checks if difficulty button is clicked

q_index = 0
while True:

    for event in pygame.event.get():
        # checks if you press x to exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if button_rect.collidepoint(mouse_pos):
                play_button_clicked = True
                draw_difficulty_screen()
                pygame.display.flip()
                #screen.fill(WHITE)

            if a.collidepoint(mouse_pos):
                level_button_clicked = True
                draw_quiz()
                pygame.display.flip()
            if b.collidepoint(mouse_pos):
               level_button_clicked = True
               draw_quiz()
               pygame.display.flip()
            if c.collidepoint(mouse_pos):
                level_button_clicked = True
                draw_quiz()
                pygame.display.flip()
            
