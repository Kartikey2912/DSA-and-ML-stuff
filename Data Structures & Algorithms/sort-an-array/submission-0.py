class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums)-1)
        return nums
    def mergesort(self, arr, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.mergesort(arr, l, mid)
        self.mergesort(arr, mid+1, r)
        self.merge(arr, l, mid , r)

    def merge(self, arr, l, m, r):
        left = arr[l: m+1]
        right = arr[m+1: r+1]
        i,j,k = l, 0, 0
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        while j < len(left):
            arr[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1
        