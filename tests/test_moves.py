from rubiks_ml.cube.moves import rotate_face_clockwise, rotate_face_counterclockwise


class TestFaceRotation:

    def test_rotate_clockwise(self):
        face = (
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        )

        rotated = rotate_face_clockwise(face)

        assert rotated == (
            6, 3, 0,
            7, 4, 1,
            8, 5, 2,
        )

    def test_rotate_counterclockwise(self):
        face = (
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        )

        rotated = rotate_face_counterclockwise(face)

       
        assert rotated == (
            2, 5, 8,
            1, 4, 7,
            0, 3, 6,
        )
    
    def test_clockwise_then_counterclockwise(self):
        face = (
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        )

        rotated = rotate_face_clockwise(face)
        rotated = rotate_face_counterclockwise(rotated)

        assert rotated == face
    
    def test_four_clockwise_rotations(self):
        face = (
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        )

        rotated = face

        for _ in range(4):
            rotated = rotate_face_clockwise(rotated)

        assert rotated == face