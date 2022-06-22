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