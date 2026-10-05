def rotate_face_clockwise(face):
    """
    Rotate a face clockwise.
    """
    return (
        face[6], face[3], face[0],
        face[7], face[4], face[1],
        face[8], face[5], face[2],
    )

def rotate_face_counterclockwise(face):
    """
    Rotate a face counterclockwise.
    """
    return (
        face[2], face[5], face[8],
        face[1], face[4], face[7],
        face[0], face[3], face[6],
    )