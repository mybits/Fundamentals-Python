######################
# looping over indices


def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    '''

    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item

    



def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and adjacent
    character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i +1]:
            repeats = repeats + 1

    return repeats


#################
# parallel lists:

def sum_items(list1, list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sume of the item
    in corresponding position og list1 and list2.

    Precondition: len(list1) == len(list2)

    >>> sum_items([1,2,3], [2,4,2])
    [3,6,5]
    '''

    sum_list = []

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list

def count_matches(s1, s2):
    ''' (str, str) -> int

    Return the number of positions in s1 that contains the same character
    at the corresponding position of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    '''
    
    num_matches = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches

##############
# nested lists

def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float


    Return the average of the grades in asn_grades.

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''
    
    total = 0

    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)


##############
# nested loops

def averages(grades):
    ''' (list of list of number) -> list of float

    Return a new list in which each item is the average of the grades
    in the inner list at the corresponding position of grades.
    
    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []

    for grades_list in grades:

        # calculate the average of grade_list and append it to averages.

        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages




