# Easy
def scoreBalance(s: str) -> bool:
    def get_score(char: str) -> int:
        return ord(char) - ord('a') + 1

    total_score = sum(get_score(c) for c in s)

    if total_score % 2 != 0:
        return False

    target_score = total_score // 2

    left_score = 0

    for i in range(len(s) - 1):
        left_score += get_score(s[i])
        if left_score == target_score:
            return True

    return False

print("Example 1", scoreBalance("adcb")) # True
print("Example 2", scoreBalance("bace")) # False
