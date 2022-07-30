from collections import deque
from heapq import merge

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

def first_subarray_with_sum(nums, target):
  l = len(nums)

  window_sum, low, high = 0, 0, 0

  while low < l: # O(n)
    if window_sum < target:
        high += 1
        if high >= l:
            return []
        window_sum += nums[high]
    elif window_sum == target:
        return nums[low:high+1]
    else:
        low += 1
        window_sum -= nums[low]

  return []

def myAtoi(self, s: str) -> int:
    cleaned_s = s.strip()
    result = ""
    negative = False
    if not cleaned_s:
        return 0
    if cleaned_s[0] == "-":
        negative = True
        cleaned_s = cleaned_s[1:]
    elif cleaned_s[0] == "+":
        cleaned_s = cleaned_s[1:]
    for char in range(len(cleaned_s)):
        if not result and cleaned_s[char] == "0":
            continue
        if cleaned_s[char] == "-" or cleaned_s[char] == "+":
            break
        elif cleaned_s[char].isdigit():
            result += cleaned_s[char]
        else:
            break
    if not result:
        return 0
    if negative == True:
        result = int(result) * -1
    if int(result) > 2**31 - 1:
        return 2**31 - 1
    if int(result) < -2**31:
        return -2**31
    return int(result)

def reverseString(string):
    l, r = len(string) - 1, len(string) - 1
    result = ""
    while l >= 0:
        if string[l] == " ":
            result += string[l+1:r+1] + " "
            l, r = l-1, l-1
        else:
            l -= 1
    result += string[l+1:r+1]
    return result

def floodFill(image, r, c, color):
    #edge 
    if image[node[0]][node[1]] == color:
        return image

    q = collections.deque([r,c])
    visited = set()
    #bfs
    while q:
        node = q.popleft()
        if node not in visited and image[node[0]][node[1]] != color:
            for newX, newY in ((1,0), (0,1), (-1,0), (0,-1)):
                if is_valid(node, newX, newY, image, visited):
                    q.append([node[0]+newX], [node[1]+newY])
        image[node[0]][node[1]] = color
    return image

# def is_valid(node, newX, newY, image, visited):
#     # within range

#     # is not 0 or new color

def kSmallest(array, k):
    array.sort()
    return array[k-1]

def mergeIntervals(intervals):
    intervals.sort()

    if len(intervals) <= 1:
        return intervals
    result = [intervals[0]]
   
    for i in range(1, len(intervals)):
        if intervals[i][0] > result[-1][1]:
            result.append(intervals[i])
        else:
            result[-1][1] = max(result[-1][1], intervals[i][1])
    
    return result




def main():
    print(kSmallest([7, 10, 4, 3, 20, 15],3))
    print(mergeIntervals([[6,7], [2,4], [5,9]]))
    print(mergeIntervals([[1,4], [2,6], [3,5]]))
    print(mergeIntervals([[1,4]]))
    print(mergeIntervals([[6,7], [5,9],[2,4]]))
    print(mergeIntervals([[0,9], [2,4],[5,8]]))
    print(mergeIntervals([[1,4], [0,4]]))
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
    # q= Queue()
    # q.push(1)
    # q.push(2)
    # print(q.pop())
    # print(q.peak())
    # print(q.isEmpty())
#     tests = [
#     { 'input': { 'nums': [1,2,3], 'target': 3 }, 'output': [1,2] },
#     { 'input': { 'nums': [1,2,3], 'target': 5 }, 'output': [2,3] },
#     { 'input': { 'nums': [1], 'target': 1 }, 'output': [1] },
#     { 'input': { 'nums': [], 'target': 0 }, 'output': [] },
#     { 'input': { 'nums': [1,2,3], 'target': 7 }, 'output': [] },
#     { 'input': { 'nums': [2,6,0,9,7,3,1,4,1,10], 'target': 15 }, 'output': [6,0,9] },
#     { 'input': { 'nums': [0,5,7,1,4,7,6,1,4,1,10], 'target': 15 }, 'output': [4,1,10] },
#     { 'input': { 'nums': [0,5,7,1,4,7,6,1,4,1,10], 'target': 8 },  'output': [7,1] },
#   ]
  
#     for i in range(len(tests)):
#         print(f'Test {i+1}:', first_subarray_with_sum(tests[i]['input']['nums'], tests[i]['input']['target']) == tests[i]['output'])
    # string = "Today is Saturday!"
    # print(reverseString(string))
main()