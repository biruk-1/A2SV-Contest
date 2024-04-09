class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        holder, seeker = 0, len(s) - 1

        while holder <= seeker:
            if s[holder] not in vowels:
                holder += 1
            elif s[seeker] not in vowels:
                seeker -= 1
            elif s[holder] in vowels and s[seeker] in vowels:
                s[holder], s[seeker] = s[seeker], s[holder]
                holder += 1
                seeker -= 1
        
        return ''.join(s)
