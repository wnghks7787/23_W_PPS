class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome_str = ""
        palindrome = True
        for c in s:
            if c.isalnum():
                palindrome_str += c.lower()
        
        for i in range(int(len(palindrome_str) / 2)):
            if palindrome_str[i] != palindrome_str[len(palindrome_str) - i - 1]:
                palindrome = False
                break

        return palindrome