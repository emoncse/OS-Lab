input_queue = list(map(int, input("Enter the value for queue: ").split(" ")))
head_start = int(input("Enter the head starts : "))

path = []
path.append(head_start)
total_distance = ""
ans = 0
while input_queue != []:
    x = input_queue.pop(0)
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
