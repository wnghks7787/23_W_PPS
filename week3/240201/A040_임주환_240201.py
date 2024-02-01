class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = int(len(s)/2)
        a_count = 0
        b_count = 0

        a = s[:length].lower()
        b = s[length:].lower()

        vowels = ['a', 'e', 'i', 'o', 'u']

        for vowel in vowels :
            a_count += a.count(vowel)
            b_count += b.count(vowel)

        if a_count == b_count:
            return True
        else:
            return False