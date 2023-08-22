class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 병합정렬 -> nums1에 넣어주기
        # [1, 2, 3, 0, 0, 0] [2, 5, 6]

        p1, p2 = 0, 0
        result = []
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                result.append(nums2[p2])
                p2 += 1
        
        # 왼쪽이 남는경우
        if p2 == n:
            while p1 < m:
                result.append(nums1[p1])
                p1 += 1
        # 오른쪽이 남는경우
        elif p1 == m:
            while p2 < n:
                result.append(nums2[p2])
                p2 += 1

        
        # 정렬된 결과를 nums1에 넣기
        for i in range(len(nums1)):
            nums1[i] = result[i]