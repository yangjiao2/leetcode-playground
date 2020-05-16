1. reversed array

```
nums[low] <= nums[mid] / nums[low] <= nums[mid]
high = mid - 1 / low = mid + 1
```

首尾 s 位和中间比较
二分法

避免 overflow:
mid = left + (right - left) / 2

faster:
mid = (low + high) >> 1
