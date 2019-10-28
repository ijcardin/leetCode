class Solution:
    def romanToInt(self, s: str) -> int:
        romanVal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M': 1000}
        sum = 0
            
        while len(s) > 1:
            if (s[0] == 'I' and s[1] == 'V') or (s[0] == 'I' and s[1] == 'X'):
                sum += romanVal[s[1]] - romanVal[s[0]]
                s = s[2:]
            elif (s[0] == 'X'and s[1] == 'L') or (s[0] == 'X' and s[1] == 'C'):
                sum += romanVal[s[1]] - romanVal[s[0]]
                s = s[2:]
            elif (s[0] == 'C'and s[1] == 'D') or (s[0] == 'C' and s[1] == 'M'):
                sum += romanVal[s[1]] - romanVal[s[0]]
                s = s[2:]
            else:
                sum += romanVal[s[0]]
                s = s[1:]
            
            
        if len(s) == 1:
            sum += romanVal[s[-1]]
            return sum
        return sum
                