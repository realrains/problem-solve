class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = [0] * 1001

        for n in nums1:
            if counter[n] == 0:
                counter[n] += 1

        for n in nums2:
            if counter[n] == 1:
                counter[n] += 1

        return [x for x in range(1001) if counter[x] == 2]
        