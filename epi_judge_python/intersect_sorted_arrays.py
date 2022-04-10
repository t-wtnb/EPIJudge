from typing import List

from test_framework import generic_test

from bisect import bisect_left

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    ans = []
    for ia in range(len(A)):
        if ia == 0 or A[ia] != A[ia - 1]:
            ib = bisect_left(B, A[ia])
            if ib < len(B) and B[ib] == A[ia]:
                    ans.append(A[ia])
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
