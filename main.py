import time
import game
import pygame
import sys
import login
from pygame import mixer

# RGB colour codes used for background & buttons
green = [13,130,28]
green_2 = [13,130,28]

#Allows all text to be shown on screen, specifying colour and text
def render_text(text, x, y, font, color=(255, 255, 255)):
    font = pygame.font.Font(None, 30)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def volume_control():
    mixer.init()
    # List of available songs to play
    songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
    current_song = songs[0]
    current_song_index = 0
    back_settings_flag = False

    running = True
    volume = 0.5  # Initial volume (0.5 is the default)
    is_dragging = False  # Flag to track slider dragging

    volume_slider_rect = pygame.Rect(width // 4, height // 2, width // 2, 10)

    # Create buttons for song selctions
    song_buttons = [Button(str(song)[:5].capitalize(), (width // 8) + i * (width // 4),
                           height // 2 + 40, lambda s=song: change_song(s)) for i, song in enumerate(songs)]

    def back_settings_flag():
        # Checks whether the user opts to go back to settings
        nonlocal running
        running = False

    def change_song(song):
        # Loads the song chosen and plays the file 
        nonlocal current_song
        nonlocal current_song_index
        current_song = song
        current_song_index = songs.index(song)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_settings_button.rect.collidepoint(event.pos):
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Check if the mouse is over the volume slider
                    if volume_slider_rect.collidepoint(event.pos):
                        is_dragging = True

                    # Check if a song button was clicked
                    for button in song_buttons:
                        if button.rect.collidepoint(event.pos):
                            button.action()

            if event.type == pygame.MOUSEMOTION:
                if is_dragging:
                    # Update the volume based on the slider position
                    volume = (event.pos[0] - volume_slider_rect.left) / volume_slider_rect.width
                    # Ensure the volume is within the range [0, 1]
                    volume = max(0.0, min(1.0, volume))
                    pygame.mixer.music.set_volume(volume)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_dragging = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Increase the volume (you can adjust the step)
                    volume += 0.1
                    # Ensure the volume does not exceed 1.0
                    volume = min(1.0, volume)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_DOWN:
                    # Decrease the volume (you can adjust the step)
                    volume -= 0.1
                    # Ensure the volume does not go below 0.0
                    volume = max(0.0, volume)
                    pygame.mixer.music.set_volume(volume)

        # Draw the volume slider
        screen.fill(green)  # Clear the screen
        pygame.draw.rect(screen, (0, 0, 0), volume_slider_rect)
        slider_pos = int((volume * volume_slider_rect.width) + volume_slider_rect.left)
        pygame.draw.rect(screen, (255, 0, 0), (slider_pos - 5, volume_slider_rect.top, 10, volume_slider_rect.height))

        # Display the current volume as a percentage
        volume_text = menu_font.render(f"Volume: {int(volume * 100)}%", True, (0, 0, 0))
        volume_text_rect = volume_text.get_rect(center=(width // 2, height // 2 - 40))
        screen.blit(volume_text, volume_text_rect)
        # Display buttons for song selection
        for button in song_buttons:
            button.draw()
        back_settings_button = Button("Back", 50, 50, back_settings_flag)
        back_settings_button.draw()
        render_text(f"Currently Playing is: Song {current_song_index + 1} ", 100, 500, None)

        pygame.display.update()

    pygame.quit()
    sys.exit()


def end_game():
    screen.fill(green)
    game_over_font = pygame.font.SysFont("comicsans", 70)
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.quit()
    sys.exit()


def back_song():
    pygame.mixer.music.load("song1.mp3")
    pygame.mixer.music.play(-1)  # minus one makes the song play on a forever loop


def open_tkinter_script():
    login.login_screen()



def rules():
 # Initialize Pygame
    pygame.init()

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set up the window
    width, height = (800, 600)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("BlackJack Rules")

    # Set up fonts
    title_font = pygame.font.Font(None, 80)
    text_font = pygame.font.Font(None, 30)
    

    # Define the title text
    title_text = "BlackJack Rules"
    title_render = title_font.render(title_text, True, WHITE)
    title_rect = title_render.get_rect(center=(width // 2, 50))
    

    # Define the text content
    text_content = [
        "Aim of the Game: Have cards which values add up to 21.",
        "If above 21, you go BUST",
        "If values < 21, highest between user & dealer wins",
        "Controls: Navigate through the program using the labeled buttons.",
        "Music preferences can be changed in volume control.",
        "Your Points, Wins & Losses will be counted",
        "Progress is tracked on the bottom right of the game page"
    ]

    # Render the title text
    title_render = title_font.render(title_text, True, WHITE)
    title_rect = title_render.get_rect(center=(width // 2, 50))
    

    # Render the bullet-pointed text
    text_objects = [text_font.render("• " + line, True, WHITE) for line in text_content]

    # Calculate total text height and adjust starting position
    total_text_height = sum(obj.get_height() for obj in text_objects)
    text_y = (height - total_text_height) // 2

    # Blit the title text and bullet-pointed text onto the screen
    screen.fill(green)

    back_settings_button = Button("Back", 530, 100, None)
    back_settings_button.draw() 
            
    screen.blit(title_render, title_rect)

    for obj in text_objects:
        text_rect = obj.get_rect(topleft=(50, text_y))
        screen.blit(obj, text_rect)
        text_y += obj.get_height()

    # Update the display
    pygame.display.flip()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_settings_button.rect.collidepoint(event.pos):   
                        return      

                        # Control the frame rate
            pygame.time.Clock().tick(30)


def settings():
    def volume_cont():
        volume_control()

    def show_rules():
        rules()

    def endgame():
        end_game()

    def menu_button():
        print("")

    volume_button = Button("Volume Control", (width // 2) - 100, 200, volume_control)
    rules_button = Button("Game Rules", (width // 2) - 100, 270, show_rules)
    end_button = Button("End Game", (width // 2) - 100, 410, endgame)
    main_button = Button("Main Menu", (width // 2) - 100, 340, menu_button)
    settings_button = [volume_button, rules_button, end_button, main_button]
    settings_menu_running = True
    while settings_menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_menu_running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if main_button.rect.collidepoint(event.pos):
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in settings_button:
                        if button.rect.collidepoint(event.pos):
                            button.action()
        screen.fill(green)
        for button in settings_button:
            button.draw()
        pygame.display.update()


class Button:
    def __init__(self, button_name, x, y, action):
        self.rect = pygame.rect.Rect(x, y, 200, 50)
        self.button_name = button_name
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, green_2, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)
        text_surface = menu_font.render(self.button_name, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


print(login.logged_in())

pygame.init()
width = 800
height = 600
white = (255, 255, 255)
menu_font = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("NEA")

title_page_font = pygame.font.SysFont(None, 50)
title_page_text = title_page_font.render("BlackJack NEA", True, (255, 0, 0))
title_page_rect = title_page_text.get_rect(center=(width // 2, height // 2))
screen.blit(title_page_text, title_page_rect)


def game_open():
    game.main()


if login.logged_in():
    signin_button = Button("Start Game", (width // 2) - 100, 200, game_open)
elif login.logged_in()==False:
    signin_button = Button("Login & Signup", (width // 2) - 100, 200, open_tkinter_script)
settings_button = Button("Settings", (width // 2) - 100, 270, settings)
end_button = Button("End Game", (width // 2) - 100, 340, end_game)

buttons = [signin_button, settings_button, end_button]

back_song()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        button.action()



    screen.fill(green)

    title_page_font = pygame.font.SysFont(None, 70)
    title_page_text = title_page_font.render("BlackJack NEA", True, (255, 255, 255))
    title_page_rect = title_page_text.get_rect(center=(width // 2, height / 10))
    screen.blit(title_page_text, title_page_rect)

    username_page_font = pygame.font.SysFont(None, 32)
    username_page_text = username_page_font.render("Welcome to the game: " + login.username_page1(), True, (255, 255, 255))
    username_page_rect = username_page_text.get_rect(center=(width // 2, height / 5))
    screen.blit(username_page_text, username_page_rect)

    for button in buttons:
        button.draw()
    pygame.display.update()
pygame.quit()
sys.exit()


