# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:37:53 2022

@author: Rishabh
"""

# importing the pygame
import pygame

# setting up the width and the background color of the window
WIDTH = 550
background_color = (38, 38, 38)
original_grid_element_color = (255, 255, 255)
buffer = 5

#creating base grid
grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

grid_solved = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

#adding the functionality that can add the number on user bases
def insert(win, position):
    i,j = position[1], position[0]
    #adding the font and its size
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    box_color = (205,51,51)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                   
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, box_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 < 10):  #We are checking for valid input
                    pygame.draw.rect(win, box_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (179, 179, 179))
                    win.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return

# create a home page
def create_home_page(win):
    # create a home page message
    # screen = pygame.display.set_mode((400,300))
    smallHomeFont = pygame.font.SysFont('Comic Sans MS', 14)
    bigHomeFont = pygame.font.SysFont('Comic Sans MS', 20)
    welcomeMessage = bigHomeFont.render("Welcome to SUDOKU!", True, (255,97,3))
    instruction1 = smallHomeFont.render("1. Hit an empty box and choose number 1-9", True, (0, 255, 0))
    instruction2 = smallHomeFont.render("2. Fill all empty boxes", True, (0, 255, 0))
    instruction3 = smallHomeFont.render("3. If you want to end the game early. hit ESC key or X button", True, (0, 255, 0))
    message = bigHomeFont.render("Press ENTER to start the game, ENJOY!", True, (255, 0, 0))

    # draw the messages on the screen
    win.blit(welcomeMessage, (100,100))
    win.blit(instruction1, (100,200))
    win.blit(instruction2, (100,250))
    win.blit(instruction3, (100,300))
    win.blit(message, (100,450))

    # update the screen
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # if the user presses the `Enter` key, go to the next screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                win.fill(background_color)
                create_grid(win)
                return

#function that if we press the quit key then the pygame window will close.   
def is_quit(win):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
                # This part needs to be changed in a way where when enter is clicked then it moves to the final screen function that shows whether it is solved or not
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                 create_final_screen(win)
                 pygame.display.update()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                pygame.quit()
                return

# creating grid        
def create_grid(win):
    gridFont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0,10):
        if(i % 3 == 0):
            #drawing the block line (vertical)
            pygame.draw.line(win, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            #(Horizontal)
            pygame.draw.line(win, (255, 255, 255), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        #drawing vertical line
        pygame.draw.line(win, (166, 166, 166), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        #drawing horizontal line
        pygame.draw.line(win, (166, 166, 166), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
   
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10):
                value = gridFont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
    is_quit(win)

def is_filled():
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 0:
                return False

    return True

def is_solved():
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] != grid_solved[row][col]:
                return False

    return True

def create_final_screen(win):
    resultFont = pygame.font.SysFont('Comic Sans MS', 30)
    if is_solved() == True:
        resultMessage = resultFont.render("Congratulations! You have won!", True, (255,97,3))
    else:
        resultMessage = resultFont.render("You have lost:(", True, (255,97,3))

    win.fill(background_color)
    win.blit(resultMessage, (100, 300))

#initializing pygame
def main():   
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH)) # creating the window
    pygame.display.set_caption("Sudoku") #giving caption
    win.fill(background_color) # filling the window with background color
    create_home_page(win)

main()


# import pygame

# # Initialize Pygame
# pygame.init()

# # Set the screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# # Create the screen object
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # Create a variable to track whether the game is running
# running = True

# # Create a font object to use for rendering text
# font = pygame.font.Font(None, 24)

# # Create a text surface object to render the text
# text = font.render("Press Enter to start", True, (255, 255, 255))

# # Define the position of the text on the screen
# text_rect = text.get_rect()
# text_rect.centerx = screen.get_rect().centerx
# text_rect.centery = screen.get_rect().centery

# # Main game loop
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 # Move to the next screen when the enter key is pressed
#                 pass

#     # Clear the screen
#     screen.fill((0, 0, 0))

#     # Render the text
#     screen.blit(text, text_rect)

#     # Update the screen
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
