number_of_process = int(input("Enter Number of Process : "))
process = list()
while number_of_process != 0:
    process_name = input('Process Name: ')
    brust_time = int(input('Brust Time: '))
    priority = int(input('Priority: '))

    temp = (process_name, brust_time, priority)
    process.append(temp)
    number_of_process -= 1


def gantt_generator(process):
    time = 0
    waiting_time = 0
    gantt_string = ''
    for x in process:
        waiting_time += time
        gantt_string = gantt_string + str(time) + x[0]
        time += x[1]

    gantt_string = gantt_string + str(time)
    return (gantt_string, waiting_time / len(process))


def sorting_process(task):
    return sorted(task, key=lambda x: x[2])


sorted_process = sorting_process(task=process)
p = gantt_generator(process=sorted_process)
print('GANTT Chart String: ', p[0])
print('Average waiting Time: ', p[1])