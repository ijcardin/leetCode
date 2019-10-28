class Solution:
    def reverse(self, x: int) -> int:
        intAsString = str(x)
        reverseWord = ''

        if(intAsString[0] == '-'):
            reverseWord += '-'
            intAsString = intAsString[1:]

        for i in range(len(intAsString) - 1, -1, -1):
            reverseWord += intAsString[i]

        if int(reverseWord) > -2**31 and int(reverseWord) < 2**31 - 1:
            return int(reverseWord)
        return 0
        