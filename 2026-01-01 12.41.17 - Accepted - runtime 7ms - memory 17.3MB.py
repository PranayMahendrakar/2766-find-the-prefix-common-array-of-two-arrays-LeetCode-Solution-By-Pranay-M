class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = []
        seen_a = set()
        seen_b = set()
        common = 0
        
        for i in range(n):
            seen_a.add(A[i])
            seen_b.add(B[i])
            
            # If A[i] was already in B, increment common
            if A[i] in seen_b:
                common += 1
            # If B[i] was already in A (and B[i] != A[i]), increment common
            if B[i] in seen_a and B[i] != A[i]:
                common += 1
            
            result.append(common)
        
        return result