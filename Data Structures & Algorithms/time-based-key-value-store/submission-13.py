from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        l, r = 0, len(self.map[key]) - 1

        while l <= r:
            m = (l+r)//2
            
            if self.map[key][m][0] > timestamp:
                r = m - 1
            elif self.map[key][m][0] < timestamp:
                l = m + 1
            else:
                return self.map[key][m][1]
        return self.map[key][r][1] if r >= 0 else ""