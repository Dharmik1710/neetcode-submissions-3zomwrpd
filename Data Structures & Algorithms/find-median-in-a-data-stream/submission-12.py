class MedianFinder:

    def __init__(self):
        self.data = []
        self.medIdx = 0

    def addNum(self, num: int) -> None:
        
        l, r = 0, len(self.data) - 1
        while l <= r:
            mid = (l+r) >> 1
            if self.data[mid] > num:
                r = mid - 1
            else:
                l = mid + 1

        if len(self.data) % 2 != 0:
            self.medIdx += 1
        
        self.data.insert(l, num)
        print(self.data, self.medIdx, l)

    def findMedian(self) -> float:
        sum_ = self.data[self.medIdx]
        div = 1
        if len(self.data) and len(self.data) % 2 == 0:
            sum_ += self.data[self.medIdx - 1]
            div+=1
        return sum_ / div
        

'''
odd:[1,2,3]
if new number not added to left; current_med_idx+=1

even:[1,2,3,4]
if new num added to left or at cur med; current_med_idx -= 1
'''