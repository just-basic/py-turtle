""":class:`ScenariosLib`"""
import random
from typing import List, Callable, Any, Optional

from classes import TurtleSetup
from scenarios import spiral_circle_art, spiral_simple_art, simple_shape_art
from values import ColorPalette


class ScenariosLib:
    """
    Class links all scenarios
    """

    def __init__(self, *, turtle_setup: TurtleSetup, speed: Optional[int] = None,
                 pallet: Optional[ColorPalette] = None):
        self.speed = speed if speed else random.randint(1, 11)
        self.pallet: ColorPalette = pallet if pallet else random.choice([ColorPalette.RAINBOW, ColorPalette.WHITE])
        self.calls: List[Callable[[], Any]] = [
            # Rainbow Spiral Art
            lambda: spiral_circle_art(turtle=turtle_setup, times=90, rotation_angle=random.randint(1, 360), speed=self.speed,
                                      pallet=self.pallet),
            # Rainbow Simple Art
            lambda: spiral_simple_art(turtle=turtle_setup, times=135, rotation_angle=random.randint(1, 360), speed=self.speed,
                                      pallet=self.pallet),
            # Simple shapes
            lambda: simple_shape_art(turtle=turtle_setup, edges=random.randint(1, 36), speed=self.speed,
                                      pallet=self.pallet),
        ]
        self.size = len(self.calls)
