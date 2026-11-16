class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low<=high:
            mid = (low+high)//2
            target = mid * mid
            if target == x:
                return mid
            elif target < x:
                low = mid+1
            elif target > x:
                high = mid-1
        return low-1