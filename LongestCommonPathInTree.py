

def length(curr, A, ref, maxLen, visited):
    common = 0
    max1, max2 = 0, 0
    if curr not in ref:
        return 0
    for neighbor in ref[curr]:
        if neighbor not in visited:
            visited.add(neighbor)
            currLen = length(neighbor, A, ref, maxLen, visited)
            if A[neighbor-1] == A[curr-1]:
                common += 1
                if currLen > max1:
                    max2, max1 = max1, currLen
                elif currLen > max2:
                    max2 = currLen
    if not common:
        return 0
    if common>=2:
        maxLen[0] = max(maxLen[0],max1+max2+2)
    elif common == 1:
        maxLen[0] = max(maxLen[0], max1+1)
    return max1+1

def longestCommonPath(A, E):
    ref = {}
    for i in range(0, len(E), 2):
        if E[i] not in ref:
            ref[E[i]] = [E[i+1]]
        else:
            ref[E[i]].append(E[i+1])
        if E[i+1] not in ref:
            ref[E[i+1]] = [E[i]]
        else:
            ref[E[i+1]].append(E[i])
    maxLen = [0]
    visited = set()
    for i in range(1, len(A)+1):
        if i not in visited:
            visited.add(i)
            length(i, A, ref, maxLen, visited)
    return maxLen[0]
