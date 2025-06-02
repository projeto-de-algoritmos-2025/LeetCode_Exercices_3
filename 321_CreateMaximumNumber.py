class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def max_subsequence(nums, k_sub):
            stack = []
            drop = len(nums) - k_sub
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k_sub]

        def merge(seq1, seq2):
            result = []
            while seq1 or seq2:
                if seq1 > seq2:
                    result.append(seq1.pop(0))
                else:
                    result.append(seq2.pop(0))
            return result

        max_val = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            part1 = max_subsequence(nums1, i)
            part2 = max_subsequence(nums2, k - i)
            candidate = merge(part1[:], part2[:])
            if candidate > max_val:
                max_val = candidate
        return max_val

if __name__ == "__main__":
    solver = Solution()

    nums1_ex1 = [3, 4, 6, 5]
    nums2_ex1 = [9, 1, 2, 5, 8, 3]
    k_ex1 = 5
    resultado_ex1 = solver.maxNumber(nums1_ex1, nums2_ex1, k_ex1)
    print(f"Exemplo 1:")
    print(f"nums1: {nums1_ex1}")
    print(f"nums2: {nums2_ex1}")
    print(f"k: {k_ex1}")
    print(f"Resultado: {resultado_ex1}")
    print("-" * 20)

    nums1_ex2 = [6, 7]
    nums2_ex2 = [6, 0, 4]
    k_ex2 = 5
    resultado_ex2 = solver.maxNumber(nums1_ex2, nums2_ex2, k_ex2)
    print(f"Exemplo 2:")
    print(f"nums1: {nums1_ex2}")
    print(f"nums2: {nums2_ex2}")
    print(f"k: {k_ex2}")
    print(f"Resultado: {resultado_ex2}")
    print("-" * 20)

    nums1_ex3 = [3, 9]
    nums2_ex3 = [8, 9]
    k_ex3 = 3
    resultado_ex3 = solver.maxNumber(nums1_ex3, nums2_ex3, k_ex3)
    print(f"Exemplo 3:")
    print(f"nums1: {nums1_ex3}")
    print(f"nums2: {nums2_ex3}")
    print(f"k: {k_ex3}")
    print(f"Resultado: {resultado_ex3}")
    print("-" * 20)

    nums1_ex4 = [1, 2, 3]
    nums2_ex4 = [4, 5, 6]
    k_ex4 = 0
    resultado_ex4 = solver.maxNumber(nums1_ex4, nums2_ex4, k_ex4)
    print(f"Exemplo 4 (k=0):")
    print(f"nums1: {nums1_ex4}")
    print(f"nums2: {nums2_ex4}")
    print(f"k: {k_ex4}")
    print(f"Resultado: {resultado_ex4}")
    print("-" * 20)

    nums1_ex5 = [1, 2]
    nums2_ex5 = [3, 4]
    k_ex5 = 4
    resultado_ex5 = solver.maxNumber(nums1_ex5, nums2_ex5, k_ex5)
    print(f"Exemplo 5 (k=len(nums1)+len(nums2)):")
    print(f"nums1: {nums1_ex5}")
    print(f"nums2: {nums2_ex5}")
    print(f"k: {k_ex5}")
    print(f"Resultado: {resultado_ex5}")
    print("-" * 20)
    
    nums1_ex6 = []
    nums2_ex6 = [4,5,6]
    k_ex6 = 2
    resultado_ex6 = solver.maxNumber(nums1_ex6, nums2_ex6, k_ex6)
    print(f"Exemplo 6 (nums1 vazio):")
    print(f"nums1: {nums1_ex6}")
    print(f"nums2: {nums2_ex6}")
    print(f"k: {k_ex6}")
    print(f"Resultado: {resultado_ex6}")
    print("-" * 20)

    nums1_ex7 = [1,2,3]
    nums2_ex7 = []
    k_ex7 = 2
    resultado_ex7 = solver.maxNumber(nums1_ex7, nums2_ex7, k_ex7)
    print(f"Exemplo 7 (nums2 vazio):")
    print(f"nums1: {nums1_ex7}")
    print(f"nums2: {nums2_ex7}")
    print(f"k: {k_ex7}")
    print(f"Resultado: {resultado_ex7}")
    print("-" * 20)

    nums1_ex8 = [2,5,6,4,4,0]
    nums2_ex8 = [7,3,8,0,6,5,7,6,2]
    k_ex8 = 15
    resultado_ex8 = solver.maxNumber(nums1_ex8, nums2_ex8, k_ex8)
    print(f"Exemplo 8 (Teste de desempate):")
    print(f"nums1: {nums1_ex8}")
    print(f"nums2: {nums2_ex8}")
    print(f"k: {k_ex8}")
    print(f"Resultado: {resultado_ex8}")
    print("-" * 20)
