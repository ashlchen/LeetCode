from cgitb import reset
from re import X


def isIsomorphic(s,t):
    _dict= {}
    if len(s) != len(t):
        return False
    if not s or not t:
        return False
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        if c1 in _dict:
            if _dict[c1] != c2:
                return False
        else:
            _dict[c1] = c2
    return True


def majority(nums):
# linear 
    _dict = {}
    if not nums:
        return -1
    for char in nums:
        if char in _dict:
            _dict[char] += 1
        else:
            _dict[char] = 1
    for key, value in _dict.items():
        if value > len(nums)//2:
            return key

# nLogn
    nums.sort()
    i = len(nums)//2
    return nums[i]


def RomanToInteger(s):
    # linear time
    # constant space
    _lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    p = 0
    if not s:
        return -1
    while p < len(s):
        if p+1 < len(s):
            if s[p] not in _lookup or s[p+1] not in _lookup:
                return -1
            if _lookup[s[p]] >= _lookup[s[p+1]]:
                res += _lookup[s[p]]
            else:
                res -= _lookup[s[p]]
        else:
            res += _lookup[s[p]]
        p += 1
    return res

        

def main():
    # print(isIsomorphic("abb","cdd"))
    # print(isIsomorphic("",""))
    # print(isIsomorphic("","a"))
    # print(majority([3,2,3]))
    # print(majority([2,2,1,1,1,2,2]))
    # print(majority([1]))
    print(RomanToInteger("MCMXCIV")) #1994
    print(RomanToInteger("III"))
    print(RomanToInteger("LVIII"))
    print(RomanToInteger("AIII"))
    print(RomanToInteger(""))
    print(RomanToInteger("IA"))
    # print(RomanToInteger("MCMLXXXIV"))
main()