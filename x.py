import sys
from typing import List
sys.setrecursionlimit(10 ** 6)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        dp = {}

        def fun(i, flag):
            if i >= len(stoneValue):
                return 0
            
            if (i, flag) in dp:
                return dp[(i, flag)]
            
            if flag:
                sm = 0
                c = 0
                j = i
                while j < len(stoneValue) and sm + stoneValue[j] > sm and c < 3:
                    sm += stoneValue[j]
                    c += 1
                    j += 1
                dp[(i, flag)] = sm + fun(j, False)
            else:
                sm = 0
                c = 0
                j = i
                while j < len(stoneValue) and sm + stoneValue[j] > sm and c < 3:
                    sm += stoneValue[j]
                    c += 1
                    j += 1
                dp[(i, flag)] = sm + fun(j, True)
            
            return dp[(i, flag)]
        fun(0, True)
        x = max(dp.values())
        print(dp)
        ans = None
        flag = False
        for i in dp:
            if flag:
                return 'Tie'
            if dp[i] == x:
                flag = True
                if i[1] == True:
                    ans = "Alice"
                else:
                    ans = "Bob"
        return ans

s = Solution()
print(s.stoneGameIII([1,2,3,7]))
