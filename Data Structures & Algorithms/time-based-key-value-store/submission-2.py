class TimeMap:

    def __init__(self):
        self.key_val_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_val_map:
            self.key_val_map[key].append((timestamp, value))
        else:
            self.key_val_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_val_map:
            return ""
        
        l, r = 0, len(self.key_val_map[key]) - 1
        prev = -1

        while l <= r:
            m = (l+r)//2

            if self.key_val_map[key][m][0] == timestamp:
                return self.key_val_map[key][m][1]
            elif self.key_val_map[key][m][0] > timestamp:
                r = m - 1
                prev = r
            else:
                l = m + 1
                prev = m
        return "" if prev==-1 else self.key_val_map[key][prev][1]