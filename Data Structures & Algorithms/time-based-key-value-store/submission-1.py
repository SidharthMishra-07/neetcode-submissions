class TimeMap:

    def __init__(self):
        self.TimeMap = {}   #key :[[value, timestamp], ....]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.TimeMap.get(key, [])  # if key doesnt exist returns an empty array

        l, r = 0, len(values)-1
        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
