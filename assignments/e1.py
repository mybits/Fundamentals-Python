def smaller_of_largest(L1, L2):
    '''(list of int, list of int) -> int

    Return the smaller of the largest value in L1 and the largest value in
    L2.

    Precondition: L1 and L2 are not empty.

    >>> smaller_of_largest([1, 4, 0], [3, 2])
    3
    >>> smaller_of_largest([4], [9, 6, 3])
    4
    '''

    return min(max(L1), max(L2))
               


def same_length(L1, L2):
    '''(list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    '''
    return len(L1) == len(L2)


def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n

    return result


def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for k in d:
        if k in L:
            result.append(k)

    return result



def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.

    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if d[k] in d:
            result = result + 1

    return result


def double_values(collection):
    for v in range(len(collection)):
        collection[v] = collection[v] * 2
        print(collection)




def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):
            if row == col:
                diagonal.append(L[row][col])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)



def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}

    for c in s:
        if not (c in d):
            d[c] = 1
        else:
            d[c] = d[c] + 1

    return d







