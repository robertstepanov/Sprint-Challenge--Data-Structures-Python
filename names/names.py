import time
from collections import defaultdict
start_time = time.time()

name = {}
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements

for name_1 in names_1:
    if name_1 not in name:
        name[name_1] = 1
    else:
        if name[name_1] == 1:
            duplicates.append(name_1)
        name[name_1] += 1

for name_2 in names_2:
    if name_2 not in name:
        name[name_2] = 1
    else:
        if name[name_2] == 1:
            duplicates.append(name_2)
        name[name_2] += 1

# ORIGINAL
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# for name in names_1:
#     name[name] += 1
# for name in names_2:
#     if name[name]:
#         duplicates.append(name)

# NOT SURE IF DEFAULTDICT IS CONSIDERED A DICT
# l = defaultdict(int)
# for name in names_1:
#     l[name] += 1
# for name in names_2:
#     if l[name]:
#         duplicates.append(name)

# SETS NOT ALLOWED
# duplicates = set(names_1) & set(names_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
