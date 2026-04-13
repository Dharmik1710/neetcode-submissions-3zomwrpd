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
        
        value_list = self.key_val_map[key]
        l, r = 0, len(value_list) - 1
        prev = -1

        while l <= r:
            m = (l+r)//2

            if value_list[m][0] == timestamp:
                return value_list[m][1]
            elif value_list[m][0] > timestamp:
                r = m - 1
                prev = r
            else:
                l = m + 1
                prev = m
        return "" if prev==-1 else value_list[prev][1]