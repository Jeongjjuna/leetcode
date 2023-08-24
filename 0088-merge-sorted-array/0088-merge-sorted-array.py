class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # 병합정렬 -> nums1에 넣어주기
        # [1, 2, 3, 0, 0, 0] [2, 5, 6]

        p1, p2, idx = m - 1, n - 1, m + n - 1
        
        while p1 >= 0  and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[idx] = nums1[p1]
                idx -= 1
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[idx] = nums2[p2]
                idx -= 1
                p2 -= 1
        
        # 왼쪽이 남는경우
        if p2 < 0:
            while p1 >= 0:
                nums1[idx] = nums1[p1]
                idx -= 1
                p1 -= 1
        # 오른쪽이 남는경우
        elif p1 < 0:
            while p2 >= 0:
                nums1[idx] = nums2[p2]
                idx -= 1
                p2 -= 1