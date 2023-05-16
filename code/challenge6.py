import re
from collections import Counter
import sys

memo = {}

def make_vocab(str0):
    '''
    Returns a set of the unique chars in str0
    '''
    return set(str0)

def initial_reduce(str0, vocab):
    '''
    Reduces the serial substrings of str0 to a single character
    '''
    t=str0[:]
    # create the serial pattern for each char in the vocabulary of str0
    patterns = [ str(ch)+"{2,}" for ch in vocab ]

    for i, ch in enumerate(vocab):
        t = re.sub( patterns[i], ch, t)
        #print("Replace", ch)
        #print("Result string:")
        #print(t)
        #print()

    #print()
    return t


def unique_chars(s):
    '''
    Returns True if every character in string s appears once or none
    '''
    count=list(Counter(s).values())
    return all( [i<2 for i in count] ) 


# we know s0 has at least 1 pair of same character , but never adjacent
def find_middle(s0):
    s0_len=len(s0)
    mid = s0_len//2
    mid_left = mid
    found = False
    while not found:
        mid_char = s0[mid_left]
        for i in range(mid_left+2, s0_len):
            if s0[i]==mid_char:
                mid_right = i
                found=True
                break
        if not found:
            mid_left-=1
    return mid_left, mid_right


# recursive function
def step_delete(s0):

    if s0 in memo:
        print("Retrieved from memo", s0, "steps:", memo[s0])
        return memo[s0]

    s0_len = len(s0)
    # base case: no serial substrings possible
    if unique_chars(s0):
        print("["+s0+"]", "steps:", s0_len)
        return s0_len
    else:   # recurse 
        mid_left, mid_right = find_middle(s0) 
        inner_str = s0[mid_left+1 : mid_right]
        outer_str = s0[:mid_left+1]+s0[mid_right+1:]
        print("inner_str:", inner_str)
        print("outer_str", outer_str)
        steps = step_delete(outer_str) + step_delete(inner_str)
        if s0 not in memo:
           memo[s0]=steps
        return steps   
    



if __name__ == '__main__':

    s0 = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"

    #s0="aabba"
    #s0="aabbbccccccaa"
    #s0="aabbbcccaacccaa"
    #s0= "aabcdea"
    print("String length:", len(s0))

    # make a vocabulary of the characters in the string
    vocabulary = list( make_vocab(s0) )
    print("Vocabulary:")
    print(vocabulary)
    print()

    # initial string reduce
    s1 = initial_reduce(s0, vocabulary)
    print("Initial Reduced string after shrinking serials:")
    print(s1)
    print("Length of initial reduced string:", len(s1))
    print()

    # start the recursive reduce
    min_steps = step_delete(s1)
    print("Min steps:", min_steps)

