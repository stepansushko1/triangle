from math import sqrt


def input_data(side1: float, side2: float, side3: float, accuracy: float):
    """ Input data from user
    >>> input_data(10, 10, 12, 2)
    (10, 10, 12, 2)
    """

    return side1, side2, side3, accuracy


def file_reader(path: str):
    """ Read data from file """
    with open(path, "r", encoding="utf-8") as file:
        data = []
        for line in file:
            line = line.strip()
            data.append(float(line))
        return tuple(data)


def triangle_square(side1: float, side2: float, side3: float):
    """ Find square of triangle
    >>> print(triangle_square(10,10,12))
    48.0
    """
    semi_perimetr = (side1 + side2 + side3) / 2

    square = sqrt(semi_perimetr * (semi_perimetr - side1) *
                  (semi_perimetr - side2) * (semi_perimetr - side3))

    return square


def height(square: float, side3: float):
    """ Find height of triangle
    >>> print(height(48, 12))
    8.0
    """
    height = 2 * square / side3

    return height


def square_side(side3, square, height, accuracy):
    """ Find side of square
    >>> print(square_side(12, 48, 8, 2))
    4.80
    """
    sq_side = 2 * square / (height + side3)

    return '{:.{}f}'.format(sq_side, accuracy)


def file_writer(sq_side: float, path: str):
    """ Write data to file """
    with open(path, "w", encoding="utf-8") as file:
        file.write(f"line of square = {str(sq_side)}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()