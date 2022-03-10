# C-LOOK Disk Scheduling
disk_size = 200
queue = [53, 98, 183, 37, 122, 14, 124, 65, 67]
head = 53


def c_look(arr, head):
    seek_count = 0
    distance = 0
    cur_track = 0

    left = []
    right = []

    path = []

    for i in range(len(arr)):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    left.sort()
    right.sort()

    for i in range(len(right)):
        cur_track = right[i]

        path.append(cur_track)

        distance = abs(cur_track - head)

        seek_count += distance

        head = cur_track

    seek_count += abs(head - left[0])
    head = left[0]

    for i in range(len(left)):
        cur_track = left[i]

        path.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    print("Total number of head movement =", seek_count)
    print("Path")

    for i in range(len(path)):
        print(path[i], end=' ')
    print(' ')
    print('Distance')
    for i in range(len(path) - 1):
        print('(', path[i + 1], '-', path[i], ')', '+', end=' ')


c_look(queue, head)
