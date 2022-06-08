# Project made by Anthony
# imports turtle to draw
import turtle

# Adds the valid colors in a string
VALID_COLORS: list = [
    "red", "blue", "green", "purple", "yellow", "orange", "pink", "black",
    "white", "rainbow"
]
# Adds the colors of the rainbow in order in a string
RAINBOW: tuple = ("red", "blue", "green", "purple", "yellow", "orange", "pink",
                  "black", "white")


def gui_input_checker(title: str, question: str, valid_answers: list,
                      screen: turtle.Screen()):
    """
    Checks if the input is valid
    :param title: title of the question
    :param question: the question to ask the user
    :param valid_answers: the valid answers
    :param screen: the screen
    :return: the valid answer
    """
    # has a quit button to exit as you got stuck on the color screen if you put in wrong input
    while True:
        answer = screen.textinput(title, question)
        if answer in valid_answers:
            return answer
        elif answer == "quit":
            exit()
        else:
            print("Invalid input Please try again")


def main():
    """
    Main function
    """
    # sets ups for turtle and screen so its full screen
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    t = turtle.Turtle()
    t.speed(1.5)
    spyro_list = []

    # asks the Questions also have limits of how big/small
    angle = 180 - int(
        screen.numinput("Angle", "What interior Angle?", 90, -360, 360))
    spynum = int(screen.numinput("Number", "How many sides?", 3, -1000, 1000))
    size = screen.numinput("Size", "How big?", 30, -1000, 1000)
    color = gui_input_checker("Color", "What color?(Type 'quit' to quit)",
                              VALID_COLORS, screen)
    repeat = int(
        screen.numinput("Repeat", "How many times do you want to repeat?", 3,
                        -1000, 1000))

    # how many sides for the list depending on how many numbers entered
    for i in range(spynum):
        spyro_list.append(
            int(
                screen.numinput("sides",
                                f"what size do you want for side {i + 1}?", 0,
                                -10, 10)))

    # Sets up to get it ready to draw
    def draw(angle_val, size_val, color_val, repeat_val, list_val):
        """
        Draws the shape with the given parameters.
        :param angle_val: the angle
        :param size_val: the size
        :param color_val: the color
        :param repeat_val: the repeat
        :param list_val: the list
        """
        # set up for the rainbow color and for turtle to draw the spyro
        if color_val == "rainbow":
            for _ in range(repeat_val):
                for i in range(len(list_val)):
                    t.color(RAINBOW[i])
                    t.forward(size_val * list_val[1])
                    t.left(angle_val)
        else:
            t.color(color_val)
            for _ in range(repeat_val):
                for i in range(len(list_val)):
                    t.forward(size_val * list_val[i])
                    t.right(angle_val)

    # Draws the spyro
    draw(angle, size, color, repeat, spyro_list)

    # lifts the pen after drawing shape
    t.pu()


# this is the end of the Main Function
if __name__ == "__main__":
    main()
