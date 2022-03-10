# C-SCAN Disk Scheduling algorithm

queue = [53, 98, 183, 37, 122, 14, 124, 65, 67]
head = 53
disk_size = 200


def CSCAN(arr, head):
    count = 0
    distance = 0
    cur_track = 0
    left = []
    right = []
    path = []

    left.append(0)
    right.append(disk_size - 1)

    for i in range(len(arr)):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] >= head):
            right.append(arr[i])

    left.sort()
    right.sort()

    for i in range(len(right)):
        cur_track = right[i]

        path.append(cur_track)

        distance = abs(cur_track - head)

        count += distance

        head = cur_track

    head = 0
    count += (disk_size - 1)

    for i in range(len(left)):
        cur_track = left[i]
        path.append(cur_track)
        distance = abs(cur_track - head)
        count += distance
        head = cur_track

    print("Total number of head movements =", count)
    print("Path")
    print(*path, sep=" ")

    print('Distance')
    for i in range(len(path) - 1):
        print('(', path[i + 1], '-', path[i], ')', '+', end=' ')


CSCAN(queue, head)