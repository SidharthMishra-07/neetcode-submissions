class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while(l < r):
            # Skip non-alphanumeric characters
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            # Compare lowercase characters
            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1
        return True

# Rule of Thumb for Two-Pointer Problems
# Whenever you:
#     Modify pointers inside nested loops
#     Skip elements conditionally

# Always preserve the invariant:
# while left < right

# This is defensive pointer programming.
