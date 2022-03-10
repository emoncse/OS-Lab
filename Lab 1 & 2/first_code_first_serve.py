b_time = []
number_of_process = int(input("Enter the number of Processes: "))
process_serial = 1
for i in range(number_of_process):
    print("For process = ", process_serial, end='')
    b_time.append(int(input(", Burst_time = ")))
    process_serial = process_serial + 1
print("\n")
w_time = []
avg_w_time = 0
w_time.insert(0, 0)
for j in range(1, len(b_time)):
    w_time.insert(j, (w_time[j - 1] + b_time[j - 1]))
    avg_w_time += w_time[j]
avg_w_time = float(avg_w_time / number_of_process)
process = 1

for k in range(0, number_of_process):
    if k == 0:
        print(w_time[k], end=" ")
    print("P" + str(process), (w_time[k] + b_time[k]), end=' ')
    process += 1

print("\n Average Waiting Time = ", avg_w_time)