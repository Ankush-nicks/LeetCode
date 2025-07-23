class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        # print(len(nums1))
        mid = len(nums1)/2
        # print(mid)
        if len(nums1) % 2 ==0:
            return float(nums1[mid]+nums1[mid-1])/2
        else:
            return nums1[mid]
        