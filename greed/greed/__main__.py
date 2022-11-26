# It imports the modules and classes that the game needs.
# It imports the os and random modules.
import os
import random

# It imports the Actor, Artifact, and Cast classes from the game.casting module.
from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

# It imports the Director class from the game.directing module.
from game.directing.director import Director

# Importing the KeyboardService and VideoService classes from the game.services module.
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

# Importing the Color and Point classes from the game.shared module.
from game.shared.color import Color
from game.shared.point import Point

# Defining the constants of the game.
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "GREED"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

def main():
    """
    It creates a cast, adds a banner and a robot to it, and then creates a number of artifacts and adds
    them to the cast then starts the game.
    """
    
    # create the cast
    cast = Cast()
    
    # It creates a banner actor and adds it to the cast.
    banner = Actor()
    banner.set_text("Score: ")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    position = Point(x, MAX_Y - 20)

    # Creating a robot actor and adding it to the cast.
    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(['*', 'O', '^', 'X'])

        # Creating a random position for the artifact.
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # Creating a random color.
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # It creates an artifact actor and adds it to the cast.
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(Point(0, 5))
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

# A way to tell Python that this file is the main file.
if __name__ == "__main__":
    main()