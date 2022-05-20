from functools import lru_cache

with_small_cache = lru_cache(maxsize=5)


@with_small_cache
def climbStairs(n: int) -> int:
            
    if n < 3:
        return n
    
    elif n == 1 or n == 2:
        return 1
    else:
        return climbStairs(n-1) + climbStairs(n-2)

# print(climbStairs(3))
print(climbStairs(4))
    
        