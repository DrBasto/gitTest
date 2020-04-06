import math
groups = []
for _i in range(0, 3):
    groups.append(int(input("Give number of students\t")))
chair_1 = math.ceil(groups[0] / 2)
chair_2 = math.ceil(groups[1] / 2)
chair_3 = math.ceil(groups[2] / 2)
chairs = chair_1 + chair_2 + chair_3 
print(chairs)