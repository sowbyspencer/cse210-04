from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """A subclass inherited from Actor

    Attributes:
        _message (string): The text to display when found by the robot.
    """

    def __init__(self):
        """Constructs a new Artifact"""
        super().__init__()

    def calculate_points(self):
        """
        This function takes in an artifact object and returns the points associated with that artifact
        :return: The points that the artifact is worth.
        """
        
        points = 0

        # Checking the text of the artifact and assigning points based on the text.
        if (self.get_text() == '*'):
            points = 1
        elif (self.get_text() == '^'):
            points = 2
        elif (self.get_text() == 'X'):
            points = -3
        else:
            points = -1
        
        return points