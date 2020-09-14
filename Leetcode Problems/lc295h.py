import heapq


class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        s, l = self.heaps
        heapq.heappush(s, -heapq.heappushpop(l, num))
        if len(l) < len(s):
            heapq.heappush(l, -heapq.heappop(s))

    def findMedian(self):
        s, l = self.heaps
        if len(l) > len(s):
            return float(l[0])
        return (l[0] - s[0]) / 2
