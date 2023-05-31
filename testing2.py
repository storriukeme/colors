from settings import logger
from colors.color import get_color

def color_for_car():
    color  = get_color()
    logger.info(f"The color for the car is {color}")
    

if __name__ == "__main__":
    color_for_car()