class Cube:
    """
    Represents a 3x3x3 Rubik's Cube.

    State:
        6 faces × 9 stickers = 54 stickers

    Face order:
        U = 0
        R = 1
        F = 2
        D = 3
        L = 4
        B = 5
    """

    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5

    NUM_FACES = 6
    STICKERS_PER_FACE = 9
    NUM_STICKERS = 54

    def __init__(self):
        self.state = self._create_solved_state()

    @classmethod
    def _create_solved_state(cls):
        return tuple(
            face
            for face in range(cls.NUM_FACES)
            for _ in range(cls.STICKERS_PER_FACE)
        )

    def is_solved(self):
        return self.state == self._create_solved_state()

    def is_valid(self):
        if len(self.state) != self.NUM_STICKERS:
            return False

        if any(color not in range(self.NUM_FACES) for color in self.state):
            return False

        for color in range(self.NUM_FACES):
            if self.state.count(color) != self.STICKERS_PER_FACE:
                return False

        return True

    def copy(self):
        new_cube = Cube()
        new_cube.state = self.state
        return new_cube

    def __eq__(self, other):
        if not isinstance(other, Cube):
            return NotImplemented

        return self.state == other.state

    def __str__(self):
        return f"Cube(state={self.state})"