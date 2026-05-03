class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        matching = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in '([{':
                st.append(ch)
            elif ch in ')}]':
                if not st or st[-1] != matching[ch]:
                    return False
                else:
                    st.pop()
        return len(st) == 0