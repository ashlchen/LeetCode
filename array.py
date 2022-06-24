class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # understand
        # not sorted > dictionary to store count
        # a loop to store top k element
        
        # input: list of unsorted integers
        # output: a list of top k element
        # 1<=k<=unique elements
        # guarentee answer
        
        # fixed size res? 
        # max()?
        
        # plan
        # res
        res = []
        # hashmap
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        # loop through hashmap for k times
        for _ in range(k):
            key_list = list(hmap.keys())
            val_list = list(hmap.values())
            maxVal = max(val_list)
            position = val_list.index(maxVal)
            res.append(key_list[position])
            del hmap[key_list[position]]
        return res
    
    
        # ret = []
        # count = defaultdict(int)
        # for n in nums:
        #     count[n] += 1
        
        # heap = []
        # for n, c in count.items():
        #     heap.append((-c, n))
        # heapq.heapify(heap)
        # for _ in range(k):
        #     ret.append(heapq.heappop(heap)[1])
            
        # return ret
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: a list of integer
        # output: a list of integer (product)
        
        #min length is 2
        # might have 0 or negative numbers
        
        #match
        # n^2 solution
        # for loop * for loop
        
        # n solution -- caculate left and right portion separately
        n = len(nums)
        res = [None] * n
        left = 1
        for i in range(n):
            if i > 0:
                left = left * nums[i-1]
            res[i] = left
        right = 1
        for i in range(n-1, -1, -1):
            if i < (n-1):
                right = right * nums[i+1]
            res[i] *= right
        return res

    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: # if empty
        #     return 0
        # nums= list(set(nums)) # takes care duplicates
        # heapq.heapify(nums) # heapify the list
        # count = 1
        # temp = 1
        # first = heapq.heappop(nums) 
        # while nums:
        #     second = heapq.heappop(nums)
        #     if second - first == 1:
        #         temp +=1
        #     else:
        #         count = max(count, temp)
        #         temp = 1
        #     first = second
        # count = max(count,temp)
        # return count
            
        count = 1
        temp = 1
        if not nums:
            return 0
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                y = n+1
                while y in nums:
                    temp +=1
                    y += 1
                count = max(count, temp)
                temp = 1
        return count

    def threeSum(nums):
        # input: a list of number
        # output; a list of lists
        # there might be duplicates
        # if input length < 3 return empty res

        # match
        # sort and sliding window
        res = []
        if not nums or len(nums)<3:
            return res
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num > 0:
                return res
            l, r = i+1, len(nums)-1
            while l<r:
                temp = num + nums[l] + nums[r]
                if temp > 0:
                    r -=1
                elif temp == 0:
                    if [num,nums[l],nums[r]] not in res:
                        res.append([num,nums[l],nums[r]])
                else:
                    l += 1
        return res

        # edge
        # [0,0,0,0]

    def maxArea(height):
        # understand
        # area = width * height
        # height = min(height[i], height[j])
        # width = j - i
        # maximize both height and width

        # min of 2 elements in the list
        # height[i] can be 0

        # match
        # 2 pointers

        # plan
        res = 0 
        l, r = 0, len(height)-1
        while l < r:
            cur = (r-l) * min(height[r], height[l])
            res = max(cur, res)
            if height[l] <= height[r]:
                l +=1
            else:
                r -= 1
        return res
        