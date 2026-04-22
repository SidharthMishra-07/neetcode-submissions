class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since the array is sorted i will use the 2-pointer approach
        n = len(numbers)
        low = 0
        high = n-1

        while(low < high):
            if(numbers[low] + numbers[high] == target):
                return list((low+1, high+1))
            elif (numbers[low] + numbers[high] < target):
                low+=1
            else:
                high-=1
        return -1
