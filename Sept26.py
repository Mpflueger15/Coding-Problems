class Solution:
    def buddyStrings(self, A, B):
        swap = False
        swap_A=""
        swap_B=""
        if len(A)!=len(B):
          return False
        for n in range(0,len(A)):
            if A[n]==B[n]:
                pass
            else:
                if swap_A == A[n] and swap_B == B[n]:
                    pass
                elif swap == True:
                  return False
                swap_A=B[n]
                swap_B=A[n]
                swap=True
        return True

print Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
# True
print Solution().buddyStrings('aaaaaabbc', 'aaaaaabcb')
# False