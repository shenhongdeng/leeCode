class Solution:
    def lengthOfLongestSubstring(self, s: str):
        # st存放的是每一子串的结束的位置，
        st = {}
        i, ans = 0, 0 # i记录的是子串开始的位置
        for j in range(len(s)):
            # 可以直接这么写，相当于dict.get()
            if s[j] in st:
                # 选取最大的开始
                i = max(st[s[j]], i) # 新的起始位置i=max(st[s[j]], i)，即重复字符的位置如果在原起始位置前面，则新起始位置不用动；如果在原起始位置的后面，则用重复字符的位置去更新起始位置
            #
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        print(ans)

def main():
    solution = Solution()
    solution.lengthOfLongestSubstring('pwwkew')

if __name__ == "__main__":
    main()
