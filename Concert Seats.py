def can_see_stage(seats):
    num_rows = len(seats)
    num_cols = len(seats[0])
    for col in range(num_cols):
        for row in range(1, num_rows):
            # Check if the current element is not greater than the element before it
            if seats[row][col] <= seats[row - 1][col]:
                return False  # If not, someone cannot see the front-stage

    return True  # If all elements pass the visibility check


print(can_see_stage([[2, 0, 0],
                     [1, 1, 1],
                     [2, 2, 2]
                     ]))
