def solution(A, K):
    # write your code in Python 3.6
    if K > len(A) or len(A) ==0:
        return -1
    even = list()
    odd = list()

    A.sort(reverse = True)

    def is_even_odd(x):
        if  A[x] % 2 == 0:
            even.append(A[x])
        else:
            odd.append(A[x])

    for j in range(len(A)):
        is_even_odd(j)

    ei, oi = 0,0
    suma = 0

    while K > 0:
        if K % 2 == 1:
            if (len(even) > 0):
                suma += even[ei]
                ei += 1
                K -= 1
            else:
                return -1
        else:
            if ei < len(even) - 1 and oi < len(odd) - 1:
                suma += max(even[ei] + even[ei + 1], odd[oi] + odd[oi + 1])
                ei += 2
                oi += 2
            elif ei < len(even) - 1:
                suma += even[ei] + even[ei + 1]
                ei += 2
            elif oi < len(odd) - 1:
                suma += odd[oi] + odd[oi + 1]
                oi += 2

            K -= 2
    return suma

print(solution([4, 9, 8, 2, 6], 3))
print(solution([5, 6, 3, 4, 2], 5))
print(solution([7, 7, 7, 7, 7], 1))