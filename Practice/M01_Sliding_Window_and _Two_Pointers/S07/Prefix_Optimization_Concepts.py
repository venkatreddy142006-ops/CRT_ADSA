# 1480. Running Sum of 1d Array
'''nums = [1,2,3,4,5]
res = [0] * (len(nums))
for i in range(len(nums)):
    curr_sum = 0
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)
'''

# 1732. Find the Highest Altitude
'''class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt,max_alt = 0,0
        for ele in gain:
            curr_alt += ele
            max_alt=max(curr_alt,max_alt)
        return max_alt'''