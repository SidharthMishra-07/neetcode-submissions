class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        currsum = 0
        total = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            currsum += gain
            if currsum < 0:
                currsum = 0
                start = i+1
            
        return start if total >= 0 else -1
