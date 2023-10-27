def robot_path(commands):
    xY1 = {"x": 3,
           "y": 2}
    xY2 = {"x": -4,
           "y": 3}
    sum = {"x": 0,
           "y": 0}
    for i in commands:
        if i == "n":
            sum["y"] += 1
        elif i == "e":
            sum["x"] += 1
        elif i == "s":
            sum["y"] -= 1
        else:
            sum["x"] -= 1
    return sum == xY1 or sum == xY2


print(robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"]))
