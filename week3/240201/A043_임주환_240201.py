class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        full_flag = False

        min_len = 200

        for x in strs:
            length = len(x)
            if min_len > length:
                min_len = length

        for i in range(min_len):
            flag = True
            prefix += strs[0][i]
            for j in range(len(strs)):
                if prefix[-1] != strs[j][i]:
                    flag = False
                    break
            if flag == False:
                break
            if i == min_len - 1:
                full_flag = True
            
        if not full_flag and len(strs) != 1:
            prefix = prefix[:-1]
        return prefix