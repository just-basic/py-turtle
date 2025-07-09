"""
    **Description:**

    This package contains turtle rainbow spiral art scenario

    **Functions:**

    -:func:`spiral_simple_art` - Turtle spiral simple art
    -:func:`rainbow_spiral_art_minimal` - Turtle rainbow spiral art minimal
"""
from typing import List, Tuple

from values import ConstantsValues as Constant, ColorPalette
from classes import TurtleSetup


# region Turtle rainbow simple art
def spiral_simple_art(*, turtle: TurtleSetup, times: int = 200, rotation_angle: int, speed:int, pallet: ColorPalette = ColorPalette.RAINBOW) -> None:
    """
    In this scenario Turtle will draw rainbow circle art
    :param turtle:
    :param times:
    :param rotation_angle:
    :param speed:
    :param pallet:
    :return:
    """
    turtle.init(speed=speed)
    turtle.display_text(position_x=0, position_y=340, message=f"{pallet.value} Simple Spiral Art")
    turtle.display_text(position_x=280, position_y=300, message=f"Angle: {rotation_angle}")
    turtle.display_text(position_x=280, position_y=260, message=f"Speed: {speed if speed <= 10 else "Instant"}")
    color_palet: List[Tuple[int, int, int]] = Constant.get_color_pallet(pallet=pallet)
    for i in range(times):
        turtle.turtle.color(color_palet[i % len(color_palet)])
        turtle.turtle.forward(i * 2)  # Move forward by increasing distance
        turtle.turtle.right(rotation_angle)


# endregion
# region Turtle rainbow simple art minimal
def rainbow_spiral_simple_art_minimal() -> None:
    """
    In this scenario Turtle will draw rainbow circle art, standalone minimal version
    :return:
    """
    import turtle
    from turtle import Turtle

    times: int = 135
    rotation_angle: int = 51

    _turtle: Turtle = turtle.Turtle()

    turtle.bgcolor('black')

    _turtle.speed(11)  # See docs

    colors: List[str] = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    for i in range(times):
        _turtle.color(colors[i % len(colors)])
        _turtle.forward(i * 2)  # Move forward by increasing distance
        _turtle.right(rotation_angle)

    turtle.done()


# endregion
if __name__ == '__main__':
    rainbow_spiral_simple_art_minimal()
