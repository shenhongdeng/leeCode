class Solution():
    def isMatch(self, s: str, p: str):
        while(s != ""):
            if p == "":
                return False
            if p[0] == s[0]:
                p = p[1:]
                s = s[1:]
            elif p[0] == '.':
                p = p[1:]
                s = s[1:]
            elif p[0] == '*':
                s = s[1:]
                if len(p[1:]) > 1 and p[1] == s[0]:
                    p = p[1:]
                else:
                    p = ""
            else:
                return False
        return True


def main():
    S = Solution()
    s = "aa"
    p = "a*"
    print(S.isMatch(s, p))

if __name__ == main():
    main()


