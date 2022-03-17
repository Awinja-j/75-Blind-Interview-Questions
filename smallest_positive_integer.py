"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

def solution(A):
    # write your code in Python 3.6
    n = []
    A.sort()
    mn,mx = min(A), max(A)
    if mn < 1:
        return min(A)
    for x in range(mn, mx + 1):
        if x > 0 and x not in A:
            n.append(x)
        else:
            n.append(mx + 1)

    return n[0]


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))