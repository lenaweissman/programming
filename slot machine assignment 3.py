#This program creates a slot machine game
#Created by Lena Weissman
from DrawingPanel import *
import random

def main():
    # Create slot machine layout
    panel = DrawingPanel(600, 500, background="red")
    panel.fill_rect(10, 10, 580, 300, color="white")
    panel.fill_rect(10, 350, 580, 100, color="blue")

    # Set up initial display with token count
    tokens = 5
    new_random = 1
    panel.draw_image(f"/Users/lenaweissman/Desktop/MIS 443 /Programming Assignment 3 Pictures 2/picture{new_random}.png", 75, 50)

    # Create a list of token values
    token_values =[5,4,1,2,3,0,1,0,0,3,2,0,4,10,2,0,2,0,0,0,-1,0,0,-1,-5,0,0]


    # Image names for the fruit combinations (from picture1.png to picture27.png)
    image_names = [f"picture{i}.png" for i in range(1, 28)]

    # Define the path to images
    image_path = "/Users/lenaweissman/Desktop/MIS 443 /Programming Assignment 3 Pictures 2"

    # Display the initial message
    panel.draw_string("Let's get started", 205, 385, color="white", font=("Helvetica", 24, "bold"))
    panel.sleep(2000)
    panel.fill_rect(10, 350, 580, 100, color="blue")
    panel.draw_string(f"You start with {tokens} tokens", 175, 385, color="white", font=("Helvetica", 24, "bold"))
    panel.sleep(2000)
    panel.fill_rect(10, 350, 580, 100, color="blue")  # Clear the bottom area

    first_spin = True  # Flag to check if user has spun at least once

    # Main game loop
    while tokens > 0:
        # Ask if the user wants to play again
        if not panel.message_yes_no('Do you want to spin?', title='Play?'):
            panel.fill_rect(10, 350, 580, 100, color="blue")  # Clear the bottom area
            if first_spin:
                panel.draw_string("Have a great day!", 200, 375, color="white", font=("Helvetica", 24, "bold"))
            else:
                panel.draw_string(f"Your final token count is {tokens}", 150, 375, color="white", font=("Helvetica", 24, "bold"))
            panel.sleep(2000)
            exit()  # End the game if the player chooses not to spin

        first_spin = False  # Set flag to false after first spin

        # Deduct 1 token for the spin
        tokens -= 1
        panel.fill_rect(10, 350, 580, 100, color="blue")  # Clear the bottom area
        panel.draw_string("Spin", 270, 385, color="white", font=("Helvetica", 24, "bold"))

        # Randomly choose one fruit image and the corresponding token value
        new_random = random.randint(0, 26)  # Randomly pick 1 index (0-26 for picture1.png to picture27.png)
        image_to_show = image_names[new_random]
        points_won = token_values[new_random]

        # Display the image in the slot machine area
        panel.draw_image(f"{image_path}/{image_to_show}", 75, 50)

        # Calculate tokens won or lost and update token count
        win_loss = points_won
        tokens += win_loss

        # Display the result
        panel.sleep(1000)  # Give some time to show the image
        panel.fill_rect(10, 350, 580, 100, color="blue")  # Clear the bottom area

        # Show the points won/lost and the updated token count
        panel.draw_string(f"Token value of spin: {win_loss}", 215, 375, color="white", font=("Helvetica", 18, "bold"))
        panel.draw_string(f"Current tokens: {tokens}", 235, 400, color="white", font=("Helvetica", 18, "bold"))

        panel.sleep(2000)  # Wait a bit before asking to spin again

        if tokens <= 0:
            panel.fill_rect(10, 350, 580, 100, color="blue")  # Clear the bottom area
            panel.draw_string("Sorry, you're out of tokens", 135, 380, color="white", font=("Helvetica", 24, "bold"))
            panel.sleep(2000)

main()
