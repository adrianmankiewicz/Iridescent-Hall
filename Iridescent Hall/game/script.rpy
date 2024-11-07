# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#dcffcc")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "Examples will show up in a window like the one above. You'll need to click outside of the example window in order to advance the tutorial."

    e "When an example is bigger than the screen, you can scroll around in it using the mouse wheel or by simply dragging the mouse."

    e "Do you understand me??"
 
    menu:
        
        "Yes, I do.":
            jump choice1_yes
        "No, I don't.":
            jump choice1_no

    label choice1_yes:
        $ menu_flag = True
        e "Good."
        jump choice1_done

    label choice1_no:
        $ menu_flag = False
        e "Idiot."
        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 

    # This ends the game.

    return
