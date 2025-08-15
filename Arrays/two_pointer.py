# Reverse words in a string

# Since Strings in python aren't mutable, we can't just reverse the string like in some other languages
class Solution: 
    def reverseWords_manual(s): # both are O(n)
        res = ''
        l, r = 0, 0 

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else: 
                res += s[l:r+1][::-1]
                r += 1
                l = r

        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]
    
    print(reverseWords_manual("Testando Solucao"))


