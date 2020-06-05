class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)]
              for j in range(len(text1) + 1)]

        text1 = " " + text1
        text2 = " " + text2

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for i in range(len(text2) + 1)]
        
        text1 = " " + text1
        text2 = " " + text2
        
        for i in range(1, len(text1)):
            prev = 0
            for j in range(1, len(text2)):
                temp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = prev+1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
                print (text2[j], dp)
        return dp[-1]