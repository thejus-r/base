# 2273. Find Resultant Array After Removing Anagrams
# Easy

def removeAnagrams(words: list[str]) -> list[str]:
    res = [words[0]]  # result
    n = len(words)


    def compare(word1: str, word2: str) -> bool:
        freq = [0]* 26
        for ch in word1:
            freq[ord(ch) - ord('a')] += 1
        for ch in word2:
            freq[ord(ch) - ord('a')] -= 1

        return all(x == 0 for x in freq)

    for i in range(1, n):
        if compare(words[i], words[i - 1]):
            continue
        res.append(words[i])

    return res

print("Example 1: ", removeAnagrams(["abba","baba","bbaa","cd","cd"]))
print("Example 2: ", removeAnagrams(["a","b","c","d","e"]))
