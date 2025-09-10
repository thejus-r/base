from typing import List
def minimumTeachings(n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
    cncon = set()

    for u, v in friendships:
        can_comm = False
        mp = set(languages[u - 1])
        for lang in languages[v - 1]:
            if lang in mp:
                can_comm = True
                break
        if not can_comm:
            cncon.add(u - 1)
            cncon.add(v - 1)

    if len(cncon) == 0:
        return 0

    cnt = [0] * n
    for person in cncon:
        for lang in languages[person]:
            cnt[lang - 1] += 1

    max_cnt = 0
    for c in cnt:
        max_cnt = max(max_cnt, c)

    print(cncon, cnt)
    return len(cncon) - max_cnt


print("Example 1 :", minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))