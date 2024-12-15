import pygame
import time
import random
pygame.init()
WIDTH ,HEIGHT = 1000, 800
font = pygame.font.Font(None, 36)
score = 0
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('memory_game')
BG = pygame.transform.scale(pygame.image.load("Downloads/bg.jpg"),(WIDTH, HEIGHT) )
back_image = pygame.transform.scale(pygame.image.load("Downloads/pattern.jpg"),(150, 150) )
front_images = [
    pygame.transform.scale(pygame.image.load("Downloads/cat.jpg"),(150, 150) ),
    pygame.transform.scale(pygame.image.load("Downloads/froggy.jpg"),(150, 150) ),
    pygame.transform.scale(pygame.image.load("Downloads/kitty.jpg"),(150, 150) ),
    pygame.transform.scale(pygame.image.load("Downloads/melody.jpg"),(150, 150) ),
    pygame.transform.scale(pygame.image.load("Downloads/doggy.jpg"),(150, 150) ),
    pygame.transform.scale(pygame.image.load("Downloads/cinnamon.jpg"),(150, 150) )
]
questions = [
    ("What is the maximum number of times the graph of a polynomial function of degree n intersects the x-axis?", "n"),
    ("Where are vectors usually indexed from?", "0"),
    ("What is the limit of 1/x when x approaches infinity?", "0"),
    ("Is a constant function a polynomyal function? (yes/no)", "yes"),
    ("What does the graph of a second degree polynomial function look like?", "parabola"),
    ("What is the amplitude of the sine function?", "1"),
    ("What is the period of the tangent function?(answer in words)", "pi"),
    ("What is the numeric difference between the ASCII code of a capital and a lower case letter?", "32"),
    ("What does the operation 1&&(and)0 give?", "0")
    ]
card_rects = []
card_faces = []
card_status = []
cards = front_images * 2  
random.shuffle(cards)
def end_game_screen():
    WINDOW.blit(BG, (0, 0))
    message = "Great Job, you finished the game!"
    message_surface = font.render(message, True, (255, 255, 255))
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    WINDOW.blit(message_surface, message_rect)
    button_text = "Restart"
    button_surface = font.render(button_text, True, (0, 0, 0))
    button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 20, 150, 50)
    pygame.draw.rect(WINDOW, (255, 255, 255), button_rect)
    WINDOW.blit(button_surface, (button_rect.x + (button_rect.width - button_surface.get_width()) // 2,
                                 button_rect.y + (button_rect.height - button_surface.get_height()) // 2))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_position):
                    return 

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] > max_width:
            lines.append(current_line) 
            current_line = word       
        else:
            current_line = test_line 

    if current_line:
        lines.append(current_line)

    return lines

def draw(score):
    WINDOW.blit(BG, (0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    WINDOW.blit(score_text, (10, 10))
def display_question(question):
    max_width = WIDTH - 100
    wrapped_lines = wrap_text(question, font, max_width)
    total_height = len(wrapped_lines) * font.size("Tg")[1]
    start_y = (HEIGHT // 2) - total_height // 2 - 50 

    for i, line in enumerate(wrapped_lines):
        line_surface = font.render(line, True, (255, 255, 255))
        line_x = (WIDTH // 2) - (line_surface.get_width() // 2)
        line_y = start_y + i * font.size("Tg")[1]
        WINDOW.blit(line_surface, (line_x, line_y))

    pygame.display.update() 


def get_user_input(question):
    user_input = ""
    input_active = True
    input_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40) 
    color_active = (255, 255, 255)  
    current_color = color_active 
    draw(score)  
    display_question(question)  
    pygame.display.update()  

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    input_active = False
                elif event.key == pygame.K_BACKSPACE: 
                    user_input = user_input[:-1]
                else: 
                    user_input += event.unicode

        pygame.draw.rect(WINDOW, (0, 0, 0), input_rect) 
        pygame.draw.rect(WINDOW, current_color, input_rect, 2)  

        input_text = font.render(user_input, True, (255, 255, 255))
        WINDOW.blit(input_text, (input_rect.x + 10, input_rect.y + 5))  

        pygame.display.update()  

    return user_input


def show_wrong_answer_message():
    wrong_message = "Wrong Answer! Your score remains the same :("
    message_surface = font.render(wrong_message, True, (255, 0, 0))
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    WINDOW.blit(message_surface, message_rect)
    pygame.display.update()
    pygame.time.wait(1000) 
    WINDOW.fill((0, 0, 0)) 
    pygame.display.update()
def get_user_input(question):
    user_input = ""
    input_active = True
    input_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40)
    color_active = (255, 255, 255)
    current_color = color_active

    draw(score)
    display_question(question)
    pygame.display.update()

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        pygame.draw.rect(WINDOW, (0, 0, 0), input_rect)
        pygame.draw.rect(WINDOW, current_color, input_rect, 2)

        input_text = font.render(user_input, True, (255, 255, 255))
        WINDOW.blit(input_text, (input_rect.x + 10, input_rect.y + 5))

        pygame.display.update()

    return user_input

def main():
    global score, card_rects, card_faces, card_status, cards
    card_rects = []
    card_faces = []
    card_status = []
    cards = front_images * 2
    random.shuffle(cards)

    matched_cards = []
    score = 0
    selected_cards = []
    flip_back_time = 0
    b = 20

    for i in range(4):
        a = 250
        for j in range(3):
            rect = back_image.get_rect(topleft=(a, b))
            card_rects.append(rect)
            if len(cards) > 0:
                card_faces.append(cards.pop())
            card_status.append(False)
            a += 170
        b += 170

    clock = pygame.time.Clock()

    run = True
    try:
        while run:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONUP and flip_back_time == 0:
                    mouse_position = pygame.mouse.get_pos()
                    for i, rect in enumerate(card_rects):
                        if rect.collidepoint(mouse_position) and not card_status[i] and i not in matched_cards:
                            card_status[i] = True
                            selected_cards.append(i)
                            if len(selected_cards) == 2:
                                if card_faces[selected_cards[0]] == card_faces[selected_cards[1]]:
                                    matched_cards.extend(selected_cards)
                                    selected_cards = []

                                    if len(matched_cards) == len(card_rects):
                                        end_game_screen() 
                                        return  

                                    question, answer = random.choice(questions)
                                    questions.remove((question, answer))
                                    user_answer = get_user_input(question)
                                    if user_answer.strip().lower() == answer.lower():
                                        score += 1
                                    else:
                                        show_wrong_answer_message()

                                else:
                                    flip_back_time = current_time + 1000

            if flip_back_time > 0 and current_time >= flip_back_time:
                card_status[selected_cards[0]] = False
                card_status[selected_cards[1]] = False
                selected_cards = []
                flip_back_time = 0

            draw(score)
            for i, rect in enumerate(card_rects):
                if i in matched_cards or card_status[i]:
                    WINDOW.blit(card_faces[i], rect.topleft)  
                else:
                    WINDOW.blit(back_image, rect.topleft)  
            pygame.display.flip()
            clock.tick(60)

    except Exception as e:
        print(f"Error occurred: {e}")
    
    pygame.quit()
if __name__ == "__main__":
    while True:
        pygame.init()  
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) 

        main() 
