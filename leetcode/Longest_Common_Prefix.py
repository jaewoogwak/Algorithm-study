class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs = sorted(strs, key=lambda s: len(s))

        result = strs[0]
        ans = []

        for i in range(1, len(strs)):

            ans = []
            for j in range(0, min(len(strs[i]), len(result))):

                if result[j] == strs[i][j]:
                    ans.append(result[j])

                else:

                    result = "".join(ans)
                    break

        return result


print(Solution.longestCommonPrefix(Solution, ["dog", "racecar", "car"]))
