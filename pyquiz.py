import pygame
import json
import random

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Are You Smarter Than a Cybersecurity Student?")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 128, 255)
GREEN = (105, 245, 66)
ORANGE = (245, 160, 24)
RED = (240, 26, 14)
# Define global variables
difficulty = ""
button_rect_easy = pygame.Rect(screen_width // 3 - 100, screen_height // 2, 200, 200)
button_rect_medium = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 200)
button_rect_hard = pygame.Rect(screen_width // 1.5 - 100, screen_height // 2, 200, 200)
play_again_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2, 100, 100)
button_y = int(screen_height / 3)
option_centers = []
option_rects = []
option_texts = []

selected_topic = ""
current_screen = "start"
option_buttons = []
correct_answer = ""
num_correct = 00

topics = [
    {"rect": pygame.Rect(screen_width // 3 - 50, button_y + (screen_height // 10 * 0), 100, 100),
     "name": "Secure Coding", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 3 - 50, button_y + (screen_height // 10 * 1), 100, 100),
     "name": "Vulnerability Discovery", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 3 - 50, button_y + (screen_height // 10 * 2), 100, 100), "name": "Fuzzing",
     "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 3 - 50, button_y + (screen_height // 10 * 3), 100, 100),
     "name": "Penetration Testing", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 3 - 50, button_y + (screen_height // 10 * 4), 100, 100),
     "name": "Ethical Hacking", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 1.5 - 50, button_y + (screen_height // 10 * 0), 100, 100),
     "name": "Exploits/Attacks", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 1.5 - 50, button_y + (screen_height // 10 * 1), 100, 100),
     "name": "Countermeasures", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 1.5 - 50, button_y + (screen_height // 10 * 2), 100, 100),
     "name": "Internet Infrastructure", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 1.5 - 50, button_y + (screen_height // 10 * 3), 100, 100),
     "name": "Forensic Analysis", "answered_correctly": False},
    {"rect": pygame.Rect(screen_width // 1.5 - 50, button_y + (screen_height // 10 * 4), 100, 100),
     "name": "ML for Cybersecurity", "answered_correctly": False}
]

topic_buttons = 10 * [None]
for i in range(10):
    if i < 5:
        topic_buttons[i] = pygame.Rect(screen_width // 3 - 50, button_y + (screen_height // 10 * i), 100, 100)
    else:
        topic_buttons[i] = pygame.Rect(screen_width // 1.5 - 50, button_y + (screen_height // 10 * (i - 5)), 100, 100)

# Load images and resize always
background_image = pygame.image.load("background.png")
logo_image = pygame.image.load("logo.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
logo_image = pygame.transform.scale(logo_image, (int(screen_width / 4), int(screen_width / 4)))

# Calculate position of images
logo_image_rect = logo_image.get_rect()
logo_image_x = (screen_width / 2) - (logo_image_rect.width / 2)
logo_image_y = screen_height * 0.1  # 10% of the screen height

# Set up fonts
title_font = pygame.font.SysFont("Arial", int(screen_height / 14))
subtitle_font = pygame.font.SysFont("Arial", int(screen_height / 20))
button_font = pygame.font.SysFont("Arial", int(screen_height / 25))


# =========================================================================

# Draw the Start Game Button
def draw_start_game_button():
    global button_rect
    button_text = button_font.render("Start Game", True, (255, 255, 255))
    button_rect = button_text.get_rect()
    button_rect.center = (screen_width // 2, int(screen_height * (2 / 3)))
    pygame.draw.ellipse(screen, (0, 128, 255), button_rect.inflate(20, 20))
    screen.blit(button_text, button_rect)


# Draw the title screen
def draw_title_screen():
    # Clear the screen
    screen.fill(BLACK)
    # Set up screen and draw it
    screen.blit(background_image, (0, 0))
    screen.blit(logo_image, (logo_image_x, logo_image_y))
    title_text = title_font.render("Are You Smarter Than a Cybersecurity Student?", True, (255, 255, 255))
    title_rect = title_text.get_rect()
    title_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(title_text, title_rect)
    draw_start_game_button()


# Draw buttons in general
def draw_button(text, center, color):
    button_text = button_font.render(text, True, WHITE)
    button_rect = button_text.get_rect(center=center)
    button_rect.inflate_ip(50, 40)  # increase the size of the rect
    pygame.draw.ellipse(screen, color, button_rect)  # draw a rect
    button_rect_center = button_rect.center
    screen.blit(button_text, (
    button_rect_center[0] - button_text.get_width() // 2, button_rect_center[1] - button_text.get_height() // 2))


def draw_difficulty_screen():
    # Clear the screen
    screen.fill(BLACK)

    # Renders and draws the title text
    screen.blit(background_image, (0, 0))
    topic_text = title_font.render("Choose a difficulty", True, WHITE)
    topic_rect = topic_text.get_rect()
    topic_rect.center = (screen_width // 2, screen_height // 4)

    screen.blit(topic_text, topic_rect)

    # Draw the buttons
    draw_button("Easy", button_rect_easy.center, GREEN)
    draw_button("Medium", button_rect_medium.center, ORANGE)
    draw_button("Hard", button_rect_hard.center, RED)


def draw_topic_screen():
    # Clear the screen
    screen.fill(BLACK)

    # Renders and draws the title text
    screen.blit(background_image, (0, 0))
    topic_text = title_font.render("Choose a Topic", True, WHITE)
    topic_rect = topic_text.get_rect()
    topic_rect.center = (screen_width // 2, screen_height // 5)
    screen.blit(topic_text, topic_rect)

    # Draw the buttons
    for i, topic in enumerate(topics):
        draw_button(topic["name"], topic["rect"].center, GRAY)


def load_questions_for_topic(selected_topic, selected_difficulty):
    with open('questions.json', 'r') as f:
        questions = json.load(f)

    if selected_topic not in questions:
        return []

    selected_questions = [q for q in questions[selected_topic] if q['difficulty'] == selected_difficulty]

    return selected_questions


def draw_question_screen(topic, difficulty):
    # Clear the screen
    screen.fill(BLACK)

    # Renders and draws the title text
    screen.blit(background_image, (0, 0))
    topic_text = title_font.render("Question: ", True, WHITE)
    topic_rect = topic_text.get_rect()
    topic_rect.center = (screen_width // 2, 50)
    screen.blit(topic_text, topic_rect)

    # Load the questions for the selected topic
    questions = load_questions_for_topic(topic, difficulty)

    # Select a random question from the list
    random_question = random.choice(questions)

    # Set the question text and options
    question_text = subtitle_font.render(random_question['question'], True, WHITE)

    # Determine the maximum width and height for the question text
    max_width = screen_width - (screen_width // 5)
    max_height = screen_height // 6

    # Wrap the question text onto multiple lines if it's too long to fit on one line
    lines = []
    words = random_question['question'].split(' ')
    line = ''
    for word in words:
        if subtitle_font.size(line + word)[0] < max_width:
            line += word + ' '
        else:
            lines.append(line)
            line = word + ' '
    lines.append(line)

    # Just set font_size so long questions don't go past screen
    font_size = 39

    # Render and blit each line of the question text to the screen
    y = max_height - (len(lines) * font_size) // 8
    for line in lines:
        text = pygame.font.Font(pygame.font.get_default_font(), font_size).render(line.strip(), True, WHITE)
        rect = text.get_rect()
        rect.center = (screen_width // 2, y)
        screen.blit(text, rect)
        y += font_size * 1.2

    # Reset option_centers and option_texts to an empty list
    option_centers = []
    option_rects = []
    option_texts = []

    # Calculate and append option center coordinates to option_centers list
    option_spacing = screen_height // 10
    option_y = screen_height // 2
    for i, option_text in enumerate(random_question['options']):
        option_center = (screen_width // 2, option_y + (i * option_spacing))
        option_centers.append(option_center)

    # Get the text from the question
    option_texts = random_question['options']
    correct_answer = random_question['answer']

    # Create the rectangle button object around the text
    for i, option_text in enumerate(random_question['options']):
        text_surface = button_font.render(option_text, True, (255, 255, 255))  # render the text to create a surface
        text_rect = text_surface.get_rect()  # get the rect of the text surface
        button_width = text_rect.width + 20  # add padding on either side of the text
        button_height = text_rect.height + 10  # add padding above and below the text
        option_rect = pygame.Rect(option_centers[i][0] - button_width // 2, option_centers[i][1] - (button_height // 2),
                                  button_width, button_height)
        option_rects.append(option_rect)

    # Draw the actual button
    for i, option_text in enumerate(option_texts):
        draw_button(option_text, option_centers[i], BLUE)

    # Update the display
    pygame.display.update()

    return option_centers, option_texts, option_rects, correct_answer


def draw_game_over_screen():
    # Clear the screen
    screen.fill(BLACK)

    # Render and draw the "Game Over" message
    screen.blit(background_image, (0, 0))
    game_over_text = title_font.render("GAME OVER", True, RED)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (screen_width // 2, screen_height // 3)
    screen.blit(game_over_text, game_over_rect)

    # Draw the "Play Again" button
    play_again_center = (screen_width // 2, screen_height // 2)
    draw_button("Play Again", play_again_center, BLUE)

    # Create a text surface with the number of questions answered successfully
    num_correct_text = subtitle_font.render(f"Number of questions answered correctly: {num_correct}", True, WHITE)
    num_correct_rect = num_correct_text.get_rect()
    num_correct_rect.center = (screen_width // 2, play_again_rect.bottom + 20)

    # Blit the text surface onto the screen surface
    screen.blit(num_correct_text, num_correct_rect)

    # Update the display
    pygame.display.update()


def draw_victory_screen():
    # Clear the screen
    screen.fill(BLACK)

    # Render and draw the "Game Over" message
    screen.blit(background_image, (0, 0))
    game_over_text = title_font.render("YOU WON!!!", True, GREEN)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (screen_width // 2, screen_height // 3)
    screen.blit(game_over_text, game_over_rect)

    # Draw the "Play Again" button
    play_again_center = (screen_width // 2, screen_height // 2)
    draw_button("Play Again", play_again_center, BLUE)

    # Create a text surface with the number of questions answered successfully
    num_correct_text = subtitle_font.render(f"You have beaten difficulty: {difficulty.title()}", True, WHITE)
    num_correct_rect = num_correct_text.get_rect()
    num_correct_rect.center = (screen_width // 2, play_again_rect.bottom + 20)

    # Blit the text surface onto the screen surface
    screen.blit(num_correct_text, num_correct_rect)

    # Update the display
    pygame.display.update()


# =========================================================================
# Code Responsible for running game
# Initial draw


draw_title_screen()
pygame.display.flip()

# Conditions to change when playing game
play_button_clicked = False  # Checks if play button is clicked
difficulty_button_clicked = False  # Checks if difficulty button is clicked
topic_button_clicked = False  # Checks if a topic is selected
answer_button_clicked = False  # Checks if user clicks on an answer
choice_correct = False  # Checks if user clicks the correct answer

while True:
    for event in pygame.event.get():
        # Checks if Player clicks the x button on top right to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif current_screen == "game_over" or current_screen == "victory":
            if event.type == pygame.MOUSEBUTTONDOWN and play_again_rect.collidepoint(event.pos):
                # Reset all checks to false since we will reset to the difficulty button
                # Can do both victory and game over since both require full reset
                num_correct = 0
                difficulty_button_clicked = False
                topic_button_clicked = False
                answer_button_clicked = False
                difficulty = ""
                for i, topic in enumerate(topics):
                    topic["answered_correctly"] = False
                current_screen = "difficulty"

        # Checks if player will continue playing or go to gameover screen from the qustion screen
        elif current_screen == "question":
            if event.type == pygame.MOUSEBUTTONDOWN and topic_button_clicked == True:
                for i, option_rect in enumerate(option_rects):
                    if option_rects[i].collidepoint(event.pos):
                        answer_button_clicked = True
                        if option_texts[i] != correct_answer:  # Logic if wrong answer was chosen
                            current_screen = "game_over"
                            print(f"Clicked wrong option {i + 1}")
                        else:  # Logic if correct answer is chosen
                            current_screen = "topic"
                            num_correct += 1
                            for j, topic_button in enumerate(topics):
                                if topic_button["name"] == selected_topic:
                                    topic_button["answered_correctly"] = True
                            print(f"Clicked correct option {i + 1}")



        # Checks which topic is chosen and generates a random question from topic and difficulty
        elif current_screen == "topic":
            answer_button_clicked = False
            if event.type == pygame.MOUSEBUTTONDOWN and difficulty_button_clicked == True:
                for i, topic_button in enumerate(topics):
                    if topic_button["answered_correctly"] == False and topic_button["rect"].collidepoint(event.pos):
                        topic_button_clicked = True
                        selected_topic = topic_button["name"]
                        current_screen = "question"
            for i, topic_button in enumerate(topics):
                if num_correct == len(topics):
                    current_screen = "victory"


        # Checks which difficulty the player chooses
        elif current_screen == "difficulty":
            if event.type == pygame.MOUSEBUTTONDOWN and play_button_clicked == True:
                if button_rect_easy.collidepoint(event.pos):
                    difficulty_button_clicked = True
                    difficulty = "easy"
                elif button_rect_medium.collidepoint(event.pos):
                    difficulty_button_clicked = True
                    difficulty = "medium"
                elif button_rect_hard.collidepoint(event.pos):
                    difficulty_button_clicked = True
                    difficulty = "hard"
                current_screen = "topic"
        # Checks if player clicks start game
        elif current_screen == "start":
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                play_button_clicked = True
                current_screen = "difficulty"
                break

    # Conditions to check which screen the game is on
    if current_screen == "topic":
        draw_topic_screen()
        pygame.display.flip()
    # Checks if Player chose difficulty
    if current_screen == "difficulty":
        draw_difficulty_screen()
        pygame.display.flip()
    if current_screen == "question":
        option_centers, option_texts, option_rects, correct_answer = draw_question_screen(selected_topic, difficulty)
        pygame.display.flip()
    if current_screen == "start":
        draw_title_screen()
        pygame.display.flip()
    if current_screen == "game_over":
        draw_game_over_screen()
        pygame.display.flip()
    if current_screen == "victory":
        draw_victory_screen()
        pygame.display.flip()