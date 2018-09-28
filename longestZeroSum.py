'''Find the largest subarray with 0 sum '''

'''Brute Force algorithm: O(n^2)'''

def findLongestZeroSum(A):
    if A == []:
        return 0
    result = 0
    for i in range(len(A)):
        Sum = 0
        for j in range(i, len(A)):
            Sum += A[j]
            if Sum == 0 and result < j-i+1:
                result = j-i+1
    return result

'''In one iteration: O(n^2) '''
def findLongestZeroSum2(A):
    if A == []:
        return 0
    result = 0
    reference = {}
    # this loop iterates n times
    for i in range(len(A)):
        reference[i] = 0
        # this loop itereates len(reference) times which is i, so i times
        for j in range(len(reference)):
            reference[j] += A[i]
            if reference[j] == 0 and i-j+1 > result:
                result = i-j+1
    return result

'''O(n) solution:- Idea: if the sum has been seen before there is a zero sum array '''

def findLongestZeroSum3(A):
    if A == []:
        return 0
    result = 0
    Sum = 0
    reference = {0:-1}
    for i in range(len(A)):
        Sum += A[i]
        if Sum in reference:
            result = max(result, i-reference[Sum])
        else:
            reference[Sum] = i
    return result

        
