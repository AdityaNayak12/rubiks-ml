from rubiks_ml.cube.cube import Cube


class TestCube:

    def test_create_solved_state(self):
        cube = Cube()

        assert cube.state == (
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2, 2, 2, 2, 2, 2,
            3, 3, 3, 3, 3, 3, 3, 3, 3,
            4, 4, 4, 4, 4, 4, 4, 4, 4,
            5, 5, 5, 5, 5, 5, 5, 5, 5,
        )

    def test_is_solved(self):
        cube = Cube()

        assert cube.is_solved()

    def test_is_valid(self):
        cube = Cube()

        assert cube.is_valid()

    def test_state_length(self):
        cube = Cube()

        assert len(cube.state) == 54

    def test_copy(self):
        cube = Cube()

        assert cube.copy() == cube

    def test_eq(self):
        cube1 = Cube()
        cube2 = Cube()

        assert cube1 == cube2

    def test_str(self):
        cube = Cube()

        assert str(cube) == (
            "Cube(state=("
            "0, 0, 0, 0, 0, 0, 0, 0, 0, "
            "1, 1, 1, 1, 1, 1, 1, 1, 1, "
            "2, 2, 2, 2, 2, 2, 2, 2, 2, "
            "3, 3, 3, 3, 3, 3, 3, 3, 3, "
            "4, 4, 4, 4, 4, 4, 4, 4, 4, "
            "5, 5, 5, 5, 5, 5, 5, 5, 5"
            "))"
        )