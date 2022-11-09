"""Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))."""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def merge(list1, list2):
            i, j = 0, 0
            merge_list = []
            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    merge_list.append(list1[i])
                    i += 1
                else:
                    merge_list.append(list2[j])
                    j += 1

            # остатки докидываем
            while i < len(list1):
                merge_list.append(list1[i])
                i += 1
            while j < len(list2):
                merge_list.append(list2[j])
                j += 1

            return merge_list

        l1 = merge(nums1, nums2)
        median = l1[len(l1) // 2] if len(l1) % 2 != 0 else l1[len(l1) // 2] + l1[len(l1) // 2 - 1]
        return median
