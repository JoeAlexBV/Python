"""
Have the function OverlappingRectangles(strArr) read the strArr parameter
being passed which will represent two rectangles on a Cartesian coordinate
plane and will contain 8 coordinates with the first 4 making up rectangle
1 and the last 4 making up rectange 2.

It will be in the following format:
["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"]
Your program should determine the area of the space where the two rectangles
overlap, and then output the number of times this overlapping region can fit
into the first rectangle.

For the above example, the overlapping region makes up a rectangle of area 2,
and the first rectangle (the first 4 coordinates) makes up a rectangle area 4.
So your program should output 2.
The coordinates will all be integers.
If there's no overlap between the two rectangles return 0.
"""


def get_area(coords):
    x = []
    y = []
    for i in range(0, 8, 2):
        x.append(coords[i])
        y.append(coords[i + 1])

    min_x = int(min(x))
    min_y = int(min(y))
    max_x = int(max(x))
    max_y = int(max(y))

    area = abs((max_x - min_x) * (max_y - min_y))
    return area


def get_overlap(x, y):
    a_min_x = min(x[:4])
    a_min_y = min(y[:4])
    b_min_x = min(x[4:])
    b_min_y = min(y[4:])
    a_max_x = max(x[:4])
    a_max_y = max(y[:4])
    b_max_x = max(x[4:])
    b_max_y = max(y[4:])
    # 4 cases where this is True
    inner_square = []
    if (b_max_x > a_max_x > b_min_x) and (b_max_y > a_min_y):
        inner_square = [
            b_min_x,
            b_max_y,
            a_max_x,
            b_max_y,
            a_max_x,
            a_min_y,
            b_min_x,
            a_min_y,
        ]
    if (a_max_x > b_max_x > a_min_x) and (a_max_y > b_min_y):
        inner_square = [
            a_min_x,
            a_max_y,
            b_max_x,
            a_max_y,
            b_max_x,
            b_min_y,
            a_min_x,
            b_min_y,
        ]
    if (b_min_x > a_min_x > b_max_x) and (b_max_y > a_min_y):
        inner_square = [
            a_min_x,
            b_max_y,
            a_min_x,
            a_min_y,
            b_max_x,
            a_min_y,
            b_max_x,
            b_max_y,
        ]
    if (a_min_x > b_min_x > a_max_x) and (a_max_y > b_min_y):
        inner_square = [
            b_min_x,
            a_max_y,
            b_min_x,
            a_min_y,
            a_max_x,
            b_min_y,
            a_max_x,
            a_max_y,
        ]
    return inner_square


def get_coords_hacky(strArr):
    # Brain blanking so creating this method ;)
    coords = strArr[0].replace("(", "")
    coords = coords.replace(")", "")
    return coords


def create_coord_list(strArr):
    coords = get_coords_hacky(strArr)
    coords = coords.split(",")
    s1 = coords[:8]
    # s2 = coords[8:]
    x = []
    y = []
    for i in range(0, 16, 2):
        x.append(coords[i])
        y.append(coords[i + 1])

    inner_square = get_overlap(x, y)
    if inner_square:
        square_one_area = get_area(s1)
        inner_area = get_area(inner_square)
        how_many_fit = square_one_area / inner_area
        return how_many_fit
    return 0


def OverlapRectangles(strArr):
    how_many_fit = create_coord_list(strArr)
    return how_many_fit


# keep this function call here
print(OverlapRectangles(["(0,0),(1,1),(1,0),(0,1),(1,0),(1,2),(6,0),(6,2)"]))
print(OverlapRectangles(["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"]))
