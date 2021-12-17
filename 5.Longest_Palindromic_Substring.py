from itertools import combinations

def powerset(string):
    map = []
    n = len(string)
    for i in range(0,n+1):
        for element in combinations(string,i):
            map.append(''.join(element))
    return map
    
def isPalindrome(n):
        if str(n) == str(n)[::-1]:
            return n
        return False
    
def longestPalindrome(s: str) -> str:
    if not s:
        return s
    
    
    for i in range(len(s), 0, -1):
        for j in range(0, len(s)-i+1): 
            candidate = s[j:j+i]
            if isPalindrome(candidate):
                return candidate
            
    # b = [k for k in j if self.check_palindrome(k) is True and  k in s]
    # c = max(b, key=len)
    # return c
                
