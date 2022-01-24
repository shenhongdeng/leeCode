'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
'''

class Solution:
    '''暴力循环解法，用双指针'''
    def threeSum(self, nums: list):
        nums = sorted(nums)
        # numsDict = {value: index for index, value in enumerate(nums)}
        result = []
        if len(nums) < 3: # 长度小于三，直接返回
            return []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                k = 0 - (nums[i] + nums[j])
                if k in nums[j + 1:]:
                    tempList = [nums[i], nums[j], k]
                    if tempList not in result:
                        result.append(tempList)
        return result


    def threeSum2(self, nums: list):
        nums = sorted(nums)
        # numsDict = {value: index for index, value in enumerate(nums)}
        result = []
        if len(nums) < 3: # 长度小于三，直接返回
            return []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            print(i)
            while(j != k):
                print(j, k)
                if (nums[j] + nums[k]) == (0 - nums[i]):
                    tempList = [nums[i], nums[j], nums[k]]
                    if  tempList not in result:
                        result.append(tempList)
                    k -= 1 # 这两个里边执行一个就行了
                    # j += 1
                elif (nums[j] + nums[k]) > (0 - nums[i]):
                    k -= 1
                else:
                    j += 1
        return result



nums = [-1,0,1,2,-1,-4]
# print(sorted(nums, reverse=True))
# nums = [0, 0, 0, 0]
S = Solution()
print(S.threeSum2(nums))



