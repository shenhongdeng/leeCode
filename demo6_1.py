'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
'''

'''
直接暴力的斜解超出二楼时间的限制
后边是抄的答案
'''

class Solution:
    def maxArea(self, height: list):
        maxArea = 0
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                low = self.findLow(height[i], height[j])
                tempArea =  (j - i) * low
                if tempArea > maxArea:
                    maxArea = tempArea
        return maxArea

class Solution:
    def maxArea(self, height: list)
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:  # 移动较小的那一端
                l += 1
            else:
                r -= 1
        return ans



    def findLow(self, no1, no2):
        if no1 > no2:
            return no2
        else:
            return no1

def main():
    S = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(S.maxArea(height))

if __name__ == "__main__":
    main()