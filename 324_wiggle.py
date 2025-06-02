import random

class Solution(object):
    def wiggleSort(self, nums):
        def nth_element(arr_copy, n):
            def select(left, right, n_smallest):
                if left == right:
                    return arr_copy[left]
                
                pivot_idx = random.randint(left, right)
                pivot_idx = partition(left, right, pivot_idx)

                if n_smallest == pivot_idx:
                    return arr_copy[n_smallest]
                elif n_smallest < pivot_idx:
                    return select(left, pivot_idx - 1, n_smallest)
                else:
                    return select(pivot_idx + 1, right, n_smallest)

            def partition(left, right, pivot_idx):
                pivot = arr_copy[pivot_idx]
                arr_copy[pivot_idx], arr_copy[right] = arr_copy[right], arr_copy[pivot_idx]
                store_idx = left
                for i in range(left, right):
                    if arr_copy[i] < pivot:
                        arr_copy[store_idx], arr_copy[i] = arr_copy[i], arr_copy[store_idx]
                        store_idx += 1
                arr_copy[right], arr_copy[store_idx] = arr_copy[store_idx], arr_copy[right]
                return store_idx

            return select(0, len(arr_copy) - 1, n)

        n = len(nums)
        if n <= 1:
            return
            
        median = nth_element(nums[:], (n - 1) // 2)

        def idx_map(i):
            return (1 + 2 * i) % (n | 1)

        left, i, right = 0, 0, n - 1

        while i <= right:
            if nums[idx_map(i)] > median:
                nums[idx_map(left)], nums[idx_map(i)] = nums[idx_map(i)], nums[idx_map(left)]
                left += 1
                i += 1
            elif nums[idx_map(i)] < median:
                nums[idx_map(right)], nums[idx_map(i)] = nums[idx_map(i)], nums[idx_map(right)]
                right -= 1
            else:
                i += 1

if __name__ == "__main__":
    solver = Solution()

    print("Exemplo 1:")
    nums1 = [1, 5, 1, 1, 6, 4]
    print(f"Original: {nums1}")
    solver.wiggleSort(nums1)
    print(f"Wiggle Sort: {nums1}")
    print("-" * 20)

    print("Exemplo 2:")
    nums2 = [1, 3, 2, 2, 3, 1]
    print(f"Original: {nums2}")
    solver.wiggleSort(nums2)
    print(f"Wiggle Sort: {nums2}")
    print("-" * 20)

    print("Exemplo 3:")
    nums3 = [4, 5, 5, 6]
    print(f"Original: {nums3}")
    solver.wiggleSort(nums3)
    print(f"Wiggle Sort: {nums3}")
    print("-" * 20)
    
    print("Exemplo 4:")
    nums4 = [1, 1, 1, 4, 5, 6]
    print(f"Original: {nums4}")
    solver.wiggleSort(nums4)
    print(f"Wiggle Sort: {nums4}")
    print("-" * 20)

    print("Exemplo 5:")
    nums5 = [1, 2, 3, 4, 5]
    print(f"Original: {nums5}")
    solver.wiggleSort(nums5)
    print(f"Wiggle Sort: {nums5}")
    print("-" * 20)
    
    print("Exemplo 6:")
    nums6 = [6, 5, 4, 3, 2, 1]
    print(f"Original: {nums6}")
    solver.wiggleSort(nums6)
    print(f"Wiggle Sort: {nums6}")
    print("-" * 20)

    print("Exemplo 7:")
    nums7 = [1]
    print(f"Original: {nums7}")
    solver.wiggleSort(nums7)
    print(f"Wiggle Sort: {nums7}")
    print("-" * 20)

    print("Exemplo 8:")
    nums8 = [1,1,2,1,2,2,1]
    print(f"Original: {nums8}")
    solver.wiggleSort(nums8)
    print(f"Wiggle Sort: {nums8}")
    print("-" * 20)