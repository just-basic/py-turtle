"""
    **Description:**

    This package contains turtle simple shape scenario

    **Functions:**

    -:func:`simple_shape_art` - Turtle simple shape
    -:func:`rainbow_spiral_art_minimal` - Turtle rainbow spiral circle art minimal
"""
from typing import List, Tuple

from values import ConstantsValues as Constant, ColorPalette
from classes import TurtleSetup


# region Turtle simple shape
def simple_shape_art(*, turtle: TurtleSetup, edges: int = 3, speed: int,
                      pallet: ColorPalette = ColorPalette.RAINBOW) -> None:
    """
    In this scenario Turtle will draw rainbow circle art
    :param turtle:
    :param edges:
    :param speed:
    :param pallet:
    :return:
    """
    turtle.init(speed=speed)
    turtle.display_text(position_x=0, position_y=340, message=f"{pallet.value} {edges}-edges simple shape")
    turtle.display_text(position_x=280, position_y=300, message=f"Edges: {edges}")
    turtle.display_text(position_x=280, position_y=260, message=f"Speed: {speed if speed <= 10 else "Instant"}")
    color_palet: List[Tuple[int, int, int]] = Constant.get_color_pallet(pallet=pallet)
    turtle.turtle.speed(10)  # See docs
    step: int = 1200

    rotation_angle: float = 360 / edges

    turtle.turtle.right(90)
    turtle.turtle.forward(int(step / 4))
    turtle.turtle.right(-90)
    turtle.turtle.backward(int(step/edges/2))

    for i in range(edges):
        turtle.turtle.color(color_palet[i % len(color_palet)])
        turtle.turtle.forward(step/edges)
        turtle.turtle.right(-rotation_angle)



# endregion
# region Turtle rainbow spiral circle art minimal
def simple_shape_art_minimal() -> None:
    """
    In this scenario Turtle will draw rainbow circle art, standalone minimal version
    :return:
    """
    import turtle
    from turtle import Turtle

    edges: int = 8
    step: int = 1200
    rotation_angle: int = int(360 / edges)
    _turtle: Turtle = turtle.Turtle()
    turtle.bgcolor('black')
    _turtle.speed(10)  # See docs
    _turtle.right(90)
    _turtle.forward(int(step / 4))
    _turtle.right(-90)
    _turtle.backward(int(step/edges/2))

    for i in range(edges):
        _turtle.color('white')
        _turtle.forward(step/edges)
        _turtle.right(-rotation_angle)
    _turtle.forward(int(step/edges/2))
    turtle.done()


# endregion
if __name__ == '__main__':
    simple_shape_art_minimal()
