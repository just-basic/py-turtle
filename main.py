"""MAIN PACKAGE"""
import random
import time
import tkinter
import turtle
from classes import TurtleSetup,ScenariosLib
from values import ColorPalette

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    turtle_setup: TurtleSetup = TurtleSetup()
    scenarios_lib: ScenariosLib = ScenariosLib(turtle_setup=turtle_setup, speed=11, pallet=ColorPalette.RAINBOW)

    try:
        while True:
            try:
                scenarios_lib.pallet = random.choice(list(ColorPalette))
                random.choice(scenarios_lib.calls)()
                time.sleep(3)
                turtle_setup.reset()
            except (turtle.Terminator, tkinter.TclError):
                print("Turtle window was closed manually. Exiting loop.")
                break
    except KeyboardInterrupt:
        print("\nInterrupted by user with Ctrl+C.")
    finally:
        try:
            turtle_setup.exit()
        except (turtle.Terminator, tkinter.TclError):
            print("Turtle already closed.")


