class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        low = 1
        high = n-2
        peak = 0
        while low<=high:
            mid = (low+high) // 2
            l, m, r = mountainArr.get(mid-1), mountainArr.get(mid), mountainArr.get(mid+1)
            if l<m and m>r:
                break
            elif l>m>r:
                high = mid - 1
            elif l<m<r:
                low = mid + 1

        peak = mid

        #search the left half first
        low, high = 0, peak-1
        while low<=high:
            mid = (low+high)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid+1
            else:
                high = mid-1
        
        #search the right half next
        low, high = peak, n-1
        while low<=high:
            mid = (low+high)//2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            if val < target:
                high = mid - 1
            else:
                low = mid + 1

        return -1