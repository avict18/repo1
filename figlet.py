import os
import pyfiglet

# create function
def create_ascii_text():

    # create a list of fonts
    font_list = pyfiglet.FigletFont.getFonts()

    # Set default text
    default_text = "Lorem Ipsum"

    while True:
        os.system("cls")
        # Get text input from user
        print(" ------------------------- Avict's ASCII Text Creator Tool ----------------------- ")
        print("                                                                       'q' to quit ")
        print(" --------------------------------------------------------------------------------- ")

        text = input(f" >>> What text do you wish to convert to ASCII art? ({default_text}): ")
        if text == "q":
            exit()

        # set default test text - this will change if you add specific text!
        elif text == "":
            text = default_text
            print(f"\n ... Text input using default: '{text}'\n")

        # assign input text to default text for this run of the script
        else:
            default_text = text
            print(f"\n ... Text set to '{text}' and assigned to default for this session\n")

        # Get font choice from user
        while True:
            font_choice = input(" >>> Enter a font, '?' for a list or [ENTER] for all': ")
            if font_choice == "q":
               break

            # Display all fonts in a list if user enters '?'
            elif font_choice == "?":
                for font in font_list:
                    print(f"   {font}   ")

            # Display entered text in each font in list if no input
            elif font_choice == "":
                for font in font_list:
                    ASCII_art_1 = pyfiglet.figlet_format(text,font)
                    print(" --------------- ")
                    print(f" text: {text} ")
                    print(f" font: {font}\n ")
                    print(ASCII_art_1)
                    print(" --------------- ")

            # Try to display text in font input provided - error if no match!
            else:
                try:
                    ASCII_art_1 = pyfiglet.figlet_format(text,font=font_choice)
                    print(" --------------- ")
                    print(f" text: {text} ")
                    print(f" font: {font_choice}\n ")
                    print(ASCII_art_1)
                    print(" --------------- ")
                except:
                    print(" *** There was an error! The entered font '{font})' probably doesn't exist!")

            print(" --------------------------------------------------------------------------------- ")
            print("                                                                       'q' to quit ")
            print(" --------------------------------------------------------------------------------- ")
        # Get user input on checking another font or starting over.

# call function
while True:
    create_ascii_text()

# eof