def take_queue():
    input_queue = (input('Input queue : ')).strip(',')
    array = input_queue.split(',')
    length_of_queue = len(array)
    return length_of_queue, array


def take_head_start():
    head_start = int(input('Input Head Starts : '))
    return head_start


def main_function():
    length_of_queue, array = take_queue()
    head_start = take_head_start()
    result = 0
    path = str(head_start)
    two_array = []
    for i in range(0, len(array)):
        value_head_difference = [int(array[i]), head_start, 0]
        two_array.append(value_head_difference)
    for z in range(length_of_queue, 0, -1):
        value_head_difference = []
        finding_min = []
        for m in range(0, len(two_array)):
            two_array[m][2] = (abs(two_array[m][0] - two_array[m][1]))
            finding_min.append(two_array[m][2])
        print(two_array)
        minimum = min(finding_min)
        print(minimum)
        for j in range(0, len(two_array)):
            if two_array[j][2] == minimum:

                result = result + two_array[j][2]
                print(result)
                for k in range(0, len(two_array)):
                    two_array[k][1] = two_array[j][0]
                head_start = two_array[j][1]
                a = two_array[j]
        path = path + ' ' + str(a[1])
        two_array.remove(a)

        length_of_queue = int(len(two_array))
        print(len(two_array))
        print(two_array)
        print('T    otal distance : ' + str(sum))
        print('Path : ' + path)


main_function()
