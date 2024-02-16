# # def last_name_lensort(names):
# #     final = {}
# #     Final = []
# #     for a in names:
# #         final[a.split()[-1]] = len(a.split()[-1])
# #     finaly = sorted(final.items(), key=lambda x: x[1])
# #     for i in names:
# #         if finaly.keys() in i.split():
# #             Final.append(names)
# #     return Final


# # print(last_name_lensort(["Jennifer Figueroa",
# #                         "Heather Mcgee",
# #                          "Amanda Schwartz",
# #                          "Nicole Yoder",
# #                          "Melissa Hoffman"]))
# def last_name_lensort(names):
#     final = {}
#     Final = []

#     # Create a dictionary with last names as keys and their lengths as values
#     for a in names:
#         last_name = a.split()[-1]
#         final[last_name] = len(last_name)

#     # Sort the dictionary by the length of the last names
#     final_sorted = sorted(final.items(), key=lambda x: x[1])

#     # Create a list of names based on the sorted last names
#     for last_name, length in final_sorted:
#         for name in names:
#             if last_name == name.split()[-1]:
#                 Final.append(name)

#     return Final


# # Test the function
# print(last_name_lensort(["Jennifer Figueroa",
#                          "Heather Mcgee",
#                          "Amanda Schwartz",
#                          "Nicole Yoder",
#                          "Melissa Hoffman"]))
def last_name_lensort(names):
    final = {}
    Final = []

    for a in names:
        last_name = a.split()[-1]
        final[last_name] = len(last_name)

    final_sorted = sorted(final.items(), key=lambda x: (x[1], x[0]))

    for last_name, _ in final_sorted:
        for name in names:
            if last_name == name.split()[-1]:
                Final.append(name)

    return Final


# Test the function
print(last_name_lensort([
    "Jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Nicole Yoder",
    "Melissa Hoffman"
]))
