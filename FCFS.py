def take_queue():
    input_queue = input('Input queue : ')
    array = input_queue.split(',')
    length_of_queue = len(array)
    return length_of_queue, array


def take_head_start():
    head_start = int(input('Input Head Starts : '))
    return head_start


def main_process(length_of_queue, head_start, array):
    second_value = head_start
    total_distance = 0
    path = str(head_start)

    for x in range(0, length_of_queue):
        if int(array[x]) > second_value:
            path = path+' ' + array[x]
            total_distance = total_distance+(int(array[x])-second_value)
            second_value = int(array[x])
        else:
            path = path + ' ' + array[x]
            total_distance = total_distance+(second_value-int(array[x]))
            second_value = int(array[x])

    print('Total Distance : ' + str(total_distance))
    print('Path : '+path)


a, b = take_queue()
c = take_head_start()
main_process(a, c, b)
