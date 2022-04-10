from test_framework import generic_test
from collections import defaultdict

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_count = defaultdict(int)
    magazine_count = defaultdict(int)

    for c in letter_text:
        letter_count[c] += 1
    for c in magazine_text:
        magazine_count[c] += 1
    
    for k, v in letter_count.items():
        if v > magazine_count[k]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
