def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only DNA sequence contains no other characters
    then 'A' 'T' 'C' 'G'

    >>> is_valid_sequence('BBZZZ')
    False
    >>> is_valid_sequence('ATCGGC')
    True
    """
    
    for char in dna:
        if not (char in 'ATCG'):
            return False

    return True


def insert_sequence(dna1, dna2, i):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting dna2 into dna1 at the
    given index - (i)

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATCGGC', 'CC', -1)
    'ATCGGCCC'
    """

    dna3 = dna1[:i] + dna2 + dna1[i:]
    return dna3


def get_complement(n):
    """ (str) -> str

    Return complement nucleotide for given one (A is complement for T,
    and C is complement for G)

    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    
    """

    if n == 'A':
        return 'T'
    elif n == 'T':
        return 'A'
    elif n == 'C':
        return 'G'
    elif n == 'G':
        return 'C'
    else:
        return False
        
    
        

def get_complementary_sequence(dna):
    """ (str) -> str

    Return DNA sequence which is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('GC')
    'CG'
    
    """
    
    cn = ''
    for n in dna:
        
        cn = cn + get_complement(n)

    return cn
    

    
    
