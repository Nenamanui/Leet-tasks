# Time:   O(log n)
# Space:  O(1)


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        early_version = 1
        last_version = n

        if isBadVersion(early_version) == True:
            return 1

        while early_version<last_version:
            central_version = early_version + (last_version - early_version)//2
            if isBadVersion(central_version):
                last_version = central_version
            else:
                early_version = central_version + 1

        return early_version