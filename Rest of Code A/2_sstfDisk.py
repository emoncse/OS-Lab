input_queue = list(map(int, input("Enter the value for queue: ").split(" ")))  # 98 183 37 122 14 124 65 67
head_start = int(input("Enter the head starts : "))

path = []
path.append(head_start)
total_distance = ""
ans = 0
while input_queue != []:
    mini = 99999
    index = 0
    for i in range(len(input_queue)):
        if abs(head_start - input_queue[i]) < mini:
            mini = abs(head_start - input_queue[i])
            index = i
    x = input_queue.pop(index)
    path.append(x)
    if x > head_start:
        total_distance += "(" + str(x) + "-" + str(head_start) + ")"
        ans += (x - head_start)
    else:
        total_distance += "(" + str(head_start) + "-" + str(x) + ")"
        ans += (head_start - x)

    if len(input_queue) > 0:
        total_distance += " + "

    head_start = x

print(f"Path: {path}")
print(f"Total Distances: {total_distance}")
print(f"Illustration shows total head movement of {ans} cylinders")
