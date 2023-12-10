class Solution:
    def reverse(self, x: int) -> int:
        min_val = -2**31
        max_val = 2**31 -1
        
        is_neg = x<0
        if is_neg:
            x=abs(x)
        rev_new=int(str(x)[::-1])
        if min_val>rev_new or rev_new>max_val:
            return 0
        if is_neg:
            rev_new = -rev_new
        return rev_new        
        
