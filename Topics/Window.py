def minWindow(self, s: str, t: str) -> str:
    # edge case
    if len(t) > len(s):
        return ""
    
    # initialize counter
    _dict = {}
    temp = {char:0 for char in t}
    index = [0, 0]
    minL = float("infinity")
    target = len(t)
    cur = 0
    
    for char in t:
        _dict[char] = 1 + _dict.get(char, 0)
    
    l, r = 0, 0
    while r < len(s):
        if s[r] not in _dict:
            r += 1
            continue
        temp[s[r]] += 1
        if temp[s[r]] <= _dict[s[r]]:
            cur += 1
        while cur == target:
            if minL > r - l + 1:
                minL = r - l + 1
                index = [l, r]
            if s[l] in temp:
                temp[s[l]] -=1
                if temp[s[l]] < _dict[s[l]]:
                    cur -= 1
            l += 1
        r += 1
            
    if minL != float("infinity"):
        return s[index[0]:index[1]+1]
    else:
        return ""
            