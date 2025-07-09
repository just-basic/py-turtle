""":class:`TurtleSetup`"""
import turtle

from values.value_constant import ConstantsValues


class TurtleSetup:
    """
    Turtle setup class is custom implementation for turtle management

    turtle - main turtle drawer
    label - additional hidden turtle drawer for displaying text

    """

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.label = turtle.Turtle()

    def init(self, *, speed: int = 10):
        """
        Init new turtle sandbox
        :param speed: Speed of tutle, see documentation. In short 1-10, other values instant speed
        :type speed: int
        :return:
        """
        turtle.title(titlestring="Turtle ART")
        turtle.setup(width=ConstantsValues.WINDOW_WIDTH, height=ConstantsValues.WINDOW_HEIGHT)
        turtle.bgcolor('black')
        turtle.colormode(255)  # Accept RGB tuples in 0–255 range
        self.turtle.speed(speed=speed)

    @staticmethod
    def stop() -> None:
        """
        Method for stopping turtle
        :return:
        """
        turtle.done()

    @staticmethod
    def exit() -> None:
        """
        Method for killing turtle
        :return:
        """
        turtle.bye()

    def reset(self) -> None:
        """
        This method will restart turtle and reset color.
        :return:
        """
        # Reset main turtle
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()
        self.turtle.speed(11)  # or your default speed
        self.turtle.color("black", "white")  # Reset to default pen and fill color

        # Reset label turtle
        self.label.clear()
        self.label.hideturtle()
        self.label.penup()
        self.label.home()
        self.label.color("black", "white")  # Reset label color

    def display_text(self, *, position_x: int, position_y: int, message: str) -> None:
        """
        This method display custom UI text in window. It will set the text form original turtle position
        :param position_x: Step x
        :type position_x: int
        :param position_y: Step y
        :type position_y: int
        :param message: Text to display
        :type message: str
        :return:
        """
        self.label.hideturtle()
        self.label.penup()
        self.label.goto(position_x, position_y)
        self.label.color("white")
        self.label.write(message, align="center", font=("Arial", 20, "bold"))
