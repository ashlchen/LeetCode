class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller, -1* num)
        
        if self.smaller and self.larger and -1 * self.smaller[0] > self.larger[0]:
            val = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, val)
        
        if len(self.smaller) > len(self.larger) + 1:
            val = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, val)
        
        if len(self.larger) > len(self.smaller) + 1:
            val = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -1*val)

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -1*self.smaller[0]
        elif len(self.larger) > len(self.smaller):
            return self.larger[0]
        else:
            return (-1*self.smaller[0] + self.larger[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()