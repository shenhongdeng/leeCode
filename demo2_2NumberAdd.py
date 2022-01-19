'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
'''
class Solution:
    def twoSum(self, nums:list, target:int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return None

    def twoSum2(self, nums:list, target:int):
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[value] = index

        for i in range(len(nums)):
            if hashmap.get(target - nums[i]) and hashmap[target - nums[i]] != i:
                return [i, hashmap[target - nums[i]]]



def main():
    solution = Solution()
    nums = [1, 3, 3]
    target = 6
    print(solution.twoSum2(nums, target))


if __name__ == "__main__":
    main()
