class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to have time log n
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <=nums[r]:
                    l = mid
                else:
                    r = mid - 1
        
        return -1

    def findMin(self, nums: List[int]) -> int:

    # two pointer
    l, r = 0, len(nums) - 1
    if len(nums)==1:
        return nums[0]
    if nums[0] < nums[r]:
        return nums[0]
    # mid
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[l] <= nums[mid]:
            l = mid
        else:
            r = mid - 1
    # smaller should be right after the peak
    
    #edge
    #[0]
    #[2,1]

    def woodCut(self, L):
        l, r = 1, max(L)
        while l + 1 < r:
            mid = l + r // 2
            if self.get_pieces(L, mid) >= k:
                l = mid
            else:
                r = mid
        if self.get_pieces(L, r) >= k:
            return r
        if self.get_pieces(L, l) >= k:
            return l

    def get_pieces(self, L, length): # 確認output篇大還偏小
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces

    #find k closest element
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        right = self.findElement(arr, k, x)
        left = right - 1
        result = []
        # expand from left and right
        for _ in range(k):
            if self.is_left(arr, x, left, right):
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        return sorted(result)
    
    def findElement(self, arr, k, x): # find right starting point
        # find the element >= x
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if x >= arr[mid]:
                start = mid
            else:
                end = mid
        if arr[start] >= x :
            return start
        if arr[end] >= x:
            return end
        return end + 1
        # from that element, expand both left and right until result array size == k
        
    def is_left(self, arr, x, l, r): # determine if left element is closer to x
        if l < 0:
            return False
        if r >= len(arr):
            return True
        return abs(arr[l] - x) <= abs(arr[r] - x)
                             
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l + 1 < r:
            mid = (l+r) // 2
            if self.finish_hour(piles, mid) > h:
                l = mid
            else:
                r = mid
        if self.finish_hour(piles, l) <= h:
            return l
        return r

        
        
    def finish_hour(self, piles, banana_per_hour):
        result = 0
        for pile in piles:
            if pile > banana_per_hour and pile % banana_per_hour != 0:
                result += pile // banana_per_hour
                result += 1
            elif pile >= banana_per_hour:
                result += pile // banana_per_hour
            else:
                result += 1
        return result


class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        arr = self.map[key]
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start+end) // 2
            if timestamp >= arr[mid][0]:
                start = mid
            else:
                end = mid
        if arr[end][0] <= timestamp:
            return arr[end][1]
        if arr[start][0] <= timestamp:
            return arr[start][1]
        return ""