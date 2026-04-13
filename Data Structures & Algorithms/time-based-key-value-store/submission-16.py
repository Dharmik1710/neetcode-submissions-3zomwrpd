from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        value_list = self.map[key]
        l, r = 0, len(value_list) - 1

        while l <= r:
            m = (l+r)//2
            
            if value_list[m][0] > timestamp:
                r = m - 1
            elif value_list[m][0] < timestamp:
                l = m + 1
            else:
                return value_list[m][1]
        return value_list[r][1] if r >= 0 else ""