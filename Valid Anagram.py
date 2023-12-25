class Solution:
    def isAnagram(self,s,t):
        if sorted(s) == sorted(t):
            return True
        return False

def main():
    solution = Solution()
    print(solution.isAnagram(s = "rat", t = "car"))
main()
