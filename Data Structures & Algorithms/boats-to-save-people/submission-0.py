class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        low = 0
        high = n-1
        count = 0
        while low <= high:
            remain = limit - people[high]
            high -=1
            count+=1
            if low <= high and remain >= people[low]:
                low+=1
        return count