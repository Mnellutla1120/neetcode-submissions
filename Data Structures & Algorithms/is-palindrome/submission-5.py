class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter and lowercase everything in one line
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        
        # Check against its reverse
        return cleaned == cleaned[::-1]