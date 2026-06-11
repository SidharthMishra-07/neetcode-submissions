class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize!=0:
            return False

        hand.sort()
        hm = Counter(hand)
        for x in hand:
            if hm[x]:
                for i in range(x, x + groupSize):
                    if not hm[i]:
                        return False
                    hm[i]-= 1
        return True

                