""":class:`ConstantsValues`"""
from typing import List, Tuple

from values.color_palette_values import ColorPalette


class ConstantsValues:
    """This class contains constant values"""
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 800

    WHITE_RGB: Tuple[int, int, int] = (255, 255, 255)
    RED_RGB: Tuple[int, int, int] = (255, 0, 0)
    ORANGE_RGB: Tuple[int, int, int] = (255, 127, 0)
    YELLOW_RGB: Tuple[int, int, int] = (255, 255, 0)
    GREEN_RGB: Tuple[int, int, int] = (0, 255, 0)
    BLUE_RGB: Tuple[int, int, int] = (0, 0, 255)
    INDIGO_RGB: Tuple[int, int, int] = (75, 0, 130)
    VIOLET_RGB: Tuple[int, int, int] = (148, 0, 211)

    @staticmethod
    def get_color_pallet(pallet: ColorPalette) -> List[Tuple[int, int, int]]:
        """
        Returns color pallet, default rainbow
        :param pallet: pallet name default rainbow
        :type pallet: str
        :return:
        """
        if pallet == ColorPalette.RAINBOW:
            return [
                ConstantsValues.RED_RGB,
                ConstantsValues.ORANGE_RGB,
                ConstantsValues.YELLOW_RGB,
                ConstantsValues.GREEN_RGB,
                ConstantsValues.BLUE_RGB,
                ConstantsValues.INDIGO_RGB,
                ConstantsValues.VIOLET_RGB
            ]
        else:
            return [ConstantsValues.WHITE_RGB]
