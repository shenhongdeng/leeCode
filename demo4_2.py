'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        index1 = 0
        index2 = 0
        tempList = []
        total = (len(nums1) + len(nums2))
        print
        for i in range(total):
            if index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] <= nums2[index2]:
                    tempList.append(nums1[index1])
                    index1 += 1
                else:
                    tempList.append(nums2[index2])
                    index2 += 1
            elif index1 == len(nums1):
                tempList.append(nums2[index2])
                index2 += 1
            else:
                tempList.append(nums1[index1])
                index1 += 1

            if len(tempList) > total / 2:
                if total / 2  == int(total / 2):
                    return (tempList[-1] + tempList[-2]) / 2
                else:
                    return tempList[-1]


def main():
    solution = Solution()
    print(solution.findMedianSortedArrays([1,2], [3,4, 5]))

if __name__ == "__main__":
    main()




