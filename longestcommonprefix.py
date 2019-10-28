class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        common = ""
        shortestWord = min(strs)
        index = 0
        
        
        while index < len(shortestWord):
            if all(word[index] == shortestWord[index] for word in strs):
                common += shortestWord[index]
                index += 1
            else:
                break
        
        return common
        