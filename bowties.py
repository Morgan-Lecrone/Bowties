"""
This program draws bowties recursively using Python's Turtle Graphics.

@author Morgan Lecrone
"""
import turtle

def draw_one_bowtie(size):
    """
    This function draws a singular bowtie.

    size: The initial size of one side of the triangle that makes up the bowtie.

    Preconditions: The turtle is at the center of the bowtie, facing the bowtie's local East.
    Postconditions: The turtle is at the center of the bowtie, facing the bowtie's local East.
    """
    turtle.up()
    turtle.pencolor("#4e6ef2")
    turtle.fillcolor("#ba8fff")
    turtle.begin_fill()
    turtle.left(30)
    turtle.forward(size/4)
    turtle.left(90)
    turtle.down()
    turtle.circle(size/4)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(size*.75)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size*.75)
    turtle.up()
    turtle.forward(size/2)
    turtle.down()
    turtle.forward(size*.75)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size*.75)
    turtle.up()
    turtle.forward(size/4)
    turtle.right(30)


def draw_bowties(depth,size):
    """
    This function draws bowties recursively beginning with one bowtie in the middle and drawing
    4 additional bowties for each level of depth, one from each corner of the original bowtie.

    depth: The number of times that the function recurses to draw the picture.
    size: The initial size of one side of the triangle that makes up the bowtie.

    Preconditions: The turtle is at the origin, facing East.
    Postconditions: The turtle is at the origin, facing East.
    """
    if depth == 1:
        draw_one_bowtie(size)
    elif depth > 1:
        draw_one_bowtie(size)
        turtle.up()
        turtle.left(30)
        turtle.forward(size * 2)
        draw_bowties(depth-1, size/3)
        turtle.up()
        turtle.back(size * 2)
        turtle.left(120)
        turtle.forward(size * 2)
        draw_bowties(depth-1, size/3)
        turtle.up()
        turtle.back(size * 2)
        turtle.left(60)
        turtle.forward(size * 2)
        draw_bowties(depth-1, size/3)
        turtle.up()
        turtle.back(size*2)
        turtle.left(120)
        turtle.forward(size*2)
        draw_bowties(depth-1, size/3)
        turtle.back(size*2)
        turtle.left(30)

def main():
    """
    This function sets the turtle speed at 0 and asks the user what the depth
    of the drawing will be.  It then draws the recursive bowties.

    Preconditions: The turtle is at the origin, facing East.
    Postconditions: The turtle is at the origin, facing East.
    """
    turtle.speed(0)
    draw_bowties(int(input("What will the depth be?")),120)
    turtle.done


if __name__ == '__main__':
    main()
