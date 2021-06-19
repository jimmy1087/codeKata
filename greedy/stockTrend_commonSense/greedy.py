# Find three values in an upward trend. They might not be sequential numbers.
def upwardTrendExists(array):

    lowest = array[0]     # Greedily set the first item to be the lowest. Always update the lowest
    middle = float('inf') # set the middle to infinity to stablish a boundary. Always update the middle
    biggest = None        # The goal is to find one item greater than the middle one

    found = False

    for i in range(1, len(array)):

        # Identify and update the lowest value in the array
        if array[i] < lowest:
            lowest = array[i]
        # Identify a middle value, which at the beggining should > lowest < infinity
        # later on update any middle value
        if array[i] > lowest and array[i] < middle:
            middle = array[i]
        # the objective is to find the biggest value, which is > middle.
        if array[i] > middle:
            biggest = array[i]
            found = True

    print('Lowest', lowest, 'Middle', middle, 'Biggest', biggest)
    
    if found:
        return True
    else:
        return False

a = [8, 9, 7, 10]  # 8, 9, 10 is a valid trend, eventhough the algorithm will greedily print 7, 9, 10

if upwardTrendExists(a):
    print('Exists')
else:
    print('Does not exists')


a = [7, 6, 8, 4, 1, 5]  # Does not exists, lowest(1), middle(5) but no Biggest found.

if upwardTrendExists(a):
    print('Exists')
else:
    print('Does not exists')
