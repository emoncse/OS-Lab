# Disk Scheduling - FCFS

queue = [53, 98, 183, 37, 122, 14, 124, 65, 67];
head = 53;


def FCFS(queue, head):
    seek_count = 0
    distance, cur_track = 0, 0
    print("Path")
    for i in range(len(queue)):
        print(queue[i], end=' ')

    for i in range(len(queue)):
        cur_track = queue[i]
        # calculate absolute distance
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    print(' ')
    print("Total Head movement = ", seek_count, 'cylinders')


FCFS(queue, head)
print('')
print('Distance')
for i in range(len(queue) - 1):
    print('(', queue[i + 1], '-', queue[i], ')', '+', end=' ')
