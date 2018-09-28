"""Generate valid parenthesis combinations of n braces """

def Generate(n):
    result = []
    _Generate([], n, result, 0, 0)
    return result

def _Generate(A,n, result, left, right):
    if len(A) == 2*n:
        result.append(''.join(A))
        return
    if left < n:
        A.append('(')
        _Generate(A, n, result, left+1, right)
        A.pop()
    if left > right:
        A.append(')')
        _Generate(A, n, result, left, right+1)
        A.pop()


        
