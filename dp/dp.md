climbingStairs

- find ways: a, b = b, a + b
-

matrix 或者 lcm:

1. 边际： 长度 + 1
2. 记录 prev： prev = 修改前 memo[j], matrix[j]的上方 = prev & 左边 = memo[j-1s]
3. 比较： max(current, dependency) min(memo[j] , min(prev, memo[j-1])) + 1 或者 累积 prev + 1
4. 其他： 归零 或者延续 max(dp[j], dp[j-1])
