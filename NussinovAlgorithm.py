from queue import LifoQueue
# GGCAGUACCAAGUCGCGAAAGCGAUGGCCUUGCAAAGGGUAUGGUAAUAAGCUGCC


def compute_matrix(arr, my_seq):
    length = len(my_seq)
    count = length-1  # the amount of diagonals
    while count != 0:  # running on length-1 diagonals
        distance = length - count  # num of cells in the diagonal
        for i in range(length-distance):
            j = i+distance
            val = is_base_pair(my_seq[i], my_seq[j], i, j)  # check if it is a base pair
            val1 = 0
            val2 = 0
            val3 = 0
            if val == 2:  # if Watson-Crick base pair
                val1 = 2 + arr[i+1][j-1]
            elif val == 1:  # if wobble base pair
                val2 = 1 + arr[i+1][j-1]
            val3 = get_maximal_val(arr, i, j)
            arr[i][j] = max(val1, val2, val3)
        count -= 1
    for i in range(length):
        print(arr[i])
    reconstruct(arr, my_seq)


def reconstruct(arr, my_seq):
    count = 0
    length = len(my_seq)
    stack = LifoQueue(length)
    stack.put([0, length-1])
    while not stack.empty():
        curr_cell = stack.get()
        i = curr_cell[0]
        j = curr_cell[1]
        if i < j:
            if arr[i][j] == arr[i+1][j-1] + 2 and is_base_pair(my_seq[i], my_seq[j], i, j) == 2:
                print(my_seq[i] + ' , ' + my_seq[j], i, j)
                count += 2
                stack.put([i + 1, j - 1])
            elif arr[i][j] == arr[i+1][j-1] + 1 and is_base_pair(my_seq[i], my_seq[j], i, j) == 1:
                print(my_seq[i] + ' , ' + my_seq[j], i, j)
                count += 2
                stack.put([i + 1, j - 1])
            else:
                k = i
                while k < j:
                    if arr[i][j] == arr[i][k] + arr[k + 1][j]:
                        stack.put([k + 1, j])
                        stack.put([i, k])
                        break
                    k += 1
        elif(i == j):
            print(my_seq[i], i)
            count += 1


def get_maximal_val(arr, i, j):
    maximum = 0
    for k in range(i, j):
        val = arr[i][k] + arr[k+1][j]
        if val > maximum:
            maximum = val
    return maximum


def is_base_pair(x, y, i, j):
    if i == j-1:
        return 0
    elif x == 'C' and y == 'G':
        return 2
    elif x == 'G' and y == 'C':
        return 2
    elif x == 'A' and y == 'U':
        return 2
    elif x == 'U' and y == 'A':
        return 2
    elif x == 'U' and y == 'G':
        return 1
    elif x == 'G' and y == 'U':
        return 1
    else:
        return 0


# initialize the matrix with zeros
def get_matrix(my_length):
    arr = [[0 for i in range(my_length)] for j in range(my_length)]
    return arr


seq = input("Enter the RNA sequence : ")
initialized_matrix = get_matrix(len(seq))
compute_matrix(initialized_matrix, seq)



