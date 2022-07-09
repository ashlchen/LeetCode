

from ctypes import sizeof


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
    cur = 0
    if not s:
        return -1
    while cur < len(s):
        if cur+1 < len(s):
            if s[cur] not in _lookup or s[cur+1] not in _lookup:
                return -1
            if _lookup[s[cur]] >= _lookup[s[cur+1]]:
                res += _lookup[s[cur]]
            else:
                res -= _lookup[s[cur]]
        else:
            res += _lookup[s[cur]]
        cur += 1
    return res


def postFix(data):
    post_fix_data = data.split(" ")
    stack = []
    
    if not post_fix_data:
        return None
    
    for i in post_fix_data:
        if i.isdigit():
            stack.append(i)
        else:
            first = stack.pop()
            second = stack.pop()
            stack.append(eval(str(second)+i+str(first)))

    return stack[0]
        
def sortStack(self, input):
    # 1. Create an additional temporary Stack.
    tempStack = []

    # 2. While input stack is NOT empty do:
    while len(input) != 0:
        # 3. Pop an element from input stack called temp.
        temp = input.pop()

        # 4. While temporary stack is NOT empty and top of temporary stack is greater than temp:
        while len(tempStack) != 0 and tempStack[len(tempStack)-1] > temp:
            # 5. Pop from temporary stack and push it to the input stack.
            input.append(tempStack[len(tempStack)-1])
            tempStack.pop()

        # 6. Push temp in temporary stack.
        tempStack.append(temp)

    # 7. In the end, the sorted numbers are in the temporary Stack.
    return tempStack       

class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.append(x)

    def pop(self):
        temp = self.queue[0]
        self.queue = self.queue[1:]
        return temp

    def peak(self):
        return self.queue[0]

    def isEmpty(self): #True/False
        return self.queue == 0


class MovingAverage:
    def __init__(self, window_size):
        self.queue = []
        self.sum = 0
        self.size = window_size
     
        

    def next(self, val):
        self.queue.append(val)
        self.sum += val

        return self.sum / len(self.queue)



def main():
    # print(isIsomorphic("abb","cdd"))
    # print(isIsomorphic("",""))
    # print(isIsomorphic("","a"))
    # print(majority([3,2,3]))
    # print(majority([2,2,1,1,1,2,2]))
    # print(majority([1]))
    # print(RomanToInteger("MCMXCIV")) #1994
    # print(RomanToInteger("III"))
    # print(RomanToInteger("LVIII"))
    # print(RomanToInteger("AIII"))
    # print(RomanToInteger(""))
    # print(RomanToInteger("IA"))
    # print(RomanToInteger("MCMLXXXIV"))
    # print(postFix("5 1 + 4 * 3 -"))
    # test = MovingAverage(2)
    # print(test.next(2))
    q= Queue()
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.peak())
    print(q.isEmpty())
main()