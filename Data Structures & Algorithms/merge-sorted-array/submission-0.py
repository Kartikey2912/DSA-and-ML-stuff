class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        i,j = 0, 0
        n,m = len(nums1), len(nums2)
        n -= m
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        while i < n:
            ans.append(nums1[i])
            i += 1
        while j < m:
            ans.append(nums2[j])
            j += 1
        for i in range(n + m):
            nums1[i] = ans[i]
        